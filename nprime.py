import math
def prime(x):
    for i in range(2, int(math.sqrt(x)+2)):
        if (x % i) == 0:
            return False
    return True


n = int(input())
p = 0
i = 1
end = False

while not end:
    #print(i)
    if prime(i):
        p += 1
        #print("prime #{}".format(p))
    if (p == n):
        print(str(i))
        end = True
    i += 1
