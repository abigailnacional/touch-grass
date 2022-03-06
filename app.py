from flask import Flask, render_template, flash, request, redirect, url_for
from touchgrass import create_app
import os
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.orm
import random

UPLOAD_FOLDER = './static'

app = create_app()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
sessionmaker = sqlalchemy.orm.sessionmaker(db.engine)

class User():
    def __init__(
        self,
        current_category):
        self.current_category=current_category
    current_category = db.Column(db.String(20), nullable=True)

    #sets current category
    def set_cat(theCategory):
        User.current_category = theCategory

    # index page
@app.route("/")
def index():
    #List all categories, "cats" for short
    cats = {1: 'Bird', 2: 'Tree', 3: 'Dog', 4: 'Cat', 5: 'Insect',
                6: 'Rock'}
    #Picks a random challenge category
    selected = random.randint(1,6)
    challenge = cats[selected]
    User.set_cat(challenge)
    #Print the category on the home page
    return render_template("index.html", challenge=challenge)

#Allows a user to upload an image and then calls run_quickstart on the image path
@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
             return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        return check_labels(path)
    #If the form wasn't just submitted, AKA you just loaded the page:
    return render_template('upload.html')

#Function check_labels is based off of run_quickstart
#  from https://github.com/googleapis/python-vision/blob/HEAD/samples/snippets/quickstart/quickstart.py
#Function finds all the labels for the image and then iterates them
#  to find out if the category is one of those labels

def check_labels(imgPath):
    # [START vision_quickstart]
    import io

    # Imports the Google Cloud client library
    # [START vision_python_migration_import]
    from google.cloud import vision
    # [END vision_python_migration_import]

    # Instantiates a client
    # [START vision_python_migration_client]
    client = vision.ImageAnnotatorClient()
    # [END vision_python_migration_client]

    # The name of the image file to annotate
    file_name = os.path.abspath(imgPath)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    #Set default value for confirmation message
    confirm_image = "Sorry, but this picture doesn't have something from the challenge category."
    #Iterate through labels and tell the person if their picture fits in the category
    for label in labels:
        if label.description == User.current_category:
            confirm_image = "Great job, you took a picture of something in the challenge category!"
            break
    return render_template('labels.html', confirm_image=confirm_image)


if __name__ == "__main__":
  app.run()