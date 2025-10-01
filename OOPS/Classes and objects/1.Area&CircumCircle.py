'''class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def calculate_circum(self):
        self.circum=2 * Circle.pi * self.radius
        print("Circumference :",self.circum)
    def calculate_area(self):
        self.area= Circle.pi * self.radius * self.radius
        print("Area :",self.area)
circle1=Circle(11.6)
circle1.calculate_circum()
circle1.calculate_area()

circle2=Circle(8.76)
circle2.calculate_circum()
circle2.calculate_area()'''

class Solution(object):
    def isSameAfterReversals(self, num):
        if num == 0:
            return True

        def reverse(n):
            rev = 0  # ✔️ defined inside function
            while n > 0:
                digit = n % 10
                rev = rev * 10 + digit
                n = n // 10
            return rev

        first = reverse(num)
        second = reverse(first)

        return second == num

number = Solution()
print(number.isSameAfterReversals(234))  # ✔️ Will print: True




















































































































