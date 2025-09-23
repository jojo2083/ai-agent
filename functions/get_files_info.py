import os

def get_files_info(working_directory, directory=None):     
    abs_working_directory = os.path.abspath(working_directory)
    if directory is None:
        directory = "."
    abs_directory = os.path.abspath(os.path.join(abs_working_directory, directory))
    
    #verify joined path respects working directory, else return error
    
    if not os.path.commonpath([abs_working_directory, abs_directory]) == abs_working_directory:         
       return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    #verify directory variable is a directory, else return error
    
    if os.path.isdir(abs_directory) == False:
       return f'Error: "{directory}" is not a directory'
    results=[]    
    #iterate over contents, print size and is directory
    try:
        contents = os.listdir(abs_directory)
        for content in contents:                        
            abs_content = os.path.join(abs_directory, content)
            size = os.path.getsize(abs_content)
            is_dir = os.path.isdir(abs_content) 
            results.append(f"- {content}: file_size={size} bytes, is_dir={is_dir}")
    except Exception as e:
         error_message = str(e)
         return f'Error: {error_message}'

    return "\n".join(results)
