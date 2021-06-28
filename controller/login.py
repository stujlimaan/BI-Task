from datetime import datetime, timedelta


from flask import config,jsonify
from database import client
SECRET_KEY='thisismysecretkey'
import jwt
def login(data):
    mydb=client['BI_TASK']
    collection=mydb['user']
    user_data = collection.find({'email':data['email'],'password':data['password']})
    user_data = list(user_data)
    if (len(user_data)==0):
        return 'userid or password is wrong',404
    token = jwt.encode({'email':data['email'],'exp':datetime.utcnow()+timedelta(minutes=30),'user_type':user_data[0]['user_type']},SECRET_KEY)
    return jsonify({'token': token})
    
