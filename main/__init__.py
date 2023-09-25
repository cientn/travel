from tkinter import *
from tkinter import ttk
from frontend.signin import SignInGUI
from frontend.signup import SignUpGUI

from PIL import ImageTk

window = Tk()
window.title("App")
ex = SignInGUI(window)
window.mainloop()
