.PHONY: setup
setup:  # Requires an active virtualenv
	pip install -U pip wheel pip-tools
	make reqs
	pip install -r requirements/dev-requirements.txt
	pip install -e .
	python manage.py db upgrade
	cd static && npm install

.PHONY: run
run:
	python manage.py run

.PHONY: test
test:
	pytest -x rem/tests

.PHONY: lint
lint:
	flake8 --config=setup.cfg rem

.PHONY: db
db:
	rm db/rem.sqlite || true
	python manage.py db upgrade

.PHONY: reqs
reqs:
	pip-compile requirements/requirements.ini
	pip-compile requirements/test-requirements.ini
	pip-compile requirements/prod-requirements.ini
	pip-compile requirements/dev-requirements.ini

