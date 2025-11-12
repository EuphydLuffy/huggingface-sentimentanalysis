install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
#	pip install -r requirements.txt
# pip install pipreqs; pipreqs . --force after pip freeze to record only necessary packages.
# But remember to add pytest and pytest-cov. 

lint:
	pylint **/*.py

format:
	black .

test:
	python -m pytest --cov=app

launch:
	python app.py
		
all: install lint format test launch