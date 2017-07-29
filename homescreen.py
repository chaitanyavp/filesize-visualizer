from tkinter.filedialog import askdirectory
from tkinter import Label
from tkinter import Button
import tkinter


class Homescreen:
    """
    A instance of the starting screen where you can choose a directory.

    === Private Members ===
    @type _filepath: String
        The directory path that the user chooses to be visualized.
    @type _root: Tk
        A top-level widget made using tkinter which creates a interactable home screen.

    """
    def __init__(self):
        """

        @type self: Homescreen
        """
        self._filepath = ""
        self._root = tkinter.Tk("Filesize Visualizer")

    def create_homescreen(self):
        """
        Creates the home screen which the user will initially use to run the
        visualization using tkinter.
        """
        self._root.geometry("300x200")
        self._root.configure(background="#696ed2")
        self._root.iconbitmap("TreeIcon.ico")
        self._root.wm_title("Filesize Visualizer")
        welcome_msg = Label(self._root, text="Welcome to the Filesize Visualizer!",
                            pady=20, font="Helvetica 13")
        welcome_msg.configure(foreground="#291a42")
        welcome_msg.configure(background="#696ed2")
        proceed_msg = Label(self._root, text="Please click the button below to choose "
                                             "a directory to visualize.", pady=10,
                            wraplength=200, font="Helvetica 9")
        proceed_msg.configure(foreground="#291a42")
        proceed_msg.configure(background="#696ed2")
        start = Button(self._root, text="Choose Directory Path",
                       command=self._open_file_screen, width=22, height=2,
                       highlightcolor="blue")
        start.configure(background="#7f85f4")
        welcome_msg.pack()
        proceed_msg.pack()
        start.pack()
        self._root.mainloop()

    def _open_file_screen(self):
        """
        Opens the File Selection screen so the user can choose a directory to be
        visualized. However, you cannot choose a lone file for visualization.
        """
        self._filepath = askdirectory()
        tkinter.Tk("Filesize Visualizer").quit()

    def get_filepath(self):
        """
        The encompassing method which generates the home screen, and gets a
        directory string to be visualized.

        :return: Path of selected file.
        :rtype: String
        """
        self.create_homescreen()
        return self._filepath
