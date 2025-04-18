# app/gpt_engine.py

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import os
from dotenv import load_dotenv

load_dotenv()


def call_gpt_summary(text, role="General", custom_instruction=None):
    """Calls GPT to interpret the document content"""

    base_prompt = f"""
You are an expert AI assistant helping a {role}.
Given the following document, please identify:
1. Purpose of the content
2. A short summary in 3 bullet points
3. 2-3 potential use cases
4. 2 action recommendations based on the content

Document:
{text}
"""

    if custom_instruction:
        base_prompt += f"\n\nAdditional Instruction: {custom_instruction}"

    try:
        response = client.chat.completions.create(model="gpt-4",
        messages=[
            {"role": "system", "content": "You analyze business documents for strategic and operational insight."},
            {"role": "user", "content": base_prompt}
        ],
        temperature=0.5,
        max_tokens=600)
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ GPT Error: {str(e)}"
