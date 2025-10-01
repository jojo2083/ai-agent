#import OS and dotenv for reading api key from .env file
import os
from dotenv import load_dotenv
from functions.get_files_info import *
load_dotenv()

SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""




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
    model='gemini-2.0-flash-001',
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions],system_instruction=SYSTEM_PROMPT),
    ) 
   
# log prompt tokens used
prompt_tokens = response.usage_metadata.prompt_token_count

# log response tokens used
response_tokens = response.usage_metadata.candidates_token_count

def main():
    print("Hello from aiagent!")

for arg in sys.argv[1:]:
    if arg == "--verbose":
        print(f"Prompt tokens: {prompt_tokens}"),
        print(f"Response tokens: {response_tokens}"),
        print(f"User prompt: {user_prompt}")

    if response.function_calls != None:
        for call in response.function_calls:
            print(f"Calling function: {call.name}({call.args})")
    else:
        print(f'{response.text}')

#print(get_files_info("calculator","pkg"))

if __name__ == "__main__":
    main()
