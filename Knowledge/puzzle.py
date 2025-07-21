from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is either a knight or a knave, but not both.
    Biconditional(AKnight, Not(AKnave)),

    # If A is a knight, then what A says is true.
    # If A is a knave, then what A says is false.
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A is either a knight or a knave.
    Biconditional(AKnight, Not(AKnave)),
    # B is either a knight or a knave.
    Biconditional(BKnight, Not(BKnave)),

    # A's statement
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A is either a knight or a knave.
    Biconditional(AKnight, Not(AKnave)),
    # B is either a knight or a knave.
    Biconditional(BKnight, Not(BKnave)),

    # A says we are the same kind (both knights or both knaves)
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),

    # B says we are of different kinds (one knight, one knave)
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Basic structure: each character is a knight or a knave
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(CKnight, Not(CKnave)),

    # C's statement
    Biconditional(CKnight, AKnight),

    # B's statement about C
    Biconditional(BKnight, CKnave),

    # B's statement about what A said.
    # Let's represent "A said 'I am a knave'" with a new proposition.
    # Let's say: BStatementAboutA = Biconditional(AKnight, AKnave)
    # B is a knight if and only if B's statement about A is true.
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),

    # A's statement. A said one of two things.
    # Either A said "I am a knight" OR A said "I am a knave".
    # This means either (AKnight <=> AKnight) is true, or (AKnight <=> AKnave) is true.
    # The first one (AKnight <=> AKnight) is a tautology (always true).
    # The second one is (AKnight <=> Not(AKnight)) which is a contradiction (always false).
    # So A says something that is either True or False.
    # This doesn't constrain A much, but the other statements will.
    # The information from B is more useful.
    # If B is a knight, A said "I am a knave". So (AKnight <=> AKnave) is in our KB.
    # If B is a knave, A did NOT say "I am a knave". Since A said one of two things, A must have said "I am a knight". So (AKnight <=> AKnight) is in our KB.
    # This can be encoded as:
    Biconditional(BKnight, Biconditional(AKnight, AKnave))
    # This is actually redundant with the previous statement from B, but keeping it makes the logic clearer.

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
