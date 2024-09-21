# Ronald G. De Villa Jr. BSCPE 2-3
while True:
    try:
        temp = float(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
    else:
        break
print("Enter F for Celsius to Fahrenheit\nEnter C for Fahrenheit to Celsius")
while True:
    conversion = input("(C/F): ").lower()
    if conversion in ["c", "f"]:
        break
    else:
        print("Invalid input. Please enter C or F")

if conversion == "f":
    result = round((temp * 9/5) + 32, 2)
    print(f"{temp}°C is equal to {result}°F")
else:
    result = round((temp - 32) * 5/9, 2)
    print(f"{temp}°F is equal to {result}°C")