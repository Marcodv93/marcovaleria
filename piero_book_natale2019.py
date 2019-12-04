### AM I DOING THE RIGHT THING AT THE BOTTOM? SHOULD I SEPARATE THE CONTROLS FROM THE PAGE? ####


import tkinter as tk


app = tk.Tk()
app.geometry('1600x900') 

class frame_master(tk.Frame):
    def __init__(self, parent, leftpage_text, rightpage_text):
        tk.Frame.__init__(self, parent, bg='black', height=900, width=1600)
        self.place(x=0,y=0)

        frame_leftpage = tk.Frame(self, height=800, width=800, bg='red')
        frame_leftpage.place(x=0,y=0)

        frame_rightpage = tk.Frame(self, height=800, width=800, bg='blue')
        frame_rightpage.place(x=800,y=0)

        label_leftpage = tk.Label(frame_leftpage, text=leftpage_text)
        label_leftpage.place(relx=0.5,rely=0.5)
        label_rightpage = tk.Label(frame_rightpage, text=rightpage_text)
        label_rightpage.place(relx=0.5,rely=0.5)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class page(tk.Frame):
    def __init__(self, left_text, right_text):
        tk.Frame.__init__(self)
        master_frame = frame_master(app, left_text, right_text)

        frame_controls = tk.Frame(master_frame, height=100, width=1600, bg="green")
        frame_controls.place(x=0, y=800)

        button_previous = tk.Button(frame_controls, text ="Previous Page", command=lambda: self.decrease_page(page_counter))
        button_previous.place(x=10, y=25,relheight=0.5, relwidth=0.2)

        page_counter = tk.IntVar()
        page_counter.set(1)
        label_counter = tk.Label(frame_controls, textvariable=page_counter)
        label_counter.place(x=800,y=25)

        button_next = tk.Button(frame_controls, text ="Next Page", command=lambda: self.increase_page(page_counter))
        button_next.place(anchor = "ne", x=1590, y=25, relheight=0.5, relwidth=0.2)

    def increase_page(self, page_number):
        page_number.set(page_number.get()+1)
    def decrease_page(self, page_number):
        if page_number.get()>1:
            page_number.set(page_number.get()-1)
    def show(self):
        self.lift()

pages_dictionary = {}
for page_number in range(1, 7):
    if page_number%2 == 0:
        pages_dictionary[page_number] = "RIGHT" + str(page_number)
    else:
        pages_dictionary[page_number] = "LEFT" + str(page_number) 

pages = []
for page_number, text in pages_dictionary.items():
    if page_number%2 != 0:
        left_text = text
    pages.append(page(left_text, text))

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.pages = pages
        for page in pages:
            page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        pages[0].show()
  
main = MainView(app)
main.pages[0].show()
app.mainloop()