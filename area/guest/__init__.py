#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   guest.py
@Time    :   2019/04/12 17:47:35
@Author  :   jiegemena 
@Version :   1.0
@Contact :   jiegemena@outlook.com
@License :   https://github.com/jiegemena
@Desc    :   None
'''


# here put the import lib
from flask import Blueprint, request, current_app, render_template, redirect, make_response
import webCore.Tools
import uuid
import entity.Entity
import jgpycshare.StringTools
import services.userservice
import area.guest.deal

guest_bp = Blueprint('guest', __name__, template_folder="templates",
                   static_url_path='', static_folder='static')

@guest_bp.after_request
def after_request(response):
    return response

@guest_bp.before_request
def print_request_info():
    pass
    # print("api_bp.before_request-请求地址：print_request_info:" + str(request.path))
    # for key in request.form:
    #         print("api_bp.before_request-key：{}   value：{}".format(key, request.form[key]))


@guest_bp.route('/home', methods=['GET', 'POST'])
def home():
    cookie = request.cookies.get(current_app.config['WEBNAME']) 
    return webCore.Tools.apibakjson(data=cookie)


@guest_bp.route('/', methods=['GET', 'POST'])
def index():
    return redirect('/ui/index')
    # resp = make_response(render_template('index.html'))
    # gio = str(uuid.uuid1())
    # resp.set_cookie(current_app.config['WEBNAME'], gio)
    # return resp

@guest_bp.route('/api/<action>', methods=['GET', 'POST'])
def api(action):
    CApiData = webCore.Tools.CApiData(request)
    userService = services.userservice.CUserService()
    # login
    if action == 'login':
        username = webCore.Tools.request_post(request, 'username')
        pwd = webCore.Tools.request_post(request, 'pwd')
        pwd = jgpycshare.StringTools.StringTools.get_login_pass(pwd)
        user = userService.getUserFromUserNameAndPwd(username,pwd)
        print(user)
        if user is None:
            return CApiData.respdata(code=0,data='',msg='errorlogin') # webCore.Tools.apibakjson(code=0,data='',msg='errorlogin')

        userService.updateLoginGuidById(user['id'])

        user = userService.userentity.findById(user['id'])
        if user is None:
            return CApiData.respdata(code=0,data='',msg='errorlogin')
        print(user)
        
        user['password'] = ''
        return CApiData.respdata(code=1,data=user,msg='success') # webCore.Tools.apibakjson(code=1,data=user,msg='success')

    # login in
    guid = action
    user = userService.getUserByLoginGuid(guid)
    if user is None:
        return CApiData.respdata(code=0,data='',msg='errorlogin')
    
    CApiData.postdata()

    print(CApiData.guid)

    if CApiData.method == 'register':
        resp = area.guest.deal.register()
        return CApiData.respdata(code=1,data='',msg=resp)

    if CApiData.method == 'unregister':
        resp = area.guest.deal.register()
        return CApiData.respdata(code=1,data='',msg=resp)


    return 'welcome web api!'


@guest_bp.route('/ui/<action>', methods=['GET', 'POST'])
def ui(action):
    if action == 'index':
        # resp = make_response(render_template('index.html'))
        # gio = str(uuid.uuid1())
        # resp.set_cookie(current_app.config['WEBNAME'], gio)
        return render_template('index.html')
    if action == 'login':
        return render_template('login.html')
    if action == 'log':
        return render_template('log.html')
    if action == 'settings':
        return render_template('settings.html')
    return 'welcome web demo!'