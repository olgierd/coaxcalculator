install-dev:
	pip3 install -r requirements.txt

generate-html:
	rm docs/index.html
	python genhtml.py
