# WhatsApp-AI-Responder 🤖

<div align="center">

### **Never Miss a Message Again!**  
*AI-Powered WhatsApp Conversations That Feel Human*

<br>

[![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python&style=for-the-badge)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-Automation-green?logo=selenium&style=for-the-badge)](https://selenium.dev)
[![Gemini AI](https://img.shields.io/badge/Google-GeminiAI-yellow?logo=google&style=for-the-badge)](https://gemini.google.com)

<br>

**Your 24/7 AI Assistant for WhatsApp Messaging**

</div>

---

## 🎯 About The Project

Tired of missing important messages? Busy but want to stay connected? 

**WhatsApp-AI-Responder** is your intelligent messaging companion that automatically replies to WhatsApp messages using Google's Gemini AI. It crafts natural, human-like responses so you never leave anyone on read!

### ✨ Key Features

- 🧠 **Smart AI Conversations** - Powered by Google Gemini AI
- 🛡️ **Complete Privacy** - Runs locally on your machine
- ⚡ **Quick Setup** - Get started in under 5 minutes
- 🎯 **Smart Filtering** - Automatically ignores unknown numbers
- 🎨 **Customizable** - Adjust the AI's personality and style
- 🔄 **Auto-Recovery** - Handles errors and continues running

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Google Chrome browser
- Google Gemini API key ([Get it free](https://aistudio.google.com))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/WhatsApp-AI-Responder.git
cd WhatsApp-AI-Responder
```

2. **Install dependencies**
```bash
pip install selenium google-generativeai
```

3. **Download ChromeDriver**
   - Visit [ChromeDriver website](https://chromedriver.chromium.org/)
   - Download the version matching your Chrome browser
   - Place it in your PATH or project directory

### Configuration

1. **Get your Gemini API key** from [Google AI Studio](https://aistudio.google.com)

2. **Update the configuration** in the script:
```python
API_key = "your_actual_gemini_api_key_here"
custom_text = "Your custom prompt for AI behavior"
```

3. **Run the bot**
```bash
python whatsapp_bot.py
```

4. **Scan QR code** when WhatsApp Web opens and you're ready!

---

## ⚙️ Customization

### Change AI Personality
Modify the `custom_text` variable to change how the AI responds:

```python
# Professional style
custom_text = "Reply professionally as a business assistant"

# Friendly style  
custom_text = "Talk like we're best friends, keep it casual"

# Funny style
custom_text = "Be hilarious and witty in your replies"
```

### Contact Filtering
The bot automatically ignores numbers starting with +91. Add more filters:

```python
def is_unknown_number():
    # Add your custom logic here
    return any(pattern in contact_name for pattern in ['+91', 'spam', 'marketing'])
```

---

## ⚠️ Current Limitations

- **Requires constant internet connection**
- **WhatsApp Web must remain open and active**
- **Works best with individual chats (group chats limited)**
- **Text messages only (no media/image support)**
- **No conversation memory between messages**
- **May require updates when WhatsApp changes their interface**

---

## 🔮 Future Enhancements

### Planned Features
- **User-specific reply styles** - Different personalities for different contacts
- **Chat history storage** - Remember past conversations
- **Scheduled messaging** - Send messages at specific times
- **Media support** - Handle images and documents
- **Group chat integration** - Better group message handling
- **Multi-language support** - Detect and reply in different languages

### Technical Improvements
- **Web dashboard** for easy control and monitoring
- **Docker support** for easy deployment
- **Database integration** for conversation storage
- **Plugin system** for extended functionality
- **Enhanced error recovery** for better stability

---

## 🆘 Troubleshooting

**Common Issues & Solutions:**

- **"ChromeDriver not found"** - Ensure ChromeDriver is downloaded and in your PATH
- **"Stale element reference"** - The bot will automatically recover, just wait
- **"API quota exceeded"** - Check your Gemini API usage limits
- **QR code won't scan** - Refresh the page and try again
- **Messages not detected** - Ensure you're using the latest version of the script

---

## 📝 Important Notes

> ⚠️ **Please use responsibly** - This tool is for educational purposes. Always respect WhatsApp's terms of service and people's privacy.

> 🔐 **Keep your API keys secure** - Never commit actual API keys to version control

> 🧪 **Test with small groups** - Try with a few contacts before wider use

> 📞 **Be transparent** - Let people know they're talking to an AI when appropriate

---

## 🤝 Contributing

We welcome contributions! Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

---

<div align="center">

### **Made with ❤️ for the Open Source Community**

⭐ **If you find this project useful, please give it a star!**

**Happy messaging!** 🎉

</div>

---

*Disclaimer: This project is for educational purposes. Users are responsible for complying with WhatsApp's terms of service and applicable laws.*
