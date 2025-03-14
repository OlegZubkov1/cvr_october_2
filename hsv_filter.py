# H - hue (цветовой тон, цвет)
# S - saturation (насыщенность)
# V - value (яркость)
# l - low (нижняя граница)
# n - high (верхняя граница)
# lh - нижняя граница цвета

import numpy as np
import cv2

cv2.namedWindow("mask")

lh, ls, lv = (0, 0, 0)
hh, hs, hv = (255, 255, 255)
def nothing(x):
    pass


cv2.createTrackbar("lh", "mask",lh , 255, nothing)
cv2.createTrackbar("ls", "mask", ls, 255, nothing)
cv2.createTrackbar("lv", "mask", lv, 255, nothing)
cv2.createTrackbar("hh", "mask", hh, 255, nothing)
cv2.createTrackbar("hs", "mask", hs, 255, nothing)
cv2.createTrackbar("hv", "mask", hv, 255, nothing)

cam = cv2.VideoCapture(0)

while (True):
    success, frame = cam.read()

    # frame[100 : 550, 100 : 550, 0] = 240
    # frame[:, :, 2] += 50

    # print(frame.shape)

    # frame = 255 - frame

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("lh", "mask")
    ls = cv2.getTrackbarPos("ls", "mask")
    lv = cv2.getTrackbarPos("lv", "mask")
    hh = cv2.getTrackbarPos("hh", "mask")
    hs = cv2.getTrackbarPos("hs", "mask")
    hv = cv2.getTrackbarPos("hv", "mask")

    print(lh, ls, lv), (hh, hs, hv)

    mask = cv2.inRange(hsv, (lh, ls, lv), (hh, hs, hv))

    cv2.imshow("mask", mask)

    connectivity = 4
    # Perform the operation
    output = cv2.connectedComponentsWithStats(mask, connectivity, cv2.CV_32S)

    # Get the results
    # The first cell is the number of labels
    num_labels = output[0]
    # The second cell is the label matrix
    labels = output[1]
    # The third cell is the stat matrix
    stats = output[2]

    filtered = np.zeros_like(mask)

    for i in range(1, num_labels):
        a = stats[i, cv2.CC_STAT_AREA]
        t = stats[i, cv2.CC_STAT_TOP]
        l = stats[i, cv2.CC_STAT_LEFT]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]

        # print(a)

        if (a >= 500 and a < 5500):
            filtered[np.where(labels == i)] = 255
            # print(a)

            cv2.putText(frame, str(a), (l, t), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (l, t), (l + w, t + h), (255, 255, 0), 2)


    # print("=====================")
    # break

    cv2.imshow("frame", frame)
    # cv2.imshow("hsv", hsv[:, :, 0])
    cv2.imshow("filtered", filtered)

    key = cv2.waitKey(1) & 0xFF

    if (key == ord('q')):
        break

cam.release()
cv2.destroyAllWindows()
cv2.waitKey(10)