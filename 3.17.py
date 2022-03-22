import random
#随机生成一个整数1到100
randomnumber=random.randint(1,100)

a=int(input("猜一猜，请输入一个整数："))
flag=False
while flag==False:

    if a < randomnumber:
        print("哈哈哈，猜的太小了，再猜一次吧！")
        a=int(input("猜一猜，请输入一个整数："))
    elif a > randomnumber:
        print("哈哈哈，猜的太大了，再猜一次吧！")
        a=int(input("猜一猜，请输入一个整数:"))
    else:
        print("恭喜你，终于猜对啦!")
        a=int(input("good job"))
        flag==True
