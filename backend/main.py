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

class UserInfo(db.Model):  # Corrected from db.Models to db.Model
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(100), nullable=False)  # Full name
    phone = db.Column(db.String(15), nullable=False)  # Phone number
    image_filename = db.Column(db.String(200), nullable=False)  # Image file name

    def __repr__(self):
        return f"<UserInfo {self.name}>"


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