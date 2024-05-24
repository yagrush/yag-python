req:
	pip freeze > requirements.txt

venv-init:
	python -m venv .venv
	chmod 777 .venv/bin/activate
	source ./.venv/bin/activate

deactivate:
	deactivate

pip-r:
	pip install -r requirements.txt