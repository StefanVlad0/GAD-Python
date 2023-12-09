"""
This is the homework for session 3 of the Google Python Workshop "Google Atelierul Digital - Programare", November 2023

Student - Vlad Stefan
"""


# 1. Write a function that takes an undefined number of parameters and calculate the sum of the parameters
# that represent integers or real numbers.

def my_function(*args, **kwargs):
    numbers_sum = 0
    for item in args:
        if isinstance(item, (int, float)):
            numbers_sum += item
    for item in kwargs.values():
        if isinstance(item, (int, float)):
            pass
    return numbers_sum


print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))  # will return 3 (1 + 5 - 3).
print(my_function())  # will return 0
print(my_function(2, 4, 'abc', param_1=2))  # will return 6 (2+4)


# 2. Write a recursive function that receives a list of integers and returns:
# a) the total sum of the numbers
# b) sum of even numbers
# c) sum of odd numbers


def rec_function(my_list):
    if not my_list:
        return 0, 0, 0

    total_sum, even_sum, odd_sum = rec_function(my_list[1:])

    current_number = my_list[0]

    new_total_sum = total_sum + current_number
    mew_even_sum = even_sum
    new_odd_sum = odd_sum

    if current_number % 2 == 0:
        mew_even_sum += current_number
    else:
        new_odd_sum += current_number

    return new_total_sum, mew_even_sum, new_odd_sum


simple_list = [1, 2, 3, 4]

total_result, even_result, odd_result = rec_function(simple_list)

print(f'Even sum: {even_result}; Odd sum: {odd_result}; Total: {total_result}')  # will print 6, 4, 10


# 3. Write a function that reads from the keyboard and returns the value if it is an integer, otherwise return
# value 0.

def is_integer():
    my_var = input("int number: ")
    try:
        my_int = int(my_var)
    except ValueError as e:
        print('Your input is not an integer!', e)
        return 0
    else:
        return my_int


print(is_integer())
