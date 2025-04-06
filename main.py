from app.io.input import (
    enter_text_from_console,
    reading_files_with_pandas,
    reading_files_with_python,
)
from app.io.output import (
    print_text_to_console,
    write_output_to_file_with_python,
)


def main():
    user_input = enter_text_from_console("Enter your value: ")
    file_content = reading_files_with_python(R".\data\hello_world.txt")
    df = reading_files_with_pandas(R".\data\students.csv")

    print_text_to_console(user_input)
    print_text_to_console(file_content)
    print_text_to_console(df)

    write_output_to_file_with_python(R".\data\output.txt", user_input + "\n")
    write_output_to_file_with_python(R".\data\output.txt", file_content + "\n")
    write_output_to_file_with_python(R".\data\output.txt", str(df) + "\n")


if __name__ == "__main__":
    main()
