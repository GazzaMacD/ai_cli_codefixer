import os
import subprocess


def run_python_file(working_directory, file_path):
    """Run arbitary python code within the working directory"""
    if not file_path or not isinstance(file_path, str):
        return "Error: The second argument to get_files_info is required and must be a string"
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    cwd_path = os.path.abspath(working_directory)
    print("cwd", cwd_path)

    if working_directory not in abs_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        capture = subprocess.run(
            ["python3", abs_path],
            text=True,
            timeout=30,
            capture_output=True,
            cwd=cwd_path,
        )
        if capture.returncode == 0:
            return f"Return code: {capture.returncode}\nSTDOUT: {capture.stdout}\nSTDERROR: {capture.stderr}"
        else:
            return f"Return code: {capture.returncode}\nSTDOUT: {capture.stdout}\nSTDERROR: {capture.stderr}\nProcess exited with code {capture.returncode}"

    except Exception as e:
        return f"Error: executing Python file: {e}"
