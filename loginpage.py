import tkinter as tk

class LoginUI:                  # Step 1: Class
        def __init__(self, root):  # Step 2: Indented method
                self.root = root       # Step 3: Inside method

                self.root.title("Login")
                self.root.geometry("400x300")

        frame = tk.Frame(self.root)   # ✅ use self.root
        frame.pack()

        self.username = tk.Entry(frame)  # ✅ self used inside class
        self.username.pack()

        self.password = tk.Entry(frame, show="*")
        self.password.pack()

        tk.Button(frame, text="Login", command=self.login).pack()
def login(self):            # Step 4: Same indentation as __init__
        print(self.username.get())


# Step 5: Outside class (NO indentation)
root = tk.Tk()
app = LoginUI(root)
root.mainloop()