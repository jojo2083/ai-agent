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
    try:
        completed_process = subprocess.run(["uv","run", abs_file_path, *args],cwd=abs_working_directory,timeout=30,capture_output=True,text=True)
        str_stderr =str(completed_process.stderr)
        str_stdout = str(completed_process.stdout)
        X = completed_process.returncode
        if not completed_process.returncode == 0:
            return f'STDOUT: {str_stdout} \n STDERR: {str_stderr}\n Process exited with code {X}'
        if str_stderr == "" and str_stdout == "":
            return "No output produced."
        else:
            return f'STDOUT: {str_stdout} \n STDERR: {str_stderr}'
    except Exception as e:
        return f'Error: executing Python file: {e}'
    
        
    