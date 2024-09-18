# USER_input Experiments

This repository contains experiments related to handling user inputs using the Pydantic library and configuration files in TOML format. The `USER_input` class is used to define user parameters, and the data is read from a TOML file. The repository aims to provide a flexible, easily configurable setup for initializing parameters via external configuration files.

## Project Structure

- **`user_input.py`**: This Python script defines the `USER_input` class using Pydantic and provides functionality to read data from a TOML file and instantiate the class.
- **`input_data.toml`**: A TOML file containing sample input values for the `USER_input` class, including fields such as `Variable`, `Project`, `Product`, and more.
- **`README.md`**: The project documentation (this file).

## Prerequisites

- Python 3.6+
- Pydantic library
- TOML parsing library (`tomllib` for Python 3.11+, or `tomli` for older versions)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/USER_input_experiments.git
   cd USER_input_experiments
   ```

2. Install the required dependencies (if you don't have Pydantic or TOML parsing library installed):

    ```bash 
    pip install pydantic tomli  # For Python < 3.11
    ```

