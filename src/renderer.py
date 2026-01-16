from __future__ import annotations

from pathlib import Path

from src.generator import WorksheetConfig, generate_exercises

TEMPLATE_PATH = Path(__file__).parent / "templates" / "worksheet.tex"


def render_page(config: WorksheetConfig, exercises: list[str]) -> str:
    midpoint = len(exercises) // 2
    left_items = "\n".join(exercises[:midpoint])
    right_items = "\n".join(exercises[midpoint:])
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
        page_config = WorksheetConfig(
            difficulty=config.difficulty,
            count=config.count * 2,
            seed=seed,
        )
        exercises = generate_exercises(page_config)
        blocks.append(render_page(config, exercises))

    pages_content = "\n\\newpage\n".join(blocks)

    return template.replace("{{ pages }}", pages_content)
