# -*- coding: utf-8 -*-
"""
Tcl/Tk のサンプル
cf. http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/event-types.html
cf. http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/event-modifiers.html
"""
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(anchor="w", padx="1", pady="1", fill="x")
        self.create_widgets()
        self.master.attributes('-topmost', True)
                

    def create_widgets(self):
        linklist = {"Gohst":"linkA", "Golem":"LinkB", "Panther":"LinkC", "おおきなやぎのがらがらどん":"LinkD"}
         
        for key in linklist:
            label = key
            folder = linklist[key]
                
            self.label = tk.Button(self)
            self.label["text"] = label
            self.label.bind("<Enter>", self.change_color_true)
            self.label.bind("<Leave>", self.change_color_false)


        # command の定義 
            # パターン1: python 公式のサンプル
#            self.label["command"] = self.say_hi
            # パターン2: 引数に値を入れて渡すと、定義した時点で実行される。     
#　　　　　      self.label["command"] = self.run_it(folder = folder)
            # パターン3: 呼びされたメソッド側で関数定義をネストさせる。これはうまくいく。
            self.label["command"] = self.run_that(folder)
            self.label["anchor"] = "w"
            self.label.pack(anchor="w", fill="x")
        
              
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom", anchor="w")
        
    def say_hi(self):
        print("hi there, everyone!")


    def run_it(self, folder):
        # この関数はうまくいかない。button から引数を渡されるようにすると、即時実行してしまう。
        print(folder)
        print("runt_it called")


    def run_that(self, folder):
        # これはうまくいく。
        def print_foldername():
            print(folder)
        return print_foldername
       

    # ウィジェットにマウスをかざすと色を付ける。
    def change_color_true(application, event):
#        print(type(application))
#        print(type(event))
        event.widget["fg"] = "white"
        event.widget["bg"] = "teal"
  
    # ウィジェットからマウスが離れると、色を元に戻す
    def change_color_false(application, event):
#        print(type(application))
#        print(type(event))
        event.widget["fg"] = "black"
        event.widget["bg"] = "SystemButtonFace"


# 処理開始
root = tk.Tk()
root.title("ランチャー")
app = Application(master=root)
app.mainloop()
