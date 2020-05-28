# Program imports
#
import tkinter
from tkinter import messagebox
from tkinter import TOP, BOTTOM, RIGHT, LEFT, N, S, E, W, BOTH
import subprocess

# Message Box
mbox = messagebox

# Window Section
#Window Dimensions
window_width = 1000
window_height = 600


# Convert dimensions to a string
window_dimensions = '{}x{}'.format(window_width, window_height)


# Configure Window
parent_widget = tkinter.Tk()
parent_widget.geometry(window_dimensions)
parent_widget.title('Network Utilities Control Panel')
parent_widget.configure(background="gray")


# Menu Callback functions
def file_menu_exit_callback():
    if mbox.askokcancel(title='Terminating Program', message = 'Do you really want to Exit?'):
        print('Exit Application')
        parent_widget.destroy()
    else:
        mbox.showinfo('Note', 'Program was not terminated')

def post_local_OS_data():
    subprocess.call("uname")

# Frames and Buttons
frame1_widget = tkinter.Frame(master=parent_widget,\
                width = 600, height = 100,\
                background = 'blue')
exit_button_widget = tkinter.Button(frame1_widget,\
                text = "Exit", fg = 'red',\
                command=file_menu_exit_callback)
exit_button_widget.pack(side = RIGHT)
post_OS_button_widget = tkinter.Button(frame1_widget,\
                text = "System", fg = 'black',\
                command=post_local_OS_data)
post_OS_button_widget.pack(side = RIGHT)
frame1_widget.pack(side=BOTTOM, anchor=E, fill=BOTH)

frame2_widget=tkinter.Frame(master=parent_widget,\
                height=400, width=600)
text_widget=tkinter.Text(master=frame2_widget,\
                background='white')
text_widget.pack(side=LEFT, anchor=S)
frame2_widget.pack(side=TOP, anchor=W, fill=BOTH)

frame3_widget = tkinter.Frame(master = parent_widget,\
                height=300, width=600)
text3_widget = tkinter.Text(master = frame3_widget,\
                background='green')
label3_widget = tkinter.Label(master = frame3_widget,\
                text='Hardware')
label3_widget.pack(side=TOP, anchor=N)
text3_widget.pack(side=LEFT, anchor=S)
frame3_widget.pack(side=BOTTOM, anchor=W, fill=BOTH)



# Main Function - Central control of the program
def main():
    menu_widget = tkinter.Menu(parent_widget)
    submenu1_widget = tkinter.Menu(menu_widget, tearoff=False)
    submenu2_widget = tkinter.Menu(menu_widget, tearoff=False)
    submenu1_widget.add_command(label="Settings",\
                                underline = 0,\
                                accelerator = 'Alt+S')
    submenu1_widget.add_command(label="Exit", \
                                underline = 1,\
                                accelerator = 'Alt+X',\
                                activebackground = 'red',\
                                command = file_menu_exit_callback)
    submenu2_widget.add_command(label="Tools")
    menu_widget.add_cascade(label="File", menu=submenu1_widget)
    menu_widget.add_cascade(label="Network", menu=submenu2_widget)
    parent_widget.config(menu=menu_widget)
    parent_widget.mainloop()

# Main - processing starts here
if __name__ == '__main__':
    main()





