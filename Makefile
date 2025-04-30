install:
	pip install -r requirements.txt

run:
	jupyter nbconvert --to notebook --execute CS506_Project_Final_Report.ipynb --output executed_notebook.ipynb

test:
	pytest test/


