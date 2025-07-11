# Destroyer of Numbers
**DON** (Destroyer of Numbers) is a fun and challenging number-fighting game played in the terminal. The player enters their name and takes on the role of DON — a hero of the letter-kind — who must defeat enemy numbers in 20 intense rounds to save the world!

## 🎮 Game Overview

DON must fight and consume enemy numbers lower than or equal to his **Life Score**. The game progresses through 20 levels of increasing difficulty. If he survives all 20 chances, he wins. If not, the numbers win!

---

## How to Play

1. Enter your name at the start of the game.
2. A random **Life Score** (1–50) is assigned to you at the beginning.
3. You get 20 attempts to defeat enemy numbers.
4. At each attempt:
   - You're shown **5 random numbers**.
   - Choose **one** from them to fight.
   - If it's ≤ your Life Score: You defeat it and add its value to your Life Score.
   - If it's > your Life Score: You die.
   - If you choose a number **not shown** or enter invalid input: Game ends immediately.

---

## Game Difficulty

The number ranges increase as the game progresses:

| Attempts | Enemy Number Range |
|----------|--------------------|
| 1–5      | 15–100             |
| 6–10     | 250–2000           |
| 11–15    | 3000–10000         |
| 16–20    | 20000–100000       |

---

## Game Logs

- After each session, a game report is saved automatically.
- File name format: `YYYY_MM_DD_HH_MM_SS_random.txt`
  - Example: `2025_06_07_14_30_21_4821.txt`
- It stores:
  - Player name
  - Attempts made
  - Final Life Score
  - Game outcome

---

## How to Run

1. Make sure you have Python 3 installed.
2. Open terminal or command prompt.
3. Run the script:
   ```bash
   python Main.py
Example Gameplay
plaintext
Copy
Edit
Player name: Anshaff
Attempt: 1
Nishan's life score is: 30
69 94 60 84 19
Select a number to fight: 19
Nishan killed 19

Attempt: 2
Anshaff's life score is: 49
43 98 69 94 95
Select a number to fight: 43
Nishan killed 43
...
