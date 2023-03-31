from dotenv import load_dotenv
import openai
import os 

load_dotenv()   

openia.api_key = os.getenv("CHATGPT_API_KEY")


def chatgpt_response(prompt):
    response = openai.Completion.create(

    )