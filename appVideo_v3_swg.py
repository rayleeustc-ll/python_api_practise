from flask import Flask
from flask_restplus import Api,Resource

app = Flask(__name__)
api = Api()
api.init_app(app)


@api.route('/hello_world')
class Hello(Resource):
    def get(self):
     return 'Hello World! I am running on port 5000'

if __name__ == '__main__':
    app.run()


