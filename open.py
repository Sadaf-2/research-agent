import os
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔎"
)

st.title("🔎 AI Research Agent")
st.write("Enter a topic and get a simple AI research report.")

HF_TOKEN = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN
)

topic = st.text_input(
    "Enter your research topic",
    placeholder="e.g. Artificial Intelligence"
)

if st.button("🔍 Start Research"):

    if not topic:
        st.warning("Please enter a topic.")
        st.stop()

    with st.spinner("Researching..."):

        try:

            prompt = f"""
You are a helpful AI research assistant.

Research topic: {topic}

Create a beginner-friendly research report.

Include:

1. Introduction
2. Definition
3. Main Concepts
4. Important Facts
5. Real-Life Applications
6. Advantages
7. Limitations
8. Conclusion

Use simple English.
Use clear headings.
Use bullet points where useful.
Do not make up information.
"""

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=1200
            )

            st.success("Research completed!")

            st.subheader("📄 Research Report")

            st.write(
                response.choices[0].message.content
            )

        except Exception as e:

            st.error("Something went wrong.")
            st.code(str(e))
