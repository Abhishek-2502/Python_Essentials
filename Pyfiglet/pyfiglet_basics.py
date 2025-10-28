"""
1. `pyfiglet` is a Python library for creating ASCII art text using FIGlet fonts.
2. It supports a variety of font styles to make terminal output more visually appealing.
3. Useful for banners, headers, or enhancing CLI applications.

"""

import pyfiglet

# Example 1: Basic ASCII Art
print("Example 1: Basic ASCII Art")
ascii_art = pyfiglet.figlet_format("Hello, World!")
print(ascii_art)

# Example 2: Using a Different Font
print("\nExample 2: Using a Different Font")
ascii_art_with_font = pyfiglet.figlet_format("Custom Font", font="slant")
print(ascii_art_with_font)

# Example 3: Listing Available Fonts
print("\nExample 3: Listing Available Fonts")
available_fonts = pyfiglet.FigletFont.getFonts()
print(f"Total fonts available: {len(available_fonts)}")
print("Sample fonts:", ", ".join(available_fonts[:5]))

# Example 4: Printing ASCII Art with Custom Width
print("\nExample 4: Custom Width")
ascii_art_with_width = pyfiglet.figlet_format("Custom Width", width=100)
print(ascii_art_with_width)
