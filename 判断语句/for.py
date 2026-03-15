# for 元素 in 待处理数据集：
#     具体处理代码
# else：（可选结构）
#     循环结束时执行的代码

msg="hello-python"

for i in msg:
    print(f"元素{i}")
else:
    print("循环结束")
#-----------------------
# range语句
# 作用:生成指定规则的数字序列
# 用法1:range(end)->
# 获取一个从o开始，到end结束的数字序列(不含end本身)
# range(5)获取的数据就是 0,1,2,3,4

# 用法2:range(start,end)->
# 获取一个从start开始，到end结束的数字序列(不含end本身)
# range(2,8)获取的数据就是 2,3,4,5,6,7

# 用法3:range(start,end,step)->
# 获取一个从start开始，到end结束的数字序列，
# step步长(不含end本身)
# range(0,10,2)获取的数据就是 0,2,4,6,8
sum=0
for j in range(1,101,2):
    sum+=j
print(sum)
