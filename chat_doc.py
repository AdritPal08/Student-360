import streamlit as st
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
# from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.3)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    # print(response) # No need to print the response
    # st.write("Reply: ", response["output_text"]) # No need to write the response
    return response["output_text"] # Just return the response

def app():
    st.header(':green[Chat] with files 📝',divider= 'rainbow')


    # Initialize the session state for the messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Allow the user to enter a question
    user_question = st.chat_input("Ask your Question...")

    # If the user entered some text
    if user_question:
        # Append the user's question to the messages
        st.session_state.messages.append({"role": "user", "content": user_question})
        # Display the user's question
        with st.chat_message("user"):
            st.markdown(user_question)
        # Get the answer from the user_input function
        answer = user_input(user_question)
        # Append the answer to the messages
        st.session_state.messages.append({"role": "assistant", "content": answer})
        # Display the answer
        with st.chat_message("assistant"):
            st.success(answer)
