"""
1. `pprint` (pretty print) is a Python module for printing data structures in a more human-readable format.
2. Useful for debugging and logging complex or nested data structures like dictionaries, lists, or JSON.
3. Comes with the Python standard library (no installation required).
4. Key Features:
   - Formats nested elements with proper indentation.
   - Adjustable width and depth for customizing output.
   - Provides the `PrettyPrinter` class for advanced usage.

"""

from pprint import pprint, PrettyPrinter
import json

# Example 1: Pretty Printing a Dictionary
data = {
    "name": "John Doe",
    "age": 30,
    "hobbies": ["reading", "gaming", "cycling"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zipcode": 12345
    }
}

print("Example 1: Pretty Printing a Dictionary")
pprint(data)

# Example 2: Pretty Printing JSON Data
json_data = '{"name": "Alice", "age": 25, "skills": ["Python", "Django", "Docker"]}'
parsed_data = json.loads(json_data)

print("\nExample 2: Pretty Printing JSON Data")
pprint(parsed_data)

# Example 3: Adjusting Width and Depth
nested_data = {
    "key1": {"subkey1": {"subsubkey1": "value1", "subsubkey2": "value2"}},
    "key2": "value3",
}

print("\nExample 3: Adjusting Width and Depth")
pprint(nested_data, width=30, depth=2)

# Example 4: Using PrettyPrinter Class for Custom Formatting
data_numbers = {"numbers": list(range(20))}

print("\nExample 4: Using PrettyPrinter Class")
pp = PrettyPrinter(width=40, compact=True)
pp.pprint(data_numbers)
