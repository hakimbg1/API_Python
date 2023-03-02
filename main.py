from fastapi import FastAPI
from typing import List
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mypassword",
  database="DB")

app = FastAPI()

from typing import Optional

from pydantic import BaseModel, validator

class Food(BaseModel):
    Nom: str
    type: str
    adress: str
    note: Optional[int] = None

    @validator('note')
    def validate_note(cls, note):
        if note is not None and (note < 0 or note > 5):
            raise ValueError('La note doit être comprise entre 0 et 5')
        return note

# récupérer tous les aliments
@app.get("/foods", response_model=List[Food])
async def read_foods():
    # récupérer les aliments depuis la base de données
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM foods")

    foods = cursor.fetchall()
    return foods

# récupérer un aliment par son nom
@app.get("/foods/{nom}", response_model=Food)
async def read_food(nom: str):
    # récupérer l'aliment depuis la base de données
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM foods WHERE Nom=%s", (nom,))

    food = cursor.fetchone()
    return food

# créer un nouvel aliment
@app.post("/foods", response_model=Food)
async def create_food(food: Food):
    # insérer l'aliment dans la base de données
    cursor = mydb.cursor()
    query = "INSERT INTO foods (Nom, type, adress, note) VALUES (%s, %s, %s, %s)"

    values = (food.Nom, food.type, food.adress, food.note)
    cursor.execute(query, values)
    mydb.commit()

    # récupérer l'aliment depuis la base de données
    cursor.execute("SELECT * FROM foods WHERE Nom=%s", (food.Nom,))
    created_food = cursor.fetchone()

    return created_food

# mettre à jour un aliment existant
@app.put("/foods/{nom}", response_model=Food)
async def update_food(nom: str, food: Food):
    # mettre à jour l'aliment dans la base de données
    cursor = mydb.cursor()
    query = "UPDATE foods SET type=%s, adress=%s, note=%s WHERE Nom=%s"

    values = (food.type, food.adress, food.note, nom)
    cursor.execute(query, values)
    mydb.commit()

    # récupérer l'aliment mis à jour depuis la base de données
    cursor.execute("SELECT * FROM foods WHERE Nom=%s", (nom,))
    updated_food = cursor.fetchone()

    return updated_food


# supprimer un aliment existant
@app.delete("/foods/{nom}")
async def delete_food(nom: str):
    # supprimer l'aliment de la base de données
    cursor = mydb.cursor()
    query = "DELETE FROM foods WHERE Nom=%s"

    values = (nom,)
    cursor.execute(query, values)
    mydb.commit()

    return {"message": "Food deleted successfully"}
