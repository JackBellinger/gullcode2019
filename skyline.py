nums = input("input numbers (seperated by spaces)\n").split()
triplets = []
triplet = []
i = 0

for num in nums:
    if i%3 == 0 and i != 0 or i == len(nums):
        triplets.append(triplet)#[x for x in triplet])
        triplet = []
    triplet.append(int(num))
    i+= 1
triplets.append(triplet)

y_sorted = sorted(triplets, key=lambda point: point[2])
x_left_sorted = sorted(triplets, key=lambda point: point[0])
x_right_sorted = sorted(triplets, key=lambda point: point[1])

min = x_left_sorted[0][0]
max = x_right_sorted[-1][1]

r = [i for i in range(min, max+1)]

skyline = [[y_sorted[-1][0], y_sorted[-1][2]] ]

for point in reversed(y_sorted):
    for del_p in range(point[0] + 1, point[1]):
        r.remove(del_p)

    for add_p in range(point[0], point[1]):
        if add_p in r:
            skyline.append([point[2], add_p])

print(skyline)
