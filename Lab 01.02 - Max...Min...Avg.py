import json
"""Lab 01.02"""
def main():
    """Lab 01.02"""
    alln = 0
    my_list = json.loads(input())
    most = my_list[0]
    least = my_list[0]
    for i in my_list:
        alln += float(i)
        if float(i) > most:
            most = i
        elif float(i) < least:
            least = i
    avg = alln / len(my_list)
 
    def print_f(inp):
        """asdad"""
        two = "%.2f" % inp
        if two[-2:] == "00":
            return two[0:-3]
        elif two[-1] == "0":
            return two[0:-1]
        else:
            return two
    print("(%s, %s, %s)" % (print_f(most), print_f(least), print_f(avg)))
 
main()
