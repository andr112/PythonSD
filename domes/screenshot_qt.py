from PyQt5.QtWidgets import QApplication
import win32gui
import sys
import cv2
import numpy as np

hwnd_title = dict()  # 创建字典保存窗口的句柄与名称映射关系


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)

for h, t in hwnd_title.items():
    if t != "":
        print(h, t)

# 以上代码，会打印所有窗口的hwnd和title，有了title就可以进行截图了


# 这个是截取全屏的
hwnd = win32gui.FindWindow(None, 'cmd.xls  [兼容模式] - Excel')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()
img.save("screenshot.jpg")


def convertQImageToMat(incomingImage):
    '''  Converts a QImage into an opencv MAT format  '''
    # Format_RGB32 = 4,存入格式为B,G,R,A 对应 0,1,2,3
    # RGB32图像每个像素用32比特位表示，占4个字节，
    # R，G，B分量分别用8个bit表示，存储顺序为B，G，R，最后8个字节保留
    incomingImage = incomingImage.convertToFormat(4)
    width = incomingImage.width()
    height = incomingImage.height()

    ptr = incomingImage.bits()
    ptr.setsize(incomingImage.byteCount())
    arr = np.array(ptr).reshape(height, width, 4)  # Copies the data
    # arr为BGRA，4通道图片
    return arr

hwnd = win32gui.FindWindow(None, 'cmd.xls  [兼容模式] - Excel')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()

img = convertQImageToMat(img)  # 将获取的图像从QImage转换为RBG格式
cv2.imshow("asd", img)  # imshow
cv2.waitKey(0)
