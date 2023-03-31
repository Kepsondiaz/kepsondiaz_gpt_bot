from dotenv import load_dotenv
import openai
import os 

load_dotenv()   

openai.api_key = os.getenv("CHATGPT_API_KEY")


def chatgpt_response(prompt):
    response = openai.Completion.create(
        model= "text-davinci-003",
        prompt= prompt,
        temperature= 1,
        max_tokens=100,
    )

    response_dict = response.get