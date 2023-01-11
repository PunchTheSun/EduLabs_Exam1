# Exam1 - Question2

def fizz_buzz(num: int) -> list[str]:
    ret_val = []
    for i in range(1,num+1):
        if i % 3 == 0 and i % 5 == 0:
            ret_val.append("FizzBuzz")
        elif i % 3 == 0:
            ret_val.append("Fizz")
        elif i % 5 == 0:
            ret_val.append("Buzz")
        else:
            ret_val.append(str(i))
    return ret_val

while True:
    num = input("Please enter a number ($$$ to exit): ")
    if num == "$$$":
        break
    if not num.isnumeric():
        print("Invalid input, Not a number.\nTry again.")
    else:
        print(fizz_buzz(int(num)))
