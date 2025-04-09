import streamlit as st
from constants import ORDERED_FEATURES
import numpy as np
import matplotlib.pyplot as plt

class DataVisualizer:
    @staticmethod
    def visualize(input_df):
        """Visualize sensor data with error handling"""
        try:
            st.subheader("📈 Sensor Data Visualization")
            
            if 'sensor_type' not in st.session_state:
                st.session_state.sensor_type = "EEG"
            
            sensor_type = st.selectbox(
                "Select sensor type to visualize:", 
                ["EEG", "EMG", "Accelerometer", "Gyroscope"], 
                key='sensor_type'
            )
            
            if sensor_type == "EEG":
                eeg_features = [f for f in ORDERED_FEATURES if f in ['FP1', 'FP2', 'F3', 'F4', 'C3', 'C4', 'O1', 'O2']]
                fig, ax = plt.subplots(figsize=(12, 6))
                input_df[eeg_features].iloc[0].plot(kind='bar', ax=ax)
                ax.set_title("EEG Sensor Readings")
                ax.set_ylabel("Value")
                ax.tick_params(axis='x', rotation=45)
                st.pyplot(fig)
            
            elif sensor_type == "EMG":
                emg_features = [f for f in ORDERED_FEATURES if 'EMG' in f]
                fig, ax = plt.subplots(figsize=(10, 4))
                input_df[emg_features].iloc[0].plot(kind='bar', ax=ax, color='red')
                ax.set_title("EMG Sensor Readings")
                ax.set_ylabel("Value")
                ax.tick_params(axis='x', rotation=45)
                st.pyplot(fig)
            
            elif sensor_type in ["Accelerometer", "Gyroscope"]:
                sensor_prefix = "ACC" if sensor_type == "Accelerometer" else "GYRO"
                locations = ["LShank", "RShank", "Waist", "Arm"]
                
                fig, axes = plt.subplots(2, 2, figsize=(12, 8))
                axes = axes.flatten()
                
                for i, loc in enumerate(locations):
                    features = [f for f in ORDERED_FEATURES if f.startswith(loc) and sensor_prefix in f]
                    if features:
                        input_df[features].iloc[0].plot(kind='bar', ax=axes[i], title=loc)
                        axes[i].set_ylabel("Value")
                        axes[i].tick_params(axis='x', rotation=45)
                
                plt.tight_layout()
                st.pyplot(fig)
        except Exception as e:
            st.error(f"Failed to visualize data: {str(e)}")