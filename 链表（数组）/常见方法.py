s=[23,234,545,24,545,665,755,75,45]
print(s)

# append ()--在列表的尾部追加元素
s.append(188)
print(s)

# insert()--在指定索引之前，插入该元素
s.insert(2,80)
print(s)

# remove()--移除列表中第一个匹配到的值。
s.remove(s[0])
#或者直接删除要删的
#s.remove(23)
print(s)

# pop()--删除列表中指定索引位置的元素(如果未指定索引，默认删最后一个)
s.pop(1)
print(s)
s.pop()
print(s)

# sort()--对列表进行排序(列表元素的数据类型一致，才可以进行排序)
s.sort()
print(s)

# reverse()--反转列表元素
s.reverse()
print(s)