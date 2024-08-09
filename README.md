# Translation Chatbot

This project is a translation chatbot application that uses the DeepL API to translate text into various languages. The application provides a graphical user interface (GUI) created using PyQt5.

## Features

- Translate text to various languages using the DeepL API
- Simple and user-friendly graphical user interface (GUI)
- Real-time translation display

## Requirements

- Python 3.x
- requests
- PyQt5

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/translation-chatbot.git
    cd translation-chatbot
    ```

2. Install the required Python packages:
    ```sh
    pip install requests pyqt5
    ```

3. Obtain your DeepL API key from the [DeepL website](https://www.deepl.com/pro-api).

4. Add your API key to the script:
    ```python
    api_key = 'YOUR_DEEPL_API_KEY'  # Replace 'YOUR_DEEPL_API_KEY' with your actual API key
    ```

## Usage

1. Run the application:
    ```sh
    python translate_chatbot.py
    ```

2. Enter text into the input field and press "Send" to translate the text to the target language (default is Turkish).

## Example Code

Here is an example of how the main script looks:

```python
import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget

# Function to translate text using the DeepL API
def translate(text, target_language):
    api_key = 'YOUR_DEEPL_API_KEY'  # Add your API key here
    url = "https://api-free.deepl.com/v2/translate"
    payload = {
        'auth_key': api_key,
        'text': text,
        'target_lang': target_language.upper()
    }
    response = requests.post(url, data=payload)
    response_data = response.json()

    if 'translations' in response_data:
        return response_data['translations'][0]['text']
    else:
        return "Translation failed. Please try again."

class TranslateChatBotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Translation Chatbot")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        self.user_input = QLineEdit()
        self.layout.addWidget(self.user_input)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.respond)
        self.layout.addWidget(self.send_button)

        self.central_widget.setLayout(self.layout)

    def respond(self):
        user_text = self.user_input.text()
        self.chat_display.append(f"You: {user_text}")

        # Translation (English -> Turkish)
        translated_text = translate(user_text, 'TR')
        self.chat_display.append(f"Bot: {translated_text}")
        self.user_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = TranslateChatBotApp()
    mainWin.show()
    sys.exit(app.exec_())
