from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

book_details = {

}

class Book(Resource):
    def get(self, book_id):
        if book_id in book_details:
            return book_details[book_id]
        
        return {'message' : 'Book with ID ' + book_id + ' not found in our details'}
    def post(self, book_id):
        if book_id in book_details:
            return {'message' : 'Book with ID ' + book_id + ' already exists in our details'}
        
        print('Request body contains '+ str(request.form))
        book_details[book_id] = request.form
        print(book_details)
        return {'message' : 'Book with ID ' + book_id + ' is added in our details'}
api.add_resource(Book, '/book/<string:book_id>')

if __name__ == '__main__':
    app.run(debug=True)