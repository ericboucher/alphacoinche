# /bin/bash
lint:
	flake8 alphacoinche tests
	pep257 alphacoinche

# Run test suite locally.
test: FORCE
	py.test -s tests

# Run coverage.
coverage:
	pytest --cov=alphacoinche

# Start game.
play:
	python ./alphacoinche/runner.py

# [Dummy dependency to force a make command to always run.]
FORCE:
