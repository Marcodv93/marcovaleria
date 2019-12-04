### CHANGE TEXT IN LABEL INSTEAD OF CHANGING PAGE####


import tkinter as tk


app = tk.Tk()
app.geometry('1600x900') 

class frame_master(tk.Frame):
    def __init__(self, leftpage_text, rightpage_text):
        tk.Frame.__init__(self, bg='black', height=900, width=1600)
        self.place(x=0,y=0)

        frame_leftpage = tk.Frame(self, height=800, width=800, bg='red')
        frame_leftpage.place(x=0,y=0)

        frame_rightpage = tk.Frame(self, height=800, width=800, bg='blue')
        frame_rightpage.place(x=800,y=0)

        label_leftpage = tk.Label(frame_leftpage, text=leftpage_text)
        label_leftpage.place(relx=0.5,rely=0.5)
        label_rightpage = tk.Label(frame_rightpage, text=rightpage_text)
        label_rightpage.place(relx=0.5,rely=0.5)

        frame_controls = tk.Frame(self, height=100, width=1600, bg="green")
        frame_controls.place(x=0, y=800)

        button_previous = tk.Button(frame_controls, text ="Previous Page", command=lambda: self.decrease_page(self.page_counter_left, self.page_counter_right))
        button_previous.place(x=10, y=25,relheight=0.5, relwidth=0.2)

        self.page_counter_left = tk.IntVar()
        self.page_counter_left.set(1)
        self.page_counter_right = tk.IntVar()
        self.page_counter_right.set(2)
        left_counter = tk.Label(frame_controls, textvariable=self.page_counter_left)
        left_counter.place(x=400,y=25)
        right_counter = tk.Label(frame_controls, textvariable=self.page_counter_right)
        right_counter.place(x=1200,y=25)

        button_next = tk.Button(frame_controls, text ="Next Page", command=lambda: self.increase_page(self.page_counter_left, self.page_counter_right))
        button_next.place(anchor = "ne", x=1590, y=25, relheight=0.5, relwidth=0.2)
    def increase_page(self, page_counter_left,page_counter_right):
        page_counter_left.set(page_counter_left.get()+2)
        page_counter_right.set(page_counter_right.get()+2)
    def decrease_page(self, page_counter_left, page_counter_right):
        if page_counter_left.get()>2:
            page_counter_left.set(page_counter_left.get()-2)
            page_counter_right.set(page_counter_right.get()-2)
        

pages_dictionary = {}
for page_number in range(1, 5):
    if page_number%2 == 0:
        pages_dictionary[page_number] = "RIGHT" + str(page_number)
    else:
        pages_dictionary[page_number] = "LEFT" + str(page_number) 

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        #tk.Frame.__init__(self, *args, **kwargs)
        frame = frame_master(pages_dictionary[1],pages_dictionary[2])


          
main = MainView(app)

app.mainloop()