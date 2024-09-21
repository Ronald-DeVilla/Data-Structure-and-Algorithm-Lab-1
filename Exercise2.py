# Ronald G. De Villa Jr. BSCPE 2-3
print("Type V to calculate for Voltage\nType C to calculate for Current\nType R to calculate for Resistance")
while True:
    choice = input("Enter your answer: ").strip().lower()
    if choice in ["v", "c", "r"]:
        break
    else:
        print("\nInvalid choice. Please try again.\n")

if choice == "v":
    while True:
        try:
            current = float(input("Enter the value of current: "))
            resistance = float(input("Enter the value of resistance: "))  
        except ValueError:
            print("\nInvalid input. Please try again.\n")
        else:
            voltage = round(current * resistance, 2)
            print(f"Voltage = {voltage} volts")
            break
elif choice == "c":
    while True:
        try:
            voltage = float(input("Enter the value of voltage: "))
            resistance = float(input("Enter the value of resistance: "))
            current = round(voltage / resistance, 2)
        except ValueError:
            print("\nInvalid input. Please try again.\n")
        except ZeroDivisionError:
            print("\nInvalid resistance value.\n")
        else:
            print(f"Current = {current} amperes")
            break
else:
    while True:
        try:
            voltage = float(input("Enter the value of voltage: "))
            current = float(input("Enter the value of current: "))
            resistance = round(voltage / current, 2)
        except ValueError:
            print("\nInvalid input. Please try again.\n")
        except ZeroDivisionError:
            print("\nInvalid current value.\n")
        else:
            print(f"Resistance = {resistance} ohms")
            break