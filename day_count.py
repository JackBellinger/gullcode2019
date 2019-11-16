def isLeap(y):
    if(y % 400 == 0):
        return 1
    elif (y%100) == 0:
        return 0
    elif (y%4) == 0:
        return 1
    return 0

date = input()
fy = int(date.split(" ")[0])
fm = int(date.split(" ")[1])
fd = int(date.split(" ")[2])

cy = 2019
cm = 11
cd = 16


diff = 0
if (fy > (cy + 1)):
    leap = 0
    for i in range(cy, fy):
        if isLeap(i):
            leap += 1

    diff = leap + 365*(fy - cy - 1)

if fy == cy:
    if fm == cm:
        diff += fd - 16
    else:
        diff = fd + 14

else:
    diff += 45
    if (fm > 2) and isLeap(fy):
        diff += 1
        #ignore 1
    if fm == 2:
        diff += 31
    elif fm == 3:
        diff += 59
    elif fm == 4:
        diff += 90
    elif fm == 5:
        diff += 120
    elif fm == 6:
        diff += 151
    elif fm == 7:
        diff += 181
    elif fm == 8:
        diff += 212
    elif fm == 9:
        diff += 243
    elif fm == 10:
        diff += 273
    elif fm == 11:
        diff += 304
    elif fm == 12:
        diff += 334

    diff += fd

print(str(diff))
