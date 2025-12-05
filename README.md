<!-- # Guessing-Number-Game-in-Python
This is Game simple and make in Python and GUI Python -->

# 🎯 Ultimate Number Guessing Game

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A modern, feature-rich number guessing game built with Python's Tkinter library. Test your guessing skills with multiple difficulty levels, hints, and scoring system!

![Game Screenshot](https://via.placeholder.com/800x400/0a192f/64ffda?text=Ultimate+Number+Guessing+Game+Screenshot)

## ✨ Features

### 🎮 **Gameplay Features**
- **Multiple Difficulty Levels**: Easy (1-50), Medium (1-100), Hard (1-200)
- **Smart Scoring System**: Start with 1000 points, deduct for hints and attempts
- **Time Bonus**: Faster guesses earn bonus points
- **Hot/Cold Indicators**: Visual feedback on how close your guess is
- **Multiple Hint Types**: Get strategic hints (costs points)
- **Progress Tracking**: Visual progress bar with color coding
- **Best Score Tracking**: Keep track of your highest achievement

### 🎨 **UI/UX Features**
- **Modern Dark Theme**: Eye-friendly color scheme
- **Responsive Design**: Centered window with proper scaling
- **Emoji Visuals**: Engaging visual feedback
- **Real-time Stats**: Live score, attempts, and timer
- **Status Bar**: Current game status updates
- **Intuitive Controls**: Well-organized button layout

### 🎯 **Game Controls**
- **New Game**: Start fresh with new number
- **Reset Game**: Reset current game with new number
- **Quit Current Game**: End current game mid-session
- **Get Hint**: Receive strategic hint (costs 100 points)
- **Exit App**: Close the application

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Tkinter (usually comes with Python)

### Quick Start
1. Clone or download the repository
2. Run the game:
```bash
python number_guessing_game.py
```
## 🎮 How to Play
### Basic Rules
1. Click "NEW GAME" to start
2. Select your preferred difficulty level
3. Enter your guess in the input box
4. Click "GUESS" or press Enter
5. Use hints strategically (they cost points!)
6. Try to guess the number in the fewest attempts

### Scoring System
- Starting Score: 1000 points
- Each Wrong Guess: -50 points
- Each Hint Used: -100 points
- Time Bonus: Up to 500 points for fast completion
- Best Score: Tracks your highest score

### Difficulty Levels
Level	Range	Max Attempts
Easy	1-50	8
Medium	1-100	10
Hard	1-200	12

## 🎨 Interface Guide
### Main Components
1. Title Bar: Game title and best score
2. Stats Panel: Current score, attempts, timer
3. Input Area: Number input and guess button
4. Action Buttons: Reset and Quit current game
5. Result Display: Game feedback and hints
6. Progress Bar: Visual attempt counter
7. Control Panel: New Game, Hint, Exit buttons
8. Difficulty Selector: Choose game difficulty
9. Status Bar: Real-time game status

### Button Functions
Button	             Icon	Function
New Game	          🆕	Start completely new game
Guess   	          🚀	Submit your number guess
Reset Game	          🔄	Reset current game with new number
Quit Current Game	  ⏹️	End current game session
Get Hint	          💡	Receive strategic hint (costs points)
Exit App	          🚪	Close application

## 📊 Game Features in Detail
### Hot/Cold System
🔥 Very Hot: Within 5 numbers

♨️ Hot: Within 15 numbers

🌤️ Warm: Within 30 numbers

❄️ Cold: More than 30 numbers away

### Hint System
The game provides 4 types of hints:
1. Even/Odd number hint
2. Range hint (±20 from target)
3. Sum of digits hint
4. Half-range hint

### Progress Visualization
- Green Bar: Good progress (0-60% attempts used)
- Yellow Bar: Caution (60-80% attempts used)
- Red Bar: Critical (80-100% attempts used)

## 🛠️ Technical Details
File Structure
number_guessing_game.py  # Main game file
README.md                # This documentation

### Dependencies
- Python 3.8+
- Tkinter (built-in)
- No external packages required

### Code Structure
NumberGuessingGame Class
├── __init__()          # Initialize game and UI
├── setup_ui()          # Create all UI components
├── new_game()          # Start new game
├── reset_game()        # Reset current game
├── quit_current_game() # Quit current game
├── play_game()         # Process guess
├── give_hint()         # Provide hint
├── update_stats()      # Update game statistics
└── update_status()     # Update status bar

## 🎯 Strategies & Tips
### Beginner Strategy
1. Start with Easy difficulty
2. Use the middle number approach (guess 25 for 1-50)
3. Pay attention to hot/cold indicators
4. Save hints for when you're stuck

### Advanced Strategy
1. Use binary search for optimal guessing
2. Track your guesses to narrow down possibilities
3. Use hints strategically when narrowed to small range
4. Balance speed vs accuracy for maximum score

### Scoring Optimization
- Fewer attempts = Higher base score
- Faster completion = Time bonus
- Fewer hints = Less point deduction
- Difficulty multiplier: Hard mode = potential higher scores

## 🔧 Troubleshooting
### Common Issues
1. Game doesn't start: Ensure Python and Tkinter are installed
2. Input not working: Click the input field first
3. Buttons not responding: Check if game is active (status bar)
4. Window too small: Game is designed for minimum 800x600 resolution

### Keyboard Shortcuts
- Enter: Submit guess
- Tab: Navigate between UI elements
- Escape: Focus on input field

## 🤝 Contributing
Feel free to contribute to this project! Here are some ways you can help:

### Feature Ideas
Add sound effects
Implement multiplayer mode
Create achievement system
Add theme selector
Implement save/load game state

### How to Contribute
Fork the repository
Create a feature branch
Make your changes
Test thoroughly
Submit a pull request

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments
Built with Python's Tkinter library
Inspired by classic number guessing games
Thanks to all contributors and testers

## 📊 Performance Metrics
System Requirements
Minimum: Any system running Python 3.8+
Recommended: Modern OS with 4GB RAM
Storage: Less than 1MB required

### Game Statistics
Average Game Time: 2-5 minutes
Optimal Score Range: 500-1500 points
Record Attempts: 3 (minimum possible)

## 🎨 Theme Colors
The game uses a carefully selected dark theme palette:
Background: #0a192f (Dark Blue)
Primary: #64ffda (Cyan)
Secondary: #112240 (Darker Blue)
Text: #ccd6f6 (Light Blue)
Accent: #ff6b6b (Red)
Success: #4ecdc4 (Teal)
Warning: #ffe66d (Yellow)
Reset: #ff9e00 (Orange)
Quit: #ff4757 (Red-Pink)

## 🚀 Quick Start Guide
Installation Steps:
bash
1. Download the game file
2. Open terminal/command prompt
3. Navigate to the folder containing the game python number_guessing_game.py

### First Game Tips:
1. Start with Easy mode to learn the mechanics
2. Read the hot/cold indicators carefully
3. Don't use hints too early - save them for when you're stuck
4. Watch the timer - faster completion gives bonus points

Happy Guessing! 🎯✨

Can you beat the high score? Challenge yourself with harder difficulties and perfect your guessing strategy!
Made with ❤️ using Python and Tkinter