from tkinter import *

class Program:
  def __init__(self):
    self.program_frame = Frame()
    self.program_frame.configure(bg="#FFFFFF")
    self.program_frame.grid(padx=30, pady=5)
    # row 0
    self.program_heading = Label(self.program_frame, text="Card Game", font=("Arial", 12, "bold"))
    self.program_heading.grid(row=0)
    # row 1
    program_image = "PhotoImage(file='path/to/your/image.png')"
    self.program_image_label = Label(self.program_frame, text=program_image)
    self.program_image_label.grid(row=1, padx=40, pady=90)
    # row 2
    self.program_button = Button(self.program_frame, text="play", bg="blue", fg="white", font=("Arial", 12, "bold"), command=lambda: to_frame("get start"))
    self.program_button.grid(row=2)

  def to_frame(frame_name):
    if frame_name == "get start":
      GetStart()
    elif frame_name == "setting":
      Setting()
class Setting:
  pass
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