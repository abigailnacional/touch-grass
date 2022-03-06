from flask import Flask
from touchgrass import create_app
import os
from flask_sqlalchemy import SQLAlchemy, request
import sqlalchemy.orm

app = create_app()
db = SQLAlchemy(app)
sessionmaker = sqlalchemy.orm.sessionmaker(db.engine)

# a simple page that says hello
@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
  app.run()