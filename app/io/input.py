import pandas as pd


def enter_text_from_console(prompt: str = "Enter value: ") -> str:
    """Allows user to enter text from console.

    Args:
        prompt (optional): Prompt that indicates the user to input. Defaults to "Enter value: ".

    Returns:
        User input.
    """
    return input(prompt)


def reading_files_with_python(file_name: str) -> str:
    """Allows to read content from file.

    Args:
        file_name: The name of the file for reading.

    Returns:
        Content from file.
    """
    with open(file_name, "r") as file:
        return file.read()


def reading_files_with_pandas(file_name: str) -> pd.DataFrame:
    """Reads files with pandas.
    Function reads data frame in CSV format.

    Args:
        file_name: The name of the file for reading.

    Returns:
        Parsed data frame from file.
    """
    return pd.read_csv(file_name)
