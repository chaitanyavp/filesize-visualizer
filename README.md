---------------------------------------------------
		
		Filesize Visualizer

	Developed by: Chaitanya Peesapati
	Documentation by: Raymond Liu
	
	Version: 1.0.0
	Updated: August 10th, 2017

---------------------------------------------------


What's this?
------------
A small standalone program developed using python 3.5
and the pygame library, used to turn a user-selected
directory into a screen of coloured rectangles. These
rectangles are sized by file space taken, oriented
by directory depth, and ordered by directory ordering.


Why is it useful?
-----------------
It's primary function is to provide more utility to 
operations involving file organization. Some will find
it more helpful to have a visual representation of their
directory tree than numbers. If they wish to delete the
biggest files for creating space or for performing housekeeping
operations - the filesize visualizer is a great aid. 
Another use is to compare relative directory sizes, whether
for fun or for purposes such as file migration.


What do I need?
---------------
You'll need all the files from the repository, simply download
the ZIP file, and extract them to a folder. 
Please make sure the files below all exist.

1) visualizer.py - Uses the pygame module to visually create file
		   representations on a screen GUI.

2) sizeprocessor.py - Backend code which performs calculations to
		      compute file sizes, organization, and decide
		      which file is selected.

3) homepage.py - Uses the tkinter module to create a homescreen GUI
	         which also enables file selection.

4) TreeIcon.ico - Makes the little tree icon appear in the homescreen.

You will also need to download python 3.5 or above (or equivalent).
You can do this from the official website below:
https://www.python.org/

After this, you're pretty much good! Of course, you could download
an IDE like Pycharm to debug the program while running it, but is by
no means required to actually launch it.


Alright, so how do I use it?
----------------------------
Steps:

(1) Navigate to the folder where you extracted all your files.

(2) Locate the "visualizer.py" file, and launch it.
    (If it does not automatically launch with Python 3.5, please
     open it with that.)

(3) After the blank command window for python appears, give it a
    few seconds, and a small screen with a button should appear.

(4) Click the "Select Directory" button and choose the
    directory you wish to display.

(5) The resulting screen should be a complete visualization
    of your directory!


Is there more functionality?
-----------------------------
Well, of course! There are currently 3 clicking functions as shown below.

[Left-Click]
Displays the directory path and file size in the bottom bar.

[Middle-Click]
Attempts to run the selected file. 
(Note: Many files will not be openable immediately, so you may receive a
prompt to find a suitable program online instead.)

[Right-Click] - Opens the selected file.


Thanks, so can I have an overview?
----------------------------------
- Filesize visualizer is a simple program for turning a directory path
  into a screen of pygame-generated rectangles
- It is ideal as a utility tool for file management and comparison
- It is launched by running visualizer.py directly from its local folder
  or from an IDE, given python 3.5 is installed
- Currently, it allows viewing of the file path/size, plus file opening
- It's very colourful!