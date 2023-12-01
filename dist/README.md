# GPT Chat

GPT Chat is a simple Flask web application that allows users to interact with the OpenAI GPT model. It features a modern chat interface using Bootstrap and includes request limits to prevent abuse.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Customization](#customization)

## Installation

1. Clone this repository to your local machine:

git clone https://github.com/RA3D/GPT-Chat.git


2. Install the required dependencies:

pip install -r requirements.txt


3. Make sure you have the necessary files in place:

- Flask application script (e.g., `app.py`)
- ChatGPT script (e.g., `chatgpt.js`)
- HTML template (e.g., `index.html`)
- Custom CSS stylesheet (optional)

## Usage

1. Run the Flask application:

python app.py


2. Open your web browser and navigate to the address where the Flask application is running (default: `http://127.0.0.1:5000/`).

3. Start chatting with ChatGPT by typing a message in the input field and clicking the "Send" button or pressing the "Enter" key.

## Configuration

Before you can use the GPT Chat application, you need to set your OpenAI API key in the `chat_gpt.py` file.

1. Generate an API key at https://platform.openai.com/account/api-keys.
2. Open the `chat_gpt.py` file in your favorite text editor.
3. Locate the line where the API key is set (e.g., `openai.api_key = "your_api_key"`).
4. Replace `"your_api_key"` with your actual OpenAI API key, which should be a string like `"sk-abcdefgh1234567890"`.
5. Save the changes to the `chat_gpt.py` file.

Now your GPT Chat application is ready to use with your OpenAI API key.

## Customization

You can customize the chat interface by modifying the HTML, CSS, and JavaScript files. 
The chat UI is built using Bootstrap. 
To further customize the appearance or behavior, you can:

- Modify the `index.html` file to add, remove, or change elements in the chat interface.
- Adjust the `chatgpt.js` file to alter the behavior of the chat interface or interact with the ChatGPT API differently.

