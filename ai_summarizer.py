# ai_summarizer.py
import requests
import dotenv
import os
dotenv.load_dotenv()

def summarize_news(news_list):
    prompt = "Summarize this news in simple words:\n" + "\n".join(news_list)

    response = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={os.getenv('gemini_apiKey')}",
        json={"contents": [{"parts": [{"text": prompt}]}]}
    )

    data = response.json()
    

    #  Check for errors
    if "candidates" not in data:
        if "error" in data:
            return f"Gemini API error: {data['error'].get('message', 'Unknown error')}"
        return "Unexpected error: 'candidates' not found in response"

    return data["candidates"][0]["content"]["parts"][0]["text"]
