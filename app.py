from flask import Flask, render_template
from .touchgrass import create_app
import os
from flask_sqlalchemy import SQLAlchemy, request
import sqlalchemy.orm

app = create_app()
db = SQLAlchemy(app)
sessionmaker = sqlalchemy.orm.sessionmaker(db.engine)

# a simple page that says hello
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
  app.run()