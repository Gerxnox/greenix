# Greenix 🌱

Welcome to Greenix, a Python script for bulk cloning Git repositories from a list of cleaned URLs.

## Overview

Greenix is designed to simplify the process of cloning multiple Git repositories listed in a file. It handles naming conflicts by appending numerical suffixes to folder names.

## Features

- Clone multiple repositories from a list of cleaned URLs.
- Automatically handle naming conflicts by appending numerical suffixes to folder names.
- Provides detailed progress and information about each clone operation.

## Usage

1. Ensure you have Git installed on your system.

2. Create a file named `cleaned_repo_urls.txt` in the same directory as this script.

3. In `cleaned_repo_urls.txt`, list the cleaned repository URLs (one URL per line):


4. Open a terminal and navigate to the script's directory.

5. Run the script using the following command:

```bash
python greenix.py

Acknowledgements

Greenix is inspired by the need to bulk clone Git repositories efficiently.
