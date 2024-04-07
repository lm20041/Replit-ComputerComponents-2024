import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Viewer")

# Load image
image = Image.open("ColorCard_image/color_card-back_card.png")
image_tk = ImageTk.PhotoImage(image)

# Display image
label = tk.Label(root, image=image_tk) #
label.pack()

root.mainloop()