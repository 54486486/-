#任务：开始金币有5个金币，每猜一次减一个为0就退出（or充钱）猜错3次也退出

import  random
randint=random.randint(1,60)#随机猜测的次数的范围:int  {}
print(randint)
i=1
j=5
while i<=3:
    print("您当前的金币为:",j)
    num=int(input("请输入您猜的数字"))
    if num==randint:
        print("恭喜你猜对了")
        break
    elif num>randint:
        print("猜大了，您的金币减一")
        j=j-1
    elif num<randint:
        print("猜小了，您的金币减一")
        j=j-1
    i=i+1




