from tkinter.filedialog import askopenfilename
from tkinter import Label
from tkinter import Button
import tkinter


def create_homescreen():
    """
    Creates the home screen which the user will initially use to run the visualization.
    """
    root = tkinter.Tk("Filesize Visualizer")
    root.geometry("300x200")
    root.configure(background="#696ed2")
    root.iconbitmap("TreeIcon.ico")
    root.wm_title("Filesize Visualizer")
    welcome_msg = Label(root, text="Welcome to the Filesize Visualizer!", pady=20, font="Helvetica 13")
    welcome_msg.configure(foreground="#291a42")
    welcome_msg.configure(background="#696ed2")
    proceed_msg = Label(root, text="Please click the button below to choose a directory or file to visualize.", pady=10,
                        wraplength=200, font="Helvetica 9")
    proceed_msg.configure(foreground="#291a42")
    proceed_msg.configure(background="#696ed2")
    start = Button(root, text="Choose File Path", command=open_file_screen, width=18, height=2, highlightcolor="blue")
    start.configure(background="#7f85f4")
    welcome_msg.pack()
    proceed_msg.pack()
    start.pack()
    root.mainloop()


def open_file_screen():
    """
    Opens the File Selection screen so the user can choose a path to be visualized.
    """
    filename = askopenfilename()

if __name__ == "__main__":
    create_homescreen()
