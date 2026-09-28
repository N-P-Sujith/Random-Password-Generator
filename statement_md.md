# Project Statement

## Problem Statement
In today's digital landscape, cyber threats are increasingly sophisticated, and weak passwords remain a primary vulnerability for user accounts. Many individuals struggle to manually create passwords that are both highly secure and compliant with the complex character requirements enforced by various platforms. There is a critical need for an accessible, offline tool that automatically generates cryptographically strong, randomized passwords based on specific user-defined constraints.

## Scope of the Project
The scope of this project involves developing a Command Line Interface (CLI) utility using Python. The system will accept integer inputs from the user detailing the minimum required count for four character categories: uppercase letters, lowercase letters, numerical digits, and special symbols. The scope is limited to terminal-based execution and focuses entirely on the logical generation and cryptographic shuffling of strings without relying on third-party external libraries.

## Target Users
*   **General Internet Users:** Individuals looking to secure their personal accounts (social media, banking, email) with strong passwords.
*   **System Administrators:** IT professionals who need to rapidly generate temporary, highly secure passwords for new employee accounts or server configurations.
*   **Developers:** Programmers needing quick generation of database credentials or API keys during local development environments.

## High-Level Features
1.  **Dynamic Input Handling:** Interactive prompts that capture specific user constraints for password composition.
2.  **Categorized Character Pools:** Distinct predefined arrays for uppercase, lowercase, numbers, and special characters.
3.  **Algorithmic Shuffling:** A customized randomization loop that extracts characters from a pooled list to ensure the final password string has an unpredictable character sequence.
4.  **Zero-Dependency Architecture:** Built entirely with standard Python libraries for maximum portability and security.