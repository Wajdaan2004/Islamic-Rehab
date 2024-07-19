from flask import Flask, request, jsonify

app = Flask(__name__)
hadiths ={
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
    }
@app.route("/get-hadith/hadith/<str:hadithNumber>")
def get_hadith(hadithNumber):
    return hadiths[hadithNumber]
    return jsonify(hadiths),200

if "__name__" == "__api__":
    app.run(debug=True)