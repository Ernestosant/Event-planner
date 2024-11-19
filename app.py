import streamlit as st
from features import get_event_plan, extract_event_details
import PyPDF2

st.title("Automatic Event Planner")

st.write("Please enter a description of your event or upload a PDF or TXT file with the event details.")

event_description = st.text_area("Event Description", "")

uploaded_file = st.file_uploader("Upload a file", type=['txt', 'pdf'])

if uploaded_file is not None:
    if uploaded_file.type == "text/plain":
        file_text = uploaded_file.read().decode('utf-8')
    elif uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        file_text = ""
        for page in pdf_reader.pages:
            file_text += page.extract_text()
    else:
        st.error("Unsupported file type.")
        file_text = ""
else:
    file_text = ""

event_details = event_description + "\n" + file_text

if st.button("Generate Event Plan"):
    if event_details.strip() == "":
        st.error("Please provide event details.")
    else:
        with st.spinner("Generating event plan..."):
            event_details = extract_event_details(event_details)
            event_plan = get_event_plan(event_details)
        st.success("Event plan generated:")
        st.write(event_plan)
