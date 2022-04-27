from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)
book_details = {

}
book_parser = reqparse.RequestParser()
book_parser.add_argument("title", location="args",type=str, required = True, help="title should not be empty", action="append",dest="titles")
book_parser.add_argument("author", location="form",type=str,  required = True, help="author should not be empty")
book_parser.add_argument("price",type=float,  location="form", required = True, help="price should not be empty and must be a numeric value")
book_parser.add_argument("quantity",type=int,  location=["args","form"], required = True, help="quantity should not be empty and must be an integer",dest="inventory")
class Book(Resource):
    def get(self, book_id):
        if book_id in book_details:
            return book_details[book_id]    
        return {'message' : 'Book with ID ' + book_id + ' not found in our details'}
   
    def post(self, book_id):
        if book_id in book_details:
            return {'message' : 'Book with ID ' + book_id + ' already exists in our details'}
        args = book_parser.parse_args()
        print('Arguments '+ str(args))
        book_details[book_id] = args
        print(book_details)
        return {'message' : 'Book with ID ' + book_id + ' is added in our details'}

api.add_resource(Book, '/book/<string:book_id>')

if __name__ == '__main__':
    app.run(debug=True)