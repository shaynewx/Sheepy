# Sheepy - Shell to Python Transpiler

Sheepy is a Python-based tool designed to transpile POSIX Shell scripts into equivalent Python scripts. This project automates the conversion process, which is often done manually when additional functionality, such as a GUI, is required in Python.

## Features

Sheepy currently supports a subset of POSIX Shell features, focusing on basic script translation to Python. The supported features include:

- **Echo Command**: Converts `echo` statements in Shell to `print` statements in Python.
- **Variable Assignment**: Translates Shell variable assignments into Python equivalents.
- **Conditional Statements**: Translates if conditions from Shell to Python.
- **Loop Constructs**: Translates for loops from Shell to Python.
- **Comments**: Preserves comments during translation for readability.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Access to a POSIX-compliant shell environment for testing

### Installation

Clone the repository to your local machine:

```sh
git clone git@github.com:shaynewx/Sheepy.git
cd sheepy
```

## Usage
1. To transpile a Shell script to Python, run the sheepy.py script with the path to the Shell script as an argument:
```sh
./sheepy.py path/to/script.sh
```

2. The Python-translated code will be printed to standard output. Redirect the output to a file if you wish to save it:
```sh
./sheepy.py path/to/script.sh > output.py
```

## Contribution
Feel free to fork this project and make your own changes. Pull requests are welcome for bug fixes, improvements, and adding new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Authors
- **[shaynewx](https://github.com/shaynewx)**

## Acknowledgments
- This project was inspired by the need to automate the conversion of Shell scripts to Python, often required for enhancing functionality or integrating additional features.
- Assignment for COMP(2041|9044) at UNSW.