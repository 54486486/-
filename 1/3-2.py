names=[["曹操","56","男","106","IBM","500","50"],
      ["大乔","19","女","203","微软","501","60",],
      ["小乔","19","女","210","Oracle","600","60"],
      ["许褚","45","男","230","Tencent","700","10"]
      ]
a=["刘备","45","男","220","alibaba","500","30"]
names.append(a)
print(names)


i=0
a=0
v=0
b=0
c=0
while i<5:
    if names[i][6]=="50":
        a=a+1
    elif names[i][6]=="60":
        v=v+1
    elif names[i][6] == "10":
        b=b+1
    elif names[i][6] == "30":
        c=c+1
    i=i+1


print("部门编号为50的人数有：%d人"%a)
print("部门编号为60的人数有：%d人"%v)
print("部门编号为10的人数有：%d人"%b)
print("部门编号为30的人数有：%d人"%c)