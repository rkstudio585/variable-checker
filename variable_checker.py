import keyword
import re
from rich.console import Console
from rich.text import Text
from pyfiglet import Figlet
from rich.live import Live
import time

# Initialize rich console
console = Console()

# Create a function to print a dynamic ASCII banner with animation
def print_animated_banner():
    banner_text = "pyVChecker"
    f = Figlet(font='slant')
    for i in range(1, len(banner_text)+1):
        banner = f.renderText(banner_text[:i])
        console.clear()
        console.print(Text(banner, style="bold cyan"))
        time.sleep(0.1)

# Check if variable name is valid
def check_variable_name(variable_name):
    pattern = r'^[A-Za-z_]\w*$'

    # Check if the variable name is a Python keyword
    if keyword.iskeyword(variable_name):
        return Text(f"Invalid variable: '{variable_name}' is a Python keyword.", style="bold red")

    # Check if it matches the valid pattern
    if re.match(pattern, variable_name):
        return Text(f"Correct: '{variable_name}' is a valid variable name!", style="bold green")
    else:
        return Text(f"Invalid variable: '{variable_name}' does not follow variable naming rules.", style="bold yellow")

# Suggest modifications to correct an invalid variable name
def suggest_corrections(variable_name):
    if not variable_name[0].isalpha() and variable_name[0] != '_':
        variable_name = '_' + variable_name  # Prefix an underscore if the first character is invalid

    # Remove any invalid characters from the name
    variable_name = re.sub(r'[^A-Za-z0-9_]', '', variable_name)

    return variable_name

# Handle multiple variable checks
def check_multiple_variables():
    console.print(Text("Enter variable names separated by commas:", style="bold magenta"))
    variable_names = console.input().split(',')
    for var in variable_names:
        var = var.strip()  # Remove leading/trailing spaces
        result = check_variable_name(var)
        console.print(result)

        if "Invalid" in result.plain:
            suggestion = suggest_corrections(var)
            console.print(Text(f"Suggested valid variable: '{suggestion}'", style="bold cyan"))

# Main function to run the tool
def main():
    # Display animated banner
    print_animated_banner()

    # Ask if user wants to check multiple variables
    choice = console.input("[bold magenta]Do you want to check multiple variable names? (yes/no): [/bold magenta] ").strip().lower()

    if choice == 'yes':
        check_multiple_variables()
    else:
        # Single variable check
        variable_name = console.input("[bold magenta]Enter a variable name to check: [/bold magenta] ")
        result = check_variable_name(variable_name)
        console.print(result)

        # Provide suggestions if invalid
        if "Invalid" in result.plain:
            suggestion = suggest_corrections(variable_name)
            console.print(Text(f"Suggested valid variable: '{suggestion}'", style="bold cyan"))

        # Instructions on how to create valid variables
        console.print("""
        [bold yellow]How to create a valid variable: [/bold yellow]
        1. Start with a letter or underscore (_).
        2. Use only letters, numbers, and underscores.
        3. Avoid using Python keywords like 'if', 'while', etc.
        4. Remember that variable names are case-sensitive.

        [bold green]Example of valid variables: [/bold green]
        - my_var
        - _myVariable
        - user123
        """)
if __name__ == "__main__":
    main()
                                             
