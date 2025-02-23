# 🤖 AI-Powered Web-Searching Chat Assistant with Tool Calling

## 🌟 Overview
This project is an AI-powered chat assistant built with Streamlit and Langchain. The assistant can engage in natural conversations, search the web using DuckDuckGo, and provide informative responses while maintaining conversational context. It utilizes Langchain's tool-calling functionality to integrate external tools like web search seamlessly.

## ✨ Features
- 💬 **Conversational AI:** Powered by the `mistral-nemo:latest` model from Ollama.
- 🌐 **Web Search with Tool Calling:** Integrates DuckDuckGo search using Langchain’s tool-calling mechanism for real-time information.
- 🎨 **Customizable Settings:** Adjustable response creativity with a temperature slider.
- 🗂️ **Conversation History:** Maintains chat history until cleared.

## 🛠️ Installation

### 📋 Prerequisites
Ensure you have the following installed:
- 🐍 Python 3.9 or later
- 🧠 Ollama installed and running locally

### 📦 Dependencies
```bash
pip install streamlit langchain-core langchain-ollama langchain-community duckduckgo-search
```

## 🚀 Usage
1. 🧩 Clone this repository:
```bash
git clone https://github.com/your-repo/ai-chat-assistant.git
cd ai-chat-assistant
```

2. ▶️ Run the Streamlit app:
```bash
streamlit run app.py
```

3. 🌍 Open the app in your browser at [http://localhost:8501](http://localhost:8501).

## 🗂️ Application Structure
- 💬 **Main Chat Interface:** Users can input messages, and the assistant responds.
- ⚙️ **Sidebar:** Allows configuration of the model's temperature and clearing chat history.

## ⚙️ Configuration
- 🎨 **Model Temperature:** Controls response creativity (0.0 = more focused, 1.0 = more creative).
- 🌐 **Web Search with Tool Calling:** Automatically triggered when external information is needed.

## 🧩 Code Highlights
- 📝 **System Prompt:** Guides the AI to be helpful, concise, and context-aware.
- 🔧 **Tool Integration:** Uses `web_search` as a callable tool within Langchain.
- 🛠️ **Tool Calling:** Langchain’s tool-calling functionality enables the assistant to invoke external tools dynamically.
- 💾 **Session State:** Manages messages, LLM instances, and tool bindings.

## 🛠️ Customization
- 🧠 **Change the LLM Model:** Modify the `ChatOllama` initialization in `initialize_session_state()`.
- 🧩 **Add More Tools:** Define additional tools using `@tool` decorators.

## 🧹 Troubleshooting
- ✅ Ensure Ollama is running locally.
- 📦 Verify that all dependencies are correctly installed.
- 🌐 Check your internet connection for web search functionality.
- 🛠️ Ensure that the tool-calling mechanism in Langchain is correctly configured.

## 📜 License
This project is licensed under the Apache2.0 License.

## 👤 Author
Sasidharan B

## 🙏 Acknowledgments
- 🎨 Streamlit for the user interface
- 🧠 Langchain for LLM and tool integration
- 🌐 DuckDuckGo for web search
