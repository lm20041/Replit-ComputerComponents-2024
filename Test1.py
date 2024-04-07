from tkinter import *

class Program:
  def __init__(self):
    self.program_frame = Frame()
    self.program_frame.grid()
    # row 0
    self.program_heading = Label(self.program_frame, text="Hello World")
    self.program_heading.grid(row=0)
    # row 1
    program_image = PhotoImage(file="path/to/your/image.png")

    self.program_image_label = tk.Label(self.program_frame, image=program_image)
    self.program_image_label.pack()
    # row 2
    self.program_button = Button(self.program_frame, text="play", bg="blue", fg="white", font=("Arial", 12, "bole"), width=10, height=2, command=lambda: to_frame("get start"))
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

if __name__ == "__main__":
  root = Tk()
  root.title("Card game")
  Program()
  root.mainloop()