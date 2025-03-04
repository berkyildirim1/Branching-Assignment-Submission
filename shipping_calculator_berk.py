# Main program for Package Express shipping calculator
# Author: John Smith
# Date: 2024

# Display welcome message
print("Welcome to Package Express. Please follow the instructions below.")

# Get package weight from user
package_mass = float(input("Please enter the package weight:\n"))

# Check if package is too heavy
if package_mass > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
    exit()

# Get package dimensions from user
package_width = float(input("Please enter the package width:\n"))
package_height = float(input("Please enter the package height:\n"))
package_length = float(input("Please enter the package length:\n"))

# Calculate total dimensions
total_dimensions = package_width + package_height + package_length

# Check if package is too large
if total_dimensions > 50:
    print("Package too big to be shipped via Package Express.")
    exit()

# Calculate shipping cost
# Formula: (width * height * length * weight) / 100
shipping_quote = (package_width * package_height * package_length * package_mass) / 100

# Display the shipping quote
print(f"Your estimated total for shipping this package is: ${shipping_quote:.2f}")
print("Thank you!") 