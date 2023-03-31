from dotenv import load_dotenv
import open
import os 

load_dotenv()   

open.api_key = os.getenv("CHATGPT_API_KEY")


def chatgpt_response(prompt):
    response = openai.Completion.create(
        
    )