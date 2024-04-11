from tkinter import *
from functools import partial # to prevent unwanted windows

class Program:
  def __init__(self):
    self.program_frame = Frame()
    self.program_frame.configure(bg="#FFFFFF")
    self.program_frame.grid(padx=30, pady=5)
    button_font_12 = ("Arial", 12, "bold")
    # row 2
    self.to_setting_button = Button(self.program_frame, text="Setting", bg="blue", fg="white", font=button_font_12, command=lambda: self.to_frame("setting"))
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
    button_font_12 = ("Arial", 12, "bold")
    self.setting_box = Toplevel()
    partner.to_setting_button.config(state=DISABLED)
    self.setting_box.protocol('WM_DELETE_WINDOW', partial(self.close_setting, partner))
    # setting_box on setting_box for window exiting
    self.setting_frame = Frame(self.setting_box, width=200, height=300, bg=background)
    self.setting_frame.configure(bg="#FFFFFF")
    self.setting_frame.grid(padx=10, pady=5)
    # row 0
    self.setting_heading = Label(self.setting_frame, text="Setting", font=("Arial", 16, "bold"))
    self.setting_heading.grid(row=0, pady=10)
    # row 1
    setting_text = "enter your username in the box below, game won't start until you do"
    self.setting_instructions = Label(self.setting_frame, text=setting_text, wrap=250, width=40, justify="left", font=button_font_12)
    self.setting_instructions.grid(row=1, pady=5)
    # row 2
    self.filename_entry = Entry(self.setting_frame, font=button_font_12, bg="#ffffff", width=25)
    self.filename_entry.grid(row=2, pady=5)
    # row 3
    setting_Error = "Error: Sorry your name has to be with out spaces and symbols"
    self.setting_Error_msg = Label(self.setting_frame, text=setting_Error, wrap=250, width=40, justify="left", font=button_font_12, fg="red")
    self.setting_Error_msg.grid(row=3, pady=5)
    # row 4
    setting_text2 = "click on the button below to initiate any change"
    self.setting_instructions = Label(self.setting_frame, text=setting_text2, font=button_font_12)
    self.setting_instructions.grid(row=4, pady=5)
    # row 5 adjustment_frame
    self.adjustment_frame = Frame(self.setting_frame)
    custom_card_buts = [["#FF3333","off","Timer"], ["#FF3333","off","Steel Card"], ["#FF3333","off","Change Colour Card"], ["#FF3333","off","Swap Stack Card"], ["#FF3333","off","Switch Colours Card"]]
    color_phase_timer = "#FF3333", "#B3FF66", "#80FF00", "#66CC00"
    ## buttons custom
    ## add-row0
    self.timer_button = Button(self.adjustment_frame,  bg=custom_card_buts[0][0], text=custom_card_buts[0][2], fg=button_fg, font=button_font_12, command=lambda: self.add_set(custom_card_buts[0][1]))
    self.timer_button.grid(row=0, column=0, padx=10, pady=10)

    self.steel_button = Button(self.adjustment_frame,  bg=custom_card_buts[1][0], text=custom_card_buts[1][2], fg=button_fg, font=button_font_12, command=lambda: self.add_set(custom_card_buts[1][1]))
    self.steel_button.grid(row=0, column=1, padx=10, pady=10)
    ## add-row 1
    self.change_colour_button = Button(self.adjustment_frame,  bg=custom_card_buts[2][0], text=custom_card_buts[2][2], fg=button_fg, font=button_font_12, command=lambda: self.add_set(custom_card_buts[2][1]))
    self.change_colour_button.grid(row=0, column=0, padx=10, pady=10)

    self.swap_stack_button = Button(self.adjustment_frame,  bg=custom_card_buts[3][0], text=custom_card_buts[3][2], fg=button_fg, font=button_font_12, command=lambda: self.add_set(custom_card_buts[3][1]))
    self.swap_stack_button.grid(row=0, column=1, padx=10, pady=10)

    self.switch_colours_button = Button(self.adjustment_frame,  bg=custom_card_buts[4][0], text=custom_card_buts[4][2], fg=button_fg, font=button_font_12, command=lambda: self.add_set(custom_card_buts[4][1]))
    self.switch_colours_button.grid(row=0, column=3, padx=10, pady=10)
    self.adjustment_frame.grid(row=5)
    # row 6
    self.start_button = Button(self.setting_frame, text="Start", bg="blue", fg="white", font=button_font_12, command=self.to_get_start())
    self.start_button.grid(row=6, column=0, padx=10, pady=10)

    self.dismiss_button = Button(self.setting_frame, font=button_font_12, text="Dismiss", bg="#666666", fg="#FFFFFF", width=12, command=partial(self.close_setting, partner))
    self.dismiss_button.grid(row=6, column=1, padx=10, pady=10)

  def add_set(self,custom_but):
    pass
  def to_get_start(self):
    pass
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