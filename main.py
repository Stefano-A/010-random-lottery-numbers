import random

extracted_numbers = random.sample(range(1, 50), 6)
extracted_numbers.sort()

for number in extracted_numbers:
    print(number)