"""Greeting application for EECE 435L Lab 10."""


def greet(name):
    """Return a personalized greeting."""
    return f"Hello, {name} from Andrew Khoury!"


def main():
    """Run the application."""
    print(greet("World"))


if __name__ == "__main__":
    main()
