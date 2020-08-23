from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from model import User

@app.route("/add")
def add_user():
    name = request.json['name']
    email = request.json['email']
    try:
        user=User(
            name=name,
            email=email
        )
        db.session.add(user)
        db.session.commit()
        return "Book added. book id={}".format(user.id)
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)