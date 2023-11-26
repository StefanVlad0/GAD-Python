"""
This is the homework for session 2 of the Google Python Workshop "Google Atelierul Digital - Programare", November 2023

Student - Vlad Stefan
"""

# 1. Declare a list containing the elements 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (in this order)
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# 2. Print a list in ascending order (the original list must be kept in the same form)
print(sorted(my_list))

# 3. Print a list sorted in descending order (the original list must be kept in the same form)
print(sorted(my_list, reverse=True))

# 4. Print even indexed numbers from the list (using slice ONLY)
print(my_list[::2])

# 5. Print odd index numbers from list (using slice ONLY)
print(my_list[1::2])

# 6. Print the elements that are multiples of 3
for item in my_list:
    if item % 3 == 0:
        print(item)
