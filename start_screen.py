import customtkinter as ctk
import subprocess

# Theme settings
ctk.set_appearance_mode("light")  # Or "dark"
ctk.set_default_color_theme("blue")

# Create window
app = ctk.CTk()
app.title("Catch the Circle")
app.geometry("600x500")  # Set the window size

# Set the window icon and title
title = ctk.CTkLabel(app, text="🎯 Catch the Circle", font=("Helvetica", 28, "bold"))
title.pack(pady=30)

# Instructions label    
instructions = ctk.CTkLabel(
    app,
    text="🖐️Use your finger to catch the circle\n   ⏱️ You have 60 seconds",
    font=("Helvetica", 18),
    justify="center"
)
instructions.pack(pady=15)

# Start game function
def start_game():
    app.destroy()
    subprocess.run(["python", "game.py"])

# Start button
start_button = ctk.CTkButton(app, text="Start", command=start_game, width=140, height=50, fg_color="#198754", text_color="white", font=("Helvetica", 16, "bold"))
start_button.pack(pady=10)

# Exit button
exit_button = ctk.CTkButton(app, text="Exit", command=app.destroy, width=140, height=50, fg_color="#dc3545", text_color="white", font=("Helvetica", 16, "bold"))
exit_button.pack(pady=5)

# Run the app
app.mainloop()