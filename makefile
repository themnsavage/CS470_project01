run:
	python3 main.py; rm -rf app/__pycache__

setup:
	pip install -r requirements.txt

clean:
	rm -rf app/__pycache__