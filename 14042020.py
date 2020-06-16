import sys 
import geometry	

print(sys.platform)
print(sys.maxsize) 
x1 = float(input("Enter value X1 : "))
y1 = float(input("Enter value Y1 : "))
x2 = float(input("Enter value X2 : "))
y2 = float(input("Enter value Y2 : "))
print("Distance = {:.2f}".format(geometry.distance(x1, y1, x2, y2)))
print("Slop = {:.2f}".format(geometry.slop(x1, y1, x2, y2)))
