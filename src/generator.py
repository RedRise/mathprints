from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass(frozen=True)
class WorksheetConfig:
    difficulty: int
    count: int
    seed: int | None


def generate_exercises(config: WorksheetConfig) -> list[str]:
    """Return LaTeX-ready exercise strings.

    Placeholder for future rules per difficulty.
    """
    rng = random.Random(config.seed)
    exercises = []

    for _ in range(config.count):
        if config.difficulty == 1:
            if rng.random() < 0.6:
                left = rng.choice([2, 3, 4, 5])
                right = rng.randint(1, 10)
                exercises.append(f"\\item ${left} \\times {right} =$")
            else:
                left = rng.randint(1, 11)
                right = rng.randint(1, 11)
                exercises.append(f"\\item ${left} + {right} =$")
        elif config.difficulty == 2:
            if rng.random() < 0.6:
                if rng.random() < 0.2:
                    small = rng.randint(2, 5)
                    other = rng.randint(2, 10)
                    left, right = (small, other) if rng.random() < 0.5 else (other, small)
                else:
                    left = rng.randint(6, 10)
                    right = rng.randint(6, 10)
                exercises.append(f"\\item ${left} \\times {right} =$")
            else:
                if rng.random() < 0.2:
                    small = rng.randint(1, 5)
                    other = rng.randint(1, 20)
                    left, right = (small, other) if rng.random() < 0.5 else (other, small)
                else:
                    left = rng.randint(6, 20)
                    right = rng.randint(6, 20)
                exercises.append(f"\\item ${left} + {right} =$")
        else:
            roll = rng.random()
            if roll < 0.5:
                if rng.random() < 0.7:
                    left = rng.randint(8, 12)
                    right = rng.randint(6, 12)
                else:
                    left = rng.randint(6, 12)
                    right = rng.randint(2, 12)
                exercises.append(f"\\item ${left} \\times {right} =$")
            elif roll < 0.75:
                if rng.random() < 0.7:
                    left = rng.randint(10, 99)
                    right = rng.randint(10, 99)
                else:
                    left = rng.randint(10, 99)
                    right = rng.randint(1, 99)
                exercises.append(f"\\item ${left} + {right} =$")
            else:
                if rng.random() < 0.5:
                    minuend = rng.randint(20, 99)
                    subtrahend = rng.randint(10, min(minuend - 1, 99))
                else:
                    minuend = rng.randint(10, 99)
                    subtrahend = rng.randint(1, minuend - 1)
                exercises.append(f"\\item ${minuend} - {subtrahend} =$")

    return exercises
