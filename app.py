import streamlit as st
from pipeline import run_pipeline_from_pdf

st.set_page_config(page_title="AI Resume Enhancer", layout="centered")

st.title("🤖 AI Resume Enhancer")

upload_file = st.file_uploader("📄 Upload your resume (PDF only)", type=['pdf'])
job_description = st.text_area("🧠 (Optional) Paste target job description")

if st.button("🚀 Enhance Resume"):
    if not upload_file:
        st.warning("Please upload a resume in PDF format.")
    else:
        with open("temp_resume.pdf", "wb") as f:
            f.write(upload_file.getbuffer())

        with st.spinner("Processing your resume..."):
            result = run_pipeline_from_pdf("temp_resume.pdf", job_description or None)

        st.success("Enhancement complete!")

        st.subheader("✨ Professional Summary")
        st.write(result["summary"])

        st.markdown("---")
        st.subheader("💼 Enhanced / Tailored Bullet Points")
        for b in result["bullets"]:
            st.write(f"- {b}")
