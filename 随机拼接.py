import os
import cv2
import random
import numpy as np


def stack(img_data):
    random.shuffle(img_data)
    for i in range(len(img_data)):
        img = img_data[i]
        img_resize = resize(img)
        img_data[i] = img_resize
    img_1 = np.hstack([img_data[0], img_data[1], img_data[2], img_data[3]])
    img_2 = np.hstack([img_data[4], img_data[5], img_data[6], img_data[7]])
    img_3 = np.hstack([img_data[8], img_data[9], img_data[10], img_data[11]])
    img_4 = np.hstack([img_data[12], img_data[13], img_data[14], img_data[15]])
    img_new = np.vstack([img_1, img_2, img_3, img_4])

    return img_new


def resize(img_origin, big_pad=True):
    # 原始图片尺寸
    h, w, _ = img_origin.shape
    # 目标尺寸大小
    ph, pw = 200, 280
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


def cv_show(img):
    cv2.imshow('name', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':

    mod = eval(input("请输入是否有无关图片：\n1.是\n2.否\n"))
    while 1:
        try:
            org_picture_dir = input("请输入原始图片文件位置:")
            org_dirs = os.path.join(org_picture_dir)
            org_img_names = os.listdir(org_dirs)
            org_len = len(org_img_names)
            if mod == 1:
                other_picture_dir = input("请输入无关图片文件位置:")
                other_dirs = os.path.join(other_picture_dir)
                other_img_names = os.listdir(other_dirs)
                other_len = len(other_img_names)
            break
        except (NotADirectoryError, FileNotFoundError):
            print("\n路径错误！")
    epochs = eval(input("请输入想输出多少张合成图片"))
    # 自定义长度
    numb = 16
    if mod == 1:
        numb = 12

    a = 1
    while 1:
        try:
            os.makedirs("image_joint/picture_{}".format(a))
            path = f"image_joint/picture_{a}"
            break
        except FileExistsError:
            a += 1

    for i in range(epochs):
        img_data = []
        org_numb = random.sample(range(0, org_len), numb)
        for j in org_numb:
            img = cv2.imread(org_dirs + "/" + org_img_names[j])
            img_data.append(img)

        if mod == 1:
            other_numb = random.sample(range(0, other_len), 4)
            for k in other_numb:
                img = cv2.imread(other_dirs + "/" + other_img_names[k])
                img_data.append(img)
                # 拼接图片数据组
        img_joint = stack(img_data)

        cv2.imwrite(path + '/img_{}.jpg'.format(i+1), img_joint)
        print(f"==========第{i+1}张完成！==========")
