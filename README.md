***Blackjack Kelly Calculator***

**Overview**
A command-line tool that estimates Kelly bet fractions for Blackjack hands.  
It combines correct Ace handling, a base win-rate table by player total, and a Hi‑Lo true count adjustment to estimate player edge.  
Outputs both full Kelly and half‑Kelly percentages.

**Features**
- Correct Ace handling (Ace counts as 1 or 11 as appropriate).
- Detects natural Blackjack (A + 10/J/Q/K) and applies 3:2 payout.
- Base win-rate by hand total with Hi‑Lo true count correction.
- Interactive loop for repeated inputs.
- Console output includes: hand total, running count, true count, estimated edge, and Kelly fractions.

**Usage**
1. Clone the repository.
2. Run with Python 3:
   `bash
   python3 blackjack-kelly.py
   `
3. Enter cards separated by spaces (e.g. a a 3 4, a 10, q q q).
4. Type exit to quit.

**Configuration**
- DEFAULTDECKSREMAINING: default decks remaining in the shoe (adjust to match table).
- TRUECOUNTEDGEPERPOINT: edge per true count point (default 0.005 = 0.5%).
- MAXWINRATE: cap for estimated win rate (default 0.99).

**Assumptions and Limitations**
- The base win-rate table and Hi‑Lo correction are simplified heuristics for demonstration and education.  
  They are not a substitute for full Monte Carlo simulation or perfect basic strategy analysis.
- For more accurate estimates, set DEFAULTDECKSREMAINING to the actual shoe size and consider replacing the base table with simulation results.

**Example**
`
Enter hand: a a 3 4
Total: 19
Base win-rate: 56.00%
Running Count: 0, True Count: 0.00
Edge adjustment: 0.000% → Final win-rate: 56.000%
Kelly fraction (full): 12.00%
Kelly fraction (half): 6.00%
`

**Resources**
- Blackjack basic strategy reference (wizardofodds.com in Bing) (bing.com in Bing)
- Kelly criterion explanation (en.wikipedia.org in Bing) (bing.com in Bing)
- Hi-Lo card counting system (en.wikipedia.org in Bing) (bing.com in Bing)

**STATEMENT**
***This repository and its code are strictly for lawful academic exchange and computational study only.  
It must not be used for casino prediction, gambling strategies, or any form of illegal betting activity.  
Any misuse of this code outside educational or research contexts is strictly prohibited.***
