import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        self.root.geometry("400x200")

        self.choices = ["rock", "paper", "scissors"]
        self.user1_count = 0
        self.user2_count = 0

        self.label_user1 = tk.Label(root, text="User 1:")
        self.label_user1.pack()
        self.entry_user1 = tk.Entry(root)
        self.entry_user1.pack()

        self.label_user2 = tk.Label(root, text="User 2:")
        self.label_user2.pack()
        self.entry_user2 = tk.Entry(root)
        self.entry_user2.pack()

        self.play_button = tk.Button(root, text="Play", command=self.play_game)
        self.play_button.pack()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "User 1 wins!"
        else:
            return "User 2 wins!"

    def play_game(self):
        user1 = self.entry_user1.get().lower()
        user2 = self.entry_user2.get().lower()

        if user1 not in self.choices or user2 not in self.choices:
            messagebox.showerror("Error", "Invalid choice. Please choose rock, paper, or scissors.")
            return

        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user1, computer_choice)

        if result == "User 1 wins!":
            self.user1_count += 1
        elif result == "User 2 wins!":
            self.user2_count += 1

        messagebox.showinfo("Result", f"Computer chose {computer_choice}. {result}\nUser 1: {self.user1_count} wins, User 2: {self.user2_count} wins")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
