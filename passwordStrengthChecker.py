# Password Strength Checker:
# Task: viewers try to come up with creative ways to assess password strength.

import re

class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password

    def check_length(self):
        return len(self.password) >= 8  # Minimum length of 8 characters

    def check_special_characters(self):
        special_characters = "!@#$%^&*()-=_+[]{}|;:'\"<>,.?/~`"
        return any(char in special_characters for char in self.password)

    def check_numbers(self):
        return any(char.isdigit() for char in self.password)

    def check_strength(self):
        length_ok = self.check_length()
        special_characters_ok = self.check_special_characters()
        numbers_ok = self.check_numbers()

        if length_ok and special_characters_ok and numbers_ok:
            return "Password is strong!"
        else:
            feedback = "Password is weak. Consider:"
            if not length_ok:
                feedback += " Increase the length."
            if not special_characters_ok:
                feedback += " Add special characters."
            if not numbers_ok:
                feedback += " Include numbers."
            return feedback

# Example
password_checker = PasswordStrengthChecker("SecurePwd123!")
result = password_checker.check_strength()
print(result)
