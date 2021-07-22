import cv2
import numpy as np


def show_pic(img, t=0):
    cv2.imshow('pic', img)
    cv2.waitKey(t)


video = cv2.VideoCapture(0)

v_w = int(video.get(3))
v_h = int(video.get(4))

fps = video.get(cv2.cv2.CAP_PROP_FPS)
# print(fps)
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# writer = cv2.VideoWriter('captured2.mp4', fourcc, fps, (v_w, v_h))  # 0x7634706d

while True:
    text = 'None'
    flag, frame = video.read()

    # Wait for 'q' key to stop the program
    if cv2.waitKey(1) == ord('q'):
        break

    if flag:
        # image_1 = histogram_equalization(frame)
        b, g, r = cv2.split(frame)
        # image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # h, s, v = cv2.split(image)

        rows, cols = b.shape
        center = (round(rows / 2), round(cols / 2))
        sub_frame_b = b[center[1] - 60:center[1] + 60, center[0] - 60: center[0] + 60]
        sub_frame_g = g[center[1] - 60:center[1] + 60, center[0] - 60: center[0] + 60]
        sub_frame_r = r[center[1] - 60:center[1] + 60, center[0] - 60: center[0] + 60]
        sub_frame = cv2.merge((sub_frame_b, sub_frame_g, sub_frame_r))
        sub_frame = cv2.medianBlur(sub_frame, 7)
        image = cv2.cvtColor(sub_frame, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(image)

        # print(np.mean(h), np.mean(s), np.mean(v))

        mean_color = np.array([np.mean(h), np.mean(s), np.mean(v)])

        lower_Cyan = np.array([80, 35, 140])
        upper_Cyan = np.array([100, 255, 255])

        lower_yellow = np.array([20, 35, 140])
        upper_yellow = np.array([40, 255, 255])

        lower_magenta = np.array([140, 35, 140])
        upper_magenta = np.array([160, 255, 255])

        lower_red = np.array([0, 35, 140])
        upper_red = np.array([20, 255, 255])

        lower_blue = np.array([110, 35, 140])
        upper_blue = np.array([130, 255, 255])

        lower_green = np.array([50, 35, 140])
        upper_green = np.array([70, 255, 255])

        lower_black = np.array([0, 0, 0])
        upper_black = np.array([0, 65, 65])

        lower_gray = np.array([0, 0, 66])
        upper_gray = np.array([0, 65, 192])

        lower_white = np.array([0, 0, 193])
        upper_white = np.array([0, 65, 255])

        # print(mean_color.shape, lower_Cyan.shape, upper_Cyan.shape)

        if np.sum(cv2.inRange(mean_color, (80, 35, 80), (100, 255, 255))/255) == 3:
            text = 'Cyan'
        elif np.sum(cv2.inRange(mean_color, (20, 35, 80), (40, 255, 255))/255) == 3:
            text = 'Yellow'
        elif np.sum(cv2.inRange(mean_color, (140, 35, 80), (160, 255, 255))/255) == 3:
            text = 'Magenta'
        elif np.sum(cv2.inRange(mean_color, (0, 35, 80), (15, 255, 255))/255) == 3:
            text = 'Red'
        elif np.sum(cv2.inRange(mean_color, (50, 35, 80), (70, 255, 255))/255) == 3:
            text = 'Green'
        elif np.sum(cv2.inRange(mean_color, (110, 35, 80), (130, 255, 255))/255) == 3:
            text = 'Blue'
        elif np.sum(cv2.inRange(mean_color, (0, 0, 0), (10, 255, 65))/255) == 3:
            text = 'Black'
        elif np.sum(cv2.inRange(mean_color, (0, 0, 66), (0, 255, 192))/255) == 3:
            text = 'Gray'
        elif np.sum(cv2.inRange(mean_color, (0, 0, 193), (0, 255, 255))/255) == 3:
            text = 'White'

        frame = cv2.GaussianBlur(frame, (31, 31), 30)

        frame = cv2.putText(frame, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2, cv2.LINE_AA)

        frame[center[1] - 60:center[1] + 60, center[0] - 60: center[0] + 60] = sub_frame
        cv2.rectangle(frame, (center[0] + 60, center[1] + 60), (center[0] - 60, center[1] - 60), color=(0, 255, 0),
                      thickness=3)

        show_pic(frame, 1)
        # frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        # writer.write(frame)


    else:
        break

video.release()
# writer.release()
cv2.destroyAllWindows()
