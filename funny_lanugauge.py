from custom_exceptions import NegativeNumberException

my_list = [2, 4, 6, 8, 10]


def print_length(obj):
    print(f"The length of the given object is {len(obj)}")


even_numbers = [number for number in range(100) if number % 2 == 0]


def square_root(num):
    if num >= 0:
        return num ** 0.5
    else:
        raise NegativeNumberException(num)


some_numbers = [1, -2, 3, "Simmy"]

for num in some_numbers:
    try:
        print(f"The square root of {num} is: {square_root(num)}")
    except NegativeNumberException:
        pass
    except TypeError:
        print(f"{num} is not a number. Please pass a number.")
