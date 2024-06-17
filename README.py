import tkinter as tk

class MathSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Problem Solver")

        self.create_widgets()

    def create_widgets(self):
        # Text widget for displaying conversation
        self.textbox = tk.Text(self.root, width=60, height=10, font=("Arial", 12))
        self.textbox.pack(pady=20)

        # Entry widget for user input
        self.entry = tk.Entry(self.root, width=50, font=("Arial", 14))
        self.entry.pack(ipady=10)

        # Solve Button
        self.solve_button = tk.Button(self.root, text="Solve", width=10, font=("Arial", 12), command=self.solve_problem)
        self.solve_button.pack(pady=10)

        # Welcome message
        self.textbox.insert(tk.END, "Welcome! Please enter a math problem and press 'Solve'.\n\n")

        # Bind the Entry widget click event to open the keyboard
        self.entry.bind("<Button-1>", self.open_keyboard)

    def open_keyboard(self, event):
        self.entry.focus_set()  # Set focus on the Entry widget
        self.root.focus_force()  # Force focus back to the root window to show the keyboard

    def solve_problem(self):
        problem = self.entry.get()

        try:
            result = eval(problem)
            self.textbox.insert(tk.END, f"You: {problem}\n")
            self.textbox.insert(tk.END, f"Bot: The result is: {result}\n\n")
            self.entry.delete(0, tk.END)  # Clear the entry field after solving
        except Exception as e:
            self.textbox.insert(tk.END, f"You: {problem}\n")
            self.textbox.insert(tk.END, f"Bot: Invalid input or error: {e}\n\n")
            self.entry.delete(0, tk.END)  # Clear the entry field after an error

def main():
    root = tk.Tk()
    app = MathSolverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
