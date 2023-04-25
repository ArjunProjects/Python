# read two nums from the user and multiply them

def mul_nums(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    else:
        return num1 * num2


read_num1 = int(input("enter first number:"))
read_num2 = int(input("enter second number:"))
print(mul_nums(read_num1, read_num2))
