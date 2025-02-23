import streamlit as st
from langchain_core.messages import HumanMessage, ToolMessage, SystemMessage, AIMessage
from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
import time

# System prompt for the chat assistant
SYSTEM_PROMPT = """
You are a helpful chat assistant with the ability to search the web and provide accurate information. You should:
1. Engage in natural conversation
2. Search the web when needed to provide accurate information
3. Maintain context of the conversation
4. Be concise but informative in your responses
5. Acknowledge when you need to search for information"""

@tool(parse_docstring=True)
def web_search(query: str):
    """
    Searches the web for relevant information.
    Use this tool when the user asks a question that requires online information.
    
    Args:
        query: The search query provided by the user.
    
    Returns:
        Relevant web search results.
    """
    search_tool = DuckDuckGoSearchRun()
    try:
        results = search_tool.invoke(query)
        return results
    except Exception as e:
        return f"Error fetching search results: {str(e)}"


def initialize_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = [SystemMessage(content=SYSTEM_PROMPT)]
    if 'llm' not in st.session_state:
        st.session_state.llm = ChatOllama(model="mistral-nemo:latest", temperature=0.7)
    if 'llm_with_tools' not in st.session_state:
        st.session_state.llm_with_tools = st.session_state.llm.bind_tools([web_search])


def display_chat_message(message, is_user: bool):
    avatar = "👤" if is_user else "🤖"
    with st.chat_message(avatar):
        st.write(message.content)
        time.sleep(0.1)


def process_message(user_input: str):
    user_message = HumanMessage(content=user_input)
    st.session_state.messages.append(user_message)
    display_chat_message(user_message, is_user=True)
    
    # Get response from the model with tool calling
    response = st.session_state.llm_with_tools.invoke(st.session_state.messages)
    
    if response.tool_calls:
        for tool_call in response.tool_calls:
            if tool_call["name"] == "web_search":
                tool_response = web_search(tool_call["args"])
                tool_message = ToolMessage(content=str(tool_response), tool_call_id=tool_call["id"])
                st.session_state.messages.append(tool_message)
                display_chat_message(tool_message, is_user=False)
    
    final_response = st.session_state.llm_with_tools.invoke(st.session_state.messages)
    st.session_state.messages.append(final_response)
    display_chat_message(final_response, is_user=False)


def create_sidebar():
    with st.sidebar:
        st.title("📱 Chat Settings")
        
        st.subheader("Model Configuration")
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1, help="Higher values make responses more creative")
        
        if temperature != st.session_state.llm.temperature:
            st.session_state.llm = ChatOllama(model="mistral-nemo:latest", temperature=temperature)
            st.session_state.llm_with_tools = st.session_state.llm.bind_tools([web_search])
        
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = [SystemMessage(content=SYSTEM_PROMPT)]
            st.rerun()
        
        st.subheader("Chat Statistics")
        message_count = len(st.session_state.messages) - 1
        st.write(f"Messages in conversation: {message_count}")


def main():
    st.set_page_config(page_title="AI Chat Assistant", page_icon="🤖", layout="wide")
    initialize_session_state()
    create_sidebar()
    
    st.title("🤖 AI Chat Assistant")
    st.caption("Ask me anything! I can search the web to help answer your questions.")
    
    for message in st.session_state.messages[1:]:
        display_chat_message(message, is_user=isinstance(message, HumanMessage))
    
    user_input = st.chat_input("Type your message here...")
    if user_input:
        process_message(user_input)


if __name__ == "__main__":
    main()
