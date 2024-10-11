# Importera os modulen
import os

# Funktion för att hämta bilmodell från märke
def get_model(car):
    # Dictionary med bilmodeller för varje märke
    car_models = {
        "Porsche": "911",
        "Ferrari": "488 GTB",
        "Lambo": "Huracan"
    }
    # Returnerar bilmodellen om märket finns, annars "Unknown model"
    return car_models.get(car, "Unknown model")

# Funktion för att skapa en numrerad lista över bilar
def create_numbered_list(cars):
    # Rensa konsolen
    os.system('cls' if os.name == 'nt' else 'clear')
    # Loopa över indexen och värdena i listan över bilar
    for i, car in enumerate(cars, start=1):
        # Skriv ut en sträng i formatet "nummer) märke modell"
        print(f"{i}) {car} {get_model(car)}")

# Exempel på användning
cars = ["Porsche", "Ferrari", "Lambo"]
create_numbered_list(cars)