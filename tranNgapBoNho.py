import tkinter as tk
from PIL import Image, ImageTk  # To handle image background
import random  # Import random module for random positioning

# Function to create a new window with content
def create_window():
    new_window = tk.Toplevel(root)  # Create a new window
    new_window.title("Cửa sổ mới")  # Title for the new window
    new_window.geometry("350x150")  # Set size for the new window
    
    # Set pastel pink background
    new_window.configure(bg="#ffcccb")

    # Create a frame with white border for the label
    frame = tk.Frame(new_window, bg="#ffcccb", highlightbackground="white", highlightthickness=2)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=320, height=120)  # Center the frame

    # Create a label inside the frame, anchored to the top-left corner
    label = tk.Label(
        frame, 
        text="Anh nhớ em!", 
        font=("Helvetica", 18, "bold"), 
        fg="white", 
        bg="#ffcccb",
        anchor="nw"  # Anchor to the top-left corner (northwest)
    )
    label.place(x=10, y=10)  # Position label with 10px margin from the top-left corner

    # Randomly position the window
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()
    x = random.randint(0, screen_width - 350)  # Random x position
    y = random.randint(0, screen_height - 150)  # Random y position
    new_window.geometry(f"+{x}+{y}")  # Set the random position

# Function triggered when the button is clicked
def on_button_click():
    for i in range(100):  # Create 100 windows
        root.after(i * 100, create_window)

# Main window
root = tk.Tk()
root.title("Nhấn zô đi !!!")

# Set window size and position in the center of the screen
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Load the background image (use your cute image path here)
background_image = Image.open("C:/Users/LENOVO/Desktop/backgroundCute.jpg")
background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)  # Fill the window with the image

# Button styling without the raised effect
button = tk.Button(
    root, 
    text="Nhấn zô đi !!!", 
    font=("Helvetica", 24, "bold"), 
    fg='white', 
    bg='#ff66b2',  # Pink button color
    activebackground='#ff4d99',  # Slightly darker pink when pressed
    activeforeground='white',  # Keep the text color white when pressed
    relief="flat",  # No raised effect
    bd=0,
    padx=20,
    pady=10,
    command=on_button_click
)

button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center the button horizontally and vertically

# Change button color on mouse hover
def on_enter(event):
    button.config(bg='#ff4d99')  # Darker pink on hover

def on_leave(event):
    button.config(bg='#ff66b2')  # Original pink when not hovering

# Bind hover events
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

root.mainloop()
