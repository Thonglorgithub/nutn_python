'''
for i in "Hello":
    print(i)
'''

'''
sum = 0
for x in range(1, 11):
    sum = sum + x
print(sum)
'''

'''
n = 0
for x in [0, 1, 2, 3]:
    if x % 2 == 0:
        continue
    print(x)
    n += 1
print("Charecter valur ", n)
'''

n = int(input("Input a integer: "))
for i in range(n):
    if i * i == n:
        print("Root integer:", i)
        break
else:
     print("Not integer root")