import os
import google.generativeai as genai
from dotenv import load_dotenv
from backend.models import appliance_info

load_dotenv()

def initialize_gemini():
    api_key = os.environ.get("Gemini_api_1")
    if not api_key:
        raise ValueError("Gemini api key was not set in .env")
    genai.configure(api_key=api_key)

async def call_gemini(info: appliance_info):
    model = genai.GenerativeModel("gemini-2.5-flash") #changeable to other models
    prompt =( f"What is the typical wattage per hour in the Philippines of a "
        f"{info.name}, {info.type}? Please return only the number in watts." 
    )
    response = await model.generate_text_async(prompt=prompt)
    text = response.text.strip()

    try:
        watts = float(''.join(filter(lambda c: c.isdigit() or c == '.', text)))
    except:
        raise ValueError(f"AI returned invalid wattage: {text}")
    return watts

    