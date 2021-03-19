BUILD_CMD=poetry build
RUN_CMD=poetry run
APP_NAME=myapp

verify:
	$(RUN_CMD) black --check --diff .
	$(RUN_CMD) mypy -p $(APP_NAME)
	$(RUN_CMD) pylint $(APP_NAME)

fmt:
	$(RUN_CMD) isort -rc .
	$(RUN_CMD) black .

test:
	$(RUN_CMD) pytest -ra --cov=$(APP_NAME)

build:
	$(BUILD_CMD) -v

run:
	$(RUN_CMD) start

clean:
	rm -Rf dist/
	find . -name '__pycache__' -type d -exec rm -Rf {} \+
