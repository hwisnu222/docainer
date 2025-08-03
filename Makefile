build:
	pyinstaller --onefile --name=docainer --add-data="templates:templates" --add-data="config.yaml:." main.py

run:
	python main.py

shell:
	poetry shell
