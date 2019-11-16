in_str = input()
array = in_str.split(" ")
for i in range(len(array)):
    array[i] = int(array[i])

min = array[0]
max = array[0]
for x in array:
    if x < min:
        min = x
    if x > max:
        max = x

fill = 0

for i in range(min+1, max+1):
    raised = False
    temp = 0
    for x in array:
        if (x >= i) and not raised:
            raised = True
        elif (x < i) and raised:
            temp += 1
        elif (x >= i) and raised:
            fill += temp
            temp = 0

print(str(fill))
