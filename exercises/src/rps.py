class Hand:
    ROCK, SCISSORS, PAPER = "rock", "scissors", "paper"
    table = {
        ROCK: SCISSORS,
        SCISSORS: PAPER,
        PAPER: ROCK
    }

    def __init__(self, kind):
        assert kind in self.table.keys()
        self.kind = kind

    def __str__(self):
        return self.kind.capitalize()

    def __gt__(self, other):
        if self.kind == other.kind:
            return False
        return self.table[self.kind] == other.kind

    def __lt__(self, other):
        if self.kind == other.kind:
            return False
        return self.table[self.kind] != other.kind
    
    def __eq__(self, other):
        return self.kind == other.kind

hand_options = [Hand(Hand.ROCK), Hand(Hand.SCISSORS), Hand(Hand.PAPER)]