'''
n = 1
sum = 0
while n <= 10:
    sum = sum + n
    n += 1
print(sum)
'''
'''
n = 0
while n < 5:
    if n == 3:
        break    
    print(n)
    n += 1
print(n)
'''

'''
n = 0
while n < 100:
    if (n/3) == 33:
        break
    print(n)
    n += 1
'''

n = int(input("Please input an integer range: "))
i = 0
while i <= n:
    if i * i == n:
        print(f"The root of {n} is {i}")
        break
    else:
        print("No integer root of", n)
        i += 1
        


