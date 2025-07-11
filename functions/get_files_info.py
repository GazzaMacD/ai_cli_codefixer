# get_files_info.py
import os
import subprocess

MAX_CHARS = 10000
FILE_EXTENSIONS = [".py", ".txt"]


def get_files_info(working_directory, directory=None):
    """One level deep check for a directory to get basic information about the files and dirs in it"""
    if not directory or not isinstance(directory, str):
        return "Error: The second argument to get_files_info is required and must be a string"
    path = os.path.abspath(os.path.join(working_directory, directory))
    if working_directory not in path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'
    info = ""
    for content in os.listdir(path):
        path_to_content = os.path.join(path, content)
        if os.path.isfile(path_to_content):
            info += f"- {content}: file_size={os.path.getsize(path_to_content)}, is_dir=False\n"
        else:
            info += f"- {content}: file_size={os.path.getsize(path_to_content)}, is_dir=True\n"
    return info


def get_file_content(working_directory, file_path):
    """Get the content of a file as a string and return it. Make sure file is not out of the scope of the directory.
    If the file is not string based then error"""
    if not file_path or not isinstance(file_path, str):
        return "Error: The second argument to get_files_info is required and must be a string"
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    if working_directory not in abs_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_path, "r") as in_file:
            chars = in_file.read(MAX_CHARS + 1)
            if len(chars) > MAX_CHARS:
                return (
                    chars[0:MAX_CHARS]
                    + f'[...File "{file_path}" truncated at 10000 characters]'
                )

            return chars

    except Exception as e:
        return f"Error: {e}"


def write_file(working_directory, file_path, content):
    """Write a file within the working directory"""
    if not file_path or not isinstance(file_path, str):
        return "Error: The second argument to get_files_info is required and must be a string"
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    if working_directory not in abs_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if os.path.exists(abs_path) and os.path.isfile(abs_path):
            with open(abs_path, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        elif not os.path.exists(abs_path) and any(
            (x in file_path.split("/")[-1:][0]) for x in FILE_EXTENSIONS
        ):
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)
            with open(abs_path, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

        # Error paths below
        elif os.path.exists(abs_path) and os.path.isdir(abs_path):
            return (
                f'Error: Cannot write to "{file_path}" as it is a directory not a file'
            )
        else:
            return f'Error: Cannot write to "{file_path}" does not have a file with a valid file extension. Please use {FILE_EXTENSIONS}'
    except Exception as e:
        return f"Error: {e}"


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
