import streamlit as st
from streamlit_option_menu import option_menu
import chat_doc, student_about, resume_ats,YT_Summarizer,course_roadmap
st.set_page_config(page_title="Intelligent Hub", page_icon="🤖", layout="centered", initial_sidebar_state = "auto")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
               
        app = option_menu(
                menu_title= None,
                options=['Chat with File','Smart ATS','Course Roadmap Generator','YT Summarizer','About'],
                icons=['chat-fill','file-earmark-person-fill','diagram-3-fill','youtube','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                orientation="horizontal",
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "8px"}, 
        "nav-link": {"color":"white","font-size": "10px", "text-align": "middle", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Chat with File":
            chat_doc.app()
        if app == "Smart ATS":
            resume_ats.app() 
        if app == "Course Roadmap Generator":
            course_roadmap.app() 
        if app == "YT Summarizer":
            YT_Summarizer.app()      
        if app == "About":
            student_about.app()                    
             
    run()            
         