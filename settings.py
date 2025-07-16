from google.genai import types as genai_types

# Constants
MAX_CHARS = 10000
FILE_EXTENSIONS = [".py", ".txt", ".md"]
WORKING_DIR = "calculator"

# Prompts
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


# Schema
schema_get_files_info = genai_types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=genai_types.Schema(
        type=genai_types.Type.OBJECT,
        properties={
            "directory": genai_types.Schema(
                type=genai_types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = genai_types.FunctionDeclaration(
    name="get_file_content",
    description="Get's the text content of a file, constrained to the working directory and a max number of characters. Will error if file is not text file ",
    parameters=genai_types.Schema(
        type=genai_types.Type.OBJECT,
        properties={
            "file_path": genai_types.Schema(
                type=genai_types.Type.STRING,
                description="The path to the file to read, relative to the working directory. If not provided, will error.",
            ),
        },
    ),
)

schema_write_file = genai_types.FunctionDeclaration(
    name="write_file",
    description="Write text content to a file specified by file_path, constrained to the working directory. Should only write files with extension specified in the constan 'FILE_EXTENSIONS'. Will error if file is not text file ",
    parameters=genai_types.Schema(
        type=genai_types.Type.OBJECT,
        properties={
            "file_path": genai_types.Schema(
                type=genai_types.Type.STRING,
                description="The path to the file to write, relative to the working directory. If not provided, will error.",
            ),
            "content": genai_types.Schema(
                type=genai_types.Type.STRING,
                description="The string content to write to the opened file",
            ),
        },
    ),
)

schema_run_python_file = genai_types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the python file as a subprocess in the working directory. Will error if file is not in the working directory or not a python file ",
    parameters=genai_types.Schema(
        type=genai_types.Type.OBJECT,
        properties={
            "file_path": genai_types.Schema(
                type=genai_types.Type.STRING,
                description="The path to the python file to run, relative to the working directory. If not provided, will error.",
            ),
        },
    ),
)

# Available functions
available_functions = genai_types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)
