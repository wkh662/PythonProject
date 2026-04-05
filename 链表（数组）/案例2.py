num1 = [1,2,3,4,5,123,12,23,3443,54,6]
num2 = [18,28,38,48,57,1623,152,423,33443,254,16]

# 1. 先合并（按你的写法）
for bum in num2:
    num1.append(bum)

# 解包操作
num3=[*num1,*num2]
print(num3)
print("合并后的列表（可能有重复）:", num1)

# 直接合并
num4=num1+num2
print(num4)

# 2. 双重 for 循环原地去重（不新建数组）
i = 0
while i < len(num1):
    j = i + 1
    while j < len(num1):
        if num1[i] == num1[j]:
            # 删除索引 j 处的元素
            del num1[j]
            # 删除后，后面的元素会前移，所以 j 不增加，继续检查新的 j 位置
        else:
            j += 1
    i += 1

print("去重后的列表:", num1)
