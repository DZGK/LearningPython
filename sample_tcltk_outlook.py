# -*- coding: utf-8 -*-
"""
Tcl/Tk のサンプル
cf. http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/event-types.html
cf. http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/event-modifiers.html
"""
import tkinter as tk
import subprocess


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(anchor="w", padx="1", pady="1", fill="x")
        self.create_widgets()
        self.master.attributes('-topmost', True)

    def create_widgets(self):
        # フォルダリストからのデータの読み取り
        linklist = {}
        with open('folderlist.txt', 'r') as f:
            read_data = [x.rstrip() for x in f.readlines()]

            for list_item in read_data:
                k, v = list_item.split(",")
                linklist[k] = v
        print(linklist)

        # ファイルを閉じる
        f.close

        self.labels =[]
        # リンクごとにボタンを生成する
        for key in linklist:
            label = key
            folder = linklist[key]

            self.label = tk.Button(self)
            self.labels.append(self.label)
            self.label["text"] = label
            self.label.bind("<Enter>", self.change_color_true)
            self.label.bind("<Leave>", self.change_color_false)
            self.label["command"] = self.run_it(folder)
            self.label["anchor"] = "w"
            self.label.pack(anchor="w", fill="x")


        self.quit = tk.Button(self, text="UPDATE", fg="blue",
                              command=self.update_list)
        self.quit.pack(anchor="w")


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom", anchor="w")
          
        

    def run_it(self, folder):
        def run_outlook():
            print(folder)
            subprocess.Popen(r'C:\Program Files\Microsoft Office\Office16\OUTLOOK.EXE /select ' + folder)

        return run_outlook

    # ウィジェットにマウスをかざすと色を付ける。
    def change_color_true(application, event):
        event.widget["bg"] = "teal"
        event.widget["fg"] = "white"

    # ウィジェットからマウスが離れると、色を元に戻す
    def change_color_false(application, event):
        event.widget["fg"] = "black"
        event.widget["bg"] = "SystemButtonFace"

    def change_menubar_color_true(application, event):
        print("chagen_MenuColor")
        event.widget["bg"] = "teal"
        event.widget["fg"] = "white"


    def update_list(self):
      #  print(self.label["text"])
        print(self.labels)
        self.labels[3]["text"] = "ヘムレンさん"
#        for i in self.label:
#            print(self.i["text"])
#        # フォルダリストからのデータの読み取り
#        linklist = {}
#        with open('folderlist.txt', 'r') as f:
#            read_data = [x.rstrip() for x in f.readlines()]
#
#            for list_item in read_data:
#                k, v = list_item.split(",")
#                linklist[k] = v
#        print(linklist)
#
#
#        # ファイルを閉じる
#        f.close
#
#        # リンクごとにボタンを生成する
#        for key in linklist:
#            label = key
#            folder = linklist[key]
#
#            self.label = tk.Button(self)
#            self.label["text"] = label
#            self.label.bind("<Enter>", self.change_color_true)
#            self.label.bind("<Leave>", self.change_color_false)
#            self.label["command"] = self.run_it(folder)
#            self.label["anchor"] = "w"
#            self.label.pack(anchor="w", fill="x")
#
#
#        self.quit = tk.Button(self, text="UPDATE", fg="blue",
#                              command=self.update_list)
#        self.quit.pack(anchor="w")
#
#
#        self.quit = tk.Button(self, text="QUIT", fg="red",
#                              command=self.master.destroy)
#        self.quit.pack(side="bottom", anchor="w")
#        


# 処理開始
root = tk.Tk()
root.title("Outlookフォルダ")
app = Application(master=root)
app.mainloop()
