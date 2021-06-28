from typing import Collection
from database import client
def signup(data):
    mydb=client['BI_TASK'] 
    collection=mydb['user']
    user_data=collection.find({'email':data['email']})
    user_data=list(user_data)
    if (len(user_data) > 0):
        return 'user already esixt',403
    collection.insert(data)

    return 'success',201

