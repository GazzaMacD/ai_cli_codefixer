from google.genai import types as genai_types

# Constants
MAX_CHARS = 10000
FILE_EXTENSIONS = [".py", ".txt"]

# Prompts
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

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

# Available functions
available_functions = genai_types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)
