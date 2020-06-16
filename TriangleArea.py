import matplotlib.pyplot as plt

class TriangleArea:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3      
            
    def __str__(self):
        a = (((self.x1 - self.x3) ** 2) + ((self.y1 - self.y3) ** 2)) ** 0.5
        b = (((self.x1 - self.x2) ** 2) + ((self.y1 - self.y2) ** 2)) ** 0.5
        c = (((self.x2 - self.x3) ** 2) + ((self.y2 - self.y3) ** 2)) ** 0.5
        s = (a + b + c) / 2
        return "{:.2f}".format((s * (s - a) * (s - b) * (s - c)) ** 0.5)
 
if __name__ == "__main__":
    p = TriangleArea(50, 10, 10, 10, 15, 50)
    print(p)


   