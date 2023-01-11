# Exam1 - Question1

def second_largest(numbers: list[float]) -> float | None:
    if len(numbers) == 0:
        print("The list is empty",end=" -> ")
        return
    if len(numbers) == 1:
        print("There is only 1 number in the list.")
        return numbers[0]

    largest = numbers[0]
    sl_num = numbers[0]

    for first_run_val in numbers:
        if first_run_val > largest:
            largest = first_run_val
        if first_run_val > sl_num and first_run_val != largest:
            sl_num = first_run_val
# In the case the largest number in the array is the first number in the list, Run another For loop.
    if largest == sl_num:
        sl_num = numbers[1]
        for second_run_val in numbers:
            if second_run_val > sl_num and second_run_val != largest:
                sl_num = second_run_val
    return sl_num

# Function Execution
example_a = [54, -1, 45, 987, 5, 2, 65, 7, 12]
example_b = [1000, 54, -1, 45, 987, 5, 2, 65, 7, 12]
example_c = [3, 0, 4.5, 4.5]
exammple_d = []
examples = [example_a,example_b,example_c,exammple_d]
for ex in examples:
    print(second_largest(ex))



