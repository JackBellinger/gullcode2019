nums = input("input 2 numbers (seperated by a space)\n")
num1 = int(nums.split(" ")[0])
num2 = int(nums.split(" ")[1])
for i in range(abs(num2)) :
    if(num2 < 0):
        num1 -= 1
    else:
        num1 += 1
print(num1)
