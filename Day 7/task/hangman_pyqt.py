import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                            QFrame, QGridLayout, QVBoxLayout, QHBoxLayout, 
                            QMessageBox, QWidget)
from PyQt5.QtGui import QFont, QPixmap, QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QRect
import hangman_words
from hangman_art import stages, logo

class HangmanCanvas(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stage = 6
        self.setMinimumSize(200, 250)
        self.setStyleSheet("background-color: #f0f0f0; border-radius: 5px;")
    
    def setStage(self, stage):
        self.stage = stage
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Draw frame
        painter.fillRect(self.rect(), QColor("#f0f0f0"))
        
        # Calculate hangman position
        width = self.width()
        height = self.height()
        
        pen = QPen(QColor("#333333"))
        pen.setWidth(3)
        painter.setPen(pen)
        
        # Draw gallows
        base_x = width * 0.2
        base_y = height * 0.8
        
        # Draw base
        painter.drawLine(int(base_x - 40), int(base_y), int(base_x + 40), int(base_y))
        
        # Draw vertical beam
        painter.drawLine(int(base_x), int(base_y), int(base_x), int(height * 0.2))
        
        # Draw top beam
        painter.drawLine(int(base_x), int(height * 0.2), int(width * 0.6), int(height * 0.2))
        
        # Draw rope
        painter.drawLine(int(width * 0.6), int(height * 0.2), int(width * 0.6), int(height * 0.25))
        
        # Draw the hangman based on the stage
        head_x = width * 0.6
        head_y = height * 0.3
        
        if self.stage <= 5:  # Head
            painter.drawEllipse(int(head_x - 20), int(head_y - 20), 40, 40)
        
        if self.stage <= 4:  # Body
            painter.drawLine(int(head_x), int(head_y + 20), int(head_x), int(head_y + 80))
        
        if self.stage <= 3:  # Left arm
            painter.drawLine(int(head_x), int(head_y + 30), int(head_x - 30), int(head_y + 60))
        
        if self.stage <= 2:  # Right arm
            painter.drawLine(int(head_x), int(head_y + 30), int(head_x + 30), int(head_y + 60))
        
        if self.stage <= 1:  # Left leg
            painter.drawLine(int(head_x), int(head_y + 80), int(head_x - 30), int(head_y + 120))
        
        if self.stage <= 0:  # Right leg
            painter.drawLine(int(head_x), int(head_y + 80), int(head_x + 30), int(head_y + 120))


class HangmanGame(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Game variables
        self.lives = 6
        self.chosen_word = random.choice(hangman_words.word_list)
        self.word_length = len(self.chosen_word)
        self.correct_letters = []
        self.game_over = False
        self.display = ["_" for _ in range(self.word_length)]
        
        # Setup UI
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Modern Hangman Game")
        self.setStyleSheet("background-color: #2C3E50;")
        self.setMinimumSize(800, 600)
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        main_layout = QVBoxLayout(main_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title_label = QLabel("HANGMAN")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 36, QFont.Bold))
        title_label.setStyleSheet("color: #ECF0F1;")
        main_layout.addWidget(title_label)
        
        # Game area layout
        game_layout = QHBoxLayout()
        
        # Left side - Hangman drawing
        self.hangman_canvas = HangmanCanvas()
        game_layout.addWidget(self.hangman_canvas, 1)
        
        # Right side - Game controls
        right_layout = QVBoxLayout()
        
        # Word display
        self.word_display = QLabel(" ".join(self.display))
        self.word_display.setAlignment(Qt.AlignCenter)
        self.word_display.setFont(QFont("Arial", 24, QFont.Bold))
        self.word_display.setStyleSheet("color: #ECF0F1; background-color: #34495E; padding: 15px; border-radius: 10px;")
        right_layout.addWidget(self.word_display)
        
        # Lives display
        self.lives_display = QLabel(f"Lives: {self.lives}")
        self.lives_display.setAlignment(Qt.AlignCenter)
        self.lives_display.setFont(QFont("Arial", 16))
        self.lives_display.setStyleSheet("color: #E74C3C; margin-top: 10px;")
        right_layout.addWidget(self.lives_display)
        
        game_layout.addLayout(right_layout, 1)
        main_layout.addLayout(game_layout)
        
        # Keyboard
        keyboard_layout = QVBoxLayout()
        keyboard_layout.setSpacing(10)
        
        # Create keyboard buttons
        self.letter_buttons = {}
        
        top_row = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
        middle_row = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
        bottom_row = ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        
        for row_chars in [top_row, middle_row, bottom_row]:
            row_layout = QHBoxLayout()
            row_layout.setSpacing(5)
            
            if row_chars == middle_row:
                row_layout.addSpacing(15)  # Indent the middle row slightly
                
            for letter in row_chars:
                btn = QPushButton(letter)
                btn.setFont(QFont("Arial", 16, QFont.Bold))
                btn.setMinimumSize(50, 50)
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: #3498DB;
                        color: white;
                        border: none;
                        border-radius: 5px;
                    }
                    QPushButton:hover {
                        background-color: #2980B9;
                    }
                    QPushButton:pressed {
                        background-color: #1B4F72;
                    }
                    QPushButton:disabled {
                        background-color: #95A5A6;
                    }
                """)
                btn.clicked.connect(lambda checked, l=letter.lower(): self.check_guess(l))
                self.letter_buttons[letter.lower()] = btn
                row_layout.addWidget(btn)
                
            if row_chars == middle_row:
                row_layout.addSpacing(15)  # Indent the middle row slightly
                
            keyboard_layout.addLayout(row_layout)
            
        main_layout.addLayout(keyboard_layout)
        
        # Action buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)
        
        # New Game button
        self.new_game_btn = QPushButton("New Game")
        self.new_game_btn.setFont(QFont("Arial", 14, QFont.Bold))
        self.new_game_btn.setMinimumSize(150, 50)
        self.new_game_btn.setStyleSheet("""
            QPushButton {
                background-color: #2ECC71;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #27AE60;
            }
            QPushButton:pressed {
                background-color: #1D8348;
            }
        """)
        self.new_game_btn.clicked.connect(self.new_game)
        button_layout.addWidget(self.new_game_btn)
        
        # Play Again button
        self.play_again_btn = QPushButton("Play Again")
        self.play_again_btn.setFont(QFont("Arial", 14, QFont.Bold))
        self.play_again_btn.setMinimumSize(150, 50)
        self.play_again_btn.setEnabled(False)  # Initially disabled
        self.play_again_btn.setStyleSheet("""
            QPushButton {
                background-color: #F39C12;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #D68910;
            }
            QPushButton:pressed {
                background-color: #B9770E;
            }
            QPushButton:disabled {
                background-color: #95A5A6;
            }
        """)
        self.play_again_btn.clicked.connect(self.play_again)
        button_layout.addWidget(self.play_again_btn)
        
        main_layout.addLayout(button_layout)
        
        # For debug only - remove in production
        self.debug_label = QLabel(f"Word: {self.chosen_word}")
        self.debug_label.setAlignment(Qt.AlignCenter)
        self.debug_label.setFont(QFont("Arial", 10))
        self.debug_label.setStyleSheet("color: #7F8C8D; margin-top: 10px;")
        main_layout.addWidget(self.debug_label)
        
    def check_guess(self, letter):
        if self.game_over:
            return
            
        # Disable the button
        self.letter_buttons[letter].setEnabled(False)
        
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
        self.word_display.setText(" ".join(self.display))
        
        # If letter not found, lose a life
        if not found:
            self.lives -= 1
            self.lives_display.setText(f"Lives: {self.lives}")
            self.letter_buttons[letter].setStyleSheet("""
                QPushButton {
                    background-color: #E74C3C;
                    color: white;
                    border: none;
                    border-radius: 5px;
                }
            """)
            self.hangman_canvas.setStage(self.lives)
        else:
            self.letter_buttons[letter].setStyleSheet("""
                QPushButton {
                    background-color: #2ECC71;
                    color: white;
                    border: none;
                    border-radius: 5px;
                }
            """)
            
        # Check game end conditions
        if "_" not in self.display:
            self.game_over = True
            QMessageBox.information(self, "You Win!", "Congratulations! You've guessed the word correctly!")
            self.play_again_btn.setEnabled(True)
            
        if self.lives == 0:
            self.game_over = True
            QMessageBox.information(self, "Game Over", f"You lose! The word was: {self.chosen_word.upper()}")
            self.play_again_btn.setEnabled(True)
            
    def new_game(self):
        self.reset_game()
        
    def play_again(self):
        self.reset_game()
        
    def reset_game(self):
        # Reset game variables
        self.lives = 6
        self.chosen_word = random.choice(hangman_words.word_list)
        self.word_length = len(self.chosen_word)
        self.correct_letters = []
        self.game_over = False
        self.display = ["_" for _ in range(self.word_length)]
        
        # Update UI
        self.word_display.setText(" ".join(self.display))
        self.lives_display.setText(f"Lives: {self.lives}")
        self.hangman_canvas.setStage(6)
        self.debug_label.setText(f"Word: {self.chosen_word}")
        self.play_again_btn.setEnabled(False)
        
        # Reset keyboard buttons
        for letter, button in self.letter_buttons.items():
            button.setEnabled(True)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #3498DB;
                    color: white;
                    border: none;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #2980B9;
                }
                QPushButton:pressed {
                    background-color: #1B4F72;
                }
            """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HangmanGame()
    window.show()
    sys.exit(app.exec_())
