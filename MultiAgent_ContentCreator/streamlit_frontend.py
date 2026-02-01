import streamlit as st
from dotenv import load_dotenv
from AgenCrew import run_tech_crew

load_dotenv()

st.set_page_config(page_title="Multi-Agent Tech Team", layout="wide")
st.title("CrewAI Hierarchical Team")

with st.sidebar:
    st.header("Configuration")
    provider = st.selectbox("LLM Provider", ["Google Gemini", "Groq (Llama 3)", "OpenAI"])

topic = st.text_input("Enter a Tech Topic:", placeholder="e.g. AI in Space Exploration")

if st.button("Start Tech Crew", type="primary"):
    if not topic:
        st.error("Please enter a topic.")
    else:
        with st.status(" Crew is collaborating...", expanded=True):
            # Calling the backend function
            result = run_tech_crew(provider, topic)
        
        st.divider()
        st.subheader(" Final Article")
        st.markdown(result)