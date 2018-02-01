import random
import math
# RGB空间转HSI空间
def rgb2hsi(r,g,b):

    h = 0
    s = 0
    i = 0

    r_tmp = r / 255
    g_tmp = g / 255
    b_tmp = b / 255
    max_tmp = max(r_tmp,g_tmp,b_tmp)
    min_tmp = min(r_tmp,b_tmp,g_tmp)
    delta = max_tmp - min_tmp

    i = (max_tmp + min_tmp) / 2

    if delta == 0:
        h = 0
        s = 0
    else:
        if max_tmp == r_tmp:
            h = 60 * (((g_tmp - b_tmp) / delta) % 6)
        elif max_tmp == g_tmp:
            h = 60 * (((b_tmp - r_tmp) / delta) + 2)
        else:
            h = 60 * (((r_tmp - g_tmp) / delta) + 4)
        
        s = delta / (1 - abs( 2 * i - 1))

    return [h,s,i]

def yiq2rgb(y,i,q):
    r = (y + ( 0.956 * i) + ( 0.621 * q))
    g = (y + (-0.272 * i) + (-0.647 * q))
    b = (y + (-1.105 * i) + ( 1.702 * q))

    if r < 0:
        r=0
    elif r > 255:
        r = 255

    if g < 0:
        g=0 
    elif g > 255:
        g = 255

    if b < 0:
        b=0
    elif b > 255:
        b = 255
    return [r,g,b]

def quickt2c(t,p,q):
    c = 0
    if t < 1/6:
        c = p + ((q - p) * 6 * t)
    elif t >= 1/6 and t < 1/2:
        c = q
    elif t >= 1/2 and t < 2/3:
        c = p + ((q - p) * 6 * (2/3 - t))
    else:
        c = p
    
    return c

def hsi2rgb(h,s,i):
    if h >= 360:
        h = 359
    c = (1 - abs(2 * i - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = i - c/2

    (rt,gt,bt) = (0,0,0)

    if h < 60:
        rt = c
        gt = x
        bt = 0
    elif h < 120:
        rt = x
        gt = c
        bt = 0
    elif h < 180:
        rt = 0
        gt = c
        bt = x
    elif h < 240:
        rt = 0
        gt = x
        bt = c
    elif h < 300:
        rt = x
        gt = 0
        bt = c
    elif h < 360:
        rt = c
        gt = 0
        bt = x
    
    r = (rt + m)
    g = (gt + m)
    b = (bt + m)

    return [r,g,b]

# 高斯噪声
# num 要加噪声的数
# range 数的范围
# level 噪声级别
def gaussianNoise(num1,num2,range,level):
    r = random.random()
    phi = random.random()

    z1 = level * math.cos(2*math.pi*phi) * math.sqrt(-2 * math.log(r))
    z2 = level * math.sin(2*math.pi*phi) * math.sqrt(-2 * math.log(r))
    
    f1 = num1 + z1
    f2 = num2 + z2

    res1 = 0
    res2 = 0

    if f1 < 0:
        res1 = 0
    elif f1 > range:
        res1 = range
    else:
        res1 = f1

    if f2 < 0:
        res2 = 0
    elif f2 > range:
        res2 = range
    else:
        res2 = f2

    return (res1,res2)