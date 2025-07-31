import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.exists(abs_working_dir):
            os.makedirs(abs_working_dir)
        with open(target_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: Unable to write file. {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes a file in the specified file_path with the content provided, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The working directory to perform the function in.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write the content into, relative to the working directory. If the working directory is not provided, it will create the directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write into the file.",
            ),
        },
        required=["working_directory", "file_path", "content"]
    ),
)