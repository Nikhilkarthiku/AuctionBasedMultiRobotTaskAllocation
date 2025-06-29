import openai
from dotenv import load_dotenv

load_dotenv()

class SummarizerAgent:
    def __init__(self):
        pass
        
    def summarize(self, text: str) -> str:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes scientific documents."},
                {"role": "user", "content": f"Summarize the following content:\n{text[:3000]}"}
            ],
            temperature=0.5,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()