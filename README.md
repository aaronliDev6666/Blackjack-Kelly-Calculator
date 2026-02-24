# Blackjack Kelly Calculator

**Overview**  
A simple command-line tool that estimates Kelly bet fractions for Blackjack hands. The program combines correct Ace handling, a base win-rate table by player total, and a Hi‑Lo true count adjustment to estimate player edge. It prints both full Kelly and half‑Kelly percentages.

**Features**
- Correct Ace handling (Ace counts as 1 or 11 as appropriate).  
- Detects natural Blackjack (A + 10/J/Q/K) and applies 3:2 payout.  
- Base win-rate by hand total with Hi‑Lo true count correction.  
- Interactive loop for repeated inputs.  
- Console output includes: hand total, running count, true count, estimated edge, and Kelly fractions.

**Usage**
1. Clone the repository.  
2. Run with Python 3:
   ```bash
   python3 blackjack_kelly.py
3. Enter cards separated by spaces (e.g. a a 3 4, a 10, q q q).
4. Type exit to quit.

**Configuration**
- DEFAULTDECKSREMAINING: default decks remaining in the shoe (adjust to match table).
- TRUECOUNTEDGEPERPOINT: edge per true count point (default 0.005 = 0.5%).
- MAXWINRATE: cap for estimated win rate (default 0.99).
