# -*- coding: utf-8 -*-
"""
Tcl/Tk のサンプル
cf. http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/event-types.html
cf. http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/event-modifiers.html
"""
import tkinter as tk
import subprocess


folderlist_file = "folderlist.txt"


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(anchor="w", padx="1", pady="1", fill="x")
        self.create_widgets()
        self.master.attributes('-topmost', True)

    def create_widgets(self):
        # フォルダリストからのデータの読み取り
        folderlist = {}
        with open(folderlist_file, 'r') as f:
            read_data = [x.rstrip() for x in f.readlines()]

            for list_item in read_data:
                k, v = list_item.split(",")
                folderlist[k] = v

        # ファイルを閉じる
        f.close


#        リンクごとにボタンを生成する。生成したボタンは link_buttons に格納する。
        self.link_buttons = []
        for key in folderlist:
            title = key
            folder = folderlist[key]

            self.link_button = tk.Button(self)
            self.link_button["text"] = title
            self.link_button.bind("<Enter>", self.change_color_true)
            self.link_button.bind("<Leave>", self.change_color_false)
            self.link_button["command"] = self.run_it(folder)
            self.link_button["anchor"] = "w"
            self.link_button.pack(anchor="w", fill="x")

            # Button ウェジットのおbジュジェクトをを操作用の配列に格納する。
            self.link_buttons.append(self.link_button)

#       UPDATE ボタンの生成
        self.update = tk.Button(self, text="UPDATE", fg="blue",
                                command=self.update_folderlist)
        self.update.pack(anchor="w")
        self.link_buttons.append(self.update)


#       open list file ボタンの生成
        self.open_listfile = tk.Button(self, text="Open List File", fg="blue",
                                       command=self.open_folderlist)
        self.open_listfile.pack(anchor="w")
        self.link_buttons.append(self.open_listfile)

#       QUIT ボタンの生成
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom", anchor="w")
        self.link_buttons.append(self.quit)

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

    def open_folderlist(self):
        print("open_folderlistfile")
        subprocess.Popen(r'C:\Windows\system32\notepad.exe ' + folderlist_file)

    def update_folderlist(self):
        print("start - update_folderlist")

        # self.link_buttons には、現在登録されている全てのボタンウェジットが格納されている
        current_buttons = self.link_buttons

        for button in current_buttons:
            print(button)
            button.destroy()

        self.create_widgets()


# 処理開始
root = tk.Tk()
root.title("Outlookフォルダ")
app = Application(master=root)
app.mainloop()
