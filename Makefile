POETRY=poetry

install:
	$(POETRY) install

calc-1:
	$(POETRY) run mathprints --difficulty 1 --pages 10

calc-2:
	$(POETRY) run mathprints --difficulty 2 --pages 10

calc-3:
	$(POETRY) run mathprints --difficulty 3 --pages 10
