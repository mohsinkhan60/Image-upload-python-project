from flask import Flask, request

app = Flask(__name__)

@app.route("/savedata", methods=["POST"])
def save_data():
    if request.method == "POST":
        full_name = request.form.get("name")
    return "Data saved successfully!"

if __name__ == "__main__":
   app.run(debug=True)