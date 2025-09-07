# Declare a string
text = "  Hello, World! Welcome to Python.  "

# ------------------------
# 1. Basic Information
# ------------------------
print(len(text))  # length of string including spaces

# ------------------------
# 2. Case Conversion
# ------------------------
print(text.upper())     # Converts entire string to uppercase
print(text.lower())     # Converts entire string to lowercase
print(text.title())     # Converts first letter of each word to uppercase
print(text.capitalize())# Converts first character to uppercase, rest to lowercase
print(text.swapcase())  # Swaps case: upper -> lower and lower -> upper

# ------------------------
# 3. Remove Whitespace
# ------------------------
print(text.strip())   # Removes spaces from both ends
print(text.lstrip())  # Removes spaces from the left
print(text.rstrip())  # Removes spaces from the right

# ------------------------
# 4. Search and Find
# ------------------------
print(text.find("World"))    # Returns index of first occurrence (-1 if not found)
print(text.rfind("o"))       # Returns last occurrence index
print(text.index("Hello"))   # Same as find but raises error if not found
print(text.rindex("o"))      # Same as rfind but raises error if not found
print(text.count("o"))       # Counts occurrences of substring

# ------------------------
# 5. Replace
# ------------------------
print(text.replace("World", "Universe"))  # Replaces substring with another

# ------------------------
# 6. Split and Join
# ------------------------
print(text.split())       # Splits string by spaces into a list
print(text.split(","))    # Splits by comma
print("-".join(['Hello','Python']))  # Joins list with '-'

# ------------------------
# 7. Check String Start/End
# ------------------------
print(text.startswith("  Hello"))  # Checks if string starts with given substring
print(text.endswith("Python.  "))  # Checks if string ends with given substring

# ------------------------
# 8. String Validation (Returns True/False)
# ------------------------
print("hello".isalpha())      # True if all characters are alphabetic
print("12345".isdigit())      # True if all characters are digits
print("hello123".isalnum())   # True if all characters are alphanumeric
print("hello".islower())      # True if all characters are lowercase
print("HELLO".isupper())      # True if all characters are uppercase
print("Hello World".istitle())# True if string is in title case
print("   ".isspace())        # True if string contains only whitespace

# ------------------------
# 9. String Formatting
# ------------------------
print("My name is {}".format("Alice"))      # Using format()
print(f"My name is {'Alice'}")              # Using f-string
print("My name is %s" % "Alice")            # Old-style formatting

# ------------------------
# 10. Encoding
# ------------------------
print(text.encode())   # Encodes string into bytes (UTF-8 by default)

# ------------------------
# 11. Zfill, Center, Ljust, Rjust
# ------------------------
print("42".zfill(5))        # Pads string with zeros: 00042
print("Hello".center(20,"*")) # Centers text with * padding
print("Hello".ljust(20,"-"))  # Left justify
print("Hello".rjust(20,"-"))  # Right justify




a = [1,2]