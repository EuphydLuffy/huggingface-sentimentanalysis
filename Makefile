install:
#	pip install --upgrade pip &&\
#	pip install -r requirements.txt
	pip install -r requirements.txt

test:
	python -m pytest --cov=app

debug:
	python -m pytest -vv --pdb

launch:
	python app.py

		
all: install test debug launch