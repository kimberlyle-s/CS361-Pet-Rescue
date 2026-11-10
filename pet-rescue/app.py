from flask import Flask, render_template, request

app = Flask(__name__)

pets = {
    1: {
        "name": "Charlie",
        "type": "Dog",
        "age": "2 Years",
        "breed": "Lab Mix",
        "image": "charlie.jpeg",
        "description": "Charlie is a 2yo lab mix. He is young and full of energy! Gets along great with other dogs, kids, and cats. He loves to play fetch with tennis balls. Due to his high energy level, a home with another dog companion would be ideal. His walking skills could use some training. He is also house trained! If Charlie sounds like a good fit, please submit an application using the button below."
    },
    2: {
        "name": "Baxter",
        "type": "Dog",
        "age": "4 Years",
        "breed": "Pug",
        "image": "baxter.jpeg",
        "description": "Baxter is a 4yo pug. He loves belly scratches and taking walks to sniff as much as his heart desires. He is great with kids and other dogs. However, it is unknown his beahvior with cats. Baxter is house trained! One sneaky habit of his that could use some training is stealing socks. If Baxter sounds like a good fit, please submit an application using the button below."
    },
    3: {
        "name": "Dobby",
        "type": "Cat",
        "age": "1 Year",
        "breed": "Sphynx",
        "image": "dobby.jpeg",
        "description": "Dobby is a 1yo sphynx cat. She loves to cuddle and loves attention. She has not been around dogs so is unknown whether she might get along with them. Dobby knows how to use her litter box. She loves feather toys and enjoys napping in a cat tree. If Dobby sounds like a great fit, please submit an application using the button below."
    }
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pets")
def pets_page():
    return render_template("pets.html", pets=pets)

@app.route("/pet/<int:pet_id>")
def details(pet_id):
    pet = pets[pet_id]
    return render_template("details.html", pet=pet)

@app.route("/apply/<int:pet_id>", methods=["GET", "POST"])
def apply(pet_id):

    pet = pets[pet_id]

    if request.method == "POST":
        return render_template("confirmation.html")

    return render_template("application.html", pet=pet)

if __name__ == "__main__":
    app.run(debug=True)