from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


def test():

    # //////////////////// Write File

    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    # //////////////////// Get File Content

    # result = get_file_content("calculator", "main.py")
    # print("Result for main.py file:")
    # print(result)
    # print()

    # result = get_file_content("calculator", "pkg/calculator.py")
    # print("Result for main.py file:")
    # print(result)
    # print()

    # result = get_file_content("calculator", "/bin/cat")
    # print("Result for main.py file:")
    # print(result)
    # print()

    # result = get_file_content("calculator", "pkg/does_not_exist.py")
    # print("Result for main.py file:")
    # print(result)
    # print()
    
    # //////////////////// Get Files Info

    # result = get_files_info("calculator", ".")
    # print("Result for current directory:")
    # print(result)
    # print("")

    # result = get_files_info("calculator", "pkg")
    # print("Result for 'pkg' directory:")
    # print(result)

    # result = get_files_info("calculator", "/bin")
    # print("Result for '/bin' directory:")
    # print(result)

    # result = get_files_info("calculator", "../")
    # print("Result for '../' directory:")
    # print(result)


if __name__ == "__main__":
    test()