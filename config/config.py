
import os

db_passw=os.environ['MYSQL_DB_PASSWORD']
db_user=os.environ['MYSQL_DB_USER']

class DevConfig:
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://{}:{}@localhost/author_db'.format(
        db_user,db_passw
    )
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY ='21a429d68b409b201eb71c5c'
