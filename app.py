import os
from flask import Flask, request, jsonify
#from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

app = Flask(__name__)
# api = Api(app)

app.config.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#from user import User


@app.route("/")
def hello():
    return "Hello Berries!"

@app.route("/add",methods=['POST'])
def add_user():
    data = request.get_json(force=True)
    try:
        user=User(
            name=data['name'],
            email=data['email']
        )
        db.session.add(user)
        db.session.commit()
        return "User added. User id={}".format(user.id)
        # return 'success'
    except Exception as e:
	    return(str(e))

@app.route("/users")
def get_users():
    try:
        user=User.query.all()
        return  jsonify([e.serialize() for e in user])
        #return  "{happy:true}"

    except Exception as e:
	    return(str(e))



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)