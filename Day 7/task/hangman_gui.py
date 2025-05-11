import random
import tkinter as tk
from tkinter import messagebox, PhotoImage
import hangman_words
from hangman_art import stages, logo

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#2C3E50")  # Dark blue background

        # Game variables
        self.lives = 6
        self.chosen_word = random.choice(hangman_words.word_list)
        self.word_length = len(self.chosen_word)
        self.correct_letters = []
        self.game_over = False
        self.display = ["_" for _ in range(self.word_length)]

        # Create GUI elements
        self.setup_ui()

    def setup_ui(self):
        # Title frame
        title_frame = tk.Frame(self.root, bg="#2C3E50")
        title_frame.pack(pady=10)

        title_label = tk.Label(
            title_frame,
            text="HANGMAN",
            font=("Courier", 36, "bold"),
            fg="#ECF0F1",
            bg="#2C3E50"
        )
        title_label.pack()

        # Hangman image frame
        self.hangman_frame = tk.Frame(self.root, bg="#2C3E50")
        self.hangman_frame.pack(pady=10)

        self.hangman_display = tk.Label(
            self.hangman_frame,
            text=stages[self.lives],
            font=("Courier", 14),
            fg="#ECF0F1",
            bg="#2C3E50",
            justify="left"
        )
        self.hangman_display.pack()

        # Word display frame
        word_frame = tk.Frame(self.root, bg="#2C3E50")
        word_frame.pack(pady=20)

        self.word_display = tk.Label(
            word_frame,
            text=" ".join(self.display),
            font=("Courier", 24, "bold"),
            fg="#ECF0F1",
            bg="#2C3E50"
        )
        self.word_display.pack()

        # Lives display
        self.lives_display = tk.Label(
            self.root,
            text=f"Lives: {self.lives}",
            font=("Courier", 16),
            fg="#E74C3C",
            bg="#2C3E50"
        )
        self.lives_display.pack(pady=10)

        # Keyboard frame
        keyboard_frame = tk.Frame(self.root, bg="#2C3E50")
        keyboard_frame.pack(pady=20)

        # Create keyboard buttons
        self.create_keyboard(keyboard_frame)

        # Debug label - remove in production
        self.debug_label = tk.Label(
            self.root,
            text=f"Word: {self.chosen_word}",
            font=("Courier", 10),
            fg="#7F8C8D",
            bg="#2C3E50"
        )
        self.debug_label.pack(side="bottom", pady=5)

    def create_keyboard(self, parent):
        letters = [
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        ]

        self.letter_buttons = {}  # Store references to letter buttons

        for i, row in enumerate(letters):
            row_frame = tk.Frame(parent, bg="#2C3E50")
            row_frame.pack(pady=5)

            for letter in row:
                btn = tk.Button(
                    row_frame,
                    text=letter.upper(),
                    font=("Courier", 14, "bold"),
                    width=4,
                    bg="#3498DB",
                    fg="#FFFFFF",
                    activebackground="#2980B9",
                    command=lambda l=letter: self.check_guess(l)
                )
                btn.pack(side="left", padx=5)
                self.letter_buttons[letter] = btn

        # Add new game button
        new_game_btn = tk.Button(
            parent,
            text="New Game",
            font=("Courier", 14, "bold"),
            bg="#2ECC71",
            fg="#FFFFFF",
            activebackground="#27AE60",
            command=self.new_game
        )
        new_game_btn.pack(pady=15)

    def check_guess(self, letter):
        if self.game_over:
            return

        # Disable the button
        self.letter_buttons[letter].config(state="disabled")

        if letter in self.correct_letters:
            return

        found = False
        for i, char in enumerate(self.chosen_word):
            if char == letter:
                self.display[i] = letter
                found = True
                if letter not in self.correct_letters:
                    self.correct_letters.append(letter)

        # Update display
        self.word_display.config(text=" ".join(self.display))

        # If letter not found, lose a life
        if not found:
            self.lives -= 1
            self.lives_display.config(text=f"Lives: {self.lives}")
            self.letter_buttons[letter].config(bg="#E74C3C")  # Red for wrong guess
            self.hangman_display.config(text=stages[self.lives])
        else:
            self.letter_buttons[letter].config(bg="#2ECC71")  # Green for correct guess

        # Check game end conditions
        if "_" not in self.display:
            self.game_over = True
            messagebox.showinfo("You Win!", "Congratulations! You've guessed the word correctly!")

        if self.lives == 0:
            self.game_over = True
            messagebox.showinfo("Game Over", f"You lose! The word was: {self.chosen_word.upper()}")

    def new_game(self):
        # Reset game variables
        self.lives = 6
        self.chosen_word = random.choice(hangman_words.word_list)
        self.word_length = len(self.chosen_word)
        self.correct_letters = []
        self.game_over = False
        self.display = ["_" for _ in range(self.word_length)]

        # Update UI
        self.word_display.config(text=" ".join(self.display))
        self.lives_display.config(text=f"Lives: {self.lives}")
        self.hangman_display.config(text=stages[self.lives])
        self.debug_label.config(text=f"Word: {self.chosen_word}")

        # Reset keyboard buttons
        for letter, button in self.letter_buttons.items():
            button.config(state="normal", bg="#3498DB")

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()
