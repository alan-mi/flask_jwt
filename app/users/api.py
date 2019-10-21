# coding:utf-8
from flask import jsonify,request
from app.users.model import User
from app.auth import Auth
from .. import common


def init_api(app):
    @app.route('/register',methods=['POST'])
    def regester():
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(email=email,username=username,password=User.set_password(password))
        result = user.add(user)
        print(result)
        if user.id:
            returnUser = {
                'id':user.id,
                'username':user.username,
                'email':user.email,
                'login_time':user.login_time
            }
            return jsonify(common.trueReturn(returnUser,'用户注册成功'))
        else:
            return jsonify(common.falseReturn('','用户注册失败'))

    @app.route('/login',methods=['POST'])
    def login():
        username = request.form.get('username')
        password = request.form.get('password')
        if not all([username,password]):
            return jsonify(common.falseReturn('','不能为空'))
        else:
            return Auth.authenticate(Auth,username,password)

    @app.route('/user',methods=['GET'])
    def get():
        result = Auth.identify(Auth,request)
        if (result['status'] and result['data']):
            user = User.get(User,result['data'])
            returnUser = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'login_time': user.login_time
            }
            result = common.trueReturn(returnUser,'请求成功')
        return jsonify(result)