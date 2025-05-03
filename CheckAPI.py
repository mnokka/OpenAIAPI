import os
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletion

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("API KEY NOT FOUND. CHECK .env FILE")
    exit(1)


client = OpenAI(api_key=api_key)


try:
    response: ChatCompletion = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Ping. Testi new key"}]
    )
    print("API OK, response:")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"General error happened: {e}")
