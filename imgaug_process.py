import imgaug
import random
import cv2
import os


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def imgaug_process(img_org, picture_num, numb, path, epochs, mod, way_numb):
    img_org = imgaug.fill(img_org)
    count = 1
    print(f'******************************第{picture_num + 1}张图片******************************\n')


    for i in range(epochs):
        img_copy = img_org.copy()
        if mod == '2':
            way_numb = random.sample(range(1, 9), numb)
        if mod == '1':
            random.shuffle(way_numb)
        print(f"####################正在进行第{i + 1}轮增强####################")
        print('本轮增强的方法代号为：', way_numb)
        for j in way_numb:
            if j == 1:
                # 缩放
                img_copy = imgaug.resize(img_copy)
                # cv2.imwrite(path + '/img_{}.jpg'.format(count), img_random_resized)
                count += 1
            if j == 2:
                # 裁剪
                # img_copy_2 = img_org.copy()
                img_copy = imgaug.cut(img_copy)
                # cv2.imwrite(path + '/img_{}.jpg'.format(count), img_random_cut)
                count += 1
            # if way_numb[j] == 3:
            #     # 马赛克
            #     img_copy_3 = img_org.copy()
            #     img_org = imgaug.mosaic(img_org)
            #     cv2.imwrite(path + '/img_{}.jpg'.format(count), img_mosaic)
            #     count += 1
            if j == 3:
                # 旋转
                # img_copy_4 = img_org.copy()
                img_copy = imgaug.rotate(img_copy)
                # cv2.imwrite(path + '/img_{}.jpg'.format(count), img_rotate)
                count += 1
            if j == 4:
                # 平移
                # img_copy_5 = img_org.copy()
                img_copy = imgaug.translation(img_copy)
                # cv2.imwrite(path + '/img_{}.jpg'.format(count), img_translation)
                count += 1
            if j == 5:
                # 高斯噪音
                # img_copy_6 = img_org.copy()
                img_copy = imgaug.gaussian(img_copy)
                # cv2.imwrite(path + '/img_{}.jpg'.format(count), img_gaussian)
                count += 1
            if j == 6:
                # 亮度
                # img_copy_7 = img_org.copy()
                img_copy = imgaug.brightness(img_copy)
                # cv2.imwrite(path + '/img_{}.jpg'.format(count), img_brightness)
                count += 1
            if j == 7:
                # 色彩
                # img_copy_8 = img_org.copy()
                img_copy = imgaug.color(img_copy)
                # cv2.imwrite(path + '/img_{}.jpg'.format(count), img_color)
                count += 1
            if j == 8:
                # 对比度
                # img_copy_9 = img_org.copy()
                img_copy = imgaug.contrast(img_copy)
                # cv2.imwrite(path + '/img_{}.jpg'.format(count), img_contrast)
                count += 1
            if j == 9:
                # 清晰度
                # img_copy_10 = img_org.copy()
                img_copy = imgaug.definition(img_copy)
                # cv2.imwrite(path + '/img_{}.jpg'.format(count), img_definition)
                count += 1
        cv2.imwrite(path + '/img_{}_{}.jpg'.format(picture_num + 1, i + 1), img_copy)
    print(f'----------完成！已保存到mode_{mod}文件夹下！----------\n')
