from tkinter.filedialog import askdirectory
from tkinter import Label
from tkinter import Button
import tkinter

_FILEPATH = ""


def create_homescreen():
    """
    Creates the home screen which the user will initially use to run the
    visualization.
    """
    _ROOT = tkinter.Tk("Filesize Visualizer")
    _ROOT.geometry("300x200")
    _ROOT.configure(background="#696ed2")
    _ROOT.iconbitmap("TreeIcon.ico")
    _ROOT.wm_title("Filesize Visualizer")
    welcome_msg = Label(_ROOT, text="Welcome to the Filesize Visualizer!",
                        pady=20, font="Helvetica 13")
    welcome_msg.configure(foreground="#291a42")
    welcome_msg.configure(background="#696ed2")
    proceed_msg = Label(_ROOT, text="Please click the button below to choose a "
                                    "directory to visualize.", pady=10,
                        wraplength=200, font="Helvetica 9")
    proceed_msg.configure(foreground="#291a42")
    proceed_msg.configure(background="#696ed2")
    start = Button(_ROOT, text="Choose Directory Path",
                   command=_open_file_screen, width=22, height=2,
                   highlightcolor="blue")
    start.configure(background="#7f85f4")
    welcome_msg.pack()
    proceed_msg.pack()
    start.pack()
    _ROOT.mainloop()


def _open_file_screen():
    """
    Opens the File Selection screen so the user can choose a path to be
    visualized.
    """
    global _FILEPATH
    _FILEPATH = askdirectory()
    tkinter.Tk("Filesize Visualizer").quit()


def get_filepath():
    """
    Prompts user to select file/folder and returns the path.
    :return: Path of selected file.
    :rtype: String
    """
    create_homescreen()
    return _FILEPATH


if __name__ == "__main__":
    print(get_filepath())
