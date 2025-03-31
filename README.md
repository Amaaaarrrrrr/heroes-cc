# Project Overview

The Superheroes API is a Flask-based RESTful API for managing superheroes and their powers. It allows you to perform CRUD operations on heroes, powers, and hero-power relationships. The project demonstrates model validations, relationship handling, and error management using Flask, SQLAlchemy, and Flask-Migrate.

# Tech Stack 🛠️
Backend: Flask, SQLAlchemy, Flask-Migrate

Database: SQLite

Serialization: Flask-Serializer

Validation: SQLAlchemy Validations

# Setup Instructions ⚙️
## 1. Clone the Repository
bash
git clone https://github.com/your-username/superheroes-api.git
cd superheroes-api

## 2. Create Virtual Environment & Activate
bash
### Linux / MacOS
python3 -m venv env
source env/bin/activate

### Windows
python -m venv env
env\Scripts\activate

## 3. Install Dependencies
bash
pip install -r requirements.txt

## 4. Set Up Environment Variables
Create a .env file and add:

ini
FLASK_APP=app
FLASK_ENV=development

## 5. Database Migration
bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

## 6. Seed the Database 
run the command seed.py

7. Run the Server
bash
flask run

The server will run on: http://127.0.0.1:5000

## API Routes & Sample Requests/Responses 🚦
GET /heroes
Returns a list of all heroes.

Request:
http
GET /heroes
Response:

json
[
  { "id": 1, "name": "Kamala Khan", "super_name": "Ms. Marvel" },
  { "id": 2, "name": "Doreen Green", "super_name": "Squirrel Girl" }
]
GET /heroes/:id
Returns a hero along with their associated powers.

Request:
http
GET /heroes/1
Successful Response:

json
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "hero_powers": [
    {
      "id": 1,
      "hero_id": 1,
      "power_id": 2,
      "strength": "Strong",
      "power": {
        "id": 2,
        "name": "flight",
        "description": "gives the wielder the ability to fly through the skies at supersonic speed"
      }
    }
  ]
}
Error Response (Hero Not Found):

json
{ "error": "Hero not found" }
GET /powers
Returns a list of all powers.

Request:
http
GET /powers

Response:
json
[
  { "id": 1, "name": "super strength", "description": "gives super-human strength" },
  { "id": 2, "name": "flight", "description": "fly through the skies at supersonic speed" }
]
GET /powers/:id
Returns a specific power.

Request:
http
GET /powers/1
Successful Response:

json
{
  "id": 1,
  "name": "super strength",
  "description": "gives super-human strength"
}
Error Response (Power Not Found):

json
{ "error": "Power not found" }
PATCH /powers/:id
Updates a power's description.

Request:
http
PATCH /powers/1
Content-Type: application/json

{
  "description": "Updated powerful description"
}
Successful Response:

json
{
  "id": 1,
  "name": "super strength",
  "description": "Updated powerful description"
}
Error Response (Power Not Found):

json
{ "error": "Power not found" }
Validation Error (Description Too Short):

json
{ "errors": ["Description must be at least 20 characters long"] }
POST /hero_powers
Creates a new HeroPower relationship.

Request:
http
POST /hero_powers
Content-Type: application/json

{
  "hero_id": 1,
  "power_id": 1,
  "strength": "Strong"
}
Successful Response:

json
{
  "id": 1,
  "hero_id": 1,
  "power_id": 1,
  "strength": "Strong",
  "hero": {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  },
  "power": {
    "id": 1,
    "name": "super strength",
    "description": "gives super-human strength"
  }
}
Error Response (Validation Error):

json
{ "errors": ["Strength must be 'Strong', 'Weak', or 'Average'"] }
Error Handling 🔧
404 Not Found for invalid resources

400 Bad Request for validation errors

Graceful error handling using try-except blocks

