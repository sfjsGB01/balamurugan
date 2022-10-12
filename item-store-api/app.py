from pickle import FALSE, TRUE
from flask import Flask
from flask_jwt_extended import JWTManager, jwt_manager
from flask_restful import Api, api
from pip import main
import sqlalchemy

from config import mysqlconfig

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = mysqlconfig
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = FALSE
app.config["JWT_SECRET_KEY"] = my.secret.key

jwt = JWTManager(app)
api=Api(app)

@app.before_first_request
def create_tables():
    pass

if __name__ == '__main__':
    app.run(debug=True)
