clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf __pycache__/
	rm -rf tests/__pycache__/
	rm -rf delivery/__pycache__/
	rm -rf delivery/ext/__pycache__/
	rm -rf delivery/ext/admin/__pycache__/
	rm -rf delivery/ext/api/__pycache__/
	rm -rf delivery/ext/auth/__pycache__/
	rm -rf delivery/ext/cli/__pycache__/
	rm -rf delivery/ext/config/__pycache__/
	rm -rf delivery/ext/db/__pycache__/
	rm -rf delivery/ext/site/__pycache__/
	rm -rf delivery/ext/toolbar/__pycache__/
	rm -rf .pytest_cache/
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov/
	rm -rf .tox/
	rm -rf docs/_build
	rm -rf .coverage
	rm -rf migrations/__pycache__/
	rm -rf migrations/versions/__pycache__/
	pip install -e .[dev] --upgrade --no-cache
		
install:
	pip install -e .['dev']

init_db:
	FLASK_APP=delivery/app.py flask create-db
	FLASK_APP=delivery/app.py flask db upgrade

test:
	FLASK_ENV=test pytest tests/ -v --cov=delivery
	# coverage html
	# chromium './htmlcov/index.html' &

format:
	isort **/*.py
	black -l 79 **/*.py	

run-dev:
	FLASK_APP=delivery/app.py FLASK_ENV=development flask run

run-prod:
	FLASK_APP=delivery/app.py FLASK_ENV=production flask run
