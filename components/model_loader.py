import streamlit as st
import pickle
import os

class ModelLoader:
    @staticmethod
    @st.cache_resource
    def load_model():
        """Load the trained model with error handling"""
        model_path = "./model/random_forest.pkl"
        if not os.path.exists(model_path):
            st.error(f"Model file not found at: {os.path.abspath(model_path)}")
            st.stop()
            
        try:
            with open(model_path, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            st.error(f"Failed to load model: {str(e)}")
            st.stop()