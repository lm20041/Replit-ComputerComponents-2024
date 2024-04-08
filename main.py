import tkinter as tk

root = tk.Tk()
root.title("Frame with Border")

# Create a frame with a border
frame = tk.Frame(root, borderwidth=20, relief=tk.SOLID)
frame.grid(row=0, column=0, padx=10, pady=10)

# Add widgets inside the frame
label = tk.Label(frame, text="borderwidth is 10")
label.pack(padx=40, pady=40)

button = tk.Button(frame, text="Click Me")
button.pack(padx=10, pady=10)

root.mainloop()