"""Deploy the application to a persistent local directory."""

import argparse
from pathlib import Path
import shutil


def deploy(target):
    """Copy app.py to the destination, replacing a previous deployment."""
    destination = Path(target).expanduser().resolve()
    destination.mkdir(parents=True, exist_ok=True)
    deployed_file = destination / "app.py"
    shutil.copy2(Path(__file__).resolve().with_name("app.py"), deployed_file)
    return deployed_file


def main():
    """Read the deployment directory from the command line."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True)
    args = parser.parse_args()
    print(f"Deployed application: {deploy(args.target)}")


if __name__ == "__main__":
    main()
