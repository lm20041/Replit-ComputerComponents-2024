import tkinter as tk

root = tk.Tk()
root.title("Nested Frames Example")

# Create the parent frame
parent_frame = tk.Frame(root, bg="lightblue")
parent_frame.grid(padx=10, pady=5)

# Create a label inside the parent frame
label_parent = tk.Label(parent_frame, text="Parent Frame", font=("Arial", 16, "bold"))
label_parent.grid(row=0, pady=5)

# Create the child frame inside the parent frame
child_frame = tk.Frame(parent_frame, bg="lightgreen")
child_frame.grid(row=1, pady=5)  # Changed .pack() to .grid()

# Create a label inside the child frame
label_child = tk.Label(child_frame, text="Child Frame", font=("Arial", 14))
label_child.grid(row=0, pady=5)  # Changed .pack() to .grid()

root.mainloop()