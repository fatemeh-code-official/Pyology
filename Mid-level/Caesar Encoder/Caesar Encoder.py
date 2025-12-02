import string

"""
Caesar Cipher Encryption Tool
=============================

This module provides a simple yet robust implementation of the classic Caesar
Cipher encryption algorithm. It allows users to input plain text (a–z and 
spaces), validates the content, and encrypts the text using a fixed shift 
value of 3.

Core Features
-------------
1. Input validation through `plain_text_analyzer()`:
   - Ensures the text is not empty.
   - Accepts only lowercase alphabetic characters and whitespace.
   - Rejects digits, punctuation marks, and unsupported characters.
   - Raises `EmptyFieldError` for missing input and `ValueError` for invalid
     content.

2. Text encryption via `plain_text_encryptor()`:
   - Implements a classical Caesar shift of 3 positions.
   - Preserves whitespace.
   - Wraps alphabet indices from 'z' back to 'a'.

3. Clear and explicit error handling to ensure predictable program behavior.

Usage
-----
The program takes user input from the command line, validates it, and outputs 
the encrypted result. Designed for demonstration, learning, and lightweight 
cryptographic experimentation.

Note
----
This implementation is intentionally minimal and should not be used for 
real-world cryptographic security. Caesar Cipher is a historically significant 
but cryptographically weak algorithm.

Author
------
Your Name (Replace before publishing)
github.com/YourRepoName
"""


class EmptyFieldError(Exception):
    pass


def plain_text_analyzer(plain_text):
    if not plain_text:
        raise EmptyFieldError(
            "You have no permission to skip the field \u274C")
    plain_text_list = []
    for char in plain_text:
        if char in string.ascii_lowercase:
            plain_text_list.append(char)
        elif char.isspace():
            plain_text_list.append(char)
        elif char in string.digits:
            raise ValueError("Numbers are not allowed \u274C")
        elif char in string.punctuation:
            raise ValueError(
                "Signs (@,#,%,...) are not allowed \u274C")
        else:
            raise ValueError("Unsupported character \u274C")

    return plain_text_list


def plain_text_encryptor(plain_text):
    shift = 3
    plain_text_list = plain_text
    alphabets = string.ascii_lowercase
    encoded_text_list = []
    for char in plain_text_list:
        if char.isspace():
            encoded_text_list.append(char)
            continue
        char_index = alphabets.index(char)
        shifted_index = char_index+shift
        if shifted_index > 25:
            shifted_index -= 26
        encoded_char = alphabets[shifted_index]
        encoded_text_list.append(encoded_char)
    return ''.join(encoded_text_list)


try:
    plain_text = input(
        "Enter your quote please (Just characters a-z)\n\u2139\ufe0f  Information will be encrypted with shift 3 : ").strip().lower()

    analyzed_text = plain_text_analyzer(plain_text=plain_text)
    result = plain_text_encryptor(analyzed_text)
    print("\U0001f504 Processing...")
    print(f"\U0001F510 The encrypted string is < {result} >")


except (EmptyFieldError, ValueError) as error:
    print(error)
