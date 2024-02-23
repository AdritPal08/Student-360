import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import chat_data, teacher_about, file_uploader, visualization
st.set_page_config(page_title="Edu Forge", page_icon="💻", layout="centered", initial_sidebar_state = "auto")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
sidebar = st.sidebar
with st.sidebar:
    st_lottie("https://lottie.host/e1de7a95-db4b-4844-b7af-04ccc2eabb4f/fsFmquVkPw.json")
# Allow the user to upload multiple CSV files
input_excel = sidebar.file_uploader(
        "Upload your excel data files here!", type=".xlsx", accept_multiple_files=True
    )


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
                options=['File Uploader','Chat with Data','Visualization','About'],
                icons=['cloud-upload-fill','chat-dots-fill','bar-chart-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                orientation="horizontal",
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "11px"}, 
        "nav-link": {"color":"white","font-size": "12px", "text-align": "middle", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "File Uploader":
            file_uploader.app()
        if app == "Chat with Data":
            chat_data.app(input_excel) 
        if app == "Visualization":
            visualization.app(input_excel)      
        if app == "About":
            teacher_about.app()                    
             
    run()            
         