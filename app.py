from flask import Flask, request, jsonify
import os

# Création de l'application Flask
app = Flask(__name__)

# Liste d'étudiants en mémoire (simule une base de données)
students = [
    {"name": "Alice", "field": "Informatique"},
    {"name": "Bob", "field": "Electronique"}
]

# =========================
# GET /students
# =========================
@app.route("/students", methods=["GET"])
def get_students():
    # Retourne toute la liste des étudiants
    return jsonify(students), 200


# =========================
# POST /students
# =========================
@app.route("/students", methods=["POST"])
def add_student():
    # Récupère les données envoyées en JSON
    data = request.get_json()

    # Vérification simple
    if not data or "name" not in data or "field" not in data:
        return jsonify({"error": "Missing name or field"}), 400

    # Création nouvel étudiant
    new_student = {
        "name": data["name"],
        "field": data["field"]
    }

    # Ajout dans la liste
    students.append(new_student)

    # Retourne le nouvel étudiant
    return jsonify(new_student), 201


# =========================
# GET /info
# =========================
@app.route("/info", methods=["GET"])
def get_info():
    # Lire variable d'environnement
    academy_name = os.getenv("ACADEMY_NAME", "Unknown Academy")

    return jsonify({
        "total_students": len(students),
        "academy_name": academy_name
    }), 200


# Lancement du serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
