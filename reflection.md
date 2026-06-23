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
|---------------------|------------------------|----------------------------|------------------------|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I used Claude for file refactoring, bug fixing, and project strategy.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

 Claude correctly identified the inverted hint strings in check_guess(). It suggested returning "Too High" /  "Go lower" when guess > secret. I verified the fix by running my pytest.

- Did AI help you design or understand any tests? How?

Claude wrote a test expecting check_guess() to return ("Correct, You got it!"), forgetting the underlying code it migrated actually returned ("Win, Correct!"). This caused a test failure. I caught the mismatch via the pytest log and manually aligned the code with the test.

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

