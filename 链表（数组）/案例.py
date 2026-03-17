num=[]
for i in range(10):
    n=int(input("给个数字："))
    num.append(n)
print(num)
num.sort()
print(num)
print("min:",num[0])
print("max:",num[-1])
print("avr:",sum(num)/len(num))

