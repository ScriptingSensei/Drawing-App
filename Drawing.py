import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Drawing App")

# Create a canvas to draw on
canvas = tk.Canvas(window, width=800, height=600, bg="white")
canvas.pack()

# Define the current tool, color, and position
tool = "pen"
color = "black"
x1, y1 = None, None

# Define the functions for drawing
def draw(event):
    global x1, y1
    if tool == "pen":
        # Draw a line from the previous point to the current point
        if x1 is not None and y1 is not None:
            canvas.create_line(x1, y1, event.x, event.y, fill=color, width=5, smooth=True)
        # Update the previous point
        x1, y1 = event.x, event.y
    elif tool == "eraser":
        # Erase a rectangle around the current point
        canvas.create_rectangle(event.x - 10, event.y - 10, event.x + 10, event.y + 10, fill="white", outline="white")

def reset(event):
    global x1, y1
    # Reset the previous point
    x1, y1 = None, None

def clear():
    # Clear the canvas
    canvas.delete("all")

def select_pen():
    global tool
    # Select the pen tool
    tool = "pen"

def select_eraser():
    global tool
    # Select the eraser tool
    tool = "eraser"

def select_color(new_color):
    global color
    # Select a new color
    color = new_color

# Create a frame for the buttons
frame = tk.Frame(window)
frame.pack()

# Create buttons for tools and colors
pen_button = tk.Button(frame, text="Pen", command=select_pen)
pen_button.grid(row=0, column=0)

eraser_button = tk.Button(frame, text="Eraser", command=select_eraser)
eraser_button.grid(row=0, column=1)

clear_button = tk.Button(frame, text="Clear", command=clear)
clear_button.grid(row=0, column=2)

black_button = tk.Button(frame, bg="black", width=2, command=lambda: select_color("black"))
black_button.grid(row=1, column=0)

red_button = tk.Button(frame, bg="red", width=2, command=lambda: select_color("red"))
red_button.grid(row=1, column=1)

green_button = tk.Button(frame, bg="green", width=2, command=lambda: select_color("green"))
green_button.grid(row=1, column=2)

blue_button = tk.Button(frame, bg="blue", width=2, command=lambda: select_color("blue"))
blue_button.grid(row=1, column=3)

# Bind the mouse events to the canvas
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset)

# Start the main loop
window.mainloop()
