import os

from settings import FILE_EXTENSIONS


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
