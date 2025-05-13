from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Import CORS
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Disable unnecessary warnings
db = SQLAlchemy(app)
CORS(app)  # Enable CORS for all routes

# Configure the upload folder
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Define the UserInfo model
class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(100), nullable=False)  # Full name
    phone = db.Column(db.String(15), nullable=False)  # Phone number
    image_filename = db.Column(db.String(200), nullable=False)  # Image file name

    def __repr__(self):
        return f"<UserInfo {self.name}>"

# Route to render the form
@app.route("/", methods=["GET"])
def home():
    return render_template("form.html")  # Render the form.html template

# Route to display user information
@app.route("/show", methods=["GET"])
def show_users():
    users = UserInfo.query.all()  # Retrieve all users from the database
    return render_template("show.html", users=users)

# Route to handle form submission and save data
@app.route("/savedata", methods=["POST"])
def save_data():
    full_name = request.form.get("name")
    phone_number = request.form.get("phone")
    image = request.files.get("image")  # Correct way to get the uploaded file

    if not full_name or not phone_number or not image:
        return "All fields are required", 400

    # Save the uploaded image
    filename = secure_filename(image.filename)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(image_path)

    # Save user info to the database
    user = UserInfo(name=full_name, phone=phone_number, image_filename=filename)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for("show_users"))  # Redirect to the show_users route

# Main entry point
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True)