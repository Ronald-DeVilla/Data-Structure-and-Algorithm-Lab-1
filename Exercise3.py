# Ronald G. De Villa Jr. BSCPE 2-3
def print_diamond(n):
    while True:
        if n % 2 != 0:
            for i in range(n // 2 + 1):
                print(" " * (n // 2 - i) + "*" * (2 * i + 1))
        
            for i in range(n // 2 - 1, -1, -1):
                print(" " * (n // 2 - i) + "*" * (2 * i + 1))
            break
        else:
            print("Please provide an odd integer.")
            n = int(input("Enter an odd integer: "))

while True:
    try:
        n = int(input("Enter an odd integer: "))
        print_diamond(n)
    except ValueError:
            print("Please provide an integer.")