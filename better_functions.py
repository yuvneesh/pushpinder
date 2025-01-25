from typing import List, Union


def calculate_average(list_of_numbers: List[Union[int, float]]) -> float:
    """
    Returns the average of the given list of numbers.
    Throws an exception if the input is not a list.
    Reads non-numeric values as 0

    >>> calculate_average([1, 2, 3])
    2.0
    >>> calculate_average([-5, 5, 3333])
    1111.0
    >>> calculate_average([1, 2, 'hello simmy'])
    1.0
    """
    if not isinstance(list_of_numbers, list):
        raise TypeError(f"Expected a list, got {type(list_of_numbers)}")

    if len(list_of_numbers) == 0:
        return 0

    total = 0

    for number in list_of_numbers:
        if isinstance(number, float) or isinstance(number, int):
            total += number

    return total / len(list_of_numbers)


# Demonstrating the benefit of using the Typing module
# calculate_average returns a float.
# Let's see what happens if we try to use string methods on its output.
my_name = "Yuvneesh"
average = calculate_average([1, 2, 3])
a_string = my_name + average  # PyCharm highlights is due to unexpected type


if __name__ == "__main__":
    my_list = [-1, 12, 'a']
    average = calculate_average(my_list)
    print(average)
