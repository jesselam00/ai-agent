import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    target_path  = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    command = ["python", file_path] + args

    try:
        completed_process = subprocess.run(
            command, 
            timeout=30, 
            capture_output=True,
            text=True,
            cwd=abs_working_dir
        )
        if completed_process.stdout is None and completed_process.stderr is None:
            return "No output produced."
        outputs = []
        if completed_process.stdout is not None:
            outputs.append("STDOUT: " + completed_process.stdout)
        if completed_process.stderr is not None:
            outputs.append("STDERR: " + completed_process.stderr)
        if completed_process.returncode != 0:
            outputs.append("Process exited with code " + completed_process.returncode)
        return "\n".join(outputs)
    except Exception as e:
        return  f"Error: executing Python file: {e}"