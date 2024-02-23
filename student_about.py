import streamlit as st
from streamlit_lottie import st_lottie

def app():
    # st.set_page_config(page_title="about")
    st.header(":red[Intelligent] Hub 👩🏻‍🎓",divider= 'rainbow')
    st.write("Chat Smart, Learn Sharp - Where Intelligence Unfolds")
    # st.write('where uploading, chatting, and visualizing your data becomes a seamless and personalized experience through the magic of Generative AI.')
    st.write("")
    st.markdown('Created by: [Adrit Pal](https://www.linkedin.com/in/adritpal/)')
    st.markdown('Contact via mail: [adritpal4@gmail.com]')
    st.markdown('GitHub: [AdritPal08](https://github.com/AdritPal08)')
    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
    with col2:
        st_lottie("https://lottie.host/dceed925-932c-4ea4-b140-3aebdeaaf1f0/JZyKl8qgfG.json", width=250, height=250)
