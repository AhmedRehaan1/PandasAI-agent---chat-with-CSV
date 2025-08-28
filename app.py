import os
import pandas as pd
import dotenv
import streamlit as st
from pandasai.llm import OpenAI
from pandasai import SmartDataframe
import matplotlib.pyplot as plt

# --- Load env vars ---
dotenv.load_dotenv()
openai_key = os.getenv("openai_api_key")

# --- Setup Streamlit UI ---
st.set_page_config(page_title="Heart Disease Data Chatbot")
st.title("Heart Disease Data Chatbot")
st.write("Chat with your CSV file using natural language queries or request charts 📊")

# --- Validate keys ---
if not openai_key:
    st.error(" Missing OPENAI_API_KEY in .env file")
    st.stop()

# --- Load CSV safely ---
CSV_FILE = "Heart_Disease_Prediction.csv"
if not os.path.exists(CSV_FILE):
    st.error(f" CSV file not found: {CSV_FILE}")
    st.stop()

df = pd.read_csv(CSV_FILE)
st.success(" CSV loaded successfully")

# --- Setup LLM and SmartDataframe (with plotting enabled) ---
llm = OpenAI(api_token=openai_key)
smart_df = SmartDataframe(df, config={"llm": llm, "enable_cache": False})

# Show preview if user wants
if st.checkbox("Show CSV Preview"):
    st.dataframe(df.head())

# Store chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("Ask a question or request a visualization:",
                           placeholder="e.g., Plot the distribution of age")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = smart_df.chat(user_input)

            # --- Detect if response is a matplotlib Figure ---
            if isinstance(response, plt.Figure):
                st.pyplot(response)  # show the figure
                st.session_state.history.append({"user": user_input, "bot": "[Chart displayed]"})
            elif response is None:
                st.warning(" No output generated. Try rephrasing your query (e.g., 'Plot age distribution as histogram').")
                st.session_state.history.append({"user": user_input, "bot": "[No output]"})
            else:
                st.session_state.history.append({"user": user_input, "bot": str(response)})

        except Exception as e:
            response = f"Error: {e}"
            st.session_state.history.append({"user": user_input, "bot": response})

# Display chat history
st.subheader("Chat History")
for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.markdown("---")
