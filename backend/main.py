# filepath: d:\Flask-image\backend\main.py
from flask import Flask, request
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Import CORS
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)
CORS(app)  # Enable CORS for all routes

app.config['UPLOAD_FOLDER'] = 'uploads'

class UserInfo(db.Models):
    id = db.column


@app.route("/savedata", methods=["POST"])
def save_data():
    full_name = request.form.get("name")
    phone_number = request.form.get("phone")
    image = request.files.get("image")  # Correct way to get the uploaded file

    print("Full Name:", full_name)
    print("Phone Number:", phone_number)

    if image:
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("Image saved as:", filename)
    else:
        return "No image uploaded", 400

    return "Data saved successfully!"

if __name__ == "__main__":
    app.run(debug=True)