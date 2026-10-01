import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

topic = input("Enter your research topic: ")

response = client.responses.create(
    model="gpt-5-mini",
    input=f"""
    Research the following topic and explain it in simple language:

    Topic: {topic}

    Give me:
    1. Introduction
    2. Main points
    3. Important facts
    4. Real-life examples
    5. Conclusion
    """
)

print("\n===== RESEARCH REPORT =====\n")
print(response.output_text)
