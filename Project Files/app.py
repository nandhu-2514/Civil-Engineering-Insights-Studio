"""
Civil Engineering Insight Studio

A Streamlit web app that analyzes images of civil engineering structures
using Google Generative AI (Gemini) to generate professional engineering descriptions.

Usage:
  python -m streamlit run app.py
"""

import os
from PIL import Image
import streamlit as st
from dotenv import load_dotenv

import google.generativeai as genai


# ============================================================
# CONFIGURATION
# ============================================================

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")

if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found in .env file")
else:
    genai.configure(api_key=GOOGLE_API_KEY)


# ============================================================
# PROMPT
# ============================================================

TEXT_REPORT_PROMPT = """

Analyze the provided image of a civil engineering structure and generate
a clear, professional engineering description.

Include:
1. Structure Type
2. Construction Materials (with visual justification)
3. Estimated Dimensions (approximate)
4. Construction Methodology
5. Project Progress (completed vs pending)
6. Notable Engineering Features or Challenges
7. Recommendations

Add brief disclaimers about limitations of visual-only analysis.
"""


# ============================================================
# CORE FUNCTION
# ============================================================

def get_gemini_response(user_notes: str, pil_image: Image.Image) -> str:
    model = genai.GenerativeModel(GEMINI_MODEL)

    content = [TEXT_REPORT_PROMPT]

    if user_notes.strip():
        content.append(f"\nUser Notes: {user_notes}\n")

    content.append(pil_image)

    response = model.generate_content(content)
    return response.text


# ============================================================
# STREAMLIT UI
# ============================================================

def main():
    st.set_page_config(
        page_title="Civil Engineering Insight Studio",
        page_icon="🚧",
        layout="wide",
    )

    st.markdown("# Civil Engineering Insight Studio")
    st.markdown(
        "**AI-powered analysis of civil engineering structures using Google Gemini**"
    )
    st.divider()

    # Layout
    col_input, col_preview = st.columns([1, 1])

    # ---------------- INPUT PANEL ----------------
    with col_input:
        st.markdown("### Input")

        user_notes = st.text_area(
            "Additional context (optional)",
            height=80,
            placeholder="E.g., focus on materials or construction progress",
        )

        uploaded_file = st.file_uploader(
            "Upload an image (JPG / JPEG / PNG)",
            type=["jpg", "jpeg", "png"],
        )

        analyze_button = st.button(
            " Describe Structure",
            disabled=uploaded_file is None,
            type="primary",
            use_container_width=True,
        )

    # ---------------- IMAGE PREVIEW ----------------
    with col_preview:
        st.markdown("### Image Preview")

        if uploaded_file:
            try:
                pil_image = Image.open(uploaded_file).convert("RGB")
                st.image(pil_image, use_column_width=True)
            except Exception as e:
                st.error(f"Could not load image: {e}")
                pil_image = None
        else:
            st.info("Upload an image ")

    # ---------------- RESULTS ----------------
    st.divider()

    if analyze_button:
        if pil_image is None:
            st.error("Please upload a valid image.")
        else:
            with st.spinner("Analyzing structure with Gemini AI..."):
                try:
                    result = get_gemini_response(user_notes or "", pil_image)
                    st.success("Analysis Complete")

                    with st.expander(" Engineering Description", expanded=True):
                        st.markdown(result)

                except Exception as e:
                    st.error(f"Analysis failed: {e}")


if __name__ == "__main__":
    main()