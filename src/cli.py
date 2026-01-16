from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

from src.generator import WorksheetConfig
from src.renderer import render_latex

DEFAULT_OUTPUT = Path("output")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate printable multiplication worksheets (LaTeX).",
    )
    parser.add_argument(
        "--difficulty",
        type=int,
        choices=[1, 2, 3],
        default=1,
        help="Difficulty level (1-3).",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=30,
        help="Number of exercises.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Seed for reproducible worksheets.",
    )
    parser.add_argument(
        "--pages",
        type=int,
        default=1,
        help="Number of pages to generate.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output directory.",
    )
    return parser


def ensure_pdflatex() -> None:
    if shutil.which("pdflatex") is None:
        raise SystemExit("pdflatex not found. Install LaTeX to render PDFs.")


def render_pdf(tex_content: str, output_dir: Path, filename: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    tex_path = output_dir / f"{filename}.tex"
    tex_path.write_text(tex_content, encoding="utf-8")

    subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex_path.name],
        cwd=output_dir,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    return output_dir / f"{filename}.pdf"


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    config = WorksheetConfig(
        difficulty=args.difficulty,
        count=args.count,
        seed=args.seed,
    )

    ensure_pdflatex()
    latex = render_latex(config, pages=args.pages)
    filename = f"tables-niveau-{args.difficulty}"
    pdf_path = render_pdf(latex, args.output, filename)

    print(f"PDF generated: {pdf_path}")


if __name__ == "__main__":
    main()
