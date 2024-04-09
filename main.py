from tkinter import *
from functools import partial # to prevent unwanted windows

class Program:
  def __init__(self):
    self.program_frame = Frame()
    self.program_frame.configure(bg="#FFFFFF")
    self.program_frame.grid(padx=30, pady=5)
    # row 2
    self.to_setting_button = Button(self.program_frame, text="Setting", bg="blue", fg="white", font=("Arial", 12, "bold"), command=lambda: self.to_frame("setting"))
    self.to_setting_button.grid(row=2)

  def to_frame(self, frame_name):
    if frame_name == "get start":
      GetStart(self)
    elif frame_name == "setting":
      Setting(self)
class Setting:
  def __init__(self, partner):
    # frames exit's
    background = "#ffe6cc"
    self.setting_box = Toplevel()
    partner.to_setting_button.config(state=DISABLED)
    self.setting_box.protocol('WM_DELETE_WINDOW', partial(self.close_setting, partner))
    # setting_box on setting_box for window exiting
    self.setting_frame = Frame(self.setting_box, width=300, height=200, bg=background)
    self.setting_frame.configure(bg="#FFFFFF")
    self.setting_frame.grid(padx=30, pady=5)
    # row 0
    self.setting_heading = Label(self.setting_frame, text="Setting", font=("Arial", 12, "bold"))
    self.setting_heading.grid(row=0)
    # row 1
    setting_text = "Setting"
    self.setting_instructions = Label(self.setting_frame, text=setting_text, font=("Arial", 12, "bold"))
    self.setting_instructions.grid(row=1)
    # row 2
    self.filename_entry = Entry(self.history_frame, font=("Arial", "12"), bg="#ffffff", width=25)
    self.filename_entry.grid(row=2)
    # row 3
    self.dismiss_button = Button(self.button_frame, font=button_font_12, text="Dismiss", bg="#666666", fg="#FFFFFF", width=12, command=partial(self.close_history, partner))
    self.dismiss_button.grid(row=3, padx=10, pady=10)

  def close_setting(self, partner):
    partner.to_setting_button.config(state=NORMAL)
    self.setting_box.destroy()

class GetStart:
  pass
class Play:
  pass
class Help:
  pass
class Stats:
  pass


if __name__ == "__main__":
  root = Tk()
  root.configure(bg="#FFFFFF", borderwidth=20, highlightbackground="green", highlightthickness=5)
  root.title("Card game")
  Program()
  root.mainloop()