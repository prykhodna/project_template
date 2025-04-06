import tempfile
from pathlib import Path
import unittest

from app.io.input import reading_files_with_python, reading_files_with_pandas


class TestReadingFilesWithPython(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_empty_file(self):
        # Arrange
        temp = Path(self.temp_dir.name) / "nothing.txt"
        with open(temp, "w") as f:
            f.write("")
        # Act
        content = reading_files_with_python(str(temp))
        # Assert
        self.assertEqual(content, "")

    def test_success(self):
        # Arrange
        expected = "Hello, World!\n"
        temp = Path(self.temp_dir.name) / "hellp_world.txt"
        with open(temp, "w") as f:
            f.write(expected)
        # Act
        content = reading_files_with_python(str(temp))
        # Assert
        self.assertEqual(content, expected)


class TestReadingFilesWithPandas(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_empty_rows(self):
        # Arrange
        temp = Path(self.temp_dir.name) / "nothing.csv"
        with open(temp, "w") as f:
            f.write("name,age\n")
        # Act
        df = reading_files_with_pandas(str(temp))
        # Assert
        self.assertEqual(df.shape, (0, 2))

    def test_success(self):
        # Arrange
        temp = Path(self.temp_dir.name) / "students.csv"
        with open(temp, "w") as f:
            f.write("name,age\nJohn,25\nJane,22\nJoshua,23")

        # Act
        df = reading_files_with_pandas(str(temp))
        # Assert
        self.assertEqual(df.shape, (3, 2))
        self.assertEqual(df[df["name"] == "John"].iloc[0]["age"], 25)
        self.assertEqual(df[df["name"] == "Jane"].iloc[0]["age"], 22)
        self.assertEqual(df[df["name"] == "Joshua"].iloc[0]["age"], 23)


if __name__ == "__main__":
    unittest.main()
