import streamlit as st
import requests
from pydantic import BaseModel
from typing import List

from app.config.settings import settings
from app.common.logger import get_logger

logger = get_logger(__name__)

st.set_page_config(page_title="Multi AI Agent", layout="centered")  # Changed "center" to "centered"
st.title("Multi AI Agent Chat")

system_prompt = st.text_area("Define your AI Agent: ", height=70)
selected_model = st.selectbox("Select Model:", options=settings.ALLOWED_MODEL_NAME)
allow_web_search = st.checkbox("Allow Web Search")
user_query = st.text_area("Enter your query: ", height=150)

API_URL = "http://127.0.0.1:9999/chat"


class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]
    allow_search: bool  # Add this field


if st.button("Ask Agent") and user_query.strip():
    payload = RequestState(
        model_name=selected_model,
        system_prompt=system_prompt,
        messages=[user_query],  # Wrap user_query in a list
        allow_search=allow_web_search,
    ).dict()

    try:
        logger.info("Sending request to backend")
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            agent_response = response.json().get("response", "")
            logger.info("Received response from backend")
            st.subheader("Agent Response")
            st.markdown(agent_response.replace("\n", "<br>"), unsafe_allow_html=True)
        else:
            logger.error(f"Error from backend: {response.text}")
            st.error(f"Error with backend: {response.text}")

    except Exception as e:
        logger.error(f"Exception occurred while sending request to backend: {str(e)}")
        st.error(f"An error occurred: {str(e)}")