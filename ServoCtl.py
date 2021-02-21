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
        self.s_center = [s_x / 2, s_y / 2]
        self.kit = ServoKit(channels=16)
        self.angle_now = [0, 0]

    def servo_angle(self, num, angle):
        self.kit.servo[num].angle = angle

    def mv(self, num, dx):
        self.angle_now[num] += dx
        self.servo_angle(num, self.angle_now[num])

    def up(self, dx=5):
        self.mv(self, 1, dx)

    def down(self, dx=5):
        self.mv(self, 1, -dx)

    def left(self, dx=5):
        self.mv(self, 0, -dx)

    def right(self, dx=5):
        self.mv(self, 0, dx)

    def ctl(self, x, y):
        if self.s_center[0] - x > EXP:
            self.left()
        elif self.s_center[0] - x < 0-EXP:
            self.right()

        if self.s_center[1] - x > EXP:
            self.up()
        elif self.s_center[1] - x < 0-EXP:
            self.down()
