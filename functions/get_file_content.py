import os

from settings import MAX_CHARS


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
