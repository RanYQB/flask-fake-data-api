from flask import Flask, json
from faker import Faker
import os.path

app = Flask(__name__)
fake = Faker("fr_FR")
path = './data.json'

@app.route("/")
def hello_world():
    return read_json_data()

def read_json_data():
    if os.path.isfile(path) == False:
        create_new_fake_data()
    return load_fake_data()

def load_fake_data():
    with open('data.json', 'r') as users_file:
        users_data = json.load(users_file)
        data = json.dumps(users_data, ensure_ascii=False)
    return data

def create_new_fake_data():
    data = {
        "users": []
    }
    for _ in range(30000):
        new_element = {
            "id": fake.unique.random_int(min=6000, max=40000),
            "last_name": fake.last_name(),
            "first_name": fake.first_name(),
            "birth_date": fake.date_of_birth(minimum_age=18, maximum_age=90),
            "address": fake.address(),
            "fidelity_points": fake.random_int(min=10, max=500)
        }
        data["users"].append(new_element)
    fake.unique.clear()
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)