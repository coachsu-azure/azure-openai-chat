"""
    Azure Open AI Chat (Application)
"""
import os
import pathlib
from dotenv import load_dotenv
from openai import AzureOpenAI
import openai

# Load .env if it exists
env_path = pathlib.Path(".env")
if env_path.exists():
    load_dotenv(dotenv_path=env_path, override=True)

# Set environment variables
KEY = os.getenv('KEY')
ENDPOINT = os.getenv('ENDPOINT')
VERSION = os.getenv('VERSION')
MODEL = os.getenv('MODEL')

try:
    # Create the Azure OpenAI client
    client = AzureOpenAI(
        api_key=KEY,  
        azure_endpoint=ENDPOINT,
        api_version=VERSION
    )

    # A sample API call for chat completions looks as follows:
    # Messages must be an array of message objects, where each object has 
    # a role (either "system", "user", or "assistant") and 
    # content (the content of the message).
    response = client.chat.completions.create(
                  model=MODEL,
                  messages=[
                        {"role": "system", "content": "You are a travel professional."},
                        {"role": "user", "content": "How would you introduce Ilan city in Taiwan?"}
                    ]
                )

    # print the response
    print(response.choices[0].message.content)

except openai.AuthenticationError as e:
    # Handle Authentication error here, e.g. invalid API key
    print(f"OpenAI API returned an Authentication Error: {e}")

except openai.APIConnectionError as e:
    # Handle connection error here
    print(f"Failed to connect to OpenAI API: {e}")

except openai.BadRequestError as e:
    # Handle connection error here
    print(f"Invalid Request Error: {e}")

except openai.RateLimitError as e:
    # Handle rate limit error
    print(f"OpenAI API request exceeded rate limit: {e}")

except openai.InternalServerError as e:
    # Handle Service Unavailable error
    print(f"Service Unavailable: {e}")

except openai.APITimeoutError as e:
    # Handle request timeout
    print(f"Request timed out: {e}")
    
except openai.APIError as e:
    # Handle API error here, e.g. retry or log
    print(f"OpenAI API returned an API Error: {e}")

except:
    # Handles all other exceptions
    print("An exception has occured.")
