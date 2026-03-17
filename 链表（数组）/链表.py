#链表中元素可以不同但是工程中一般相同

#链表中元素可以修改

#链表元素可以相同

#正向索引s[0]-s[n]    反向索引是s[-1]-s[-k]

s=[1,2,3,"a",True]
print(type(s))

#访问
print(s[0])
print(s[-5])

#修改
s[1]="(づ￣ 3￣)づ"
print(s[1])

#删除
del s[3]
print(s)

for i in s:
    print(i)



