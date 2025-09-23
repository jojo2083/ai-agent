from functions.get_files_info import get_files_info

get_files_info("calculator", ".")
 #Result for current directory:
 #- main.py: file_size=719 bytes, is_dir=False
 #- tests.py: file_size=1331 bytes, is_dir=False
 #- pkg: file_size=44 bytes, is_dir=True
 
print(f'get_files_info("calculator", "pkg"')

print(get_files_info("calculator", "/bin"))

print(get_files_info("calculator", "../"))
