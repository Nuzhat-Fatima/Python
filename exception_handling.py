"""
Exception handling in Python allows you to handle and manage errors or exceptional situations that might
occur during the execution of your code. Python provides a structured way to handle exceptions using
try, except, else, and finally blocks. Here's an overview of how exception handling works in Python:
"""
#1:Division by Zero error:
try:
    # Code that may raise an exception
    result = 10 / 0  # Attempt to divide by zero
except ZeroDivisionError:
    # Handle the specific exception (in this case, a division by zero)
    print("Division by zero is not allowed.")
except Exception as e:
    # Handle other exceptions
    print(f"An error occurred: {e}")
else:
    # Code to execute if no exception is raised
    print("No exceptions occurred.")
finally:
    # Code that runs regardless of whether an exception occurred or not
    print("This code always executes.")

#2:Value error:
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid integer for age.")
else:
    print(f"You are {age} years old.")
finally:
    print("Execution complete.")


#3:Opening and Handlng a file:
try:
    file = open("non_existent_file.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("The specified file does not exist.")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")
else:
    print("File read successfully:")
    print(content)
finally:
    print("Execution complete.")


