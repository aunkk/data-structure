"""Lab 01.05 - Point"""
class Point:
    """Point"""
    def __init__(self, x=0, y=0):
        """for set vriable in class"""
        self.set_coordinates(x, y)

    def set_coordinates(self, x, y):
        """set value x, y"""
        self.x = x
        self.y = y

    def get_coordinates(self):
        """covert value to tuples"""
        return (self.x, self.y)

    def calculate_distance(self, other_point):
        """calculate the point distance"""
        return ((other_point.x - self.x)**2 + (other_point.y - self.y)**2) ** 0.5

def main():
    """for calling and check"""
    point_boss = Point(float(input()), float(input()))
    point_art = Point(float(input()), float(input()))
    result = point_boss.calculate_distance(point_art)
    print("%.2f" % result)
main()
