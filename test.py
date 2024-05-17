from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First
        img = Image.open(r"D:\facial recognition system\images\1.webp")
        img = img.resize((800, 200), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        label1 = Label(self.root, image=self.photoimg)
        label1.place(x=0, y=0, width=800, height=200)

        # Second
        img1 = Image.open(r"D:\facial recognition system\images\1.webp")
        img1 = img1.resize((800, 200), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        label2 = Label(self.root, image=self.photoimg1)
        label2.place(x=800, y=0, width=800, height=200)

        # Background image
        img3 = Image.open(r"D:\facial recognition system\images\bg.jpg")
        img3 = img3.resize((1530, 710))  
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM" ,font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white" )
        main_frame.place(x=5,y=55,width=1480,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white" ,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)

        img_left = Image.open(r"D:\facial recognition system\images\1.webp")
        img_left = img_left.resize((720, 130), Image.ADAPTIVE)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
 
        label3 = Label(Left_frame, image=self.photoimg_left)
        label3.place(x=5, y=0, width=720, height=130)

        left_inner_frame=Frame(Left_frame,relief=RIDGE,bd=2,bg="white" )
        left_inner_frame.place(x=0,y=180,width=720,height=370)

        #Labels

        #student id
        attendanceId_label=Label(left_inner_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,sticky=W) 

        attendanceId_entry=Entry(left_inner_frame,width=20,font=("times new roman",12,"bold"),bg="white")
        attendanceId_entry.grid(row=0,column=1, padx=10,sticky=W) 

        #Roll
        rollno_label=Label(left_inner_frame,text="RollNo",font=("times new roman",12,"bold"),bg="white")
        rollno_label.grid(row=0,column=2,padx=4,sticky=W) 

        rollno_entry=Entry(left_inner_frame,width=20,font=("times new roman",12,"bold"),bg="white")
        rollno_entry.grid(row=0,column=3, pady=8,sticky=W) 

        #Name
        name_label=Label(left_inner_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0) 

        name_entry=Entry(left_inner_frame,width=20,font=("times new roman",12,"bold"),bg="white")
        name_entry.grid(row=1,column=1, pady=8) 

        #Dep
        dep_label=Label(left_inner_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2) 

        dep_entry=Entry(left_inner_frame,width=20,font=("times new roman",12,"bold"),bg="white")
        dep_entry.grid(row=1,column=3, pady=8) 

        #time
        time_label=Label(left_inner_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0) 

        time_entry=Entry(left_inner_frame,width=20,font=("times new roman",12,"bold"),bg="white")
        time_entry.grid(row=2,column=1, pady=8) 

        #Date
        date_label=Label(left_inner_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2) 

        date_entry=Entry(left_inner_frame,width=20,font=("times new roman",12,"bold"),bg="white")
        date_entry.grid(row=2,column=3, pady=8) 

        #attendance
        attendancelabel=Label(left_inner_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        attendancelabel.grid(row=3,column=0) 

        self.atten_status=ttk.Combobox(left_inner_frame,width=20,font="comicsans 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #buttons
        btn_frame=Frame(left_inner_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=270,width=715,height=35)

        importcsv_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")

        importcsv_btn.grid(row=0,column=0)

        Exportcsv_btn=Button(btn_frame,text="Export csv",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Exportcsv_btn.grid(row=0,column=1)

        Update_btn=Button(btn_frame,text="Update",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)









        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white" ,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=720,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=700,height=455)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)




        self.AttendanceReportTable.pack(fil=BOTH,expand=1)

        #fetch_data

    


    def importCsv(self):
            global mydata
            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
