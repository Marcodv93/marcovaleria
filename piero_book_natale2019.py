### FIND OUT HOW BUTTONS WORK AND HOW TO CHANGE FROM PAGE TO PAGE ####


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

first_frame = frame_master(app, "LEFT", "RIGHT")

def buttonfunction(variable):
    output_to_print = "random string"
    variable.set(output_to_print)


frame_controls = tk.Frame(app, height=100, width=1600, bg="green")
frame_controls.place(x=0, y=800)

button_previous = tk.Button(frame_controls, text ="Previous Page")
button_previous.place(x=10, y=25,relheight=0.5, relwidth=0.2)

string_counter = tk.StringVar()
string_counter.set("Valeria ti amo")
label_counter = tk.Label(frame_controls, textvariable=string_counter)
label_counter.place(x=800,y=25)

button_next = tk.Button(frame_controls, text ="Next Page", command=buttonfunction(string_counter))
button_next.place(anchor = "ne", x=1590, y=25, relheight=0.5, relwidth=0.2)


#second_frame = frame_master(app, "sinistra", "destra")

app.mainloop()