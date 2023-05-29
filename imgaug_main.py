import numpy as np
import imgaug_process
import imgaug
import random
import cv2
import os

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

    epochs = input("\n请输入生成子图片的个数:")

    while 1:
        mod = input("\n模式1：自定义增强方法\n模式2：随机使用增强方法\n请输入想使用的模式：")
        if mod == '1':
            print('\n图像增强共有如下几种方法：\n1.缩放\n2.裁剪\n3.旋转\n4.平移'
                  + '\n5.噪音\n6.随机亮度\n7.随机色彩饱和度\n8.随机对比度\n9.随机清晰度')
            way = input("\n请输入你想要的方法序号(以空格分割):")
            way_str_numb = way.split()
            way_numb = []
            for i in way_str_numb:
                way_numb.append(eval(i))
            way_numb = list(tuple(way_numb))
            random.shuffle(way_numb)
            numb = len(way_numb)
            break

        elif mod == '2':
            print('\n图像增强共有如下几种方法：\n1.缩放\n2.裁剪\n3.旋转\n4.平移'
                  + '\n5.噪音\n6.随机亮度\n7.随机色彩饱和度\n8.随机对比度\n9.随机清晰度')
            numb = eval(input("\n请输入每次图片使用增强方法的个数:"))
            if numb > 10:
                numb = 10
            if numb < 1:
                numb = 1
            way_numb = random.sample(range(1, 9), numb)
            break
        else:
            print("ERROR!")

    a = 1
    if mod == '1':
        while 1:
            try:
                os.makedirs("model_1/picture_{}".format(a))
                path = f"model_1/picture_{a}"
                break
            except FileExistsError:
                a += 1
    if mod == '2':
        while 1:
            try:
                os.makedirs("model_2/picture_{}".format(a))
                path = f"model_2/picture_{a}"
                break
            except FileExistsError:
                a += 1

    # 循环读取dirs下的图片
    for i in range(0, len(image_names)):
        image = cv2.imread(dirs + "/" + image_names[i])
        imgaug_process.imgaug_process(image, i, numb, path, eval(epochs), mod, way_numb)



