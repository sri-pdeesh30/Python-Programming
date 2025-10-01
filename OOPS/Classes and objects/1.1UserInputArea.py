class Circle:
    pi=3.14
    def __init__(self):
        self.radius=float(input("Enter radius :"))
    def calculate_circum(self):
        self.circum=2 * Circle.pi * self.radius
        print("Circumference :",self.circum)
    def calculate_area(self):
        self.area= Circle.pi * self.radius * self.radius
        print("Area :",self.area)
circle1=Circle()
circle1.calculate_circum()
circle1.calculate_area()

circle2=Circle()
circle2.calculate_circum()
circle2.calculate_area()