from enum import Enum


class TournResult(Enum):
    DNQ = 0
    GS = 1
    RO16 = 2
    QF = 3
    SF = 4
    F = 5
    W = 6


# Example usage
result = TournResult.DNQ
print(result)          # Output: GameResult.DNQ
print(result.name)     # Output: DNQ
print(result.value)    # Output: 0
