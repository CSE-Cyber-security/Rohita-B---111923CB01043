# Rohita-B---111923CB01043

# Password Strength Checker

A beginner-friendly Python command-line project that evaluates a **sample password** against five basic security rules. It is designed to practise Python strings, conditional statements, loops, functions, and Git/GitHub version control.


## Features

- Checks whether the password has at least 8 characters.
- Checks for at least one uppercase letter (`A-Z`).
- Checks for at least one lowercase letter (`a-z`).
- Checks for at least one digit (`0-9`).
- Checks for at least one special character (such as `@`, `#`, `$`, or `!`).
- Displays each rule as **Satisfied** or **Not satisfied**.
- Classifies the result as **STRONG**, **MODERATE**, or **WEAK**.
- Lets the user check multiple sample passwords in one run.

## Requirements

- Python 3.8 or newer
- A terminal, Command Prompt, PowerShell, or VS Code terminal
- No third-party packages required

## Project files

```text
Password-Strength-Checker/
├── password_checker.py
├── README.md
└── screenshots/
    
```

## How to run

1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the VS code or project folder.
4. Run:

   ```bash
   python password_checker.py
   ```

   On some systems, use `python3 password_checker.py` instead.

5. Enter made-up sample passwords to test the different outcomes. Type `exit` to quit.

## Rules and classification

| Rule | Requirement |
|---|---|
| Length | At least 8 characters |
| Uppercase | At least one uppercase letter |
| Lowercase | At least one lowercase letter |
| Number | At least one digit |
| Symbol | At least one special character |

- **STRONG:** all 5 rules pass
- **MODERATE:** 3 or 4 rules pass
- **WEAK:** 0, 1, or 2 rules pass

This simple score is only a learning exercise. It does not check leaked passwords, password reuse, entropy, or resistance to modern cracking methods. A result of “STRONG” does not guarantee that a password is safe.

## Example test cases

Use these only as examples; do not use them as actual account passwords.

| Sample input | Expected result | Reason |
|---|---|---|
| `Rohita@123` | STRONG | All five rules pass |
| `Rohi12345` | MODERATE | No special character |
| `rohita` | WEAK | Length and lowercase pass; other rules fail |

## Example output

```text
==================================
     PASSWORD STRENGTH CHECKER
==================================
Educational demo only. Do not enter a real password.
Type 'exit' to quit.

Enter a sample password: Hello@123

Password Analysis:
  ✓ Length (at least 8 characters): Satisfied
  ✓ Uppercase letter (A-Z): Satisfied
  ✓ Lowercase letter (a-z): Satisfied
  ✓ Number (0-9): Satisfied
  ✓ Special character: Satisfied

Password Strength: STRONG
```

## Concepts demonstrated

- Python functions
- Strings and character checks
- Boolean conditions
- Loops and user input
- Counting satisfied rules



