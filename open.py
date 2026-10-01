import os
import streamlit as st
from openai import OpenAI

# OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Page settings
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔎",
    layout="centered"
)

# Title
st.title("🔎 AI Research Agent")
st.write(
    "Enter a topic and the agent will research it using web search "
    "and generate a simple research report."
)

# Topic input
topic = st.text_input(
    "Enter your research topic",
    placeholder="e.g. Reinforcement Learning"
)

# Research button
if st.button("🔍 Start Research"):

    if not topic:
        st.warning("Please enter a research topic.")
        st.stop()

    with st.spinner("Researching the topic..."):

        try:
            response = client.responses.create(
                model="gpt-5-mini",
                tools=[
                    {
                        "type": "web_search_preview"
                    }
                ],
                input=f"""
You are an AI research assistant.

Research the following topic using web search:

Topic: {topic}

Create a clear and beginner-friendly research report.

Include:

1. Introduction
2. Definition
3. Main concepts
4. Important facts
5. Real-life applications
6. Advantages
7. Limitations
8. Conclusion
9. Sources

Use reliable and relevant sources.
Do not make up facts.
Keep the explanation simple and easy to understand.
"""
            )

            st.success("Research completed!")

            st.subheader("📄 Research Report")

            st.write(response.output_text)

        except Exception as e:
            st.error("Something went wrong.")
            st.code(str(e))
