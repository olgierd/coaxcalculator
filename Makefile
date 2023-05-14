install-dev:
	pip3 install -r requirements.txt

generate-html:
	rm docs/index.html
	python3 genhtml.py

serve:
	python3 -m http.server --directory docs

docker:
	docker run --rm -it -v $(PWD):/app -p 8000:8000 python:3.8 bash -c "apt update && apt install -y make python3-pip && cd /app && make install-dev generate-html serve"
