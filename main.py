import geometry.line as line
import geometry.point as point

def calPoint():
	print("---Point Calculation---")
	x = float(input("Enter Number X : "))
	y = float(input("Enter Number Y : "))
	print("Result : {:2f}".format(point.distance(x, y)))
	print("-----------------------")

def calLengh():	
	print("---Lengh Calculation---")
	x1 = float(input("Enter Number X1 : "))
	x2 = float(input("Enter Number X2 : "))
	y1 = float(input("Enter Number Y1 : "))
	y2 = float(input("Enter Number Y2 : "))
	print("Result : {:.2f}".format(line.len(x1, x2, y1, y2)))
	print("-----------------------")	

def calSlop():
	print("---Slop Calculation---")
	x1 = float(input("Enter Number X1 : "))
	x2 = float(input("Enter Number X2 : "))
	y1 = float(input("Enter Number Y1 : "))
	y2 = float(input("Enter Number Y2 : "))
	print("Result : {:.2f}".format(line.slop(x1, x2, y1, y2)))
	print("-----------------------")		




if __name__ == "__main__":
	# calPoint()
	calLengh()
	# calSlop()
    
