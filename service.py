from flask import Flask,request, jsonify
import json
import jwt
from sqlalchemy import create_engine, text
from pymysql.cursors import DictCursor
import datetime
from functools import wraps

engine = create_engine('mysql+pymysql://root:root@localhost/msportal_sqa')
conn = engine.raw_connection()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'THIS IS MY KEY'


def jwt_token_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not request.headers.get('Authorization'):
            return dict(error="No token provided")
        token = request.headers.get('Authorization').replace("Bearer","").lstrip()
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'],algorithms=['HS256'])
        except jwt.exceptions.InvalidSignatureError:
            return dict(error="Invalid token")
        except jwt.exceptions.ExpiredSignatureError:
            return dict(error="Token expired")
        return func(*args,**kwargs)
    return wrapper


@app.route('/token',methods=['POST'])
def get_token():
    if request.method == 'POST':
        data = request.data
        if not isinstance(data,dict):
            data = json.loads(data)
        if 'user' in data:
            token = jwt.encode({'user':data['user'],'exp':datetime.datetime.now()+datetime.timedelta(minutes=1)},app.config['SECRET_KEY'],algorithm="HS256")
            return jsonify({'token':token})


@app.route('/index',methods = ['POST','GET'])
@jwt_token_required
def index():
    if request.method == 'GET':
        qry = "select * from emotions"
        cursor = conn.cursor(DictCursor)
        cursor.execute(qry)
        data = cursor.fetchall()
        return {'response':data}

    if request.method == 'POST':
        data = request.data
        if not isinstance(data,dict):
            data = json.loads(data)
        return {'response':"The value is"+str(data['i']**2)}

    if request.method == 'PATCH':
        pass



if __name__ == '__main__':
    # pass
    app.run()
