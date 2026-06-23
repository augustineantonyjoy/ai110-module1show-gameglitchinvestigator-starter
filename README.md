# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

This project is a Streamlit-based number guessing game designed to demonstrate how a decoupled architecture prevents critical state and logic failures. 

Through this project, I identified and resolved several game-breaking bugs:
* **The State Bug:** The secret number was resetting on every interaction because it wasn't properly tracked in Streamlit's session state.
* **Inverted Logic:** The hints were inverted, telling users to guess lower when they needed to guess higher.
* **Type Conversion Error:** On even attempts, the secret number was cast into a string, breaking future numerical comparisons.
* **UI Inconsistencies:** The game logic returned mismatching win strings (`"Win"` vs `"Correct"`) which failed to trigger the UI victory screens.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User launches the app and selects "Normal" mode (Range: 1-100).
2. User enters a guess of 50.
3. Game returns "Too High" and displays the hint "📉 Go LOWER!".
4. User enters a guess of 25.
5. Game returns "Too Low" and displays the hint "📈 Go HIGHER!".
6. User enters a guess of 37.
7. Game returns "Correct", displays "🎉 You got it!", and updates the win score seamlessly.
8. User clicks "New Game" and the game resets with a new secret number.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
