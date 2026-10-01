import os
import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔎"
)

st.title("🔎 AI Research Agent")
st.write("Enter a topic and get a simple AI research report.")

HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(
    provider="hf-inference",
    api_key=HF_TOKEN
)

topic = st.text_input(
    "Enter your research topic",
    placeholder="e.g. Reinforcement Learning"
)

if st.button("🔍 Start Research"):

    if not topic:
        st.warning("Please enter a topic.")
        st.stop()

    with st.spinner("Researching..."):

        try:
            prompt = f"""
You are a helpful research assistant.

Research topic: {topic}

Write a beginner-friendly research report with:

1. Introduction
2. Definition
3. Main concepts
4. Important facts
5. Real-life examples
6. Advantages
7. Limitations
8. Conclusion

Use simple English.
"""

            result = client.chat_completion(
                model="Qwen/Qwen2.5-72B-Instruct",
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
            st.write(result.choices[0].message.content)

        except Exception as e:
            st.error("Something went wrong.")
            st.write(str(e))
