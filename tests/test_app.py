"""Unit and command-line tests for the greeting application."""

from contextlib import redirect_stdout
import io
from pathlib import Path
import runpy
import unittest

from app import greet, main


class TestApp(unittest.TestCase):
    """Check the required personalized greeting and entry points."""

    def test_greet_world(self):
        self.assertEqual(greet("World"), "Hello, World from Andrew Khoury!")

    def test_greet_other_name(self):
        self.assertEqual(
            greet("Jenkins"), "Hello, Jenkins from Andrew Khoury!"
        )

    def test_greet_empty_name(self):
        self.assertEqual(greet(""), "Hello,  from Andrew Khoury!")

    def test_main(self):
        output = io.StringIO()
        with redirect_stdout(output):
            main()
        self.assertEqual(
            output.getvalue(), "Hello, World from Andrew Khoury!\n"
        )

    def test_script_entry_point(self):
        output = io.StringIO()
        app_path = Path(__file__).resolve().parents[1] / "app.py"
        with redirect_stdout(output):
            runpy.run_path(str(app_path), run_name="__main__")
        self.assertEqual(
            output.getvalue(), "Hello, World from Andrew Khoury!\n"
        )
