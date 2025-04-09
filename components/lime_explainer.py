import streamlit as st
from constants import ORDERED_FEATURES
from lime.lime_tabular import LimeTabularExplainer
import numpy as np

class LimeExplainer:
    @staticmethod
    def create_explainer():
        """Create LIME explainer with error handling"""
        try:
            return LimeTabularExplainer(
                training_data=np.zeros((2, len(ORDERED_FEATURES))),
                feature_names=ORDERED_FEATURES,
                mode="classification",
                random_state=42
            )
        except Exception as e:
            st.error(f"Failed to create LIME explainer: {str(e)}")
            st.stop()
    
    @staticmethod
    def explain(model, input_df):
        """Generate LIME explanation with robust error handling"""
        explainer = LimeExplainer.create_explainer()
        
        try:
            exp = explainer.explain_instance(
                input_df.iloc[0].values,
                model.predict_proba,
                num_features=10,
                top_labels=1
            )
            return exp
        except Exception as e:
            st.error(f"Failed to generate LIME explanation: {str(e)}")
            st.stop()