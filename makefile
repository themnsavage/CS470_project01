run:
	python3 main.py; rm -rf app/__pycache__

setup:
	pip3 install -r requirments.txt

clean:
	rm -rf app/__pycache__