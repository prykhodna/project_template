from typing import Any

import pandas as pd


def print_text_to_console(obj: Any) -> None:
    """Prints text to console.

    Args:
        obj: Object to be printed to console.

    Returns:
        Nothing
    """
    print(obj)


def write_output_to_file_with_python(path: str, content: str) -> None:
    """Writes content to specific file, specified by path.

    Args:
        path: Path to the file.
        content: Content to write to file.

    Examples:
        >>> write_output_to_file_with_python("./data/simple.txt", "Line will ...")
        None

    Returns:
        Nothing
    """
    with open(path, "a") as file:
        file.write(content)


def write_output_to_file_with_pandas(path: str, df: pd.DataFrame) -> None:
    """Write data frame to file, specified by path.
    Function writes to file in CSV format.

    Args:
        path: Path to the file.
        df: data frame to write.

    Returns:
        Nothing
    """
    df.to_csv(path)
