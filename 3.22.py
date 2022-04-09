import random
#随机生成一个整数1到100
randomnumber=random.randint(1,100)

a=int(input("猜一猜，请输入一个整数吧:"))
flag=False
while flag==False:

    if a < randomnumber:
        print("哈哈哈，你猜的数太小啦，再猜一次吧！")
        int(input("猜一猜，请输入一个整数吧："))
    elif a > randomnumber:
        print("哈哈哈，你猜的数太大了，再猜一次吧！")
        int(input("猜一猜，请输入一个整数吧："))
    else:
        print("哟西，你终于猜对啦！")
        a=int(input("good job"))
        flag==True