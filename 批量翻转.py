import os
import cv2
import numpy as np


def flip(img_origin):
    img = cv2.flip(img_origin, 1)
    return img


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
            os.makedirs("flip/picture_{}".format(a))
            path = f"flip/picture_{a}"
            break
        except FileExistsError:
            a += 1

    # 循环读取dirs下的图片
    for i in range(0, len(image_names)):
        image = cv2.imread(dirs + "/" + image_names[i])
        image_new = flip(image)
        cv2.imwrite(path + '/{}.jpg'.format(i + 1), image_new)
        print(f'第 {i+1} 张图片完成！')