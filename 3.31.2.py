print("Besti计算器")
flag = True
while flag == True:
    choice = input("请选择你想要的计算器类型，1代表复数计算器，0代表普通计算器")
    if choice == "0":
        op = input("请输入需要做的操作(+、-、*、/、%、//,输入0代表退出):\n")
        if op == "0":
            break
        a = int(input("请输入操作数1\n"))
        b = int(input("请输入操作数2\n"))
    elif choice == "1":
        op = input("请输入需要做的操作(+、-、*、/、%、//,输入0代表退出):\n")
        if op == "0":
            break
        a = complex1 = complex(input("请输入第一个复数：\n"))
        b = complex2 = complex(input("请输入第二个复数：\n"))
        result = 0
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b
        elif op == "%":
            result = a % b
        elif op == "//":
            result = a // b
        else:
            print("输入有误，请重新输入\n")
            continue
        print("a" + op + "b=", result)

