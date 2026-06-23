# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- Hint suggestion is inverted. Instead of higher, it shows lower and vice versa.
- New game button does't start new game
- Normal mode has numbers ranging from 1 to 100 whereas Hard mode only has numbers ranging from 1 to 50
- Number of chances for Normal mode is higher than Easy Mode
- All modes displays guess number between 1 and 100 whereas on side bar, it shows different range for different modes
- Secret cast to string on even attempts breaks comparisons
- Win score double-penalizes attempt number
- Wrong guesses rewarded with +5 points

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input               | Expected Behavior      | Actual Behavior            | Console Output / Error |
|---------------------|------------------------|----------------------------|------------------------|
| Guess 60            | Go Higher              | Go Lower                   | None                   |
| Guess on Attempt #2 | Secret stays a number  | Secret turns into a string | None                   |
| Hard Mode           | Range increases to 200 | Range drops to 1-50        | None                   |

---

## 2. How did you use AI as a teammate?

I used Claude as my primary AI collaborator throughout this project for refactoring,
bug fixing, and designing a test strategy. Claude helped me reorganize scattered game
logic into `logic_utils.py`, making the code easier to test and reason about. I treated
Claude like a pair programmer — I described the problem, reviewed what it produced, and
then ran the code myself to confirm or challenge its suggestions.

One example where Claude was correct: it correctly identified that the hint logic in
`check_guess()` was inverted. The original code was returning "Go LOWER!" when the guess
was too low and "Go HIGHER!" when it was too high. Claude flipped the conditionals so
that `guess > secret` returns `"Too High"` with `"📉 Go LOWER!"` and `guess < secret`
returns `"Too Low"` with `"📈 Go HIGHER!"`. I verified this fix by running `pytest` and
confirming all hint-related assertions passed.

One example where Claude was incorrect: Claude originally wrote a test that expected
`check_guess()` to return `("Correct", "🎉 You got it!")`, but it had forgotten that the
underlying starter code it had migrated still returned `("Win", "🎉 Correct!")`. This
caused a test failure when I ran `pytest` in the terminal. I had to read the failure
output carefully, trace it back to the string mismatch, and correct the return value
myself. This taught me that AI-generated tests need to be treated as drafts, not ground
truth.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided a bug was fixed when it successfully passed both our automated unit tests and manual execution inside the live browser game without crashing or throwing silent errors.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I ran a `pytest` suite in the terminal to verify `check_guess()`. The test failed initially, showing me that our refactored backend logic was returning `("Win, Correct!")` while the test suite expected `("Correct, You got it!")`. This caught a critical string mismatch before deployment.

- Did AI help you design or understand any tests? How?

Yes, Claude generated the initial `pytest` structure for testing the high, low, and correct guess boundaries. When the test failed due to the string mismatch, analyzing Claude's test logs helped me understand exactly where the backend logic deviated from the expected UI behavior.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit is like a script that reruns from the very top every single time you interact with the page (like clicking a button). Because it completely resets on every rerun, "session state" acts like a tiny memory bank that saves variables (like scores or attempts) so they don't get wiped out.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

Keeping AI chats isolated to exactly one file and one specific problem at a time prevents the AI from getting confused and generating broken code.

- What is one thing you would do differently next time you work with AI on a coding task?

I would review the AI's logic line by line before running it, rather than blindly trusting its output, to catch discrepancies like the "Win" vs "Correct" string mismatch earlier.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project showed me that AI code is highly prone to logic mismatches when moving between files. It proved that automated testing is essential to verify that AI generated fixes actually work.

