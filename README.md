# ChatBot-with-Llama2
This repository contains a simple Q&amp;A chatbot application built using Streamlit and integrated with a Language Learning Model (LLM) API. The bot can have conversational interactions with users, leveraging the capabilities of models like OpenAI's GPT or Ollama's llama2.

### Features

- **Conversational AI:** Engage in natural language conversations with the bot.
- **LLM Integration:** Easily switch between different LLM providers (OpenAI, Anthropic, or Ollama).
- **Session Management:** Retain conversation context across interactions using Streamlit session state.
- **Extensible:** Modular design allows for easy customization and extension.

### Getting Started

Follow the steps below to set up and run the application on your local machine.

### Prerequisites

- Python 3.6 or higher.
- API key for your LLM provider (e.g., OpenAI).

### Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root of your project and add your API key:

    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

### Usage

Run the following command to start the Streamlit application:

```bash
streamlit run script_name.py
```

Replace `script_name.py` with the name of your script.

### Project Structure

- **main.py**: The main script to run the Streamlit app.
- **requirements.txt**: List of dependencies.
- **.env**: Environment file to store API keys (not included in the repository, to be created by the user).

### How It Works

1. **User Input**: Enter your query in the input box.
2. **Session State**: The conversation context is managed using Streamlit session state.
3. **LLM Invocation**: The input is passed to the LLM model, which processes it and generates a response.
4. **Response Display**: The response from the LLM is displayed in the Streamlit app.
