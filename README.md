# Author API V1
This is a simple REST API for authors.

## Built with
- Flask
- Flask-SQLAlchemy
- MySQL

## The Endpoints

|Route | Verb | Description|
|--------|-------|----------|
|/authors| GET   |fetch all authors|
|/authors|POST    |create an author|
|/author/<int:id>/|GET |get an author with an id (integer)|
|/author/<int:id>/|PATCH|update data of an author with an id (integer)|
|/author/<int:id>/|DELETE|delete an author with an ID (integer)|


## What I learned
- Basic CRUD Operations
- JSON responses

## Testing Environment
- Postman

## Run with
Activate virtual environment
` pipenv shell `
Run app
` python3 app.py `

## Author
[Ssali Jonathan](https://github.com/jod35)