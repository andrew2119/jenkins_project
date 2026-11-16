"""Tests for persistent local deployment."""

from contextlib import redirect_stdout
import io
from pathlib import Path
import runpy
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from deploy import deploy, main


class TestDeploy(unittest.TestCase):
    """Verify first deployment, redeployment, and command-line use."""

    def test_deploy_creates_directory_and_copies_application(self):
        with TemporaryDirectory() as temp:
            target = Path(temp) / "local deployment" / "application"
            deployed_file = deploy(target)
            source = Path(__file__).resolve().parents[1] / "app.py"
            self.assertEqual(deployed_file, target.resolve() / "app.py")
            self.assertEqual(deployed_file.read_bytes(), source.read_bytes())

    def test_redeploy_replaces_old_application(self):
        with TemporaryDirectory() as temp:
            deployed_file = deploy(temp)
            deployed_file.write_text("old application\n", encoding="utf-8")
            deploy(temp)
            self.assertIn("def greet(name):", deployed_file.read_text())

    def test_main(self):
        with TemporaryDirectory() as temp:
            output = io.StringIO()
            with patch("sys.argv", ["deploy.py", "--target", temp]):
                with redirect_stdout(output):
                    main()
            self.assertTrue((Path(temp) / "app.py").is_file())
            self.assertIn("Deployed application:", output.getvalue())

    def test_script_entry_point(self):
        with TemporaryDirectory() as temp:
            script = Path(__file__).resolve().parents[1] / "deploy.py"
            with patch("sys.argv", [str(script), "--target", temp]):
                with redirect_stdout(io.StringIO()):
                    runpy.run_path(str(script), run_name="__main__")
            self.assertTrue((Path(temp) / "app.py").is_file())
