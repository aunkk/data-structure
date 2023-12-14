"""Rectangle"""
class Rectangle:
    """class of rectangle"""
    def __init__(self, height, width):
        """for defind variable in class"""
        self.height = height
        self.width = width

    def calculate_area(self):
        """for calculate rectangle area"""
        return self.height * self.width

    def calculate_perimeter(self):
        """for calculate rectangle perimeter"""
        return self.height*2 + self.width*2

def main():
    """for run main function"""
    rectangle = Rectangle(float(input()), float(input()))

    condition = input()
    if condition == "area":
        result = rectangle.calculate_area()
    else:
        result = rectangle.calculate_perimeter()
    print("%.2f" % result)

main()
