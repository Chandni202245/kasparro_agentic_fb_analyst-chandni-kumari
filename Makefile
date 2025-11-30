
.PHONY: install test run help
install:
	python -m pip install -r requirements.txt
test:
	pytest -q
run:
	python src/orchestrator/run.py "Analyze ROAS drop"
help:
	@echo "make install | test | run"
