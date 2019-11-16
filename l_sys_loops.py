string = input()

north = 0
east = 1
south = 2
west = 3

class loopy_boi:
    def __init__(self):
        self.dir = 0
        self.pos = [0, 0]
        self.path = []
        self.num_commands = 0

    def input(self, c):
        if c == 'F':
            self.path.append(self.pos)
            self.step()
            # print(self.pos)
        if c == '+':
            self.t_right()
        if c == '-':
            self.t_left()
        if self.pos == [0, 0] and self.dir == 0:
            print("1 ", end = '')
            return 1
        return 0

    def t_right(self):
        self.dir = (self.dir + 1) % 4
        # print("turn" + str(self.dir))
    def t_left(self):
        self.dir = (self.dir - 1) % 4

    def step(self):
        # print("Step")
        # print(self.pos)
        if self.dir == 0:
            self.pos[1] += 1
        if self.dir == 1:
            self.pos[0] += 1
        if self.dir == 2:
            self.pos[1] -= 1
        if self.dir == 3:
            self.pos[0] -= 1

def main():
    lb = loopy_boi()
    # print("input: " + string)
    for i in range(1, 1000):
        for c in string:
            # print(c)
            end = lb.input(c)
            if end:
                print(i)
                return
    if not end:
        print("0")


if __name__ == "__main__":
    main()
