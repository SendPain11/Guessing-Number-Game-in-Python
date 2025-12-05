import tkinter as tk
from tkinter import messagebox, font
import random
import time

class NumberGuessingGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("🎯 Number Guessing Game")
        self.window.geometry("700x600")  # Ukuran optimal
        self.window.configure(bg='#0a192f')
        self.window.resizable(False, False)
        
        # Game variables
        self.TARGET = 0
        self.RETRIES = 0
        self.MAX_ATTEMPTS = 10
        self.SCORE = 1000
        self.game_active = False
        self.start_time = 0
        self.best_score = 0
        
        # Color scheme
        self.colors = {
            'bg': '#0a192f',
            'primary': '#64ffda',
            'secondary': '#112240',
            'text': '#ccd6f6',
            'accent': '#ff6b6b',
            'success': '#4ecdc4',
            'warning': '#ffe66d'
        }
        
        self.setup_ui()
        self.new_game()
    
    def setup_ui(self):
        # Custom fonts
        title_font = font.Font(family='Helvetica', size=22, weight='bold')
        button_font = font.Font(family='Helvetica', size=10, weight='bold')
        
        # Header Frame
        header_frame = tk.Frame(self.window, bg=self.colors['bg'])
        header_frame.pack(pady=10)
        
        # Title
        self.title_label = tk.Label(
            header_frame,
            text="🎮 NUMBER GUESSING GAME",
            font=title_font,
            fg=self.colors['primary'],
            bg=self.colors['bg']
        )
        self.title_label.pack()
        
        # Developer Credit - Simple
        credit_label = tk.Label(
            header_frame,
            text="Created by: SEND",
            font=('Helvetica', 9, 'italic'),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        credit_label.pack()
        
        # Best Score Display
        self.best_score_label = tk.Label(
            header_frame,
            text="🏆 Best Score: 0",
            font=('Helvetica', 11, 'bold'),
            fg=self.colors['warning'],
            bg=self.colors['bg']
        )
        self.best_score_label.pack(pady=5)
        
        # Stats Frame
        stats_frame = tk.Frame(self.window, bg=self.colors['secondary'], relief=tk.RAISED, bd=1)
        stats_frame.pack(pady=10, padx=20, fill='x')
        
        self.stats_text = tk.Label(
            stats_frame,
            text="",
            font=('Helvetica', 10),
            fg=self.colors['warning'],
            bg=self.colors['secondary'],
            justify=tk.LEFT
        )
        self.stats_text.pack(pady=8, padx=10)
        
        # Game Area
        game_frame = tk.Frame(self.window, bg=self.colors['bg'])
        game_frame.pack(pady=10)
        
        # Input Frame
        input_frame = tk.Frame(game_frame, bg=self.colors['bg'])
        input_frame.pack(pady=10)
        
        # Entry
        self.guessed_number = tk.StringVar()
        self.number_form = tk.Entry(
            input_frame,
            textvariable=self.guessed_number,
            font=('Helvetica', 14),
            width=12,
            justify='center',
            bd=2,
            relief=tk.SUNKEN,
            bg='#1e3a5f',
            fg=self.colors['primary']
        )
        self.number_form.pack(side=tk.LEFT, padx=5)
        
        # Guess Button
        self.guess_button = tk.Button(
            input_frame,
            text="GUESS",
            font=button_font,
            command=self.play_game,
            bg=self.colors['primary'],
            fg='black',
            padx=15,
            pady=5,
            cursor='hand2',
            state='disabled'
        )
        self.guess_button.pack(side=tk.LEFT, padx=5)
        
        self.number_form.bind('<Return>', lambda event: self.play_game())
        
        # Action Buttons Frame
        action_frame = tk.Frame(game_frame, bg=self.colors['bg'])
        action_frame.pack(pady=10)
        
        # Reset Button
        self.reset_button = tk.Button(
            action_frame,
            text="RESET",
            font=button_font,
            command=self.reset_game,
            bg='#ff9e00',
            fg='black',
            padx=15,
            pady=5,
            cursor='hand2'
        )
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
        # Quit Game Button
        self.quit_button = tk.Button(
            action_frame,
            text="QUIT GAME",
            font=button_font,
            command=self.quit_current_game,
            bg='#ff4757',
            fg='white',
            padx=15,
            pady=5,
            cursor='hand2'
        )
        self.quit_button.pack(side=tk.LEFT, padx=5)
        
        # Credits Button
        self.credits_button = tk.Button(
            action_frame,
            text="CREDITS",
            font=button_font,
            command=self.show_credits,
            bg='#6c5ce7',
            fg='white',
            padx=15,
            pady=5,
            cursor='hand2'
        )
        self.credits_button.pack(side=tk.LEFT, padx=5)
        
        # Result Display
        result_frame = tk.Frame(self.window, bg=self.colors['secondary'], relief=tk.GROOVE, bd=1)
        result_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        self.result = tk.Label(
            result_frame,
            text="Welcome!\nClick 'NEW GAME' to start.",
            font=('Helvetica', 11),
            fg=self.colors['text'],
            bg=self.colors['secondary'],
            wraplength=500,
            justify=tk.CENTER,
            pady=20
        )
        self.result.pack(expand=True, fill='both')
        
        # Progress Bar
        progress_frame = tk.Frame(self.window, bg=self.colors['bg'])
        progress_frame.pack(pady=10, padx=20, fill='x')
        
        self.progress_label = tk.Label(
            progress_frame,
            text="Attempts: 0/10",
            font=('Helvetica', 9),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        self.progress_label.pack()
        
        self.progress_bar = tk.Canvas(
            progress_frame,
            width=300,
            height=10,
            bg='#1e3a5f',
            highlightthickness=0
        )
        self.progress_bar.pack(pady=5)
        self.progress_rect = self.progress_bar.create_rectangle(0, 0, 0, 10, fill=self.colors['success'])
        
        # Control Buttons Frame
        control_frame = tk.Frame(self.window, bg=self.colors['bg'])
        control_frame.pack(pady=10)
        
        # New Game Button
        self.play_button = tk.Button(
            control_frame,
            text="NEW GAME",
            font=button_font,
            command=self.new_game,
            bg=self.colors['success'],
            fg='black',
            padx=20,
            pady=8,
            cursor='hand2'
        )
        self.play_button.pack(side=tk.LEFT, padx=5)
        
        # Hint Button
        self.hint_button = tk.Button(
            control_frame,
            text="HINT",
            font=button_font,
            command=self.give_hint,
            bg='#9b59b6',
            fg='white',
            padx=20,
            pady=8,
            cursor='hand2',
            state='disabled'
        )
        self.hint_button.pack(side=tk.LEFT, padx=5)
        
        # Exit Button
        self.exit_button = tk.Button(
            control_frame,
            text="EXIT",
            font=button_font,
            command=self.exit_game,
            bg=self.colors['accent'],
            fg='white',
            padx=20,
            pady=8,
            cursor='hand2'
        )
        self.exit_button.pack(side=tk.LEFT, padx=5)
        
        # Difficulty selector
        diff_frame = tk.Frame(self.window, bg=self.colors['bg'])
        diff_frame.pack(pady=5)
        
        tk.Label(
            diff_frame,
            text="Difficulty:",
            font=('Helvetica', 9),
            fg=self.colors['text'],
            bg=self.colors['bg']
        ).pack(side=tk.LEFT, padx=5)
        
        self.difficulty = tk.StringVar(value="medium")
        
        tk.Radiobutton(
            diff_frame,
            text="Easy (1-50)",
            variable=self.difficulty,
            value="easy",
            command=self.change_difficulty,
            font=('Helvetica', 9),
            fg=self.colors['text'],
            bg=self.colors['bg']
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Radiobutton(
            diff_frame,
            text="Medium (1-100)",
            variable=self.difficulty,
            value="medium",
            command=self.change_difficulty,
            font=('Helvetica', 9),
            fg=self.colors['text'],
            bg=self.colors['bg']
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Radiobutton(
            diff_frame,
            text="Hard (1-200)",
            variable=self.difficulty,
            value="hard",
            command=self.change_difficulty,
            font=('Helvetica', 9),
            fg=self.colors['text'],
            bg=self.colors['bg']
        ).pack(side=tk.LEFT, padx=5)
        
        # Status Bar - Simple credit
        self.status_bar = tk.Label(
            self.window,
            text="Number Guessing Game • Created by SEND",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            font=('Helvetica', 8),
            fg=self.colors['text'],
            bg=self.colors['secondary']
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def show_credits(self):
        """Simple credits display"""
        credits_text = """
╔══════════════════════════════════════╗
║          GAME CREDITS                ║
╠══════════════════════════════════════╣
║                                      ║
║  Game: Number Guessing Game          ║
║  Version: 1.0                        ║
║  Created by: SEND                    ║
║                                      ║
║  🎮 Game Design & Development        ║
║     • SEND                           ║
║                                      ║
║  🎨 UI Design                        ║
║     • SEND                           ║
║                                      ║
║  🔧 Programming                      ║
║     • Python + Tkinter               ║
║                                      ║
║  📅 Released: 2024                   ║
║                                      ║
║  Thank you for playing!              ║
║                                      ║
╚══════════════════════════════════════╝
        """
        
        # Show credits in messagebox
        messagebox.showinfo("Game Credits", credits_text)
    
    def update_status(self, message):
        """Update status bar"""
        self.status_bar.config(text=f"Status: {message}")
    
    def update_stats(self):
        elapsed_time = time.time() - self.start_time if self.game_active else 0
        stats = f"Score: {self.SCORE} | Attempts: {self.RETRIES}/{self.MAX_ATTEMPTS} | Time: {int(elapsed_time)}s"
        self.stats_text.config(text=stats)
        
        # Progress bar
        progress_width = (self.RETRIES / self.MAX_ATTEMPTS) * 300
        self.progress_bar.coords(self.progress_rect, 0, 0, progress_width, 10)
        
        # Color based on attempts
        if self.RETRIES >= self.MAX_ATTEMPTS * 0.8:
            self.progress_bar.itemconfig(self.progress_rect, fill=self.colors['accent'])
        elif self.RETRIES >= self.MAX_ATTEMPTS * 0.6:
            self.progress_bar.itemconfig(self.progress_rect, fill=self.colors['warning'])
        else:
            self.progress_bar.itemconfig(self.progress_rect, fill=self.colors['success'])
        
        self.progress_label.config(text=f"Attempts: {self.RETRIES}/{self.MAX_ATTEMPTS}")
    
    def new_game(self):
        self.game_active = True
        self.RETRIES = 0
        self.SCORE = 1000
        self.start_time = time.time()
        
        # Set difficulty
        if self.difficulty.get() == "easy":
            self.TARGET = random.randint(1, 50)
            self.MAX_ATTEMPTS = 8
        elif self.difficulty.get() == "medium":
            self.TARGET = random.randint(1, 100)
            self.MAX_ATTEMPTS = 10
        else:
            self.TARGET = random.randint(1, 200)
            self.MAX_ATTEMPTS = 12
        
        # Enable buttons
        self.guess_button.config(state='normal', bg=self.colors['primary'])
        self.hint_button.config(state='normal', bg='#9b59b6')
        self.number_form.config(state='normal')
        
        self.guessed_number.set("")
        self.update_result("🎮 New game started!\nGuess a number between 1 and 100\n\nCreated by SEND")
        self.update_stats()
        self.update_status("New game - Make your guess")
        self.number_form.focus_set()
    
    def reset_game(self):
        if not self.game_active:
            return
            
        if messagebox.askyesno("Reset Game", "Start new game with same settings?"):
            self.RETRIES = 0
            self.SCORE = 1000
            self.start_time = time.time()
            
            # New random number
            if self.difficulty.get() == "easy":
                self.TARGET = random.randint(1, 50)
            elif self.difficulty.get() == "medium":
                self.TARGET = random.randint(1, 100)
            else:
                self.TARGET = random.randint(1, 200)
            
            self.guessed_number.set("")
            self.update_result("🔄 Game reset!\nNew number generated.\nGood luck!")
            self.update_stats()
            self.update_status("Game reset - Ready to guess")
            self.number_form.focus_set()
    
    def quit_current_game(self):
        if not self.game_active:
            return
            
        if messagebox.askyesno("Quit Game", "Quit current game?"):
            self.end_game()
            self.update_result(f"Game ended.\nThe number was: {self.TARGET}\nYour score: {self.SCORE}\n\nClick 'NEW GAME' to play again!")
            self.update_status("Game ended")
    
    def play_game(self):
        if not self.game_active:
            return
        
        try:
            choice = int(self.number_form.get())
            
            # Validate input
            max_range = 200 if self.difficulty.get() == "hard" else 100 if self.difficulty.get() == "medium" else 50
            if choice < 1 or choice > max_range:
                self.update_result(f"Please enter number 1-{max_range}")
                return
                
        except ValueError:
            self.update_result("Please enter a valid number")
            return
        
        self.RETRIES += 1
        self.SCORE = max(0, self.SCORE - 50)
        
        if choice != self.TARGET:
            difference = abs(self.TARGET - choice)
            
            # Hot/cold hints
            if difference <= 5:
                hint_text = "🔥 Very Hot!"
            elif difference <= 15:
                hint_text = "♨️ Hot!"
            elif difference <= 30:
                hint_text = "🌤️ Warm"
            else:
                hint_text = "❄️ Cold"
            
            if self.TARGET < choice:
                direction = "Go LOWER 📉"
            else:
                direction = "Go HIGHER 📈"
            
            result = f"Wrong! Attempt #{self.RETRIES}\n\n"
            result += f"{hint_text}\n{direction}\n\n"
            
            if self.RETRIES >= self.MAX_ATTEMPTS:
                result += f"Game Over!\nThe number was {self.TARGET}\n\nCreated by SEND"
                self.end_game()
                self.update_status("Game over")
            else:
                result += f"Attempts left: {self.MAX_ATTEMPTS - self.RETRIES}"
                self.update_status(f"Wrong guess - Try again")
                
            self.update_result(result)
            
        else:
            elapsed_time = time.time() - self.start_time
            time_bonus = max(0, 500 - int(elapsed_time * 5))
            final_score = self.SCORE + time_bonus
            
            # Update best score
            if final_score > self.best_score:
                self.best_score = final_score
                self.best_score_label.config(text=f"🏆 Best Score: {self.best_score}")
            
            # Performance message
            if self.RETRIES <= 3:
                performance = "🌟 Amazing!"
            elif self.RETRIES <= 5:
                performance = "🎯 Excellent!"
            elif self.RETRIES <= 7:
                performance = "👍 Good job!"
            else:
                performance = "😅 You got it!"
            
            result = f"""
✅ {performance}

Guessed in {self.RETRIES} attempts
Time: {int(elapsed_time)} seconds
Score: {final_score}

🎯 Number: {self.TARGET}

━━━━━━━━━━━━━━━━━━━━━━

Created by SEND
Thanks for playing!
            """
            self.update_result(result)
            self.end_game()
            self.update_status("You won!")
        
        self.update_stats()
        self.guessed_number.set("")
        self.number_form.focus_set()
    
    def give_hint(self):
        if not self.game_active or self.RETRIES == 0:
            self.update_result("Make a guess first!")
            return
        
        self.SCORE = max(0, self.SCORE - 100)
        
        hints = [
            f"Number is {'even' if self.TARGET % 2 == 0 else 'odd'}",
            f"Between {max(1, self.TARGET-20)} and {min(200 if self.difficulty.get() == 'hard' else 100 if self.difficulty.get() == 'medium' else 50, self.TARGET+20)}",
            f"Sum of digits: {sum(int(d) for d in str(self.TARGET))}",
            f"{'Greater' if self.TARGET > 50 else 'Less'} than 50" if self.difficulty.get() != 'easy' else f"In {'first' if self.TARGET <= 25 else 'second'} half",
        ]
        
        hint = random.choice(hints)
        self.update_result(f"💡 Hint: {hint}\n\n-100 points")
        self.update_status("Hint used")
        self.update_stats()
    
    def change_difficulty(self):
        if self.game_active:
            if messagebox.askyesno("Change Difficulty", "This will start a new game. Continue?"):
                self.new_game()
    
    def update_result(self, text):
        self.result.config(text=text)
    
    def end_game(self):
        self.game_active = False
        self.guess_button.config(state='disabled', bg='#555555')
        self.hint_button.config(state='disabled', bg='#555555')
        self.number_form.config(state='disabled')
    
    def exit_game(self):
        if messagebox.askyesno("Exit", "Exit the game?\n\nCreated by SEND"):
            self.window.destroy()
    
    def run(self):
        # Center window
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
        
        self.window.mainloop()

# Run the game
if __name__ == "__main__":
    print("Number Guessing Game")
    print("Created by SEND")
    print("Starting...")
    
    game = NumberGuessingGame()
    game.run()