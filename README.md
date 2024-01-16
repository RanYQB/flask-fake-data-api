# Flask fake data JSON API

Python Json API with Faker data

## Installation

Start by installing the venv module  

```bash
sudo apt install python3.10-venv
```

Create the virtual environnement
```bash
python3 -m venv .venv
```

Activate the virtual environnement
```bash
source .venv/bin/activate
```

Install Flask
```bash
pip install flask
```

## Run the project

Export variables to run locally
```bash
export FLASK_APP=app.py
export FLASK_DEBUG=1
```

Run the project 
```bash
flask run
```

