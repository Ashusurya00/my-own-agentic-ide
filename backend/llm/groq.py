import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def groq_generate(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an expert frontend engineer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content
