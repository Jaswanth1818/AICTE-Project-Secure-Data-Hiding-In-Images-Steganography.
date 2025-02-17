from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from PIL import Image
import stepic

def decrypt_message():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png")])
    if not file_path:
        return
    
    input_password = password_entry.get().strip()
    if not input_password:
        messagebox.showerror("Error", "Please enter the password!")
        return

    try:
        img = Image.open(file_path)
        decoded_message = stepic.decode(img)  # Removed `.decode('utf-8')`

        if "||" in decoded_message:
            stored_password, secret_message = decoded_message.split("||", 1)
        else:
            messagebox.showerror("Error", "No hidden message found!")
            return

        if stored_password == input_password:
            messagebox.showinfo("Secret Message", f"Decrypted Message: {secret_message}")
        else:
            messagebox.showerror("Error", "Incorrect passcode!")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")

# GUI Setup
root = Tk()
root.title("Steganography - Decrypt")
root.geometry("400x200")

Label(root, text="Enter Passcode:").pack(pady=5)
password_entry = Entry(root, width=40, show="*")
password_entry.pack(pady=5)

Button(root, text="Select Image & Decrypt", command=decrypt_message).pack(pady=10)

root.mainloop()
