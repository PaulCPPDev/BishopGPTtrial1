import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

#to load the API_KEY
load_dotenv()

def app():

    #initialize the chat history variable
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    #st.set_page_config(page_title="Streaming BOt", page_icon=":flag-cm:")

    st.title("BishopGPT")


    # get Response from LLMs with Langchain
    def get_response(query, history):
        #template for the prompt
        template = """
            You are a helpful assistant. Answer the following questions considering the history of the conversation:
            Chat history: {chat_history}
            User question: {user_question}
            """
        
        # Create our Prompt
        prompt = ChatPromptTemplate.from_template(template)

        # Define our LLM
        llm = ChatOpenAI()

        # create our Chain
        chain = prompt | llm | StrOutputParser()

        # invoke the chain with right parameters & return it
        return chain.invoke({
            "chat_history": history,
            "user_question": query
        })



    # Conversation (chat History)
    # Display all the messages in the chat history
    for message in st.session_state.chat_history:
        if isinstance(message, HumanMessage):
            # display the human message (on the right)
            with st.chat_message("Human"):
                st.markdown(message.content)
        else:
            #display the AI message (on the left)
            with st.chat_message("AI"):
                st.markdown(message.content)

    # User input
    user_query = st.chat_input("Your message") # chatgpt styte user input
    if user_query is not None and user_query != "": #checks if the user entered something
        st.session_state.chat_history.append(HumanMessage(user_query)) #appends user text to the chat_history as a Human message

        # reprint what the user entered (like when you send a message on what's app)
        with st.chat_message("Human"):
            st.markdown(user_query)
        
        # create a generation (AI Response to the user_query)
        with st.chat_message("AI"):
            ai_response = "Due to lack of API Keys I am unable to answer, sorry." #get_response(user_query, st.session_state.chat_history)
            st.markdown(ai_response)

        # append the AI message to the session state (adds to chat history)
        st.session_state.chat_history.append(AIMessage(ai_response))