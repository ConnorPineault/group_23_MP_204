

### Sequent 1: \( F → E, E → R |- F → R \)

**Variables:**
- **F (StraightFlush):** Represents a straight flush in the player's hand.
- **E (HighestRank):** Denotes the highest possible hand ranking.
- **R (WinRound):** Indicates a win for the round.

**Description:**
Asserts the logical outcome that a straight flush leads directly to a round win, based on the hierarchy of hand rankings.

### Sequent 2: \( G → T, S → ¬ T |- G → ¬S \)

**Variables:**
- **G (ThreeOfAKind):** Stands for having three of a kind.
- **T (BetterThanStraight):** Represents a hand better than a straight.
- **S (Straight):** Indicates having a straight.

**Description:**
Illustrates that three of a kind is superior to a straight, and thus, a player with three of a kind does not merely have a straight.

### Sequent 3: \( E→ G, F → G, G → (S ∨ R)  |- (E ∨ F) → (S ∨ R) \)

**Variables:**
- **E (StraightFlush):** Indicates a straight flush.
- **F (ThreeOfAKind):** Signifies three of a kind.
- **G (StrongHand):** Represents having a strong hand.
- **S (WinPot):** Stands for winning the pot.
- **R (OpponentStrongHand):** Possibility of an opponent having a strong hand.

**Description:**
Delineates the implication that possessing either a straight flush or three of a kind leads to a high chance of winning, barring an equally strong opponent hand.




