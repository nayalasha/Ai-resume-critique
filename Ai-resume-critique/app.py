import customtkinter as ctk

window = ctk.CTk()
window.geometry("1920x1080")
window.title("AI Resume Critique")

# Background color
window.configure(bg= "#f0f0f0")


#Test label
label = ctk.CTkLabel(window,
                      text="AI Resume Critique",
                      font=ctk.
                      CTkFont
                      (family="Arial", size=50,
                       weight="bold"),
                       )
label.pack(pady=20)

window.mainloop()