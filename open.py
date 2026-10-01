import os
import streamlit as st
from huggingface_hub import InferenceClient


# -----------------------------
# Page Settings
# -----------------------------

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔎",
    layout="centered"
)


# -----------------------------
# App Title
# -----------------------------

st.title("🔎 AI Research Agent")

st.write(
    "Enter a topic and get a simple AI-generated research report."
)


# -----------------------------
# Hugging Face API
# -----------------------------

HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(
    provider="hf-inference",
    api_key=HF_TOKEN
)


# -----------------------------
# User Input
# -----------------------------

topic = st.text_input(
    "Enter your research topic",
    placeholder="e.g. Reinforcement Learning"
)


# -----------------------------
# Research Button
# -----------------------------

if st.button("🔍 Start Research"):

    if not topic:
        st.warning("Please enter a research topic.")
        st.stop()

    with st.spinner("Researching..."):

        try:

            prompt = f"""
You are a helpful AI research assistant.

Research topic:
{topic}

Create a beginner-friendly research report.

Include the following sections:

1. Introduction
2. Definition
3. Main Concepts
4. Important Facts
5. Real-Life Applications
6. Advantages
7. Limitations
8. Conclusion

Use simple English.
Explain difficult concepts in an easy way.
Use clear headings and bullet points where useful.
Do not make up information.
"""

            # -----------------------------
            # AI Model
            # -----------------------------

            result = client.chat_completion(
                model="HuggingFaceH4/zephyr-7b-beta",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=1200
            )

            # -----------------------------
            # Show Result
            # -----------------------------

            st.success("Research completed!")

            st.subheader("📄 Research Report")

            st.write(
                result.choices[0].message.content
            )

        except Exception as e:

            st.error("Something went wrong.")

            st.code(str(e))
