# while 条件表达式（布尔值）：
#     循环语句
#直到条件表达式为假或者退出循环
#else
#这里的else可有可无
i=0
while i<10:
    i+=1
    print("我真帅")
else:
    print("循环结束")
j= 0
sum=0
while j < 101:
    if j%2==0:
        sum+=j
        j+=1
    else:
        j+=1
        pass
else:
    print("循环结束")
    print(f"1到100之间偶数之和是：{sum}")