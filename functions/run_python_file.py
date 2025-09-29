import subprocess
import os

def run_python_file(working_directory, file_path, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
    common = os.path.commonpath([abs_working_directory, abs_file_path])
    if common != abs_working_directory:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if os.path.exists(abs_file_path) == False:
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    subprocess.run(uv run abs_file_path,cwd=abs_working_directory, timeout=30,capture_output=True):
    
    except Exception as e:
         f"Error: executing Python file: {e}"
    
    return f'STDOUT: {completed_process.stdout} /nl STDERR: {completed_process.stderr}'
    