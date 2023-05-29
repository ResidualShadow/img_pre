import cv2
import numpy as np


def cv_show(img):
    # 尺寸转化，方便展示
    cv2.imshow('name',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def process(img):
    #cv_show(img)
    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv_show(image_gray)
    _, img_thr = cv2.threshold(image_gray, 170, 255, cv2.THRESH_BINARY)

    dst = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 33, 4)
    retval, dst_2 = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    #cv_show(img_thr)
    image_canny = cv2.Canny(img, 30, 150)
    #cv_show(image_canny)
    image_pz = cv2.dilate(image_canny, (5, 5), iterations=5)
    #cv_show(image_pz)
    # 找到所有轮廓
    h = cv2.findContours(image_pz,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    contours = h[0]
    # 绘制轮廓
    temp = np.ones(img.shape,np.uint8)*255
    cv2.drawContours(temp, contours, -1, (0, 0, 0), 3)
    #cv_show(temp)
    # 通过面积判断找到最大轮廓
    max_contours = 0
    area_max = 0
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])

        if area > area_max:
            area_max = area
            max_contours = i

    # 绘制轮廓
    cv2.drawContours(img, contours, max_contours, (0, 255, 0), 3)
    #cv_show(img)

    return dst_2


if __name__ == '__main__':
    # image = cv2.imread('rot/1.jpg')
    # process(image)

    cap = cv2.VideoCapture('rot/vv.avi')
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        image = process(frame)

        cv2.imshow('frame', image)
        # 按q退出视频
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
