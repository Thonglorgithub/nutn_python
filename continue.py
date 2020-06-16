'''
n = int(input("Please Input Integer: "))
for i in range(n):
    if i * i == n:
        print("The Integer root of", n, " is ", i)
        break
else:
     print("No Integer root of ", n)
'''
'''
print("Please Enter 3 Numbers to Compose Triangle")
a = int(input("Number A "))
b = int(input("Number B "))
c = int(input("Number C "))
'''

print("Please Input 3 Numbers of Integer")
a, b, c = eval(input())
score = [a, b, c]
scored = sorted(score)
print(score)
if scored[2] < scored[0] + scored[1]:
	print("Yes")
	s = 0
	s = sum(scored) / 2
	area = (s * (s -a ) * (s - b) * (s - c)) ** 0.5
	print("The area is %.2f" %area)
else:
	print("No")