"""Lab 02.01 - Stack (Create Stack)"""
class ArrayStack:
    """create stack"""
    def __init__(self):
        """set default of attribute size and data"""
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        """delete the last one of data in stack"""
        if self.size == 0 or self.data == False:
            print("Underflow: Cannot pop data from an empty list")
            return None
        elif self.size != 0 or self.data == True:
            infomation = self.data[-1]
            self.data.pop()
            self.size -= 1
            return infomation

    def is_empty(self):
        """check if stack is Empty return True else return False"""
        if self.size == 0 or self.data == False:
            return True
        return False

    def get_stack_top(self):
        """get last data in stack"""
        if self.size == 0:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        return self.data[-1]

    def get_size(self):
        """get size of data"""
        return self.size

    def print_stack(self):
        """print all data in stack"""
        print(self.data)

STACK = ArrayStack()

STACK.push("100")
STACK.push(100)
STACK.push("3.14")
STACK.push(3.14)
STACK.push("66.4a")
STACK.push("Ackerman")

STACK.print_stack()

print(STACK.get_size())
VAR1 = STACK.pop()
print(VAR1)
STACK.print_stack()
print(STACK.get_size())

while not STACK.is_empty():
    print(STACK.pop())

print()
print(STACK.pop())
print(STACK.get_stack_top())
print(VAR1)
