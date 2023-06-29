import cv2
from tkinter import *
from tkinter import filedialog

pathImage = ""
x = 0

def OpenExplorer():
    path = filedialog.askopenfilename()
    global pathImage
    pathImage = path
    global x
    x.destroy()


def CreateWindow():
    starting_window = Tk()
    global x
    x = starting_window
    starting_window.title("RecognizeAndDraw")
    starting_window.geometry("500x300")
    starting_window.configure(bg="lightblue")
    Name = Label(starting_window, text="RecognizeAndDraw")
    Name.configure(bg="lightblue")
    Name.config(font=("Calibri", 30))
    Name.pack()
    BrowseButton = Button(starting_window, text="Browse...", command=OpenExplorer).pack(side=LEFT, padx=140,
                                                                                             pady=100)
    CloseButton = Button(starting_window, text="Close", command=starting_window.destroy).pack(side=RIGHT, padx=20,
                                                                                              pady=30)
    starting_window.mainloop()


def main_func():
    wnd = CreateWindow()
    path = pathImage
    img = cv2.imread(path)
    imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thrash = cv2.threshold(imgGry, 240, 255, cv2.CHAIN_APPROX_NONE)
    contours, hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    white_image = cv2.imread(r"C:\Users\Ionut B\Desktop\pythonProject\white.jpg")
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        cv2.drawContours(white_image, [approx], 0, (0, 0, 0), 5)
        cv2.imshow('RecognizeAndDraw', white_image)
        cv2.waitKey(50)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


main_func()