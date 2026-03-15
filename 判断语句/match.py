day=input("今天周几：")
match day:
    case"1":
        print("今天周一")
    case"2":
        print("今天周二")
    case "3":
        print("今天周三")
    case "4":
        print("今天周四")
    case "5":
        print("今天周五")
    case "6"|"7":
        print("今天周末")
    case _:
        print("输入错误")









