# import the required library
import math


def calculate_cosine(angle_in_degrees):
    # do not forget to round the result and print it
    radian = math.radians(angle_in_degrees)
    print(round(math.cos(radian), 2))
