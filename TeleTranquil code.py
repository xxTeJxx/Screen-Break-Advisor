import tkinter as tk
from tkinter import messagebox, simpledialog
import time

class BreakApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TeleTranquil Prototype Demo")

        self.textbox = tk.Text(root, height=20, width=60)
        self.textbox.pack(padx=10, pady=10)

        self.break_button = tk.Button(root, text="Take a Break", command=self.start_break)
        self.break_button.pack(side=tk.LEFT, padx=10)

        self.break_over_button = tk.Button(root, text="Break Over", command=self.end_break)
        self.break_over_button.pack(side=tk.RIGHT, padx=10)

        self.break_count = 0
        self.hours_worked = 0

        # Load previous content
        try:
            with open("textbox_content.txt", "r") as file:
                content = file.read()
                self.textbox.insert(tk.END, content)
        except FileNotFoundError:
            pass

    def start_break(self):
        self.break_count += 1
        self.timer_start = time.time()

    def end_break(self):
        if hasattr(self, 'timer_start'):
            elapsed_time = time.time() - self.timer_start
            messagebox.showinfo("Break Over", f"Break lasted {int(elapsed_time)} seconds.")
            delattr(self, 'timer_start')

            if self.break_count % 3 == 0:
                self.check_hours_worked()

    def check_hours_worked(self):
        breaks_message = f"You have taken {self.break_count} breaks."
        hours_worked_input = simpledialog.askfloat("Hours Worked", f"{breaks_message}\nHow many hours have you worked today?")

        if hours_worked_input is not None:
            self.hours_worked = hours_worked_input
            self.give_feedback()

    def give_feedback(self):
        feedback_message = "No problem, keep up the good work!"
        if self.hours_worked > 6 and self.break_count > 10:
            feedback_message = "You are taking adequate breaks, keep up the good work!"
        elif self.hours_worked > 6 and self.break_count <= 10:
            feedback_message = "Consider taking more breaks for better mental health."
        elif self.hours_worked <= 6 and self.break_count > 10:
            feedback_message = "No problem, keep up the good work!"
        elif self.hours_worked <= 6 and self.break_count < 3:
            feedback_message = "Consider taking more breaks for better mental health."

        messagebox.showinfo("Feedback", feedback_message)

        # Save content to a file
        with open("textbox_content.txt", "w") as file:
            file.write(self.textbox.get("1.0", tk.END))

if __name__ == "__main__":
    root = tk.Tk()
    app = BreakApp(root)
    root.mainloop()
