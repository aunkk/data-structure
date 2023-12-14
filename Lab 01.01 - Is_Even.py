"""Lab 01.01 - Is_Even"""
def is_even(number):
    """check the number if that's Even print True else False"""
    if int(number[-1]) in (2, 4, 6, 8, 0):
        print("True")
    else:
        print("False")

is_even(input())
