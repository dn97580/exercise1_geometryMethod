# This program will increase the width of the window by
# using the geometry method,so the title is visible. Set
# the width to 300 pixels and the height to 200 pixels. 
import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Set the window title and size.
        self.main_window.title('My First GUI')
        self.main_window.geometry('300x200')

        # Enter the tkinter main loop.
        tkinter.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()

