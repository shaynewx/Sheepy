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
git clone <repository-url>
cd sheepy
```

