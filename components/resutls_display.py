import streamlit as st

class ResultsDisplay:
    @staticmethod
    def display(prediction, probability):
        """Display prediction results with clear formatting"""
        st.markdown("---")
        st.subheader("🩺 Assessment Result")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            if prediction == 1:
                st.error("## 🚨 Parkinson's POSITIVE")
                st.metric("Probability Score", f"{probability:.1%}", 
                         help="Likelihood of Parkinson's based on sensor data")
                st.warning("**Clinical Interpretation:**\n\nPatterns consistent with Parkinsonian symptoms detected")
            else:
                st.success("## ✅ Parkinson's NEGATIVE")
                st.metric("Probability Score", f"{1-probability:.1%}", 
                         help="Likelihood of NOT having Parkinson's based on sensor data")
                st.info("**Clinical Interpretation:**\n\nNo strong indicators of Parkinsonism detected")
        
        with col2:
            if prediction == 1:
                st.markdown("""
                **What This Means:**
                - Sensor readings show patterns associated with Parkinson's disease
                - Motor control and resting tremor indicators were significant
                - Further clinical evaluation recommended
                
                **Next Steps:**
                1. Consult a movement disorder specialist
                2. Consider comprehensive neurological exam
                3. Monitor symptoms regularly
                """)
            else:
                st.markdown("""
                **What This Means:**
                - No concerning patterns detected in sensor readings
                - Motor function appears within normal ranges
                - Continue regular monitoring as preventive measure
                
                **Preventive Recommendations:**
                1. Maintain regular physical activity
                2. Consider neuroprotective diet
                3. Annual neurological check-ups
                """)