from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER" ,font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"images\1.webp")
        img_top = img_top.resize((1530, 720), Image.ADAPTIVE)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        label3 = Label(self.root, image=self.photoimg_top)
        label3.place(x=0 , y=55, width=1530, height=720)




if __name__ == "__main__":
    root = Tk()
    obj = Developer (root)
    root.mainloop()
