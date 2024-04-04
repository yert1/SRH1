import streamlit as st

from streamlit_option_menu import option_menu


import trending, test, your, about
st.set_page_config(
        page_title="YourContraceptionChoice",
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
        with st.sidebar:        
            app = option_menu(
                menu_title='Choices for You ',
                options=['Account','Home', 'Recommendations', 'Directory'],
                icons=['person-circle', 'house-fill', 'trophy-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'violet'},
        "icon": {"color": "black", "font-size": "23px"}, 
        "nav-link": {"color":"black","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "white"},
        "nav-link-selected": {"background-color": "white"},}
                
                )

        
        
        if app == "Account":
            test.app() 
        if app == 'Home':
            about.app()           
        if app == "Recommendations":
            trending.app() 
        if app == 'Directory':
            your.app()
           
             
          
             
    run()            
        
            
                
    
