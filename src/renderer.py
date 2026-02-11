from __future__ import annotations

from pathlib import Path

from src.generator import WorksheetConfig, generate_unique_exercises

TEMPLATE_PATH = Path(__file__).parent / "templates" / "worksheet.tex"


def render_page(
    config: WorksheetConfig,
    left_exercises: list[str],
    right_exercises: list[str],
) -> str:
    left_items = "\n".join(left_exercises)
    right_items = "\n".join(right_exercises)
    title = f"Tables de multiplication -- Niveau {config.difficulty}"

    return "\n".join(
        [
            "\\begin{multicols}{2}",
            f"\\section*{{{title}}}",
            "\\begin{itemize}",
            left_items,
            "\\end{itemize}",
            "\\columnbreak",
            f"\\section*{{{title}}}",
            "\\begin{itemize}",
            right_items,
            "\\end{itemize}",
            "\\end{multicols}",
        ]
    )


def render_latex(config: WorksheetConfig, pages: int) -> str:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    blocks = []

    for page_index in range(pages):
        seed = None if config.seed is None else config.seed + page_index
        left_seed = seed
        right_seed = None if seed is None else seed + 1
        left_config = WorksheetConfig(
            difficulty=config.difficulty,
            count=config.count,
            seed=left_seed,
        )
        right_config = WorksheetConfig(
            difficulty=config.difficulty,
            count=config.count,
            seed=right_seed,
        )
        left_exercises = generate_unique_exercises(left_config)
        right_exercises = generate_unique_exercises(right_config)
        blocks.append(render_page(config, left_exercises, right_exercises))

    pages_content = "\n\\newpage\n".join(blocks)

    return template.replace("{{ pages }}", pages_content)
