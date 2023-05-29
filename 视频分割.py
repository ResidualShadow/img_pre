import os
import cv2
import numpy as np


def readtest(path, dir_path):
    i = 1
    capture = cv2.VideoCapture(path)
    if capture.isOpened():
        while True:
            ret, img = capture.read()  # img 就是一帧图片
            if not ret:
                break  # 当获取完最后一帧就结束
            # 可以用 cv2.imshow() 查看这一帧，也可以逐帧保存
            cv2.imwrite(dir_path + '/img_{}.jpg'.format(i), img)
            i += 1
            print(f"正在分割出第 {i} 张")
    else:
        print('视频打开失败！')
    print("完成！")


if __name__ == '__main__':

    a = 1
    while 1:
        try:
            os.makedirs("image_split/picture_{}".format(a))
            dir_path = f"image_split/picture_{a}"
            break
        except FileExistsError:
            a += 1

    while 1:
        try:
            picture_dir = input("请输入视频文件位置:")
            # 添加path
            dirs = os.path.join(picture_dir)
            names = os.listdir(dirs)
            break
        except (NotADirectoryError, FileNotFoundError):
            print("\n路径错误！")
    for i in range(0, len(names)):
        readtest(dirs + "/" + names[i], dir_path)
