import time  # 引入time库
from adafruit_servokit import ServoKit  # 引入刚刚安装的PCA9685库并将名字缩写成ServoKit方便后续调用
EXP = 1
# [0]xy , [1] z
# kit = ServoKit(channels=16)  # 明确PCA9685的舵机控制数
#
# kit.servo[0].angle = 180  # channel0上的舵机旋转180度。
# time.sleep(1)  # 休眠一秒
# kit.servo[0].angle = 0  # channel0上的舵机回到初始的0度。


class ServoCtl():
    def __init__(self, s_x, s_y):
        self.s_center = [s_x / 4, s_y / 4]
        print('( '+str(s_x / 4)+' , '+str(s_y / 4)+' )')
        self.kit = ServoKit(channels=16)
        self.angle_now = [0, 0]

    def servo_angle(self, num, angle):
        self.kit.servo[num].angle = angle
        #print(num)

    def mv(self, num, dx):
        tmp = self.angle_now[num]
        tmp += dx
        print(tmp)
        if tmp >180 or tmp < 0:
            tmp -= dx
        self.angle_now[num] = tmp
        self.servo_angle(num,tmp)

    def up(self, dx=5):
        self.mv( 1, dx)
        print('dy > 0')

    def down(self, dx=5):
        self.mv( 1, 0-dx)
        print('dy < 0')

    def left(self, dx=5):
        self.mv( 0, 0-dx)
        print('dx < 0')

    def right(self, dx=5):
        self.mv( 0, dx)
        print('dx > 0')

    def ctl(self, x, y):
        print(str(self.s_center[0])+' - '+str(x)+' = '+str(self.s_center[0] - x)+'------'+str(self.s_center[1])+' - '+str(y)+' = '+str(self.s_center[1] - y))
        if self.s_center[0] - x > EXP:
            self.left()
        elif self.s_center[0] - x < (0-EXP):
            self.right()

        if self.s_center[1] - y > EXP:
            self.up()
        elif self.s_center[1] - y < (0-EXP):
            self.down()
            
if __name__== '__main__':
    s = ServoCtl(1,2)
    s.servo_angle(0,180)
