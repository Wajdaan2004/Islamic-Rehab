from flask import Flask, request, jsonify

app = Flask(__name__)

# list
hadiths = [
    {"number": 1, "source": "Sahih Bukhari", "text": "The best among you are those who learn the Quran and teach it."},
    {"number": 2, "source": "Sahih Muslim", "text": "The strong believer is better and more beloved to Allah than the weak believer."},
    {"number": 3, "source": "Tirmidhi", "text": "The best of you are those who have the best manners and character."},
    {"number": 4, "source": "Abu Dawood", "text": "When one of you prays, he should not spit in front of him, for Allah is in front of him when he prays."},
    {"number": 5, "source": "Ibn Majah", "text": "Allah does not look at your bodies nor your forms but He looks at your hearts and your deeds."}
    ]

# this function will retrieve a specific hadith
@app.route("/get-hadith/<int:number>")
def get_hadith(number):
    
    chosen_hadith = None
    for i in hadiths:               # iterate through the hadiths list
        if i['number'] == number:   # if the value after '"number": ' in the list is equal to the parameter of get_hadith(number)
            chosen_hadith = i       # make that the chosen hadith

    if chosen_hadith is not None:   # check if there is a hadith chosen, then return it
        return jsonify(chosen_hadith), 200
    else:
        return jsonify({'error': 'Hadith not found'}), 404 # if the hadith is not found, return an error

@app.route("/")
def get_all_hadiths():
    return jsonify(hadiths), 200


if "__name__" == "__api__":
    app.run(debug=True) 
    