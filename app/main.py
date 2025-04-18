# app/main.py

import streamlit as st
from datetime import datetime
import os

from version_tracker import log_version_change, get_current_log
from task_flow import get_flow_status
from gpt_engine import call_gpt_summary
from processor import extract_text_from_file

# --- Setup
st.set_page_config(
    page_title="Content Intelligence Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar
st.sidebar.title("🧠 Project Control Center")
project_name = st.sidebar.text_input("📁 Project Name", "Demo Project")
user_role = st.sidebar.selectbox("👤 Role", ["Analyst", "Manager", "Executive", "General"])
section = st.sidebar.radio("🧭 Navigate", ["Upload + Interpret", "Saved Agents", "Task Tracker", "Version Log"])

st.sidebar.markdown("---")
if st.sidebar.button("📌 Log Version Update"):
    log_version_change(component="main.py", summary="GPT integration + file parser live", developer="Van")
    st.sidebar.success("Version Logged!")

# --- Main Area
st.title(f"🧠 Content Intelligence Engine — {project_name}")

if section == "Upload + Interpret":
    st.subheader("📂 Upload Content for Interpretation")
    uploaded_file = st.file_uploader("Drop a file here", type=["pdf", "docx", "xlsx", "txt"])
    custom_prompt = st.text_area("🔍 Optional: Add a custom instruction or prompt", height=100)

    if uploaded_file:
        st.markdown("✅ File received. Click below to interpret.")
        if st.button("🧠 Interpret with GPT"):
            with st.spinner("Reading and analyzing content..."):
                extracted_text = extract_text_from_file(uploaded_file)
                result = call_gpt_summary(extracted_text, role=user_role, custom_instruction=custom_prompt)
                st.markdown("### 🧠 Interpretation Output")
                st.markdown(result)
    else:
        st.info("Upload a file to begin interpretation.")

elif section == "Saved Agents":
    st.subheader("🧠 Saved Agent Configurations")
    st.info("Listing will appear here... [coming soon]")

elif section == "Task Tracker":
    st.subheader("📋 Task Flow Tracker")
    flow_data = get_flow_status()
    st.table(flow_data)

elif section == "Version Log":
    st.subheader("🛠 Version History")
    log_df = get_current_log()
    st.dataframe(log_df)

# Footer
st.markdown("---")
st.caption("🧬 Powered by GPT | Version-controlled | Modular by design")