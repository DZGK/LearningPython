# -*- coding: utf-8 -*-
"""
Tcl/Tk のサンプル
cf. http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/event-types.html
cf. http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/event-modifiers.html

## 変更点
1. folderlist_file をスクリプト格納場所から取得するようにする。
2. "tag:" の部分が連続している場合には同じ背景色を付ける
"""
import tkinter as tk
import subprocess
import re
import os


# スクリプトの格納場所から folderlist を探すようにする。
cwd = os.getcwd()
folderlist_file = cwd + "\\" + "folderlist.txt"


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


#       生成されたボタンを格納するリスト。リストに格納することでボタンンを管理できるようにする。
        self.link_buttons = []

#       背景(bg)に使用する色のリスト。 tag 毎に色を割り当てるために予め使用する色を定義する。
        list_colors = ["lightblue", "lightgreen", "lightyellow", "pink",
                       "lightblue", "lightgreen", "lightyellow", "pink",
                       "lightblue", "lightgreen", "lightyellow", "pink",
                       "lightblue", "lightgreen", "lightyellow", "pink",
                       "lightblue"]

#       list_colors内の要素の指定に使用する。
        color_index = 0

#       ボタンとそれに割り当てられた背景色の関係を格納するディクショナリ。マウスが外れた後元の色
#       に戻すのに使用する。
        self.dic_bg = {}
        prev_tag = ""

#       folderlist から key を取得し
        for key in folderlist:
            title = key
            folder = folderlist[key]

# 　　　　　  　　title から tag を抜き出し、color_index を決定する。
#           ここでいう tag とは、 title のうち、行頭から ":" までの文字列を指す。
            curr_tag = re.sub(": .*", "", title)

            if prev_tag == "":
                color_index = 0
            elif curr_tag != prev_tag:
                color_index += 1

            prev_tag = curr_tag

#           ボタンを生成する
            self.link_button = tk.Button(self)
            self.link_button["text"] = title
            self.link_button["fg"] = "black"
            self.link_button["bg"] = list_colors[color_index]
            self.link_button.bind("<Enter>", self.change_color_true)
            self.link_button.bind("<Leave>", self.change_color_false)
            self.link_button["command"] = self.run_it(folder)
            self.link_button["anchor"] = "w"
            self.link_button.pack(anchor="w", fill="x")

#           ボタンと背景色を関連付けたディクショナリ。
            self.dic_bg[title] = list_colors[color_index]

#           Button ウェジットのオブジェクトを管理用の配列に格納する。
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
    def change_color_false(self, event):
        event.widget["fg"] = "black"
#       ウィジェットの名称を使って dic_bg から、割り当てられた背景色を取得する
        event.widget["bg"] = self.dic_bg[event.widget["text"]]

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
