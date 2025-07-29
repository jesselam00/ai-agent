import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

def main():
    verbose_flag = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Agent")
        print("\nUsage: python main.py 'your prompt here' [--verbose]")
        print("Example: python main.py 'How do I build a calculator app?'")
        sys.exit(1)

    user_prompt = " ".join(args)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    resp = generate_content(client, messages)

    if verbose_flag:
        print("User prompt:", user_prompt)
        print("Prompt tokens:", resp.usage_metadata.prompt_token_count)
        print("Response tokens: ", resp.usage_metadata.candidates_token_count)

    print("Response:")
    print(resp.text)

def generate_content(client, messages):
    resp = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages
    )
    return resp

if __name__ == "__main__":
    main()
