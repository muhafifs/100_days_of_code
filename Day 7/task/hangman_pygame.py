import pygame
import sys
import random
import os
from hangman_words import word_list
from hangman_art import stages, logo

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
BLUE = (0, 119, 190)
LIGHT_BLUE = (52, 152, 219)
DARK_BLUE = (27, 79, 114)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
YELLOW = (241, 196, 15)
FONT_NAME = "Arial"

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hangman Game")

# Set up fonts
title_font = pygame.font.SysFont(FONT_NAME, 48, bold=True)
word_font = pygame.font.SysFont(FONT_NAME, 36, bold=True)
letter_font = pygame.font.SysFont(FONT_NAME, 24, bold=True)
button_font = pygame.font.SysFont(FONT_NAME, 22, bold=True)
info_font = pygame.font.SysFont(FONT_NAME, 18)

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=WHITE):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.active = True
        self.correct = False
        self.incorrect = False

    def draw(self, surface):
        color = self.color
        if not self.active:
            if self.correct:
                color = GREEN
            elif self.incorrect:
                color = RED
            else:
                color = GRAY
        elif self.is_hovered():
            color = self.hover_color

        # Draw button background
        pygame.draw.rect(surface, color, self.rect, border_radius=5)

        # Draw button text
        text_surf = button_font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def is_clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN and
                event.button == 1 and
                self.rect.collidepoint(event.pos) and
                self.active)

class HangmanGame:
    def __init__(self):
        self.reset_game()
        self.setup_buttons()
        # Load and scale logo
        self.logo_lines = logo.strip().split('\n')

    def reset_game(self):
        self.chosen_word = random.choice(word_list).lower()
        self.display = ["_" for _ in range(len(self.chosen_word))]
        self.lives = 6
        self.guessed_letters = []
        self.game_over = False
        self.won = False

        # For debug
        print(f"Debug - Word: {self.chosen_word}")

    def setup_buttons(self):
        self.letter_buttons = {}

        # Create letter buttons (A-Z)
        top_row = "QWERTYUIOP"
        middle_row = "ASDFGHJKL"
        bottom_row = "ZXCVBNM"

        button_width = 40
        button_height = 40
        button_spacing = 5

        # Position and create keyboard rows - moved lower on the screen
        keyboard_y = 420

        # Top row
        start_x = (SCREEN_WIDTH - (len(top_row) * (button_width + button_spacing) - button_spacing)) // 2
        for i, letter in enumerate(top_row):
            x = start_x + i * (button_width + button_spacing)
            self.letter_buttons[letter.lower()] = Button(x, keyboard_y, button_width, button_height,
                                                       letter, BLUE, LIGHT_BLUE)

        # Middle row
        keyboard_y += button_height + button_spacing
        start_x = (SCREEN_WIDTH - (len(middle_row) * (button_width + button_spacing) - button_spacing)) // 2
        for i, letter in enumerate(middle_row):
            x = start_x + i * (button_width + button_spacing)
            self.letter_buttons[letter.lower()] = Button(x, keyboard_y, button_width, button_height,
                                                       letter, BLUE, LIGHT_BLUE)

        # Bottom row
        keyboard_y += button_height + button_spacing
        start_x = (SCREEN_WIDTH - (len(bottom_row) * (button_width + button_spacing) - button_spacing)) // 2
        for i, letter in enumerate(bottom_row):
            x = start_x + i * (button_width + button_spacing)
            self.letter_buttons[letter.lower()] = Button(x, keyboard_y, button_width, button_height,
                                                       letter, BLUE, LIGHT_BLUE)

        # Create action buttons (positioned at the bottom)
        button_y = SCREEN_HEIGHT - 60
        button_width = 150
        button_height = 40
        button_spacing = 100

        center_x = SCREEN_WIDTH // 2
        self.new_game_button = Button(center_x - button_width - button_spacing//2, button_y,
                                    button_width, button_height, "New Game", GREEN, (36, 174, 93))
        self.play_again_button = Button(center_x + button_spacing//2, button_y,
                                      button_width, button_height, "Play Again", YELLOW, (241, 176, 5))

    def check_guess(self, letter):
        if letter in self.guessed_letters or self.game_over:
            return

        self.guessed_letters.append(letter)

        # Disable the button
        self.letter_buttons[letter].active = False

        # Check if letter is in word
        if letter in self.chosen_word:
            for i, char in enumerate(self.chosen_word):
                if char == letter:
                    self.display[i] = letter
            self.letter_buttons[letter].correct = True

            # Check if player won
            if "_" not in self.display:
                self.game_over = True
                self.won = True
        else:
            self.lives -= 1
            self.letter_buttons[letter].incorrect = True

            # Check if player lost
            if self.lives == 0:
                self.game_over = True

    def handle_event(self, event):
        # Handle letter button clicks
        if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
            for letter, button in self.letter_buttons.items():
                if button.is_clicked(event):
                    self.check_guess(letter)
                    break

        # Handle action button clicks
        if self.new_game_button.is_clicked(event):
            self.reset_game()
            for button in self.letter_buttons.values():
                button.active = True
                button.correct = False
                button.incorrect = False

        if self.game_over and self.play_again_button.is_clicked(event):
            self.reset_game()
            for button in self.letter_buttons.values():
                button.active = True
                button.correct = False
                button.incorrect = False

    def draw_hangman(self):
        # Draw hang
