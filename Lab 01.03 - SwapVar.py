"""Lab 01.03 - SwapVar"""
def swapvar():
    """for get input and swap 2 of variable"""
    laongdao_data = convert_string_to_tuples(input())
    num1 = laongdao_data[0]
    num2 = laongdao_data[1]
    num1, num2 = num2, num1

    print(tuple((num1, num2)))


def convert_string_to_tuples(text_in):
    """for make a True tuples"""
    values = text_in.strip('()').split(', ')
    return tuple(map(float, values))

swapvar()
