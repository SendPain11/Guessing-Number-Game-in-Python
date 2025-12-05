import tkinter as tk
from tkinter import messagebox, font
import random
import time

class NumberGuessingGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("🎯 Ultimate Number Guessing Game 🎯")
        self.window.geometry("900x700")
        self.window.configure(bg='#0a192f')
        self.window.resizable(True, True)
        
        # Game variables
        self.TARGET = 0
        self.RETRIES = 0
        self.MAX_ATTEMPTS = 10
        self.SCORE = 1000
        self.game_active = False
        self.start_time = 0
        self.best_score = 0
        self.showing_credits = False
        
        # Color scheme
        self.colors = {
            'bg': '#0a192f',
            'primary': '#64ffda',
            'secondary': '#112240',
            'text': '#ccd6f6',
            'accent': '#ff6b6b',
            'success': '#4ecdc4',
            'warning': '#ffe66d',
            'reset': '#ff9e00',
            'quit': '#ff4757',
            'credits': '#9d4edd'
        }
        
        self.setup_ui()
        self.new_game()
    
    def setup_ui(self):
        # Custom fonts
        title_font = font.Font(family='Helvetica', size=28, weight='bold')
        label_font = font.Font(family='Helvetica', size=12)
        button_font = font.Font(family='Helvetica', size=11, weight='bold')
        
        # Header Frame
        header_frame = tk.Frame(self.window, bg=self.colors['bg'])
        header_frame.pack(pady=10)
        
        # Title with emoji
        self.title_label = tk.Label(
            header_frame,
            text="🎮 ULTIMATE NUMBER GUESSING GAME 🎮",
            font=title_font,
            fg=self.colors['primary'],
            bg=self.colors['bg']
        )
        self.title_label.pack()
        
        # Developer Credit
        credit_label = tk.Label(
            header_frame,
            text="Developed by: SEND Studio",
            font=('Helvetica', 10, 'italic'),
            fg=self.colors['primary'],
            bg=self.colors['bg']
        )
        credit_label.pack()
        
        # Version
        version_label = tk.Label(
            header_frame,
            text="Version 1.0.0",
            font=('Helvetica', 9),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        version_label.pack()
        
        # Best Score Display
        self.best_score_label = tk.Label(
            header_frame,
            text="🏆 Best Score: 0",
            font=('Helvetica', 12, 'bold'),
            fg=self.colors['warning'],
            bg=self.colors['bg']
        )
        self.best_score_label.pack(pady=5)
        
        # Stats Frame
        stats_frame = tk.Frame(self.window, bg=self.colors['secondary'], relief=tk.RAISED, bd=2)
        stats_frame.pack(pady=10, padx=20, fill='x')
        
        # Stats labels
        self.stats_text = tk.Label(
            stats_frame,
            text="",
            font=('Helvetica', 11, 'bold'),
            fg=self.colors['warning'],
            bg=self.colors['secondary'],
            justify=tk.LEFT
        )
        self.stats_text.pack(pady=8, padx=10)
        
        # Game Area Frame
        game_frame = tk.Frame(self.window, bg=self.colors['bg'])
        game_frame.pack(pady=15)
        
        # Input Frame
        input_frame = tk.Frame(game_frame, bg=self.colors['bg'])
        input_frame.pack(pady=10)
        
        # Entry with placeholder effect
        self.guessed_number = tk.StringVar()
        self.number_form = tk.Entry(
            input_frame,
            textvariable=self.guessed_number,
            font=('Helvetica', 16, 'bold'),
            width=15,
            justify='center',
            bd=3,
            relief=tk.SUNKEN,
            bg='#1e3a5f',
            fg=self.colors['primary'],
            insertbackground=self.colors['primary']
        )
        self.number_form.pack(side=tk.LEFT, padx=5)
        
        # Guess Button
        self.guess_button = tk.Button(
            input_frame,
            text="🚀 GUESS",
            font=button_font,
            command=self.play_game,
            bg=self.colors['primary'],
            fg='black',
            activebackground='#52d1b4',
            activeforeground='black',
            padx=20,
            pady=8,
            bd=0,
            cursor='hand2',
            state='disabled'
        )
        self.guess_button.pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key
        self.number_form.bind('<Return>', lambda event: self.play_game())
        
        # Action Buttons Frame (di tengah)
        action_frame = tk.Frame(game_frame, bg=self.colors['bg'])
        action_frame.pack(pady=15)
        
        # Reset Game Button
        self.reset_button = tk.Button(
            action_frame,
            text="🔄 RESET GAME",
            font=button_font,
            command=self.reset_game,
            bg=self.colors['reset'],
            fg='black',
            activebackground='#e68a00',
            activeforeground='black',
            padx=20,
            pady=8,
            bd=0,
            cursor='hand2',
            state='normal'
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        # Quit Current Game Button
        self.quit_button = tk.Button(
            action_frame,
            text="⏹️ QUIT GAME",
            font=button_font,
            command=self.quit_current_game,
            bg=self.colors['quit'],
            fg='white',
            activebackground='#ff2e43',
            activeforeground='white',
            padx=20,
            pady=8,
            bd=0,
            cursor='hand2',
            state='normal'
        )
        self.quit_button.pack(side=tk.LEFT, padx=10)
        
        # Credits Button
        self.credits_button = tk.Button(
            action_frame,
            text="⭐ CREDITS",
            font=button_font,
            command=self.show_credits,
            bg=self.colors['credits'],
            fg='white',
            activebackground='#8a2be2',
            activeforeground='white',
            padx=20,
            pady=8,
            bd=0,
            cursor='hand2',
            state='normal'
        )
        self.credits_button.pack(side=tk.LEFT, padx=10)
        
        # Result Display
        result_frame = tk.Frame(self.window, bg=self.colors['secondary'], relief=tk.GROOVE, bd=3)
        result_frame.pack(pady=15, padx=30, fill='both', expand=True)
        
        self.result = tk.Label(
            result_frame,
            text="Welcome! Click 'New Game' to start!",
            font=('Helvetica', 12),
            fg=self.colors['text'],
            bg=self.colors['secondary'],
            wraplength=650,
            justify=tk.CENTER,
            pady=20
        )
        self.result.pack(expand=True, fill='both')
        
        # Progress Bar Frame
        self.progress_frame = tk.Frame(self.window, bg=self.colors['bg'])
        self.progress_frame.pack(pady=10, padx=40, fill='x')
        
        self.progress_label = tk.Label(
            self.progress_frame,
            text="Attempts: 0/10",
            font=('Helvetica', 10),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        self.progress_label.pack()
        
        self.progress_bar = tk.Canvas(
            self.progress_frame,
            width=400,
            height=15,
            bg='#1e3a5f',
            highlightthickness=0
        )
        self.progress_bar.pack(pady=5)
        self.progress_rect = self.progress_bar.create_rectangle(0, 0, 0, 15, fill=self.colors['success'], width=0)
        
        # Control Buttons Frame (bawah)
        control_frame = tk.Frame(self.window, bg=self.colors['bg'])
        control_frame.pack(pady=15)
        
        # New Game Button
        self.play_button = tk.Button(
            control_frame,
            text="🆕 NEW GAME",
            font=button_font,
            command=self.new_game,
            bg=self.colors['success'],
            fg='black',
            activebackground='#3da89d',
            activeforeground='black',
            padx=25,
            pady=10,
            bd=0,
            cursor='hand2'
        )
        self.play_button.pack(side=tk.LEFT, padx=10)
        
        # Hint Button
        self.hint_button = tk.Button(
            control_frame,
            text="💡 GET HINT",
            font=button_font,
            command=self.give_hint,
            bg='#6c5ce7',
            fg='white',
            activebackground='#5a4fcf',
            activeforeground='white',
            padx=25,
            pady=10,
            bd=0,
            cursor='hand2',
            state='disabled'
        )
        self.hint_button.pack(side=tk.LEFT, padx=10)
        
        # Exit Application Button
        self.exit_button = tk.Button(
            control_frame,
            text="🚪 EXIT APP",
            font=button_font,
            command=self.exit_game,
            bg=self.colors['accent'],
            fg='white',
            activebackground='#e05555',
            activeforeground='white',
            padx=25,
            pady=10,
            bd=0,
            cursor='hand2'
        )
        self.exit_button.pack(side=tk.LEFT, padx=10)
        
        # Difficulty selector
        diff_frame = tk.Frame(self.window, bg=self.colors['bg'])
        diff_frame.pack(pady=10)
        
        tk.Label(
            diff_frame,
            text="Difficulty:",
            font=('Helvetica', 10),
            fg=self.colors['text'],
            bg=self.colors['bg']
        ).pack(side=tk.LEFT, padx=5)
        
        self.difficulty = tk.StringVar(value="medium")
        difficulties = [("Easy (1-50)", "easy"), ("Medium (1-100)", "medium"), ("Hard (1-200)", "hard")]
        
        for text, mode in difficulties:
            tk.Radiobutton(
                diff_frame,
                text=text,
                variable=self.difficulty,
                value=mode,
                command=self.change_difficulty,
                font=('Helvetica', 9),
                fg=self.colors['text'],
                bg=self.colors['bg'],
                selectcolor=self.colors['secondary'],
                activebackground=self.colors['bg']
            ).pack(side=tk.LEFT, padx=5)
        
        # Status Bar
        self.status_bar = tk.Label(
            self.window,
            text="🎮 Ultimate Number Guessing Game - Developed by SEND Studio",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            font=('Helvetica', 9),
            fg=self.colors['text'],
            bg=self.colors['secondary']
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Splash Screen on Start
        self.show_splash_screen()
    
    def show_splash_screen(self):
        """Show splash screen with developer info"""
        splash_text = """
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║      🎮 ULTIMATE NUMBER GUESSING GAME 🎮                ║
║                                                          ║
║                Developed by:                             ║
║                                                          ║
║              ███████ ███████ ███    ██ ██████           ║
║              ██      ██      ████   ██ ██   ██          ║
║              ███████ █████   ██ ██  ██ ██   ██          ║
║                   ██ ██      ██  ██ ██ ██   ██          ║
║              ███████ ███████ ██   ████ ██████           ║
║                                                          ║
║                    S T U D I O                           ║
║                                                          ║
║           Version 1.0.0 • © 2024 All Rights Reserved     ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

Press any key or click to continue...
        """
        self.update_result(splash_text)
        self.update_status("Welcome to Ultimate Number Guessing Game!")
        
        # Bind click or keypress to start
        self.window.bind('<Button-1>', self.clear_splash)
        self.window.bind('<Key>', self.clear_splash)
    
    def clear_splash(self, event=None):
        """Clear splash screen"""
        self.window.unbind('<Button-1>')
        self.window.unbind('<Key>')
        self.update_result("Welcome! Click 'New Game' to start!")
        self.update_status("Ready to play!")
    
    def show_credits(self):
        """Show game credits"""
        credits_text = """
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║                    🏆 GAME CREDITS 🏆                    ║
║                                                          ║
║  ███████╗███████╗███╗   ██╗██████╗      ██████╗███████╗ ║
║  ██╔════╝██╔════╝████╗  ██║██╔══██╗    ██╔════╝██╔════╝ ║
║  ███████╗█████╗  ██╔██╗ ██║██║  ██║    ██║     █████╗   ║
║  ╚════██║██╔══╝  ██║╚██╗██║██║  ██║    ██║     ██╔══╝   ║
║  ███████║███████╗██║ ╚████║██████╔╝    ╚██████╗███████╗ ║
║  ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝      ╚═════╝╚══════╝ ║
║                                                          ║
║                   ULTIMATE NUMBER                        ║
║                   GUESSING GAME                          ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  🎮 GAME DESIGN & DEVELOPMENT:                          ║
║     • SEND Studio                                        ║
║     • Lead Developer: [Your Name Here]                   ║
║                                                          ║
║  🎨 GRAPHICS & UI DESIGN:                               ║
║     • SEND Creative Team                                 ║
║                                                          ║
║  🔧 PROGRAMMING:                                        ║
║     • Python 3                                          ║
║     • Tkinter GUI Framework                             ║
║                                                          ║
║  🎵 SPECIAL THANKS TO:                                  ║
║     • Python Community                                  ║
║     • Tkinter Developers                                ║
║     • All Beta Testers                                  ║
║                                                          ║
║  📅 RELEASE DATE:                                       ║
║     • Version 1.0.0 - 2024                              ║
║                                                          ║
║  © 2024 SEND Studio. All Rights Reserved.               ║
║                                                          ║
║  "Creating fun experiences, one game at a time!"        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

Click anywhere or press any key to return to game...
        """
        self.showing_credits = True
        self.update_result(credits_text)
        self.update_status("Viewing Credits - Click to return")
        
        # Bind to return to game
        self.window.bind('<Button-1>', self.return_from_credits)
        self.window.bind('<Key>', self.return_from_credits)
    
    def return_from_credits(self, event=None):
        """Return from credits screen"""
        if self.showing_credits:
            self.window.unbind('<Button-1>')
            self.window.unbind('<Key>')
            self.showing_credits = False
            if self.game_active:
                self.update_result("Game in progress! Make your next guess!")
                self.update_status("Game resumed")
            else:
                self.update_result("Welcome! Click 'New Game' to start!")
                self.update_status("Ready to play!")
    
    def update_status(self, message):
        """Update status bar message"""
        self.status_bar.config(text=f"🎮 {message}")
    
    def update_stats(self):
        elapsed_time = time.time() - self.start_time if self.game_active else 0
        stats = f"🎯 Score: {self.SCORE} | 🔄 Attempts: {self.RETRIES}/{self.MAX_ATTEMPTS} | ⏱️ Time: {int(elapsed_time)}s"
        self.stats_text.config(text=stats)
        
        # Update progress bar
        progress_width = (self.RETRIES / self.MAX_ATTEMPTS) * 400
        self.progress_bar.coords(self.progress_rect, 0, 0, progress_width, 15)
        
        # Change color based on attempts left
        if self.RETRIES >= self.MAX_ATTEMPTS * 0.8:
            self.progress_bar.itemconfig(self.progress_rect, fill=self.colors['accent'])
        elif self.RETRIES >= self.MAX_ATTEMPTS * 0.6:
            self.progress_bar.itemconfig(self.progress_rect, fill=self.colors['warning'])
        else:
            self.progress_bar.itemconfig(self.progress_rect, fill=self.colors['success'])
        
        self.progress_label.config(text=f"Attempts: {self.RETRIES}/{self.MAX_ATTEMPTS}")
    
    def new_game(self):
        """Start a completely new game"""
        self.game_active = True
        self.RETRIES = 0
        self.SCORE = 1000
        self.start_time = time.time()
        
        # Set range based on difficulty
        if self.difficulty.get() == "easy":
            self.TARGET = random.randint(1, 50)
            self.MAX_ATTEMPTS = 8
        elif self.difficulty.get() == "medium":
            self.TARGET = random.randint(1, 100)
            self.MAX_ATTEMPTS = 10
        else:  # hard
            self.TARGET = random.randint(1, 200)
            self.MAX_ATTEMPTS = 12
        
        # Enable/Disable buttons
        self.guess_button.config(state='normal', bg=self.colors['primary'])
        self.hint_button.config(state='normal', bg='#6c5ce7')
        self.number_form.config(state='normal')
        self.reset_button.config(state='normal', bg=self.colors['reset'])
        self.quit_button.config(state='normal', bg=self.colors['quit'])
        self.credits_button.config(state='normal', bg=self.colors['credits'])
        
        self.guessed_number.set("")
        self.update_result("🎮 New Game Started! \nGuess the number! 🔢\n\n💡 Tip: Start with the middle number")
        self.update_stats()
        self.update_status("New game started! Make your first guess.")
        
        # Focus on entry
        self.number_form.focus_set()
    
    def reset_game(self):
        """Reset current game in the middle"""
        if not self.game_active:
            return
            
        response = messagebox.askyesno(
            "Reset Game - SEND Studio", 
            "Are you sure you want to reset the current game?\n\n" +
            f"Current Attempts: {self.RETRIES}\n" +
            f"Current Score: {self.SCORE}\n\n" +
            "This will generate a new number but keep your settings."
        )
        
        if response:
            self.RETRIES = 0
            self.SCORE = 1000
            self.start_time = time.time()
            
            # Generate new target number
            if self.difficulty.get() == "easy":
                self.TARGET = random.randint(1, 50)
            elif self.difficulty.get() == "medium":
                self.TARGET = random.randint(1, 100)
            else:
                self.TARGET = random.randint(1, 200)
            
            self.guessed_number.set("")
            self.update_result("🔄 Game Reset!\n\nNew number generated!\nMake your first guess! 🔢")
            self.update_stats()
            self.update_status("Game reset! New number generated.")
            
            # Enable buttons if they were disabled
            self.guess_button.config(state='normal', bg=self.colors['primary'])
            self.hint_button.config(state='normal', bg='#6c5ce7')
            
            # Focus on entry
            self.number_form.focus_set()
    
    def quit_current_game(self):
        """Quit current game in the middle"""
        if not self.game_active:
            return
            
        response = messagebox.askyesno(
            "Quit Current Game - SEND Studio", 
            "Are you sure you want to quit the current game?\n\n" +
            f"Attempts made: {self.RETRIES}\n" +
            f"Current Score: {self.SCORE}\n\n" +
            "This will end the current game and you'll need to start a new one."
        )
        
        if response:
            self.end_game()
            self.update_result(f"⏹️ Game Quit!\n\nYou quit after {self.RETRIES} attempts.\n" +
                             f"Final Score: {self.SCORE}\n" +
                             f"The number was: {self.TARGET}\n\n" +
                             "Click 'New Game' to play again!")
            self.update_status("Current game ended. Click 'New Game' to start again.")
    
    def play_game(self):
        if not self.game_active:
            self.update_status("Game not active. Start a new game first!")
            return
        
        try:
            choice = int(self.number_form.get())
            
            # Validate input
            max_range = 200 if self.difficulty.get() == "hard" else 100 if self.difficulty.get() == "medium" else 50
            if choice < 1 or choice > max_range:
                self.update_result(f"⚠️ Please enter a number between 1 and {max_range}!")
                self.update_status(f"Invalid input! Enter number 1-{max_range}")
                return
                
        except ValueError:
            self.update_result("⚠️ Please enter a valid number!")
            self.update_status("Invalid input! Enter a number")
            return
        
        self.RETRIES += 1
        self.SCORE = max(0, self.SCORE - 50)  # Deduct points for each attempt
        
        if choice != self.TARGET:
            difference = abs(self.TARGET - choice)
            
            # Give different hints based on how close
            if difference <= 5:
                hint_text = "🔥 Very Hot!"
                color = self.colors['accent']
            elif difference <= 15:
                hint_text = "♨️ Hot!"
                color = '#ff9966'
            elif difference <= 30:
                hint_text = "🌤️ Warm"
                color = '#ffcc00'
            else:
                hint_text = "❄️ Cold"
                color = '#6699ff'
            
            if self.TARGET < choice:
                direction = "📉 LOWER"
            else:
                direction = "📈 HIGHER"
            
            result = f"❌ Wrong Guess! Attempt #{self.RETRIES}\n\n"
            result += f"{hint_text} - Go {direction}\n"
            result += f"Difference: {difference}\n\n"
            
            if self.RETRIES >= self.MAX_ATTEMPTS:
                result += f"💔 Game Over! The number was {self.TARGET}\n"
                result += "Click 'New Game' to try again!"
                self.end_game()
                self.update_status("Game over! Maximum attempts reached.")
            else:
                result += f"You have {self.MAX_ATTEMPTS - self.RETRIES} attempts left"
                self.update_status(f"Attempt {self.RETRIES}: Wrong! Try again. {self.MAX_ATTEMPTS - self.RETRIES} attempts left.")
                
            self.update_result(result)
            
        else:
            elapsed_time = time.time() - self.start_time
            time_bonus = max(0, 500 - int(elapsed_time * 5))
            final_score = self.SCORE + time_bonus
            
            # Update best score
            if final_score > self.best_score:
                self.best_score = final_score
                self.best_score_label.config(text=f"🏆 Best Score: {self.best_score}")
            
            # Determine performance
            if self.RETRIES <= 3:
                performance = "🌟 LEGENDARY!"
                developer_note = "\n\n👑 You're a true number master!"
            elif self.RETRIES <= 5:
                performance = "🎯 EXCELLENT!"
                developer_note = "\n\n👍 Impressive skills!"
            elif self.RETRIES <= 7:
                performance = "👍 GOOD JOB!"
                developer_note = "\n\n😊 Well played!"
            else:
                performance = "😅 FINALLY!"
                developer_note = "\n\n💪 Persistence pays off!"
            
            result = f"""
✅ {performance} You guessed it in {self.RETRIES} {'attempt' if self.RETRIES == 1 else 'attempts'}!

⏱️ Time: {int(elapsed_time)} seconds
🏆 Score: {final_score} 
   (Base: {self.SCORE} + Time Bonus: {time_bonus})

🎯 The number was {self.TARGET}
{developer_note}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔄 Click 'New Game' to play again!
⭐ Check out 'CREDITS' for more info!
            """
            self.update_result(result)
            self.end_game()
            self.update_status(f"Congratulations! You won with score: {final_score}!")
            
            # Show victory message with developer credit
            victory_window = tk.Toplevel(self.window)
            victory_window.title("🎉 Victory! - SEND Studio")
            victory_window.geometry("400x300")
            victory_window.configure(bg=self.colors['bg'])
            victory_window.resizable(False, False)
            
            # Center the victory window
            victory_window.update_idletasks()
            width = victory_window.winfo_width()
            height = victory_window.winfo_height()
            x = (victory_window.winfo_screenwidth() // 2) - (width // 2)
            y = (victory_window.winfo_screenheight() // 2) - (height // 2)
            victory_window.geometry(f'{width}x{height}+{x}+{y}')
            
            # Victory message
            tk.Label(
                victory_window,
                text="🎉 VICTORY! 🎉",
                font=('Helvetica', 20, 'bold'),
                fg=self.colors['primary'],
                bg=self.colors['bg']
            ).pack(pady=20)
            
            tk.Label(
                victory_window,
                text=f"You scored: {final_score} points!",
                font=('Helvetica', 14),
                fg=self.colors['text'],
                bg=self.colors['bg']
            ).pack(pady=10)
            
            tk.Label(
                victory_window,
                text="Thank you for playing!",
                font=('Helvetica', 12),
                fg=self.colors['warning'],
                bg=self.colors['bg']
            ).pack(pady=10)
            
            tk.Label(
                victory_window,
                text="Developed by SEND Studio",
                font=('Helvetica', 10, 'italic'),
                fg=self.colors['primary'],
                bg=self.colors['bg']
            ).pack(pady=20)
            
            # Close button
            tk.Button(
                victory_window,
                text="Close",
                font=('Helvetica', 10, 'bold'),
                command=victory_window.destroy,
                bg=self.colors['success'],
                fg='black',
                padx=20,
                pady=5
            ).pack(pady=10)
        
        self.update_stats()
        self.guessed_number.set("")
        self.number_form.focus_set()
    
    def give_hint(self):
        if not self.game_active or self.RETRIES == 0:
            self.update_result("Make at least one guess to get a hint!")
            self.update_status("Make a guess first to get a hint!")
            return
        
        self.SCORE = max(0, self.SCORE - 100)  # Deduct points for hint
        
        hints = [
            f"The number is {'even' if self.TARGET % 2 == 0 else 'odd'}",
            f"The number is between {max(1, self.TARGET-20)} and {min(200 if self.difficulty.get() == 'hard' else 100 if self.difficulty.get() == 'medium' else 50, self.TARGET+20)}",
            f"The sum of digits is {sum(int(digit) for digit in str(self.TARGET))}",
            f"The number is {'greater' if self.TARGET > 50 else 'less'} than 50" if self.difficulty.get() != 'easy' else "The number is in the " + ("first" if self.TARGET <= 25 else "second") + " half",
        ]
        
        hint = random.choice(hints)
        self.update_result(f"💡 HINT: {hint}\n\n⚠️ Score reduced by 100 points!\n\nBrought to you by SEND Studio")
        self.update_status("Hint used! 100 points deducted.")
        self.update_stats()
    
    def change_difficulty(self):
        if self.game_active:
            if messagebox.askyesno("Change Difficulty - SEND Studio", "Changing difficulty will start a new game. Continue?"):
                self.new_game()
    
    def update_result(self, text):
        self.result.config(text=text)
    
    def end_game(self):
        self.game_active = False
        self.guess_button.config(state='disabled', bg='#555555')
        self.hint_button.config(state='disabled', bg='#555555')
        self.number_form.config(state='disabled')
        self.reset_button.config(state='disabled', bg='#555555')
        self.quit_button.config(state='disabled', bg='#555555')
        self.credits_button.config(state='normal', bg=self.colors['credits'])  # Keep credits enabled
    
    def exit_game(self):
        response = messagebox.askyesno(
            "Exit Game - SEND Studio", 
            "Are you sure you want to exit the game?\n\n" +
            "Thank you for playing Ultimate Number Guessing Game!\n" +
            "Developed by SEND Studio\n\n" +
            "Come back soon! 🎮"
        )
        
        if response:
            # Show goodbye message
            goodbye_text = """
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║              Thank You For Playing!                      ║
║                                                          ║
║         🎮 Ultimate Number Guessing Game 🎮             ║
║                                                          ║
║               Developed by SEND Studio                   ║
║                                                          ║
║          © 2024 All Rights Reserved                      ║
║                                                          ║
║    "Creating fun experiences, one game at a time!"       ║
║                                                          ║
║                  See you next time! 👋                   ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
            """
            self.update_result(goodbye_text)
            self.update_status("Exiting game... Thank you for playing!")
            self.window.after(2000, self.window.destroy)  # Close after 2 seconds
    
    def run(self):
        # Center window on screen
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
        
        self.window.mainloop()

# Run the game
if __name__ == "__main__":
    print("=" * 60)
    print("ULTIMATE NUMBER GUESSING GAME")
    print("Developed by: SEND Studio")
    print("Version: 1.0.0")
    print("=" * 60)
    print("Starting game...")
    
    game = NumberGuessingGame()
    game.run()