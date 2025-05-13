from flask import Flask, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

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
