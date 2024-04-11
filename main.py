from tkinter import tk
from functools import partial # to prevent unwanted windows

class window1:
  def __init__(self):
    self.parent_frame1 = tk.Frame(root, bg="lightblue")
    self.parent_frame1.grid(padx=10, pady=5)
    #Var's
    button_font_12 = ("Arial", 12, "bold")
    # Create a label inside the parent frame1
    self.label_parent1 = tk.Label(parent_frame1, text="Parent Frame", font=("Arial", 16, "bold"))
    self.label_parent1.grid(row=0, pady=5)
    
    # Create the child frame inside the parent frame
    self.child_frame1 = tk.Frame(parent_frame1, bg="lightgreen")
    self.child_frame1.grid(row=1, pady=5)  # Changed .pack() to .grid()
    # Create a open_button inside the child frame
    self.to_window2_button = tk.Button(child_frame1, text="Open Window 2", command=self.open_window2)
    self.to_window2_button.grid(pady=10)  # Changed .pack() to .grid()
  def open_window2():
    Window2(self)
    
class window2:
  def __init__(self, partner):
    #Var's
    background = "#ffe6cc"
    button_font_12 = ("Arial", 12, "bold")
    # window2_box for window exiting
    self.window2_box = Toplevel()
    partner.to_window2_button.config(state=DISABLED)
    self.window2_box.protocol('WM_DELETE_WINDOW', partial(self.close_window2, partner))
    # parent_frame2 on window2_box for window exiting
    self.setting_frame = Frame(self.window2_box, width=200, height=300, bg=background)
    self.setting_frame.configure(bg="#FFFFFF")
    self.setting_frame.grid(padx=10, pady=5)
  def close_window2(self, partner):
    partner.to_window2_button.config(state=tk.NORMAL)
    self.window2_box.destroy()

if __name__ == "__main__":
  root = tk.Tk()
  root.configure(bg="#FFFFFF", borderwidth=20, highlightbackground="green", highlightthickness=5)
  root.title("Card game")
  window1()
  root.mainloop()