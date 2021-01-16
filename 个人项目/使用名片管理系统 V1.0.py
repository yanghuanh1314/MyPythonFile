#使用名片管理系统 V1.0.py

print("{:=^30}".format("欢迎使用名片管理系统 V1.0"))

def Function ():
    print("{:=^20}".format("功能速览"))
    print("1：添加名片")
    print("2：修改名片")
    print("3：查找名片")
    print("5：帮助")

def AddCard():#添加名片
    print("{:=^15}".format("添加名片"))
    a = input("*请输入姓名：")
    b = input("*请输入性别：")
    c = input("*请输入出生日期：")
    d = input("*请输入电话：")
    e = input("请输入职业：")
    f = input("请输入住址：")
    g = input("请输入电子邮箱：")

    longA = len(a)
    longB = len(b)
    longC = len(c)
    longD = len(d)

    if longA != 0 and longB != 0 and\
        longC != 0 and  longD != 0 :
        global newCard
        newCard = []    #序列类型
        for i in a,b,c,d,e,f,g:
            newCard.append(i)
        print(newCard)
        print("保存成功！")
    else:
        print("请输入字符")
    return newCard

def FindCard():#查找名片
    print("{:=^15}".format("查找名片"))
    global newCard
    a = input("请输入姓名：")
    if a == newCard[0]:
        print(newCard)
    else:
        print("查询不到此名片")

def AlterCard():#修改名片
    print("{:=^15}".format("修改名片"))
    global newCard
    print("1：姓名")
    print("2：性别")
    print("3：生日")
    print("4：电话")
    print("5：职业")
    print("6：住址")
    print("7：电子邮箱")
    a = eval(input("q请输入序列号进行修改"))
    if a == 1:
        name = input("请输入正确姓名：")
        newCard[0] = name
        print("修改成功")
        print(newCard)
    elif a == 2:
        gender = input("请输入正确性别：")
        newCard[1] = gender
        print("修改成功")
        print(newCard)
    elif a == 3:
        birthday = input("请输入正确性别：")
        newCard[2] = birthday
        print("修改成功")
        print(newCard)
    elif a == 4:
        telephona = input("请输入正确性别：")
        newCard[3] = telephona
        print("修改成功")
        print(newCard)
    elif a == 5:
        job = input("请输入正确性别：")
        newCard[4] = job
        print("修改成功")
        print(newCard)
    elif a == 6:
        address = input("请输入正确性别：")
        newCard[5] = address
        print("修改成功")
        print(newCard)
    elif a == 7:
        email = input("请输入正确性别：")
        newCard[6] = email
        print("修改成功")
        print(newCard)

def Help():#帮助
    print("输入相关序列号")

Function()
a = eval(input("请输入序号："))
AddCard()
FindCard()
AlterCard()
Help()
