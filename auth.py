from flask import Blueprint,jsonify,request
from models import User

auth_bp = Blueprint('auth',__name__)

@auth_bp.post('/signup')
def register_user():
    
    data = request.get_json()
    user = User.get_user_by_username(username=data.get("username"))

    if user is not None:
        return {"Message":"User already exist"},404
    
    # if user does not exist, create a new user and add them to the database
    new_user = User(
        username = request.get('username')
    )
    new_user.generating_hashed_password(password=request.get("password"))
    new_user.save()

    return {"Message":"User successfully created"},200



    
