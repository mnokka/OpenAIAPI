# inspired by Udemy course  LLM Engineering: Master AI, Large Language Models & Agents
#



import os
from dotenv import load_dotenv
from openai import OpenAI



load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("API KEY NOT FOUND. CHECK .env FILE")
    exit(1)


small_model = "gpt-3.5-turbo"
big_model= "gpt-4o"

prompt_small= "You are a chatbot who just wants to end the conversation quickly. Your behaviour is like an army drill sergeant"
prompt_big = "You are a chatbot who wants to keep conversation going. You try move conversation about talking cats"

small_messages = ["Hello. When we go home"]
big_messages = ["Hello there, it is a lovely day. Maybe we could take a cat to the walk"]

openai = OpenAI(api_key=api_key)

###################################################################################################
# conversation requires taking all previous communications and feeding them in again , every time
# there is no real memory of the previous conversation
    
    
def call_small():
    messages = [{"role": "system", "content": prompt_small}]
    for small, big in zip(small_messages, big_messages):
         messages.append({"role": "assistant", "content": small})
         messages.append({"role": "user", "content": big})
    completion = openai.chat.completions.create(
    model=small_model,
    messages=messages
    )
    return completion.choices[0].message.content
    
    
    
def call_big():
    messages = [{"role": "system", "content": prompt_big}]
    for small, big in zip(small_messages, big_messages):
        messages.append({"role": "assistant", "content": small})
        messages.append({"role": "user", "content": big})
    completion = openai.chat.completions.create(
    model=big_model,
    messages=messages
    )
    return completion.choices[0].message.content

#########################################################################################################



def main():


    print(f"SMALL:\n{small_messages[0]}\n")
    print(f"BIG:\n{big_messages[0]}\n")

    for i in range(5):
        print(f"----ROUND {i+1}----")
        small_next = call_small()
        print(f"SMALL:\n{small_next}\n")
        small_messages.append(small_next)
    
        big_next = call_big()
        print(f"BIG:\n{big_next}\n")
        big_messages.append(big_next)
    
    
###########################################################################################################    
if __name__ == "__main__":
    main() 


    
    