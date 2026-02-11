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
    return [_generate_exercise(rng, config.difficulty) for _ in range(config.count)]


def generate_unique_exercises(config: WorksheetConfig) -> list[str]:
    rng = random.Random(config.seed)
    exercises: list[str] = []
    seen: set[str] = set()

    while len(exercises) < config.count:
        exercise = _generate_exercise(rng, config.difficulty)
        if exercise in seen:
            continue
        seen.add(exercise)
        exercises.append(exercise)

    return exercises


def _generate_exercise(rng: random.Random, difficulty: int) -> str:
    if difficulty == 1:
        if rng.random() < 0.6:
            left = rng.choice([2, 3, 4, 5])
            right = rng.randint(1, 10)
            return f"\\item ${left} \\times {right} =$"
        left = rng.randint(1, 11)
        right = rng.randint(1, 11)
        return f"\\item ${left} + {right} =$"
    if difficulty == 2:
        if rng.random() < 0.6:
            if rng.random() < 0.2:
                small = rng.randint(2, 5)
                other = rng.randint(2, 10)
                left, right = (small, other) if rng.random() < 0.5 else (other, small)
            else:
                left = rng.randint(6, 10)
                right = rng.randint(6, 10)
            return f"\\item ${left} \\times {right} =$"
        if rng.random() < 0.2:
            small = rng.randint(1, 5)
            other = rng.randint(1, 20)
            left, right = (small, other) if rng.random() < 0.5 else (other, small)
        else:
            left = rng.randint(6, 20)
            right = rng.randint(6, 20)
        return f"\\item ${left} + {right} =$"

    roll = rng.random()
    if roll < 0.5:
        if rng.random() < 0.7:
            left = rng.randint(8, 12)
            right = rng.randint(6, 12)
        else:
            left = rng.randint(6, 12)
            right = rng.randint(2, 12)
        return f"\\item ${left} \\times {right} =$"
    if roll < 0.75:
        if rng.random() < 0.7:
            left = rng.randint(10, 99)
            right = rng.randint(10, 99)
        else:
            left = rng.randint(10, 99)
            right = rng.randint(1, 99)
        return f"\\item ${left} + {right} =$"
    if rng.random() < 0.5:
        minuend = rng.randint(20, 99)
        subtrahend = rng.randint(10, min(minuend - 1, 99))
    else:
        minuend = rng.randint(10, 99)
        subtrahend = rng.randint(1, minuend - 1)
    return f"\\item ${minuend} - {subtrahend} =$"
