import tkinter as tk
#from tkinter import Toplevel # Temporarily added
from functools import partial # to prevent unwanted windows

class Window1:
  def __init__(self, root):
    # Create the parent frame on root
    self.parent_frame1 = tk.Frame(root, bg="lightblue")
    self.parent_frame1.grid(padx=10, pady=5)
    #Var's
    button_font_12 = ("Arial", 12, "bold")
    # Create a label inside the parent frame1
    self.label_parent1 = tk.Label(self.parent_frame1, text="Parent Frame", font=("Arial", 16, "bold"))
    self.label_parent1.grid(row=0, pady=5)
    # Create the child frame inside the parent frame
    self.child_frame1 = tk.Frame(self.parent_frame1, bg="lightgreen")
    self.child_frame1.grid(row=1, pady=5)  # Changed .pack() to .grid()
    # Create a open_button inside the child frame
    self.to_window2_button = tk.Button(self.child_frame1, text="Open Window 2", command=self.open_window2)
    self.to_window2_button.grid(pady=10)  # Changed .pack() to .grid()
  
  def open_window2(self):
    Window2(self)
    
class Window2:
  def __init__(self, partner):
    #Var's
    background = "#ffe6cc"
    button_font_12 = ("Arial", 12, "bold")
    # window2_box for window exiting
    self.window2_box = tk.Toplevel()
    partner.to_window2_button.config(state=tk.DISABLED)
    self.window2_box.protocol('WM_DELETE_WINDOW', partial(self.close_window2, partner))
    # Create the parent frame on window exiting
    self.parent_frame2 = tk.Frame(self.window2_box, bg="lightblue")
    self.parent_frame2.grid(padx=10, pady=5)
    # Create a label inside the parent frame1
    self.label_parent2 = tk.Label(self.parent_frame2, text="Parent Frame", font=("Arial", 16, "bold"))
    self.label_parent2.grid(row=0, pady=5)
    # Create the child frame inside the parent frame
    self.child_frame2 = tk.Frame(self.parent_frame2, bg="lightgreen")
    self.child_frame2.grid(row=1, pady=5)  # Changed .pack() to .grid()
    # Create a label inside the child frame
    self.label_child2 = tk.Label(self.child_frame2, text="Child Frame", font=("Arial", 16, "bold"))
    self.label_child2.grid(row=0, pady=5)
    
  def close_window2(self, partner):
    partner.to_window2_button.config(state=tk.NORMAL)
    self.window2_box.destroy()

if __name__ == "__main__":
  root = tk.Tk()
  root.configure(bg="#FFFFFF", borderwidth=20, highlightbackground="green", highlightthickness=5)
  root.title("open & close windows")
  Window1(root)
  root.mainloop()