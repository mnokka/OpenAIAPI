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

system_message = "You are computer programming teacher"
user_prompt = "Qt5 C++ UI based hello world with menu providing info section. Info section includes name of the programmer, like Urho Kalevala"

prompts = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": user_prompt}
  ]


try:
    response: ChatCompletion = client.chat.completions.create(
        model="gpt-4",
        messages=prompts 
    )
    print("API OK, response:")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"General error happened: {e}")
