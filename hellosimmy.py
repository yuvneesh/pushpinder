def print_greeting():
    def get_greeting():
        return "Asalam Waleikum"

    for i in range(5):
        # f-string
        # print(f"{i}. Hello Pushpinder")
        print("{num}. Hello Pushpinder".format(num=i))
        print(get_greeting())


print(f"The file that printed this line is: {__name__}")


def empty_function():
    pass


if __name__ == '__main__':
    print("Finish")
    # print(print_greeting())

