import jwt
SECRET_KEY='thisismysecretkey'
def auth(req,auth_type):
    token=req.headers.get('Authorization')
    if token==None:
        return False
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=['HS256']      )
    except:
        return False
    if payload['user_type']== auth_type:
        return True

