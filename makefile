
install:
	pip install --upgrade pip && \
	pip freeze | xargs -r pip uninstall -y && \
	pip install -r requirements-dev.txt && \
	pre-commit install

lint:
	@black . && flake8 .

run:
	flask run --reload