"""
The colorama library in Python is a simple and effective tool for adding color and style to your terminal output. It works on Windows, macOS, and Linux, making it a cross-platform solution for creating visually appealing console applications.

"""

from colorama import init, Fore, Back, Style

# Initialize colorama
init()

# Basic Usage Examples
def basic_usage():
    print(Fore.RED + "This is red text")
    print(Fore.GREEN + "This is green text")
    print(Fore.BLUE + "This is blue text")
    print(Back.YELLOW + "This text has a yellow background")
    print(Back.CYAN + "This text has a cyan background")
    print(Style.RESET_ALL + "Back to normal text")
    print(Style.DIM + "This is dim text")
    print(Style.BRIGHT + "This is bright text")
    

# Reset Example
def reset_example():
    print(Fore.RED + "Red text" + Style.RESET_ALL + " Normal text")

# Combine Colors and Styles
def combine_styles():
    print(Fore.WHITE + Back.MAGENTA + Style.BRIGHT + "Bright white text on a magenta background" + Style.RESET_ALL)

# Dynamic Styling with Loops
def dynamic_styling():
    colors = [Fore.RED, Fore.GREEN, Fore.BLUE]
    messages = ["Error", "Success", "Info"]

    for color, message in zip(colors, messages):
        print(color + message + Style.RESET_ALL)

# Simple Logger Example
def log_message(level, message):
    if level == "INFO":
        print(Fore.BLUE + "[INFO]" + Style.RESET_ALL, message)
    elif level == "SUCCESS":
        print(Fore.GREEN + "[SUCCESS]" + Style.RESET_ALL, message)
    elif level == "ERROR":
        print(Fore.RED + "[ERROR]" + Style.RESET_ALL, message)

def logger_example():
    log_message("INFO", "This is an informational message.")
    log_message("SUCCESS", "This operation was successful.")
    log_message("ERROR", "An error occurred.")

# Main Function
if __name__ == "__main__":
    print("=== Basic Usage ===")
    basic_usage()
    print("\n=== Reset Example ===")
    reset_example()
    print("\n=== Combine Styles ===")
    combine_styles()
    print("\n=== Dynamic Styling ===")
    dynamic_styling()
    print("\n=== Logger Example ===")
    logger_example()
