import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_txt(upload_file):
    reader = pdf.PdfReader(upload_file)
    text = ""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template
input_prompts = """
Hey Act like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech and no-tech field. Your task is to evaluate the resume
based on the given company name, job role and job description. You must consider the job market is 
very competitive and you should provide best assistance for improving the resumes. 
Assign the percentage Matching based on company name, job role, job description and the missing keywords with high accuracy.
resume : {text}
company name: {company_name}
job role :{job_role}
job desciption : {job_desciption}

I want the response in one single string having the structure -
Job desciption :"%",
Missing Keywords :[], 
Suggestions for Improvement :""

"""
def app():
    st.header("Smart ATS - Optimize Your :green[Resume] 😎",divider= 'rainbow')
    # st.header('_Streamlit_ is :blue[cool] :sunglasses:')
    # st.markdown('<style>h1{color: orange; text-align: center;}</style>', unsafe_allow_html=True)
    company_name = st.text_input("Company Name")
    job_role = st.text_input("Job role")
    job_desciption = st.text_area("Job Description")
    uploder_file = st.file_uploader("Upload Your Resume",type="pdf",help="Please upload the pdf")
    
    submit = st.button("Submit")
    if submit:
        if uploder_file is not None and job_desciption!= "":
            with st.spinner("Processing..."):
                text = input_pdf_txt(uploder_file)
                response = get_gemini_response(input_prompts) 
                st.subheader("Response :")
                st.write(response)
            
    