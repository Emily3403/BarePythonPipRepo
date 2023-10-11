# Myproject with SQLAlchemy

![Tests](https://github.com/Emily3403/BarePythonPipRepo/actions/workflows/tests.yml/badge.svg)

This repository serves as a building-block for my new python projects.

It contains most of the bloat-code required to set up `pip` installation, automatic testing (on GitHub and GitLab), and a bit of sqlalchemy.

## Getting started

Getting started is quite easy:

1. Clone this repository
2. Replace all instances of `myproject` with the actual name of your project
   - Note that if your project name contains a hyphen (`-`), you will need to replace all hyphens in the code with underscores (`_`). To do so, you can wildcard-replace all `from myprojet` with your desired name with underscores.
3. Rename the `src/myproject` directory to `src/{actual_name}`
4. Fill the required information for all the TODOs
5. Upload it to the new repository
6. Check to see that the automated tests have passed

## Using the repository

The usage is also very straightforward:

### Development

1. Create a [virtual environment](https://docs.python.org/3/library/venv.html): `python -m venv venv`
2. Activate that virtual environment: `source ./venv/bin/activate` ([For other shells](https://docs.python.org/3/library/venv.html#how-venvs-work))
3. Install the repository using `pip`: `pip install -e ".[testing]"`
   - This will install the repository in [editable mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html)
4. Execute the code with `myproject`
  - The name of this script is decided by the `console_scripts` option in the [setup.cfg](./setup.cfg)

### Publishing

1. Publish the library by executing `./bin/upload-to-PyPI.sh`
   - Don't forget to increase the version in [version.py](./src/myproject/version.py)
2. Enter your credentials into `twine`
3. Done!

### Production

1. Install the code from PyPI: `pip install myproject`
2. Execute it: `myproject`

## Credit

A lot of this code and motivation to write this code goes back to [mCoding](https://www.youtube.com/@mCoding). About two years ago (as of writing this), they published a [repository](https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject) which was the original inspiration for this project.

Since then, the repository has grown and been structured around, however without their contributions, this repository would not be what it is.