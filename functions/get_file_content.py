import os
from config import MAX_CHARS
from google import genai

schema_get_file_content = genai.types.FunctionDeclaration(
    name="get_file_content",
    description="Lists file content in the specified directory, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isfile(abs_file_path) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    file_content_string = "" 
    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) >= MAX_CHARS:
            file_content_string += (
            f'[...File "{file_path}" truncated at 10000 characters]')
        return(file_content_string)
    except Exception as e:
        return f"Error: reading file: {e}"