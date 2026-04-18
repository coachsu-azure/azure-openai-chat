"""
    Azure Open AI Chat (Web Application)
"""
import os
import pathlib
from dotenv import load_dotenv
from openai import AzureOpenAI
import openai
from flask import Flask, request, render_template

# Load .env if it exists
env_path = pathlib.Path(".env")
if env_path.exists():
    load_dotenv(dotenv_path=env_path, override=True)

# Set environment variables
KEY = os.getenv('KEY')
ENDPOINT = os.getenv('ENDPOINT')
VERSION = os.getenv('VERSION')
MODEL = os.getenv('MODEL')

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def openAIChat():
    role = ""
    q = ""
    answer = ""

    if request.method == 'POST':
        role = request.form.get("role")
        q = request.form.get("q")

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
                   {"role": "system", "content": role},
                   {"role": "user", "content": q}
                ]
         )

            answer = response.choices[0].message.content

        except openai.AuthenticationError as e:
            # Handle Authentication error here, e.g. invalid API key
            answer =  f"OpenAI API returned an Authentication Error: {e}"

        except openai.APIConnectionError as e:
            # Handle connection error here
            answer =  f"Failed to connect to OpenAI API: {e}"

        except openai.BadRequestError as e:
            # Handle bad request error here
            answer =  f"Invalid Request Error: {e}"

        except openai.RateLimitError as e:
            # Handle rate limit error
            answer =  f"OpenAI API request exceeded rate limit: {e}"

        except openai.InternalServerError as e:
            # Handle Service Unavailable error
            answer =  f"Service Unavailable: {e}"

        except openai.APITimeoutError as e:
            # Handle request timeout
            answer =  f"Request timed out: {e}"

        except openai.APIError as e:
            # Handle API error here, e.g. retry or log
            answer =  f"OpenAI API returned an API Error: {e}"

        except:
            # Handles all other exceptions
            answer =  f"An exception has occured."

    return render_template("index.html",
                           role=role,
                           q=q,
                           answer=answer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
