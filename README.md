# mathprints

Générateur de fiches d'exercices de maths imprimables (PDF LaTeX) pour l'élémentaire.

## Pré-requis

- Python 3.11+
- LaTeX avec `pdflatex`
- Poetry

## Installation

```bash
make install
```

## Génération rapide

```bash
make calc-1
```

Chaque commande `calc-*` génère un PDF dans `output/` (par défaut 10 pages).

## CLI

```bash
poetry run mathprints --difficulty 1 --count 30 --pages 10 --seed 123
```

- `--difficulty` : niveau 1, 2, 3
- `--count` : nombre d'exercices **par demi-feuille** (chaque page a deux colonnes)
- `--pages` : nombre de pages dans le PDF
- `--seed` : reproductibilité
- `--output` : dossier de sortie

## Règles par niveau

### Niveau 1
- Multiplications (tables 2, 3, 4, 5)
- Additions de deux nombres < 12

### Niveau 2
- Multiplications jusqu'à 10 (faible occurrence de facteurs < 6)
- Additions de deux nombres < 21 (faible occurrence de termes < 6)

### Niveau 3
- Multiplications tables 6–12 (biais vers facteurs élevés)
- Additions 10–99 (biais vers retenues)
- Soustractions 10–99 (résultat positif, biais vers retenues)

## Notes

- Le document est pensé pour être **coupé verticalement** en deux demi-feuilles.
- Chaque colonne répète le titre.
