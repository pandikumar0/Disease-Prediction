import streamlit as st
import pandas as pd
import pickle
import streamlit.components.v1 as components

from components.sidebar import Sidebar
from components.user_input import UserInput
from components.model_loader import ModelLoader
from components.main_content import MainContent

# Set page config
st.set_page_config(
    page_title="Parkinson's Assessment", 
    page_icon="🧠", 
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    try:
        # Display sidebar
        Sidebar.display()
        
        # Display main content header
        MainContent.display_header()
        
        # Get user input
        input_df = UserInput.get_input()
        
        # Load model
        model = ModelLoader.load_model()
        
        if st.button("🔍 Analyze Data", type="primary"):
            MainContent.display_analysis_results(model, input_df)
            
    except Exception as e:
        st.error(f"Application error: {str(e)}")
        st.stop()

if __name__ == "__main__":
    main()