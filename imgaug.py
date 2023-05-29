import cv2
import numpy as np
import random
from PIL import Image, ImageEnhance


def fill(img_org):
    h, w, _ = img_org.shape
    # 获取上、下填充尺寸
    top = bottom = h * 0.2
    left = right = w * 0.2
    img_new = cv2.copyMakeBorder(img_org, int(top), int(bottom), int(left), int(right),
                                 borderType=cv2.BORDER_CONSTANT, value=(255, 255, 255))
    return img_new


def resize(img_origin, big_pad=True):
    # 原始图片尺寸
    h, w, _ = img_origin.shape
    # 目标尺寸大小
    ph, pw = np.random.randint(h-(h/5), h*3/2), np.random.randint(h-(h/5), h*3/2)
    # 以原图为中心进行边缘填充
    if big_pad and ph > h and pw > w:
        # 获取上、下填充尺寸
        top = bottom = (ph - h) // 2
        # 为保证目标大小，无法整除则上+1
        top += (ph - h) % 2
        left = right = (pw - w) // 2
        # 为保证目标大小，同理左上+1
        left += (pw - w) % 2
        img_new = cv2.copyMakeBorder(img_origin, top, bottom, left, right,
                                     borderType=cv2.BORDER_CONSTANT, value=(0, 0, 0))
    else:
        # 最小比例缩放填充（大尺寸：高/宽比例变化较大的将被填充，小尺寸反之）
        # 计算缩放后图片尺寸
        scale = min(pw / w, ph / h)
        # 获取高/宽变化最小比例
        nw, nh = int(scale * w), int(scale * h)
        # 对原图按照目标尺寸的最小比例进行缩放
        img_resized = cv2.resize(img_origin, (nw, nh))
        # 获取上、下填充尺寸
        top = bottom = (ph - nh) // 2
        # 为保证目标大小，无法整除则上+1
        top += (ph - nh) % 2
        left = right = (pw - nw) // 2
        # 为保证目标大小，同理左上+1
        left += (pw - nw) % 2
        img_new = cv2.copyMakeBorder(img_resized, top, bottom, left, right,
                                     borderType=cv2.BORDER_CONSTANT, value=(0, 0, 0))
    return img_new


def cut(img_org):
    # 获取初始高、宽
    org_h, org_w = img_org.shape[0], img_org.shape[1]
    # 随机获取裁剪框大小
    cut_h, cut_w = np.random.randint(int(org_h / 4 * 3), int(org_h / 5 * 4)), np.random.randint(int(org_w / 4 * 3),
                                                                                            int(org_w / 5 * 4))
    # 随机获取裁剪坐标
    h = np.random.randint(0, int(org_h / 5))
    w = np.random.randint(0, int(org_h / 5))

    # 先把numpy数组转换为Image对象
    pil_img = Image.fromarray(img_org.astype('uint8')).convert('RGB')
    crop_pillow = pil_img.crop((w, h, w + cut_w, h + cut_h))
    # 再转回来
    img_new = np.array(crop_pillow)
    return img_new


def mosaic(img_org):
    img_new = img_org.copy()
    h, w, n = img_org.shape
    size = 4  # 马赛克大小
    for i in range(size, h - 1 - size, size):
        for j in range(size, w - 1 - size, size):
            i_rand = np.random.randint(i - size, i)
            j_rand = np.random.randint(j - size, j)
            img_new[i - size:i + size, j - size:j + size] = img_org[i_rand, j_rand, :]
    return img_new


def rotate(img_org):
    img_new = Image.fromarray(np.uint8(img_org))
    # 如果旋转角度未传入，则随机生成
    angle = np.random.randint(-6, 6)
    # PIL裁剪
    img_new = np.array(img_new.rotate(angle, Image.BILINEAR, expand=True))
    return img_new


def translation(img_org):
    # 创建0~3的随机数数组用于挑选平移方向
    a = np.random.randint(0, 4, size=[4])
    # 创建一个数组用于收集平移数据量
    numb = [0, 0, 0, 0]
    # 挑选边框、键入平移量
    # 1、第一个数和第二个数相等、直接按第一个数平移
    # 2、第一个数字和第二个数字的差不为2（相邻），则往这个方向平移
    # 3、第一个数字和第二个数字的差为2（相对），则取第0个数字为平移量，同1平移
    h, w, _ = img_org.shape
    b = min(h, w)
    if a[0] == a[1]:
        numb[a[0]] = np.random.randint(b/10, b/8)
    else:
        if abs(a[0] - a[1]) != 2:
            numb[a[0]], numb[a[1]] = np.random.randint(b/10, b/8), np.random.randint(b/10, b/8)
        else:
            numb[a[0]] = np.random.randint(b/10, b/8)
    img_new = cv2.copyMakeBorder(img_org, numb[0], numb[2], numb[1], numb[3],
                                 cv2.BORDER_CONSTANT, value=(0, 0, 0))
    return img_new


def gaussian(img_org):
    # 自定义随机sigma和mean
    sigma = np.random.randint(5, 15)
    mean = np.random.randint(-8, 8)
    # 从正态（高斯）分布中抽取随机样本
    noise = np.random.normal(loc=mean, scale=sigma, size=img_org.shape)
    img_new = np.add(img_org, noise)
    # 除一下才看得清图像
    # img_new = img_new / 255
    return img_new


def brightness(img_org):
    img_new = Image.fromarray(np.uint8(img_org))
    bright = np.random.uniform(0.4, 1.4)
    img_new = np.array(ImageEnhance.Brightness(img_new).enhance(bright))
    return img_new


def color(img_org):
    img_new = Image.fromarray(np.uint8(img_org))
    color = np.random.uniform(0.7, 1.5)
    img_new = np.array(ImageEnhance.Color(img_new).enhance(color))
    return img_new


def contrast(img_org):
    img_new = Image.fromarray(np.uint8(img_org))
    contrast = np.random.uniform(0.8, 1.2)
    img_new = np.array(ImageEnhance.Contrast(img_new).enhance(contrast))
    return img_new


def definition(img_org):
    img_new = Image.fromarray(np.uint8(img_org))
    sharpness = np.random.uniform(-1.5, 1.5)
    img_new = np.array(ImageEnhance.Sharpness(img_new).enhance(sharpness))
    return img_new


if __name__ == '__main__':
    img = cv2.imread('data\dog.jpg')
    cv2.imshow('gauss', gaussian(img))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
