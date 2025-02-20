from flask import Flask, render_template, request, jsonify
from utils import convert_spotify_track

app = Flask(__name__)

# Route for home page
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            result = convert_spotify_track(user_input)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/get_input", methods=["GET"])
# def get_input():
#     return jsonify({"text": user_input})  # Serve input as JSON

if __name__ == "__main__":
    app.run(debug=True)
