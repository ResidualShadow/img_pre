import cv2
import numpy as np
import os
import random


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':

    while 1:
        try:
            picture_dir = input("请输入图片文件位置(以数字命名):")
            # 添加path
            dirs = os.path.join(picture_dir)
            image_names = os.listdir(dirs)
            break
        except (NotADirectoryError, FileNotFoundError):
            print("\n路径错误！")

    num = eval(input('请输入想生成的文件夹数:'))
    a = 1
    for i in range(num):
        while 1:
            try:
                os.makedirs("image_random/{}".format(a))
                path = f"image_random/{a}"
                break
            except FileExistsError:
                a += 1
    for j in range(1, num+1):
        ls = np.random.randint(1, 33, size=[2])
        for k in ls:
            image = cv2.imread(dirs + f'\{k}.jpg')
            # cv_show('1',image)
            cv2.imwrite(f'image_random/{j}' + f'\{k}.jpg', image)
