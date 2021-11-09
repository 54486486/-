'''# 1、定义老手机类，有品牌属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的带一个Str类型参数的打电话的方法，内容为：“正在给xxx打电话...”
# 2、定义新手机类，继承老手机类，重写父类的打电话的方法，内容为2句话：“语音拨号中...”、“正在给xxx打电话...”
# 要求打印“正在给xxx打电话...”这一句调用父类的方法实现，不能在子类的方法中直接打印；提供无返回值的无参数的手机介绍的方法，内容为：“品牌为：xxx的手机很好用...”
# 3、定义测试类，创建新手机对象，并使用该对象，对父类中的品牌属性赋值；
# 4、使用新手机对象调用手机介绍的方法；
# 5、使用新手机对象调用打电话的方法；
'''
import  time
# 旧手机
class oldphone:
    Brand = ''

    def call(self):
        print(self.Brand,"正在给盖伦打电话")
p=oldphone()
p.Brand='苹果13pro max'

p.call()




#新手机


class OldPhone:
    Brand = ''

    def call(self):
        print("语音拨号中", self.Brand, "正在给盖伦打电话")


class NewPhone(OldPhone):

    def call(self):
        super(NewPhone, self).call()

        self.Brand = ""
        for i in range(3):
            print(". ", end="")
            time.sleep(1)

        print("品牌为苹果13 pro max的手机很好用")


p = NewPhone()
p.Brand = '苹果13pro max'

p.call()


#
'''
1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；
'''
class Cook:
    __Name=""
    __Age=0

    def setName(self,Name):
        self.__Name=Name

    def getName(self):
        return self.__Name

    def setAge(self,Age):
        self.__Age=Age

    def getAge(self):
        return self.__Age

    def steamed_rice(self):
        print("厨师会蒸饭")

class Cook1(Cook):

    def spatula(self):
        print("会炒菜")

class Cook2(Cook1):

    def steamed_rice(self):
        print("跟爷爷学会了蒸饭")

    def spatula(self):
        print("跟爸爸学会了炒菜")

B=Cook2()
B.setAge("年龄28岁的")
B.setName("心酸老八")
print(B.getAge())
print(B.getName())
B.steamed_rice()
B.spatula()



class Person:
    __name=""
    __age=0
    __sex=""

    def setName(self,name):
        self.__name=name

    def getName(self):
        return self.__name

    def setAge(self,age):
         self.__age=age

    def getAge(self):
        return self.__age

    def setSex(self,sex):
        self.__sex=sex

    def getSex(self):
        return self.__sex

class gongRen(Person):

    def shape(self):
        print("我可以干活")

class Student(gongRen): #工人是他爹

    def shape(self):
        print("我可以学习")

    def shape2(self):
        print("我是学生我会唱歌")

s=Student()
s.shape()
s.shape2()


