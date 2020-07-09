from flask import Flask,jsonify,request
import os
from flask_sqlalchemy import SQLAlchemy
from config.config import DevConfig


app=Flask(__name__)

app.config.from_object(DevConfig)

db=SQLAlchemy(app)


class Author(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(25),nullable=False)
    specialization=db.Column(db.String(25),nullable=True)

    def __init__(self,name,specialization):
        self.name=name
        self.specialization=specialization

    def __repr__(self):
        return f'Author {self.id}'



@app.route('/')
def index():
    return jsonify({"message":"Welcome to my API"})

@app.route('/authors',methods=['GET'])
def get_authors():
    authors=Author.query.all()
    author_list=[]
    for author in authors:
        author_list.append(
            {   "id":author.id,
                "name":author.name,
                "specialization":author.specialization
            }
        )

    return jsonify({"authors":author_list,"success":True})


@app.route('/authors',methods=['POST'])
def create_author():
    name=request.json['name']
    specialization=request.json['specialization']

    new_obj=Author(name=name,specialization=specialization)

    author={
        "id":new_obj.id,
        "name":new_obj.name,
        "specialization":new_obj.specialization
    }

    db.session.add(new_obj)
    db.session.commit()

    return jsonify(
        {
            "message":"Resource added",
            "success":True,
            "author":author
        }
    )

@app.route('/author/<int:id>',methods=['GET'])
def get_an_author(id):
    author=Author.query.get_or_404(id)

    obj={
        "id":author.id,
        "name":author.name,
        "specialization":author.specialization
    }

    return jsonify({
        "message":"author",
        "success":True,
        "author":obj
    })


@app.route('/author/<int:id>',methods=['PATCH'])
def update_author(id):
    author=Author.query.get_or_404(id)

    name=request.json['name']
    specialization=request.json['specialization']

    author.name=name
    author.specialization=specialization

    db.session.commit()

    new_info={
        "name":name,
        "specialization":specialization
    }

    return jsonify(
        {
            "message":"Resource Updated Successfully",
            "success":True,
            "author":new_info
        }
    )

@app.route('/author/<int:id>',methods=['DELETE'])
def delete_author(id):
    author=Author.query.get_or_404(id)

    db.session.delete(author)

    db.session.commit()

    deleted={
            "name":author.name,
            "specialization":author.specialization
        }

    return jsonify({
        "message":"Resource Deleted Successfully",
        "deleted":deleted,
        "success":True

    })



@app.errorhandler(404)
def not_found(error):
    return jsonify({"message":"Not Found",

    })

@app.errorhandler(500)
def internal_sever_error(error):
    return jsonify({
        "message":"Something aint right"
    })
if __name__ == "__main__":
    app.run(debug=True)
