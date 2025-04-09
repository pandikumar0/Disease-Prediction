import streamlit as st
from constants import IMPORTANT_FEATURES
import pandas as pd
from llm import get_gemini_response
class LLMResponse:
    @staticmethod
    def get_important_features(input_df: pd.DataFrame) -> dict:
        return {feature: input_df.at[0, feature] for feature in IMPORTANT_FEATURES if feature in input_df.columns}
    
    @staticmethod
    def display_response(prediction, input_df):
        st.subheader("Suggestions & Detailed Explanation")
        response = get_gemini_response(
            hasDisease=True if prediction==1 else False,
            features=LLMResponse.get_important_features(input_df)
        )
        response_container = st.empty()
        full_response = ""

        for chunk in response:
            full_response += chunk
            response_container.markdown(full_response)