import streamlit as st
import pandas as pd
from constants import FEATURE_GROUPS, ORDERED_FEATURES,DEFAULT_VALUES

class UserInput:
    @staticmethod
    def get_input():
        """Get user input with validation"""
        st.header("📝 Enter Sensor Readings")
        user_input = {}
        index = 0
        
        for group, features in FEATURE_GROUPS.items():
            with st.expander(f"🔹 {group}", expanded=False):
                cols = st.columns(3)
                for i, feature in enumerate(features):
                    try:
                        user_input[feature] = cols[i % 3].number_input(
                            f"{feature}", 
                            format="%.5f", 
                            key=feature, 
                            value=float(DEFAULT_VALUES[index])
                        )
                        index += 1
                    except Exception as e:
                        st.error(f"Error with {feature}: {str(e)}")
                        user_input[feature] = 0.0
        
        try:
            return pd.DataFrame([user_input])[ORDERED_FEATURES]
        except Exception as e:
            st.error(f"Error creating input DataFrame: {str(e)}")
            st.stop()