import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function

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
    # TODO For now, it's hard coded to use ./calculator for the working directory
    user_prompt += "'./calculator' is the working directory"
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]
    )

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    resp = generate_content(client, messages, system_prompt, available_functions)

    if verbose_flag:
        print("User prompt:", user_prompt)
        print("Prompt tokens:", resp.usage_metadata.prompt_token_count)
        print("Response tokens: ", resp.usage_metadata.candidates_token_count)

    print("Response:")
    if resp.text is not None:
        print(resp.text)
    if resp.function_calls is not None:
        for function_call_part in resp.function_calls:
            try:
                content = call_function(function_call_part, verbose_flag)
                if not verbose_flag:
                    print(content.parts[0].function_response.response)
                else:
                    print(f"-> {content.parts[0].function_response.response}")
                # print(f"Calling function: {function_call_part.name}({function_call_part.args})")
            except Exception as e:
                raise Exception(f"Error: {e}")
        

def generate_content(client, messages, system_prompt, available_functions):
    resp = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], 
            system_instruction=system_prompt
        )
    )
    return resp

if __name__ == "__main__":
    main()
