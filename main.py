#import OS and dotenv for reading api key from .env file
import os
from dotenv import load_dotenv
load_dotenv()

#load api key
api_key = os.environ.get("GEMINI_API_KEY")

#import gemini genai
from google import genai

#map client to apikey
client = genai.Client(api_key=api_key)

# user provides prompt during script execution
import sys

if len(sys.argv) < 2:
    print("please provide a prompt.")
    sys.exit(1)

#join the user input for prompt
user_prompt = " ".join(sys.argv[1:])

#user input list
from google.genai import types

messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]

#create a response model to print response text to the console
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages,
) 
   
# log prompt tokens used
prompt_tokens = response.usage_metadata.prompt_token_count

# log response tokens used
response_tokens = response.usage_metadata.candidates_token_count

# print response text, prompt tokens consumend, and response tokens consumed
print(response.text)
print(f"Prompt tokens: {prompt_tokens}"),
print(f"Response tokens: {response_tokens}")


def main():
    print("Hello from aiagent!")


if __name__ == "__main__":
    main()
