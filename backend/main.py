from flask import Flask

app = Flask(__name__)

@app.route("/savedata", methods=["POST"])
def save_data():
    return "Data saved successfully!"

if __name__ == "__main__":
   app.run(debug=True)