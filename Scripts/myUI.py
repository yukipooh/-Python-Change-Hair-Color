import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as msgbox
import os
import changeHairColor as chc 
import cv2 as cv
from PIL import ImageTk,Image


class MyApp1(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()

        #Canvas
        self.canvas1 = tk.Canvas(self)
        self.canvas1.configure(width=640, height=480, bg='gray')
        # self.canvas1.create_rectangle(0,0,120, 70, fill='green')
        self.canvas1.pack()
        self.canvas1.pack()
        
        #画像選択ボタン
        self.SELECT = tk.Button(self,bg='#000000',fg='#ffffff',width=12,height=5)
        self.SELECT["text"] = "SELECT FILE" #ボタンのテキスト
        self.SELECT["command"] = self.load_image
        self.SELECT.pack(side="left")
        
        #Saveボタン
        self.SAVE = tk.Button(self,bg='#000000',fg='#ffffff',width=12,height=5)
        self.SAVE["text"] = "SAVE IMAGE" #ボタンのテキスト
        self.SAVE["command"] = self.save_image
        self.SAVE.pack(side="left")

        #Quitボタン
        self.ButtonQuit = tk.Button(self, bg='#000000', fg='#ffffff', width=12, height = 5)
        self.ButtonQuit["text"] = "QUIT"
        self.ButtonQuit["command"] = self.QuitApp
        self.ButtonQuit.pack(side="left")

        self.selected_file_path = ""

    def save_image(self):
        path = self.selected_file_path
        for i in range(len(path)):  #拡張子の部分を削除
            path = path[:-1]
            if path[len(path) - 1] == '.':
                path = path[:-1]
                break
        path += "_converted.jpg"
        cv.imwrite(path,self.image_bgr)
    
    def load_image(self):
        fTyp = [("画像ファイル","*.png"),("画像ファイル","*.jpg")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        self.selected_file_path = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
        self.image_bgr = chc.changeColor(self.selected_file_path)
        self.height, self.width = self.image_bgr.shape[:2]
        if self.width > self.height:
            self.new_size = (640,480)
        else:
            self.new_size = (480,640)
        self.image_bgr_resize = cv.resize(self.image_bgr, self.new_size, interpolation=cv.INTER_AREA)
        self.image_rgb = cv.cvtColor( self.image_bgr_resize, cv.COLOR_BGR2RGB )  # imreadはBGRなのでRGBに変換
        self.image_PIL = Image.fromarray(self.image_rgb) # RGBからPILフォーマットへ変換
        self.image_tk = ImageTk.PhotoImage(self.image_PIL) # ImageTkフォーマットへ変換
        self.canvas1.create_image(320,320,image=self.image_tk)
        
    def QuitApp(self):
        print("quit this App")
        self.master.destroy()
        
    



