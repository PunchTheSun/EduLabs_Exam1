# Exam1 - Question3

def my_sqrt(x: int) -> int:
    sqrt = None
    for i in range(1,x+1):
        if i*i == x:
            return i
        elif i*i < x:
            sqrt = i
        elif i*i > x:
            return sqrt

while True:
    num = int(input("Enter a non-negative number (-1 to exit): "))
    if num == -1:
        break
    print(my_sqrt(num))
