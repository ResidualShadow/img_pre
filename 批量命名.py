# -*- coding: utf-8 -*-
import os

while 1:
    try:
        dir = input("请输入图片文件位置： ")
        # 添加path
        path = os.path.join(dir)
        break
    except (NotADirectoryError, FileNotFoundError):
        print("\n路径错误！")

num = eval(input("请输入第一个图片的序号："))

for file in os.listdir(path):
    os.rename(os.path.join(path,file), os.path.join(path,str(num)+".jpg"))
    num += 1
print(f'命名后的最后一张图片的名称为 {num-1}.jpg')
print(f'下一张图片的名称为 {num}.jpg')
