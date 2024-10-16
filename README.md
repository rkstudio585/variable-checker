# Python Variable Checker Tool

---

![loGo](logo/logo.webp)

---

A Python-based tool that checks if variable names are valid according to Python's naming rules. This tool provides:
- **Real-time feedback** on whether a variable name is valid or invalid.
- **Suggestions for correcting** invalid variable names.
- **Multiple variable checks** at once for quick validation.
- **Colorful interface** and an animated ASCII banner using `rich` and `pyfiglet` libraries for a user-friendly experience.

## Features

1. **Real-time Variable Validation**: The tool checks the validity of Python variable names based on standard rules.
2. **Multiple Variable Validation**: You can validate multiple variable names in one go by separating them with commas.
3. **Correction Suggestions**: If a variable is invalid, the tool suggests a corrected name (e.g., by adding an underscore if the variable starts with a number).
4. **Animated ASCII Banner**: The tool greets the user with an animated ASCII banner using `pyfiglet`.
5. **Rich Colorful UI**: The `rich` library adds vibrant colors and styling to the console output.

## Python Variable Naming Rules

- A variable name must start with a **letter (a-z, A-Z)** or an **underscore (_)**.
- Variable names cannot start with a **number (0-9)**.
- They can only contain **alphanumeric characters** (a-z, A-Z, 0-9) and underscores (_).
- Variable names are **case-sensitive**.
- **Reserved keywords** (like `if`, `else`, `while`) cannot be used as variable names.

## Dependencies

Before running the script, make sure to install the following Python libraries:
- [`rich`](https://github.com/Textualize/rich) for colorful text and user-friendly interface.
- [`pyfiglet`](https://github.com/pwaller/pyfiglet) for rendering ASCII art banners.

Install the dependencies via pip:

```bash
pip install rich pyfiglet
```
How to Use

1. Clone or Download the Project: You can clone this repository or download the Python script to your local machine.
```bash
git clone https://github.com/rkstudio585/variable-checker.git
cd variable-checker
```

2. Run the Script: To run the tool, simply execute the Python script in your terminal:
```bash
python variable_checker.py
```

3. Follow the Prompts: The tool will ask if you want to check multiple variable names at once. If you choose yes, you'll be asked to input the variable names, separated by commas.

If you enter only one variable, the tool will validate that variable and provide feedback. Here’s an example interaction:

Variable Checker

Do you want to check multiple variable names? (yes/no): yes
Enter variable names separated by commas:
myVar, 123num, _valid_var, if

Correct: 'myVar' is a valid variable name!
Invalid variable: '123num' does not follow variable naming rules.
Suggested valid variable: '_123num'
Correct: '_valid_var' is a valid variable name!
Invalid variable: 'if' is a Python keyword.

The tool will show whether each variable is valid or invalid and provide suggestions where possible.



How the Tool Works

1. Animated Banner: The tool starts by printing an animated banner saying "Variable Checker" using pyfiglet.


2. Input Validation: Users can choose to check a single variable or multiple variables at once. The tool then validates each variable based on Python’s rules:

Whether the variable starts with a valid character.

Whether it contains only valid characters.

Whether the variable name is a Python keyword.



3. Correction Suggestions: If a variable is invalid (e.g., starts with a number or contains invalid characters), the tool provides a suggestion for how to fix the name.


4. Interactive Console: Using rich, the tool adds colors and formatted output for better readability and interaction.



Example of Valid Variable Names

- my_var

- _myVariable

- user123

- age

- _counter

Example of Invalid Variable Names

- 123abc → Invalid (cannot start with a number).

- if → Invalid (Python keyword).

- my-var → Invalid (hyphens are not allowed).


For invalid variables, the tool will suggest how to correct them, like _123abc instead of 123abc.

Contributing

Feel free to contribute to this project by opening issues or submitting pull requests.


---

