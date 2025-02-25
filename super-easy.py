import math

def calculateArea(a):
    f = float((a**2) / 4.0)
    return f

def main():
    n = int(input())
    print(calculateArea(n))
    return 0


main()