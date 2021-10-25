import math
a=float(input("请输入边长a"))
b=float(input("请输入边长b"))
c=float(input("请输入边长c"))
if a+b>c and  a+c>b and b+c>a:
    print("您输入的三条边长构成普通三角形")
if a==b==c:
    print("您输入的三条边长构成等边三角形")
if a*a+b*b==c*c or b*b+c*c==a*a or c*c+a*a==b*b:
    print("您输入的三条边长构成直角三角形")
if a+b>c and  a+c>b and b+c>a and (a==b or a==c or b==c):
    print("您输入的三条边长构成等腰三角形")
if a + b < c or a + c < b or b + c < a:
    print("不能构成三角形")
