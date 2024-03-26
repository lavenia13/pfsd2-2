#1st sum
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is: {factorial}")


#2nd sum
#multiples of 7
for i in range(1, 8):
    print(f" 7 * {i} = {7*i}")

#3rd sum
def right_triangle(side1, side2, side3):
    # Sort the sides in ascending order
    sides = [side1, side2, side3]
    sides.sort()

    if sides[0]*2 + sides[1]*2 == sides[2]*2:
        return True
    else:
        return False

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if right_triangle(side1, side2, side3):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")

#4th sum
def print_pattern(rows):
    for i in range(1, rows + 1):
        print('*' * i)
    for i in range(rows - 1, 0, -1):
        print('*' * i)
num_rows = 5
print_pattern(num_rows)

#5th sum
def filter_binary_divisible_by_5(binary_sequence):
    binary_numbers = binary_sequence.split(',')
    divisible_by_5 = [binary for binary in binary_numbers if int(binary, 2) % 5 == 0]
    print(','.join(divisible_by_5))
binary_input = input("Enter a sequence of comma-separated 4-digit binary numbers: ")
filter_binary_divisible_by_5(binary_input)

