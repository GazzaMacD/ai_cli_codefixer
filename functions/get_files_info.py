import os


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
