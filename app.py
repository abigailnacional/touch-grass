from flask import Flask, render_template, flash, request, redirect, url_for
from touchgrass import create_app
import os
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.orm

UPLOAD_FOLDER = './static'

app = create_app()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
sessionmaker = sqlalchemy.orm.sessionmaker(db.engine)

# index page
@app.route("/")
def index():
    return render_template("index.html")

#Allows a user to upload an image and then calls run_quickstart on the image path
@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        return run_quickstart(path)

    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    '''
#Function run_quickstart is from https://github.com/googleapis/python-vision/blob/HEAD/samples/snippets/quickstart/quickstart.py
#Prints the labels for the image
def run_quickstart(imgPath):
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

    return render_template('labels.html', labels=labels)


if __name__ == "__main__":
  app.run()