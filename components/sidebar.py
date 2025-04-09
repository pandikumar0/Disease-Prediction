import streamlit as st

class Sidebar:
    @staticmethod
    def display():
        with st.sidebar:
            st.title("🧠 Parkinson's Assessment")
            st.markdown("""
            **About This Tool:**
            This AI analyzes sensor data to assess Parkinson's risk using:
            - Machine learning predictions
            - Explainable AI (LIME)
            - Clinical insights
            """)
            
            st.markdown("---")
            st.markdown("**Key Features:**")
            st.markdown("""
            - Clear positive/negative results
            - Probability scoring
            - Detailed explanations
            - Actionable recommendations
            """)
            
            st.markdown("---")
            st.markdown("**Clinical Resources:**")
            st.markdown("""
            - [MDS Diagnostic Criteria](https://www.movementdisorders.org/)
            - [Treatment Guidelines](https://www.parkinson.org/)
            - [Research Updates](https://www.michaeljfox.org/)
            """)