# Panadasai Chatbot 

A conversational data analysis application that allows users to interact with heart disease prediction datasets using natural language queries. Built with Streamlit and powered by OpenAI's language models through PandasAI.

## Features

- 🗣️ **Natural Language Querying**: Ask questions about your data in plain English
- 📊 **Interactive Visualizations**: Generate charts and plots with simple requests
- 📋 **Data Preview**: View your dataset structure and contents
- 💬 **Chat History**: Keep track of your analysis conversation
- ⚡ **Real-time Processing**: Get instant responses to your data queries

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Heart disease prediction CSV dataset

## Installation

1. **Clone the repository**
   ```bash
   git clone <>
   cd heart-disease-chatbot
   ```

2. **Install required dependencies**
   ```bash
   pip install streamlit pandas python-dotenv pandasai matplotlib
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   openai_api_key=your_openai_api_key_here
   ```

4. **Prepare your dataset**
   
   Place your heart disease dataset as `Heart_Disease_Prediction.csv` in the project directory.

## Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the web interface**
   
   Open your browser and navigate to `http://localhost:8501`

3. **Interact with your data**
   - Use the checkbox to preview your CSV data
   - Type natural language questions in the input field
   - Request visualizations like "Plot the distribution of age"
   - View chat history to track your analysis journey

## Example Queries

### Data Analysis
- "What is the average age of patients with heart disease?"
- "How many male vs female patients are in the dataset?"
- "Show me the correlation between cholesterol and heart disease"

### Visualizations
- "Plot the distribution of age"
- "Create a bar chart showing heart disease by gender"
- "Show a scatter plot of cholesterol vs blood pressure"
- "Generate a histogram of chest pain types"

## Project Structure

```
heart-disease-chatbot/
├── app.py                           # Main Streamlit application
├── Heart_Disease_Prediction.csv     # Dataset file
├── .env                            # Environment variables (not tracked)
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## Dependencies

- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **python-dotenv**: Environment variable management
- **pandasai**: AI-powered data analysis
- **matplotlib**: Plotting and visualization

## Configuration

The application uses the following configuration:
- **Page Title**: "Heart Disease Data Chatbot"
- **Caching**: Disabled for real-time responses
- **Error Handling**: Comprehensive error messages for missing files/keys

## Error Handling

The application includes robust error handling for:
- Missing OpenAI API key
- CSV file not found
- Query processing errors
- Empty or invalid responses

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `openai_api_key` | Your OpenAI API key for language model access | Yes |

## Troubleshooting

### Common Issues

1. **"Missing OPENAI_API_KEY in .env file"**
   - Ensure you've created a `.env` file with your OpenAI API key

2. **"CSV file not found"**
   - Verify `Heart_Disease_Prediction.csv` is in the project directory
   - Check file name spelling and case sensitivity

3. **"No output generated"**
   - Try rephrasing your query with more specific instructions
   - Use explicit chart types (e.g., "histogram", "bar chart")

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [PandasAI](https://github.com/gventuri/pandas-ai)
- Uses [OpenAI](https://openai.com/) language models

## Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the [PandasAI documentation](https://docs.pandas-ai.com/)
3. Open an issue in this repository

---

**Happy Data Analysis! 🚀**
