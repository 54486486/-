import time
for i in range(0,100):
    name = str(input("请输入用户名"))
    password = str(input("请输入密码"))
    if name=="root" and password=="admin":
            print("登录成功")
            break
    elif name!="root" or password!="admin":

            print("用户名密码错误，请重新输入")
            if i >= 2:
                print("对不起！机会只有三次，您的账号已经被锁死")
                time.sleep(999999)