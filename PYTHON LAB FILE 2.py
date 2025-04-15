# Name : SONIT AGRAWAL
# ROLL NO. : 24BEE156

# 1. Largest and smallest out of two
def largest_and_smallest(a, b):
    print("Name : SONIT AGRAWAL\nROLL NO. : 24BEE156")
    if a > b:
        print(f"Largest: {a}")
        print(f"Smallest: {b}")
    elif b > a:
        print(f"Largest: {b}")
        print(f"Smallest: {a}")
    else:
        print("Both numbers are equal.")

# 2. Largest and smallest out of three
def largest_and_smallest_three(a, b, c):
    print("Name : SONIT AGRAWAL\nROLL NO. : 24BEE156")
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    if a <= b and a <= c:
        smallest = a
    elif b <= a and b <= c:
        smallest = b
    else:
        smallest = c

    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")

# 3. Odd or Even
def odd_or_even(n):
    print("Name : SONIT AGRAWAL\nROLL NO. : 24BEE156")
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

# 4. Divisible by 10
def divisible_by_10(n):
    print("Name : SONIT AGRAWAL\nROLL NO. : 24BEE156")
    if n % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")

# 5. Minor or Major
def check_age(age):
    print("Name : SONIT AGRAWAL\nROLL NO. : 24BEE156")
    if age < 18:
        print("Minor")
    else:
        print("Major")

# 6. Number of digits
def count_digits(n):
    print("Name : SONIT AGRAWAL\nROLL NO. : 24BEE156")
    count = len(str(abs(n)))
    print(f"Number of digits: {count}")

# 7. Leap year check
def is_leap_year(year):
    print("Name : SONIT AGRAWAL\nROLL NO. : 24BEE156")
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

# 8. Valid triangle
def is_valid_triangle(a1, a2, a3):
    print("Name : SONIT AGRAWAL\nROLL NO. : 24BEE156")
    if a1 + a2 + a3 == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")

# 9. Absolute value
def absolute_value(n):
    print("Name : SONIT AGRAWAL\nROLL NO. : 24BEE156")
    if n < 0:
        print(f"Absolute value: {-n}")
    else:
        print(f"Absolute value: {n}")

# 10. Rectangle area vs perimeter
def rectangle_check(length, breadth):
    print("Name : SONIT AGRAWAL\nROLL NO. : 24BEE156")
    area = length * breadth
    perimeter = 2 * (length + breadth)
    if area > perimeter:
        print("Area is greater than Perimeter")
    else:
        print("Perimeter is greater than or equal to Area")

# 11. Check collinearity
def is_collinear(x1, y1, x2, y2, x3, y3):
    print("Name : SONIT AGRAWAL\nROLL NO. : 24BEE156")
    if (y2 - y1)*(x3 - x2) == (y3 - y2)*(x2 - x1):
        print("Points lie on a straight line")
    else:
        print("Points do not lie on a straight line")

# 12. Point-circle relation
import math
def point_circle_relation(xc, yc, r, x, y):
    print("Name : SONIT AGRAWAL\nROLL NO. : 24BEE156")
    distance = math.sqrt((x - xc)**2 + (y - yc)**2)
    if distance < r:
        print("Point is inside the circle")
    elif distance == r:
        print("Point is on the circle")
    else:
        print("Point is outside the circle")

# 13. Number to words
def num_to_word(n):
    print("Name : SONIT AGRAWAL\nROLL NO. : 24BEE156")
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
    if 0 <= n <= 19:
        print(words[n])
    else:
        print("Number out of range")

# 14. Subject marks evaluation
def calculate_result(m1, m2, m3):
    print("Name : SONIT AGRAWAL\nROLL NO. : 24BEE156")
    def grade(mark):
        if mark == -1:
            return "NA"
        elif mark <= 39:
            return "F"
        elif mark <= 44:
            return "P"
        elif mark <= 49:
            return "C"
        elif mark <= 54:
            return "B"
        elif mark <= 59:
            return "B+"
        elif mark <= 69:
            return "A"
        elif mark <= 79:
            return "A+"
        elif mark <= 100:
            return "O"
        else:
            return "Invalid"

    total = m1 + m2 + m3
    avg = total / 3
    result = "Pass" if m1 > 39 and m2 > 39 and m3 > 39 else "Fail"

    print(f"Total Marks: {total}")
    print(f"Average Marks: {avg:.2f}")
    print(f"Result: {result}")
    print(f"Grade for Subject 1: {grade(m1)}")
    print(f"Grade for Subject 2: {grade(m2)}")
    print(f"Grade for Subject 3: {grade(m3)}")
