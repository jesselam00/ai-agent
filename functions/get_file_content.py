import os

def get_file_content(working_directory, file_path):
    MAX_CHARS = 10000

    abs_working_dir = os.path.abspath(working_directory)
    target_fpath = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_fpath.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(target_fpath):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        content = ""
        with open(target_fpath, "r") as f:
            content = f.read(MAX_CHARS  + 1)
        if len(content) > 10000:
            content = content[:-1] + '\n\n[...File "{file_path}" truncated at 10000 characters]'
        return content
    except Exception as e:
        return f"Error: Could not get file content. {e}"
    return