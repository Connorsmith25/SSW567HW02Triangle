# Connor Smith
# Professor Saremi
# SSW 567
# HW 02a
# "I pledge my honor that I have abided by the Stevens Honor System"
def classifyTriangle(a, b, c):

    # check if input is valid
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    if a > 300 or b > 300 or c > 300:
        return 'InvalidInput'

    # sort sides by length for easier calculations
    sides = (a, b, c)
    a, b, c = sorted(sides)

    # check if input is a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    elif ((a ** 2) + (b ** 2)) == (c ** 2):
        return 'Right'
    if a == b == c:
        return 'Equilateral'
    elif (a == b) or (a == c) or (b == c):
        return 'Isosceles'
    else:
        return 'Scalene'
