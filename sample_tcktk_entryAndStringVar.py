# -*- coding: utf-8 -*-
"""
Tcl/Tk のサンプル: Entry ウィジェットと StringVar
cf. https://docs.python.org/ja/3.8/library/tkinter.html
cf. https://tkdocs.com/tutorial/widgets.html#entry
"""
import tkinter as tk


class App2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # 変更: Entry() を tk.Entry() に変更
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # here is the application variable
        # 変更: StringVar() を tk.StringVar()　に変更
        self.contents = tk.StringVar()
        # set it to some value
        self.contents.set("this is a variable")
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)

    def print_contents(self, event):
        print("hi. contents of entry is now ---->",
              self.contents.get())


# 処理開始
root = tk.Tk()
app = App2(master=root)
app.mainloop()
