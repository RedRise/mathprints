POETRY=poetry
NUM_PAGES=6

install:
	$(POETRY) install

calc-1:
	$(POETRY) run mathprints --difficulty 1 --pages $(NUM_PAGES)

calc-2:
	$(POETRY) run mathprints --difficulty 2 --pages $(NUM_PAGES)

calc-3:
	$(POETRY) run mathprints --difficulty 3 --pages $(NUM_PAGES)

all: calc-1 calc-2 calc-3
