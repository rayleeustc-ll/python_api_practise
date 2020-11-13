from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields,marshal_with
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base.test = True

app = Flask(__name__)
api = Api(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@192.168.146.128:5432/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer,nullable=False)
    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes})"

db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="name of the video is required.",required=True)
video_put_args.add_argument("views", type=int, help="views of the video is required",required=True)
video_put_args.add_argument("likes", type=int, help="likse on the video",required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="name of the video is required.")
video_update_args.add_argument("views", type=int, help="views of the video is required")
video_update_args.add_argument("likes", type=int, help="likse on the video")

resource_fields={
    'id':fields.Integer,
    'name':fields.String,
    'views':fields.Integer,
    'likes':fields.Integer
}

#
# def abort_if_video_dosenot_exist(video_id):
#     if video_id not in videos:
#         abort(404, message="Could not find the video.....")
#
# def abort_if_video_exists(video_id):
#     if video_id in videos:
#         abort(409, message="Video already existed.....")


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self,video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="could not find the video with the id")
        return result

    @marshal_with(resource_fields)
    def put(self,video_id):
        args = video_put_args.parse_args()
        rs = VideoModel.query.filter_by(id=video_id).first()
        if rs:
            abort(409, message="the video is taken...")
        video = VideoModel(id=video_id,name=args['name'],views=args['views'],likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self,video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="could not find the video, can not update")
        if args['name']:
            result.name=args["name"]
        if args["views"]:
            result.views = args["views"]
        if args["views"]:
            result.likes = args["likes"]
        db.session.add(result)
        db.session.commit()
        return result
    def delete(self,video_id):

        return "", 204

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)