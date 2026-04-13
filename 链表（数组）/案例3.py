#生成1-20的平方数
num=[]
for i in range(1,21):
    num.append(i**2)


print(num)


#方式2   列表推到式
#语法格式[要插入的值 for i in 序列/列表 if 条件]
                 # 要遍历的         要符合的条件
num1=[i**2 for i in range(1,21)]


#从列表中提取偶数并平方
num2=[1,2,3,4,5,6,7,89,10]
num3=[i**2 for i in num2]
num4=[i%2==0 for i in num3]#错误示范
num5=[i**2 for i in num3 if i%2==0]#错误示范

print(num4)
print(num5)