"""Elevator"""
class Elevator:
    """Elevator"""
    def __init__(self, max_floor):
        """for set in class variable"""
        self.current_floor = 1
        self.max_floor = max_floor


    def go_to_floor(self, floor):
        """for update current floor"""
        if int(floor) <= self.max_floor:
            self.current_floor = floor
        else:
            print("Invalid Floor!")
        return self.current_floor

    def report_current_floor(self):
        """for inform client to know last floor before type 'Done'"""
        print(self.current_floor)

def main():
    """for calling cls"""
    maximum = Elevator(int(input()))
    # print(maximum.report_current_floor())
    while True:
        now_floor = input()
        if now_floor != "Done":
            maximum.go_to_floor(now_floor)
        else:
            maximum.report_current_floor()
            break

main()
