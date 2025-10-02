import os
from google import genai

schema_write_file = genai.types.FunctionDeclaration(
    name="write_file",
    description="Creates the specified file, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The specific file path to create, relative to the working directory. If not provided, create file and path.",
            ),
            "content": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The content to write to file, relative to the working directory.",
            )
        },
    ),
)

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.realpath(os.path.abspath(working_directory))
    abs_file_path = os.path.realpath(os.path.abspath(os.path.join(working_directory, file_path)))
    
    common = os.path.commonpath([abs_working_dir, abs_file_path])
    if common != abs_working_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    parent = os.path.dirname(abs_file_path)
    try:    
        os.makedirs(parent, exist_ok=True)
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        error_message = str(e)
        return f'Error: {error_message}'
