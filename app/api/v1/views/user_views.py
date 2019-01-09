from flask import Blueprint, Flask, jsonify, request, redirect
from app.api.v1.models.user_models import UserInfo, MeetupInfo

mod = Blueprint('api', __name__)

@mod.route("/v1/users", methods = ['GET'])
def order():
    a = UserInfo({},'')
    b = a.eachUser()
    return jsonify({
        'users':b
    })

@mod.route('/v1/user/auth/signup', methods = ['POST'])
def user_signup():
    user = request.get_json("user")
    a = UserInfo(user,'')
    b = a.eachUser()
    return jsonify({
        'users':b
    })

@mod.route('/v1/user/auth/login/<int:user_id>', methods = ['GET'])
def user_login(user_id):
    c = UserInfo('',user_id)
    d = c.specificUser()
    return jsonify({
        'users':d
    })

@mod.route('/v1/add_meetups', methods = ['POST'])
def create_meetup():
    meetup = request.get_json("meetups")
    a = MeetupInfo(meetup,'')
    b = a.add_meetup()
    return jsonify({
        'meetups':b
    })