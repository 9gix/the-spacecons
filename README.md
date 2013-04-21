# The Spacecon Project #
## Prerequisites ##

- python >= 2.7
- django >= 1.5
- pip
- virtualenv/wrapper (optional)

## Installation ##
### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv --no-site-packages spacecon-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages spacecon-env
cd spacecon-env
source bin/activate
```

### Clone the code ###
Obtain the url to your git repository.

```bash
git clone <URL_TO_GIT_RESPOSITORY> spacecon
```

### Install requirements ###
```bash
cd spacecon
pip install -r requirements.txt
```

### Configure project ###
```bash
cp spacecon/__local_settings.py spacecon/local_settings.py
vi spacecon/local_settings.py
```

### Sync database ###
```bash
python manage.py syncdb
python manage.py migrate
```

## Running ##
```bash
python manage.py runserver
```

Open browser to http://127.0.0.1:8000

