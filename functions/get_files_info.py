import os

def get_files_info(working_directory, directory="."):     
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = ""
    if directory == ".":
        abs_directory = os.path.abspath(working_directory) 
    else:
        abs_directory = os.path.abspath(os.path.join(working_directory,directory))
 
    #verify joined path respects working directory, else return error
    
    if not abs_directory.startswith(abs_working_directory):         
       return f'Error: "{directory}" as it is outside the permitted working directory'
    
    #verify directory variable is a directory, else return error
    
    if os.path.isdir(abs_directory) == False:
       return f'Error: "{directory}" is not a directory'
   
    final_response = ""    
    #iterate over contents, print size and is directory
    try:
        contents = os.listdir(abs_directory)
        for content in contents:                        
            abs_content = os.path.join(abs_directory, content)
            size = os.path.getsize(abs_content)
            is_dir = os.path.isdir(abs_content) 
            final_response += f"- {content}: file_size={size} bytes, is_dir={is_dir}\n"
    except Exception as e:
         error_message = str(e)
         return f'Error: {error_message}'

    return final_response
