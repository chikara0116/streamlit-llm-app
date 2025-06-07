from dotenv import load_dotenv

load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

# Define the function to query the LLM based on user input and expert selection
def query_expert(input_text: str, expert_role: str) -> str:
    """
    Sends the input text and expert role to the LLM and returns the response.
    :param input_text: Text provided by the user.
    :param expert_role: Selected expert type (e.g., 'Technology', 'Business').
    :return: LLM-generated response.
    """
    # Define system messages for different experts
    system_prompts = {
        "Technology Expert": "You are a highly knowledgeable technology expert. Provide detailed technical insights.",
        "Business Strategist": "You are an experienced business strategist. Offer practical business recommendations."
    }
    
    # Select the appropriate system message
    system_message = system_prompts.get(expert_role, "You are a helpful assistant.")

    # Build the chat prompt template
    chat_prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system_message),
        HumanMessagePromptTemplate.from_template("User said: {user_input}")
    ])

    # Initialize the chat model (adjust temperature or model name as needed)
    chat = ChatOpenAI(temperature=0.7)

    # Format messages and send to model
    messages = chat_prompt.format_messages(user_input=input_text)
    response = chat(messages)
    return response.content

# Streamlit UI setup
def main():
    st.title("LLM Expert Assistant Web App")
    
    # Display overview and instructions
    st.markdown(
        """
        ### Webアプリ概要
        このアプリでは、入力フォームにテキストを入力し、ラジオボタンで専門家を選択すると、
        選択した専門家の視点でLLMが回答を生成します。
        - テキストを入力して「送信」ボタンを押してください。
        - 専門家の選択肢に応じて回答のスタイルが変わります。
        """
    )

    # Input form and expert selection
    user_input = st.text_area("入力テキスト", height=150)
    expert_option = st.radio(
        "専門家を選択", 
        ("Technology Expert", "Business Strategist")
    )

    # When the user clicks the button, call the LLM function
    if st.button("送信"):
        if not user_input.strip():
            st.warning("テキストを入力してください。")
        else:
            with st.spinner("回答を生成中... 🧠"):
                llm_response = query_expert(user_input, expert_option)
            st.subheader("LLMの回答")
            st.write(llm_response)

if __name__ == "__main__":
    main()
# This code is a Streamlit web application that allows users to interact with a language model (LLM)

# 必要なパッケージをインストール:
# pip install streamlit langchain openai

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

# Define the function to query the LLM based on user input and expert selection
def query_expert(input_text: str, expert_role: str) -> str:
    """
    Sends the input text and expert role to the LLM and returns the response.
    :param input_text: Text provided by the user.
    :param expert_role: Selected expert type (e.g., 'Technology', 'Business').
    :return: LLM-generated response.
    """
    # Define system messages for different experts
    system_prompts = {
        "Technology Expert": "You are a highly knowledgeable technology expert. Provide detailed technical insights.",
        "Business Strategist": "You are an experienced business strategist. Offer practical business recommendations."
    }
    
    # Select the appropriate system message
    system_message = system_prompts.get(expert_role, "You are a helpful assistant.")

    # Build the chat prompt template
    chat_prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system_message),
        HumanMessagePromptTemplate.from_template("User said: {user_input}")
    ])

    # Initialize the chat model (adjust temperature or model name as needed)
    chat = ChatOpenAI(temperature=0.7)

    # Format messages and send to model
    messages = chat_prompt.format_messages(user_input=input_text)
    response = chat(messages)
    return response.content

# Streamlit UI setup
def main():
    st.title("LLM Expert Assistant Web App")
    
    # Display overview and instructions
    st.markdown(
        """
        ### Webアプリ概要
        このアプリでは、入力フォームにテキストを入力し、ラジオボタンで専門家を選択すると、
        選択した専門家の視点でLLMが回答を生成します。
        - テキストを入力して「送信」ボタンを押してください。
        - 専門家の選択肢に応じて回答のスタイルが変わります。
        """
    )

    # Input form and expert selection
    user_input = st.text_area("入力テキスト", height=150)
    expert_option = st.radio(
        "専門家を選択", 
        ("Technology Expert", "Business Strategist")
    )

    # When the user clicks the button, call the LLM function
    if st.button("送信"):
        if not user_input.strip():
            st.warning("テキストを入力してください。")
        else:
            with st.spinner("回答を生成中... 🧠"):
                llm_response = query_expert(user_input, expert_option)
            st.subheader("LLMの回答")
            st.write(llm_response)

if __name__ == "__main__":
    main()

# 必要なパッケージをインストール:
# pip install streamlit langchain openai langchain_community

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

# Define the function to query the LLM based on user input and expert selection
def query_expert(input_text: str, expert_role: str) -> str:
    """
    Sends the input text and expert role to the LLM and returns the response.
    :param input_text: Text provided by the user.
    :param expert_role: Selected expert type (e.g., 'Technology', 'Business').
    :return: LLM-generated response.
    """
    # Define system messages for different experts
    system_prompts = {
        "Technology Expert": "You are a highly knowledgeable technology expert. Provide detailed technical insights.",
        "Business Strategist": "You are an experienced business strategist. Offer practical business recommendations."
    }
    
    # Select the appropriate system message
    system_message = system_prompts.get(expert_role, "You are a helpful assistant.")

    # Build the chat prompt template
    chat_prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system_message),
        HumanMessagePromptTemplate.from_template("User said: {user_input}")
    ])

    # Initialize the chat model (adjust temperature or model name as needed)
    chat = ChatOpenAI(temperature=0.7)

    # Format messages and send to model
    messages = chat_prompt.format_messages(user_input=input_text)
    response = chat(messages)
    return response.content

# Streamlit UI setup
def main():
    st.title("LLM Expert Assistant Web App")
    
    # Display overview and instructions
    st.markdown(
        """
        ### Webアプリ概要
        このアプリでは、入力フォームにテキストを入力し、ラジオボタンで専門家を選択すると、
        選択した専門家の視点でLLMが回答を生成します。
        - テキストを入力して「送信」ボタンを押してください。
        - 専門家の選択肢に応じて回答のスタイルが変わります。
        """
    )

    # Input form and expert selection
    user_input = st.text_area("入力テキスト", height=150)
    expert_option = st.radio(
        "専門家を選択", 
        ("Technology Expert", "Business Strategist")
    )

    # When the user clicks the button, call the LLM function
    if st.button("送信"):
        if not user_input.strip():
            st.warning("テキストを入力してください。")
        else:
            with st.spinner("回答を生成中... 🧠"):
                llm_response = query_expert(user_input, expert_option)
            st.subheader("LLMの回答")
            st.write(llm_response)

if __name__ == "__main__":
    main()
