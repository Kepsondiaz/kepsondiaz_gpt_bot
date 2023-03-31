from dotenv import load_dotenv
import openia
import os 

load_dotenv()   

openia.api_key = os.getenv("CHATGPT_API_KEY")


def chatgpt_response(prompt):