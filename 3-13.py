# 分析一个水杯的属性和功能，使用类描述并创建对象
# 高度，容积，颜色，材质
# 能存放液体
class watercup:
    __high = 0.0 #高度
    __volum = 0    #容积
    __color =  ""    #绿色
    __texture = ""    #材质
    #高度
    def setHigh(self,high):
        if high>30 or high <10:
                print("你觉得这是个水杯？")
        else:
                self.__high = high
    def getHigh(self):
            return self.__high
    #容积
    def setVolum(self,volum):
        if volum>300 or volum<10:
             print("真有你的")
        else:
             self.__volum = volum
    def getvVolum(self):
        return self.__volum

    #颜色
    def setColor(self,color):
        self.__color = color
    def getColor(self):
        return self.__color

    #材质
    def setTexture(self,texture):
        self.__texture = texture
    def getTexture(self):
        return self.__texture

    #功能
    def water(self,num):
        if num > self.__volum:
            print("水倒的属实有点儿多")
        else:
            print("容积为",self.__volum,"ml的",self.__color,self.__texture,"水杯倒了",num,"ml水")
C = watercup()

C.setHigh(int(input('请输入水杯的高度')))
C.setVolum(int(input('请输入水杯的容积')))
C.setColor(input('请输入水杯的颜色'))
C.setTexture(input('请输入水杯的材质'))

C.water(int(input("你要倒多少水，单位是毫升：")))

# 有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）

class compuder:
    __Screen = 0  #屏幕大小
    __Price = 0  #价格
    __Cpu = ""   # cpu型号
    __Memory = ""  # 内存大小
    __Standby = ""  #待机时长
#屏幕
    def setScreen(self,screen):
        if screen >=12 and screen <=20:
            self.__screen=screen
        else:
            print('你的电脑真不错')
    def getScreen(self):
        return self.__screen
#价格
    def setPrice(self,price):
        if price >2000 and price <=5000:
            self.__Price=price
        else:
            print('您的电脑真的贵')
    def getPrice(self):
        return self.__Price
#CPU型号
    def setCpu(self,cpu):
        if cpu < 5 and cpu>0:
            print('勉强勉强')
        else:
            self.__Cpu=cpu
            print('你的电脑真的顶')
    def getCpu(self):
        return self.__Cpu
#内存
    def setMemory(self,memory):
        if memory>512 and memory<2000:
            self.__Memory=memory
            print('您的电脑内存刚刚好')
        else:
            print('您的电脑内存太小了吧')
    def getMemory(self):
        return self.__Memory
#打字
    def Typing(self, typing):
        if typing > 0:
            print("您一共打了", typing, "个字幅")
        else:
            print("请输入正确的数值")
#打游戏
    def PlayGames(self,Gamename,hour):
        if hour > 0 and hour < 24 :
            print("你今天玩",Gamename,"已经玩了",hour,"小时")
#看视频
    def Videos(self,Watchvideo,hour):
        if hour > 0 and hour < 24:
            print("你今天看",Watchvideo,"已经看了", hour, "小时")








DN=compuder()
DN.setScreen(int(input('请输入电脑屏幕大小')))
DN.setPrice(int(input('请输入电脑的价格')))
DN.setCpu(int(input('请输入cpu型号')))
DN.setMemory(int(input('请输入电脑的内存')))


DN.Typing(500)
DN.PlayGames("英雄联盟",8)
DN.Videos("回村的诱惑",12)


