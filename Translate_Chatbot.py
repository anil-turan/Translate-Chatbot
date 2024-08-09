import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget

# DeepL API kullanarak metni çevirmek için fonksiyon
def translate(text, target_language):
    api_key = 'YOUR_DEEPL_API_KEY'  # Buraya kendi API anahtarınızı ekleyin
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
        return "Çeviri işlemi başarısız oldu. Lütfen tekrar deneyin."

class TranslateChatBotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Çeviri Chatbot")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        self.user_input = QLineEdit()
        self.layout.addWidget(self.user_input)

        self.send_button = QPushButton("Gönder")
        self.send_button.clicked.connect(self.respond)
        self.layout.addWidget(self.send_button)

        self.central_widget.setLayout(self.layout)

    def respond(self):
        user_text = self.user_input.text()
        self.chat_display.append(f"Sen: {user_text}")

        # Çeviri işlemi (İngilizce -> Türkçe)
        translated_text = translate(user_text, 'TR')
        self.chat_display.append(f"Bot: {translated_text}")
        self.user_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = TranslateChatBotApp()
    mainWin.show()
    sys.exit(app.exec_())
