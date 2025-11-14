# Math Professor

A Python program that generates simple math problems for students to practice their arithmetic skills. The program adapts to different difficulty levels and provides immediate feedback on answers.

## Features

- **Three Difficulty Levels**:
  - Level 1: Single-digit numbers (0-9)
  - Level 2: Two-digit numbers (10-99)
  - Level 3: Three-digit numbers (100-999)

- **Smart Retry System**: Each problem allows up to 3 attempts
- **Immediate Feedback**: Displays "EEE" for incorrect answers
- **Answer Reveal**: Shows correct answer after 3 failed attempts
- **Score Tracking**: Calculates and displays final score out of 10 problems

## How It Works

1. **Level Selection**: User chooses difficulty level (1, 2, or 3)
2. **Problem Generation**: Program creates 10 random addition problems
3. **Answer Validation**: 
   - Correct answer: +1 point, move to next problem
   - Incorrect answer: Display "EEE" and allow retry (up to 3 times)
   - After 3 failures: Show correct answer and continue
4. **Score Display**: Final score shown after all 10 problems

## Example Usage
Level: 2
17 + 42 = 59
Correct!
23 + 15 = 30
EEE
23 + 15 = 35
EEE
23 + 15 = 38
EEE
23 + 15 = 38
... (continues for 10 problems)
Score: 7

## Requirements

- Python 3.x
- Standard library modules: `random`

## Installation & Execution

1. Save the program as `professor.py`
2. Run from terminal:
   ```bash
   python professor.py
## Educational Value

This program helps students:

- **Practice mental math and arithmetic skills**

- **Learn from mistakes with immediate feedback**

- **Build confidence through progressive difficulty levels**

- **Develop persistence with the retry system**

## Error Handling

- **Invalid level inputs are rejected with reprompt**

- **Non-numeric math answers show "EEE" message**

- **Program gracefully handles unexpected user input**
