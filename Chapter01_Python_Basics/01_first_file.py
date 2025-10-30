# Print a welcome message
name = "John"
age = 24
print(f"My name is {name} and I am {age} years old")

# Simple arithmetic
print("--- Arithmetic Operations ---")
a = 20
b = 8
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}") # integer division
print(f"{a} % {b} = {a % b}")   # modulus operator


# Interactive sample
name = input("Enter your name: ")
age = int(input("Enter your age: ")) # convert to int
print(f"My name is {name} and I am {age} years old")
print(f"Next year, I will be {age + 1}")


# Selenium Hint:
# element = driver.find_element(By.ID, "username")
# username = element.text   # stored as a string