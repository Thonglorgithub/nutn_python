class IO:
    supportedSrcs = ["console", "file"]
    @staticmethod
    def read(src):
        # self.src = src
        if src not in IO.supportedSrcs:
            print("{}! Not supported".format(src))
        else:
            print("Read from", src)
        

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def distance(self, targetX, targetY):
        return (((self.x - targetX) ** 2) + ((self.y - targetY) ** 2)) ** 0.5


