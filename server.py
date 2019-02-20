from flask import Flask, render_template,request, redirect
from mysqlconn import connectToMySQL 

app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('cr_pets')
    pets = mysql.query_db('SELECT * FROM pets;')
    print(pets)
    return render_template("index.html", all_pets = pets)

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    mysql = connectToMySQL("cr_pets")
    
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(n)s, %(t)s, NOW(), NOW());"

    data = {
        "n": request.form["name"],
        "t": request.form["type"]
    }
    db = connectToMySQL('cr_pets')
    db.query_db(query,data)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)