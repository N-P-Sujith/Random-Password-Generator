# RNGPassword: Customizable Random Password Generator

## Overview
RNGPassword is a lightweight, Python-based Command Line Interface (CLI) application designed to generate highly secure, randomized passwords. It allows users to specify the exact minimum requirements for uppercase letters, lowercase letters, numbers, and special characters, ensuring the final password meets the strict security criteria often required by modern websites and systems.

## Features
*   **Customizable Security:** Users dictate the exact composition of the password.
*   **Guaranteed Character Inclusion:** Ensures that the specified number of character types (Uppercase, Lowercase, Numbers, Symbols) are strictly included.
*   **Advanced Randomization:** Utilizes Python's `random` module to shuffle the generated characters, preventing predictable character sequencing.
*   **Lightweight & Fast:** Runs efficiently in any standard terminal without requiring external dependencies.

## Technologies and Tools Used
*   **Language:** Python 3.x
*   **Libraries:** `random` (Standard Python Library)
*   **Environment:** Command Line Interface (CLI)

## Steps to Install & Run the Project
1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/{your-github-username}/RNGPassword.git
    cd RNGPassword
    ```
    *(Note: Replace `{your-github-username}` with your actual GitHub username)*
2.  **Verify Python Installation:** Ensure you have Python 3 installed on your system. You can check this by running `python --version` or `python3 --version` in your terminal.
3.  **Run the Script:**
    ```bash
    python RNGPassword.py
    ```
4.  **Follow the Prompts:** Enter the integer values for the requested character types when prompted in the terminal.

## Instructions for Testing
To thoroughly test the application, perform the following test cases:
1.  **Standard Input:** Enter `3` for uppercase, `3` for lowercase, `2` for numbers, and `2` for special characters. Verify the output is exactly 10 characters long and contains the correct distribution.
2.  **Zero-Value Input:** Enter `0` for uppercase, `5` for lowercase, `0` for numbers, and `0` for special characters. Verify the output consists of exactly 5 lowercase letters.
3.  **Large Input Handling:** Enter large numbers (e.g., `20` for each category) to ensure the script handles larger loop iterations and list manipulations without performance degradation.