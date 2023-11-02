# Project Title

A brief description of what this project does and who it's for.

## Description

This project explores the application of formal logic to the game of 3 Card Poker, using sequents to represent the possible outcomes of the game based on the player's hand.

### Sequent 1: \( F \rightarrow E, E \rightarrow R \vdash F \rightarrow R \)

**Variables:**
- **F (StraightFlush):** Represents a straight flush in the player's hand.
- **E (HighestRank):** Denotes the highest possible hand ranking.
- **R (WinRound):** Indicates a win for the round.

**Description:**
Asserts the logical outcome that a straight flush leads directly to a round win, based on the hierarchy of hand rankings.

### Sequent 2: \( G \rightarrow T, S \rightarrow \neg T \vdash G \rightarrow \neg S \)

**Variables:**
- **G (ThreeOfAKind):** Stands for having three of a kind.
- **T (BetterThanStraight):** Represents a hand better than a straight.
- **S (Straight):** Indicates having a straight.

**Description:**
Illustrates that three of a kind is superior to a straight, and thus, a player with three of a kind does not merely have a straight.

### Sequent 3: \( E \rightarrow G, F \rightarrow G, G \rightarrow (S \lor R) \vdash (E \lor F) \rightarrow (S \lor R) \)

**Variables:**
- **E (StraightFlush):** Indicates a straight flush.
- **F (ThreeOfAKind):** Signifies three of a kind.
- **G (StrongHand):** Represents having a strong hand.
- **S (WinPot):** Stands for winning the pot.
- **R (OpponentStrongHand):** Possibility of an opponent having a strong hand.

**Description:**
Delineates the implication that possessing either a straight flush or three of a kind leads to a high chance of winning, barring an equally strong opponent hand.

## Installation

Provide instructions on how to install and run your project. For example:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
# Further steps...
