import os
import sys

from dotenv import load_dotenv
from google.genai import Client
from google.genai import types as genai_types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = Client(api_key=api_key)


def main():
    user_prompt = None
    flag1 = None
    if len(sys.argv) < 2:
        print("Error: A text query for the LLM is required after main.py")
        exit(1)
    user_prompt = sys.argv[1]

    if len(sys.argv) == 3:
        flag1 = sys.argv[2]

    messages = [
        genai_types.Content(role="user", parts=[genai_types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=messages
    )

    if flag1 and flag1 == "--verbose":
        print(response.text)
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
