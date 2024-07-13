from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-hadith/hadith")
def get_hadith():
    hadiths ={
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
    }
    return jsonify(hadiths),200


if "__name__" == "__api__":
    app.run(debug=True)