from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First
        img = Image.open(r"D:\facial recognition system\images\1.webp")
        img = img.resize((510, 130), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        label1 = Label(self.root, image=self.photoimg)
        label1.place(x=0, y=0, width=500, height=130)

        # Second
        img1 = Image.open(r"D:\facial recognition system\images\1.webp")
        img1 = img1.resize((510, 130), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        label2 = Label(self.root, image=self.photoimg1)
        label2.place(x=510, y=0, width=500, height=130)

        # Third
        img2 = Image.open(r"D:\facial recognition system\images\1.webp")
        img2 = img2.resize((510, 130), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        label3 = Label(self.root, image=self.photoimg2)
        label3.place(x=1020, y=0, width=500, height=130)

        # Background image
        img3 = Image.open(r"D:\facial recognition system\images\bg.jpg")
        img3 = img3.resize((1530, 710))  
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM ATTENDANCE SYSTEM" ,font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"D:\facial recognition system\images\1.webp")
        img4 = img4.resize((220, 220), Image.ADAPTIVE)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #Detect Face button
        img5=Image.open(r"D:\facial recognition system\images\1.webp")
        img5= img5.resize((220, 220), Image.ADAPTIVE)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #Attendance Face button
        img6=Image.open(r"D:\facial recognition system\images\1.webp")
        img6= img6.resize((220, 220), Image.ADAPTIVE)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        #Help Desk
        img7=Image.open(r"D:\facial recognition system\images\1.webp")
        img7= img7.resize((220, 220), Image.ADAPTIVE)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #Train Face
        img8=Image.open(r"images\1.webp")
        img8= img8.resize((220, 220), Image.ADAPTIVE)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40)

        #Photos
        img9=Image.open(r"images\1.webp")
        img9= img9.resize((220, 220), Image.ADAPTIVE)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=600,width=220,height=40)

        #Developer
        img10=Image.open(r"images\1.webp")
        img10= img10.resize((220, 220), Image.ADAPTIVE)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=400,width=220,height=220)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=600,width=220,height=40)

        #Exit 
        img11=Image.open(r"images\1.webp")
        img11= img11.resize((220, 220), Image.ADAPTIVE)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=400,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1100,y=600,width=220,height=40)

    
    def open_img(self):
        os.startfile("data")
    
    
    #----function buttons------------------
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)





if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
