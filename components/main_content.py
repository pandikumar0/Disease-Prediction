import streamlit as st
import streamlit as st
import pandas as pd
import pickle  
import streamlit.components.v1 as components

from .resutls_display import ResultsDisplay
from .lime_explainer import LimeExplainer
from constants import ORDERED_FEATURES
from .data_visualizer import DataVisualizer
from .llm_response import LLMResponse

class MainContent:
    @staticmethod
    def display_header():
        st.title("Parkinson's Disease Detection System")
        st.markdown("""
        This advanced tool analyzes multi-modal sensor data to provide:
        - **Clear assessment** for Parkinson's disease
        - **Probability score** indicating confidence level
        - **Detailed explanations** of key findings
        - **Personalized recommendations** based on results
        """)
    
    @staticmethod
    def display_analysis_results(model, input_df):
        with st.spinner("Analyzing data..."):
            try:
                # Make prediction
                prediction = model.predict(input_df)[0]
                proba = model.predict_proba(input_df)[0][1]
                
                # Display result
                ResultsDisplay.display(prediction, proba)
                

                # Generate and display LIME explanation
                exp = LimeExplainer.explain(model, input_df)
                st.subheader("LIME Explanation - Explainable AI")
                components.html(exp.as_html(), height=500)
            
                
                # with col2:
                #     # Visualize sensor data
                #     DataVisualizer.visualize(input_df)
                
                # Display LLM response
                LLMResponse.display_response(prediction, input_df)
                
            except Exception as e:
                st.error(f"An error occurred during analysis: {str(e)}")
                st.info("Please check your input data and try again.")
