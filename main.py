import tkinter as tk
from tkinter import ttk, messagebox
from gpt_utils import generate_text

# Setup main window
root = tk.Tk()
root.title("Text Generation Model Using GPT")
root.geometry("850x550")
root.configure(bg="#f0f4f8")  # Light background

# Set modern style
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#f0f4f8", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 11, "bold"), padding=6)
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TText", font=("Helvetica", 12), padding=5)

# Hover style
def on_enter(e): generate_button.config(style="Hover.TButton")
def on_leave(e): generate_button.config(style="TButton")

style.map("Hover.TButton",
          background=[("active", "#1f6f8b")],
          foreground=[("active", "white")])

style.configure("Hover.TButton", background="#4a90e2", foreground="white", borderwidth=0)

# ---------- UI Components ----------

# Title Label
title = ttk.Label(root, text="Generative Text Model", font=("Helvetica", 18, "bold"), background="#f0f4f8", foreground="#1f6f8b")
title.pack(pady=15)

# Prompt input label
prompt_label = ttk.Label(root, text="Enter your prompt below:")
prompt_label.pack()

# Prompt Entry
prompt_entry = tk.Entry(root, font=("Helvetica", 12), width=90, bd=2, relief="groove")
prompt_entry.pack(pady=10, padx=20)

# Generate button
generate_button = ttk.Button(root, text="Generate Text", command=lambda: on_generate())
generate_button.pack(pady=8)
generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)

# Output Label
output_label = ttk.Label(root, text="Generated Output:")
output_label.pack(pady=5)

# Output Text Box
output_box = tk.Text(root, height=13, width=100, font=("Helvetica", 11), wrap="word", bd=2, relief="sunken", bg="white", fg="#333")
output_box.pack(padx=20, pady=10)

# ---------- Footer ----------
footer = tk.Label(root, text="Designed by Samrat Singh", font=("Helvetica", 10, "bold"),
                  bg="#f0f4f8", fg="#555")
footer.pack(side=tk.BOTTOM, pady=5)

# ---------- Function ----------

def on_generate():
    prompt = prompt_entry.get().strip()
    if not prompt:
        messagebox.showwarning("Missing Prompt", "Please enter a prompt.")
        return
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Thinking...\n")
    root.update()
    result = generate_text(prompt)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

# Run the main loop
root.mainloop()
