import cv2
import time

class ShowFPS:
    p_time: int  = 0

    @classmethod
    def show_fps(cls, img):
        c_time = time.time()
        fps = 1 // (c_time - cls.p_time)
        cls.p_time = c_time
        cv2.putText(img, f"FPS: {fps}", (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)


class WindowSize:
    @classmethod
    def set_size(cls, cap, width: int = 1280, height: int = 720) -> None:
        cap.set(3, width)           # set width: 3 for width
        cap.set(4, height)          # set height: 4 for height