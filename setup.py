from setuptools import setup

# Unfortunately the version cannot be imported. But this does the trick
exec(compile(open('src/myproject/version.py').read(), 'src/myproject/version.py', 'exec'))

if __name__ == "__main__":
    setup(version=__version__)  # type: ignore
