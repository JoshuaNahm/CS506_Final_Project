install:
	pip install -r requirements.txt

run:
	jupyter nbconvert --to notebook --execute CS506_Final_Project.ipynb --output executed_notebook.ipynb

test:
	pytest test/


