# Variables for basic data types

name = "Alice"      # string
age = 25            # integer
height = 5.6        # float
is_student = True   # boolean

# Print values with their types
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Type conversion (casting)
age_as_string = str(age)    # convert integer to string
height_as_int = int(height) # convert float to integer


print("Age as string:", age_as_string)
print("Height as integer:", height_as_int)

# Arithmetic with conversion
year_of_birth = 2025 - age
print(f"{name} was born on {year_of_birth}")


# Exercise =============================================
print("\n========== Exercise ==========")
# Variables
city = "New York"
monthly_income = 4500.75
own_a_car = False

# Print values with their types
print(city, "-", type(city))
print(monthly_income, "-", type(monthly_income))
print(own_a_car, "-", type(own_a_car))

# Convert monthly_income to integer
income_as_int = int(monthly_income)
print(f"Monthly income as int: {income_as_int} - {type(income_as_int)}")

# Calculate yearly income
yearly_income = monthly_income * 12
print(f"Yearly income is: {round(yearly_income, 2)}")


# Selenium Hint =============================================
# Store form values (strings, numbers, booleans)
# Convert them into the right type for calculations or validation
# Example:
# price_text = driver.find_element(By.ID, "price").text
# price = float(price_text.replace("$", ""))

# Your type conversions (str(), int(), float()) will be critical later when extracting numbers like prices, quantities,
# or ages from webpages, since Selenium always returns strings.
# Example: converting "$4500.75" to a float for calculations is exactly the same concept you just practiced.

get_text_price = "$4500.75"
text_price_as_float = float(get_text_price.replace("$", ""))
print(f"Text price as float {text_price_as_float}")