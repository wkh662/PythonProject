#import random--生成随机数
import random
num=random.randint (1,100)
while 1:
    ing = int(input("猜猜是几呢(づ￣ 3￣)づ"))
    if ing==num:
        print(f"wow您猜对了,就是{num}")
        break
    elif ing>num:
        print("猜大了哟(づ￣ 3￣)づ")
    else:
        print("猜小了哟(づ￣ 3￣)づ")