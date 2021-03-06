## Quickstart Guide

Use `git clone` to clone the repository from `git clone https://github.com/heheheejin/boe.git`.
```
git clone https://github.com/heheheejin/boe.git
```

Change directory into the project folder
```
cd .\boe\
```

Create a python virtual environment in the directory of the project
```
python -m venv env
```

Activate the virtual environment that we've just created.
```
.\env\Scripts\activate        # for windows
# or
source .\env\bin\activate     # for linux
```

Update `pip` to the latest version
```
pip install --upgrade pip
```

Install all the required dependencies for the project
```
pip install -r requirements.txt
```

Check for any required database migrations.
```
python manage.py makemigrations
```

Execute any migrations required.
```
python manage.py migrate
```

Populate the database with course requirements for C2001 for testing purposes. 
```
python manage.py runscript populate_reqs
```

Run the server
```
python manage.py runserver
```

The application should be hosted and available on `https://127.0.0.1:8000`  
Two sample .csv files are included in the `scripts` folder as sample inputs.  
* [Sample data with only C2001 students](https://github.com/heheheejin/boe/blob/master/scripts/only_c2001_dummy.csv)
* [Full callista sample data](https://github.com/heheheejin/boe/blob/master/scripts/dummy_data.csv)

Both datasets are provided by the challenge organizers
