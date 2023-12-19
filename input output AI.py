#
"""
Created on Tue Dec 19 09:34:05 2023

@author: tanaya
"""
def print_positive_numbers(input_list):
    positive_numbers = [num for num in input_list if num > 0]
    print("Output:", positive_numbers)

# Example usage:
list1 = [12, -7, 5, 64, -14]
print("Input:", list1)
print_positive_numbers(list1)

list2 = [12, 14, -95, 3]
print("Input:", list2)
print_positive_numbers(list2)

print("END")