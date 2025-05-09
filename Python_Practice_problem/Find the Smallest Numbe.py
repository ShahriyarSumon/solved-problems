numbers = [12, 4, 7, 1, 9, 15]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number is:", smallest)
