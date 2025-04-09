from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=GOOGLE_API_KEY)

def get_gemini_response(hasDisease, features):

    query = f"""You are a medical assistant AI helping analyze sensor data for early detection and support of Parkinson's Disease. 

                Given a set of sensor feature names and values:
                {features}
                And a boolean field `is_positive` indicating Parkinsons detection (true = positive, false = negative) which value is: {hasDisease}

                If **is_positive** is `true`, provide:
                1. The **most affected part of the body** based on the given feature values.
                2. Suggested **mitigation steps** with medical reasoning.
                3. Recommended **exercises** and **food habits**, including justification for each recommendation.

                If **is_positive** is `false`, provide:
                1. A brief explanation of **potential risks or early signs** visible from the data.
                2. Recommended **precautionary steps** to avoid progression or onset.
                3. Lifestyle and diet recommendations to maintain neurological health.

                Ensure the response is medically relevant, clear, and actionable."""

    try:
         
       response = client.models.generate_content_stream(
                        model="gemini-2.0-flash", 
                        contents=query
        )
       for chunk in response:
          yield chunk.text
            
    except Exception as e:
        return f"Error generating response: {str(e)}"