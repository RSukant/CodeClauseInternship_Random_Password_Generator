import random
import tkinter as tk

def generate_passwords():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"
    no_of_chars_wanted = int(char_entry.get())
    no_of_passwords_wanted = int(password_entry.get())
    passwords = []
    for _ in range(no_of_passwords_wanted):
        password = []
        for _ in range(no_of_chars_wanted):
            random_int = random.randint(0, len(chars) - 1)
            password.append(chars[random_int])
        passwords.append("".join(password))
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "\n".join(passwords))

root = tk.Tk()
root.title("Random Password Generator")

char_label = tk.Label(root, text="Enter the number of characters for random password:")
char_label.pack()
char_entry = tk.Entry(root)
char_entry.pack()

password_label = tk.Label(root, text="Enter the number of random passwords needed:")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()

generate_button = tk.Button(root, text="Generate Passwords", command=generate_passwords)
generate_button.pack()

result_text = tk.Text(root, height=10, width=40)
result_text.pack()

root.mainloop()
