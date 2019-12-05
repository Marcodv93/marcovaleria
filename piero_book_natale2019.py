### CHANGE TO CANVAS IF WE FIGURE OUT HOW TO ADD PICTURE AND MAKE TEXT TRANSPARENT####


import tkinter as tk
import os

app = tk.Tk()
app.geometry('1600x900') 

class frame_master(tk.Frame):
    def __init__(self, pages_dictionary):
        tk.Frame.__init__(self, bg='black', height=900, width=1600)
        self.place(x=0,y=0)

        frame_leftpage = tk.Frame(self, height=800, width=800, bg='red')
        frame_leftpage.place(x=0,y=0)

        frame_rightpage = tk.Frame(self, height=800, width=800, bg='blue')
        frame_rightpage.place(x=800,y=0)

        label_leftpage = tk.Canvas(frame_leftpage, width=800, height=800)
        label_leftpage.place(x=0,y=0)
        tkvar_left_text = pages_dictionary[1]
        self.tag_left_text = label_leftpage.create_text((5,10), anchor="nw", text=tkvar_left_text, width=800, font="Helvetica 16", justify="center")

        tkvar_right_text = tk.StringVar()
        tkvar_right_text.set(pages_dictionary[2])
        label_rightpage = tk.Label(frame_rightpage, textvariable=tkvar_right_text, width=70, height=35,font=("Helvetica", 14), wraplength = 700)
        label_rightpage.place(x=0,y=0)

        frame_controls = tk.Frame(self, height=100, width=1600, bg="green")
        frame_controls.place(x=0, y=800)

        button_previous = tk.Button(frame_controls, text ="Previous Page", command=lambda: self.decrease_page(tkvar_left_text, tkvar_right_text))
        button_previous.place(x=10, y=25,relheight=0.5, relwidth=0.2)

        self.page_counter_left = tk.IntVar()
        self.page_counter_left.set(1)
        self.page_counter_right = tk.IntVar()
        self.page_counter_right.set(2)
        left_counter = tk.Label(frame_controls, textvariable=self.page_counter_left)
        left_counter.place(x=400,y=25)
        right_counter = tk.Label(frame_controls, textvariable=self.page_counter_right)
        right_counter.place(x=1200,y=25)

        button_next = tk.Button(frame_controls, text ="Next Page", command=lambda: self.increase_page(label_leftpage, tkvar_right_text))
        button_next.place(anchor = "ne", x=1590, y=25, relheight=0.5, relwidth=0.2)
    def increase_page(self, tkvar_left_text, tkvar_right_text):
        if self.page_counter_right.get() < len(pages_dictionary.keys()):
            self.page_counter_left.set(self.page_counter_left.get()+2)
            self.page_counter_right.set(self.page_counter_right.get()+2)
            self.update_pages(tkvar_left_text, tkvar_right_text)
    def decrease_page(self, tkvar_left_text, tkvar_right_text):
        if self.page_counter_left.get()>2:
            self.page_counter_left.set(self.page_counter_left.get()-2)
            self.page_counter_right.set(self.page_counter_right.get()-2)
            self.update_pages(tkvar_left_text, tkvar_right_text)
    def update_pages(self, label_leftpage, tkvar_right_text):
        #tkvar_left_text.set(pages_dictionary[self.page_counter_left.get()])
        label_leftpage.itemconfigure(self.tag_left_text, text=pages_dictionary[self.page_counter_left.get()])
        tkvar_right_text.set(pages_dictionary[self.page_counter_right.get()])


pages_dictionary = {}
path = "D:\\Documents\\Programming\\Python Programming\\marcovaleria"+'\\story\\'
for file in os.listdir(path):
    page_number = int(file.split("page")[-1].split(".txt")[0])
    current_file = open(path+file, "r")
    pages_dictionary[page_number] = current_file.read()

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        #tk.Frame.__init__(self, *args, **kwargs)
        frame = frame_master(pages_dictionary)



          
main = MainView(app)

app.mainloop()