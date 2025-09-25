from functions.get_files_info import get_files_info

def main():
    working_dir = "calculator"
    root_contents = get_files_info(working_dir)
    print(root_contents)
    pkg_contents = get_files_info(working_dir, "pkg")
    print(pkg_contents)
    boundry_test = get_files_info(working_dir, "/bin")
    print(boundry_test)
    boundry_test2 = get_files_info(working_dir, "../")
    print(boundry_test2)

main()



