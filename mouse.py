import cv2

image = cv2.imread("girl.jpg")
cv2.namedWindow("mouse_event")
x1, y1 = 0, 0


def show_event():
    events = [i for i in dir(cv2) if 'EVENT' in i]
    print(events)


def mouse_handler(event, x, y, flags, userdata):
    global x1, y1
    if event == cv2.EVENT_LBUTTONDOWN:
        print("左键点击")
        x1, y1 = x, y
        print(x1, y1)

    # if event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        # print("鼠标左键按下拖动")
        # cv2.rectangle(image, (x1, y1), (x, y), (0, 255, 0), -1)


if __name__ == "__main__":
    cv2.setMouseCallback("mouse_event", mouse_handler)
    while True:
        cv2.imshow("mouse_event", image)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
