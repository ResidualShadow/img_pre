import os
import cv2
import numpy as np


def resize(img_origin, big_pad=True):
    # 原始图片尺寸
    h, w, _ = img_origin.shape
    # 目标尺寸大小
    ph, pw = 480, 640
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


if __name__ == '__main__':

    while 1:
        try:
            picture_dir = input("请输入图片文件位置:")
            # 添加path
            dirs = os.path.join(picture_dir)
            image_names = os.listdir(dirs)
            break
        except (NotADirectoryError, FileNotFoundError):
            print("\n路径错误！")

    a = 1
    while 1:
        try:
            os.makedirs("resize/picture_{}".format(a))
            path = f"resize/picture_{a}"
            break
        except FileExistsError:
            a += 1



    # 循环读取dirs下的图片
    for i in range(0, len(image_names)):
        image = cv2.imread(dirs + "/" + image_names[i])
        image_new = resize(image)
        cv2.imwrite(path + '/{}.jpg'.format(i + 1), image_new)
        print(f'第 {i+1} 张图片完成！')