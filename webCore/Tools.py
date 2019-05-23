#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Tools.py
@Time    :   2019/04/12 16:37:13
@Author  :   jiegemena 
@Version :   1.0
@Contact :   jiegemena@outlook.com
@License :   https://github.com/jiegemena
@Desc    :   None
'''

# here put the import lib
import json
import jgpycshare.LogTools
import jgpycshare.DateTime
from flask import session, redirect
from functools import wraps
import uuid

class Session:
    @staticmethod
    def get_session(key):
        try:
            return session.get(key)
        except Exception as e:
            print('db_sqlite3.exec:', e)
            return None

    @staticmethod
    def set_session(key, val):
        session[key] = val

def backjson(code=0, data=None, msg='error'):
    bakJson = {}
    bakJson['code'] = code
    bakJson['msg'] = msg
    bakJson['timestamp'] = jgpycshare.DateTime.DateTime().Now().ToString()
    if data is not None:
        bakJson['data'] = data
    return json.dumps(bakJson)

# 通过继承Exception或者BaseException类实现自定义异常类
class OutException(BaseException):
    def __init__(self, mesg="throw a Exception"):
        print(mesg)

def qxlog():
    log = jgpycshare.LogTools.LogTools.get_logger('web', 'info')
    return log

def apibakjson(code=0, data=None, msg='error', merid=None, key=None,datatype='json'):
    bakJson = {}
    bakJson['code'] = code
    bakJson['msg'] = msg
    bakJson['merid'] = merid
    bakJson['datatype'] = datatype
    bakJson['timestamp'] = jgpycshare.DateTime.DateTime().Now().ToString()
    bakJson['data'] = data
    bakJson['ranstr'] = str(uuid.uuid1())
    return json.dumps(bakJson)

def request_get(request,key):
    try:
        return request.args[key]
    except Exception as e:
        print(key,'is no none',e)
        return None
    
def request_post(request,key):
    try:
        return request.form[key]
    except Exception as e:
        print(key,'is no none',e)
        return None

class CApiData:
    def __init__(self, requests):
        self.log = jgpycshare.LogTools.LogTools.get_logger('api', 'info')

        self.guid = request_post(requests,'guid')
        if self.guid is None:
            self.guid = ''
        else:
            self.timespan = request_post(requests,'timespan')
            self.data = request_post(requests,'data')
            self.sign = request_post(requests,'sign')
            self.signtype = request_post(requests,'signtype')
            self.method = request_post(requests,'method')

    def postdata(self, requests):
        self.log.info('timespan=' + self.timespan + '&guid=' + self.guid + '&data=' + self.data + '&sign=' + self.sign + '&signtype=' + self.signtype + '&method=' + self.method)

    def respdata(self, code=0, data=None, msg='error', merid=None, key=None ,datatype='json'):
        bakJson = {}
        bakJson['code'] = code
        bakJson['msg'] = msg
        bakJson['merid'] = merid
        bakJson['datatype'] = datatype
        bakJson['timestamp'] = jgpycshare.DateTime.DateTime().Now().ToString()
        bakJson['data'] = data
        bakJson['ranstr'] = str(uuid.uuid1())
        jsond = json.dumps(bakJson)
        self.log.info(self.guid + '--::--' + jsond)
        return jsond

def requirLogin(func):
    @wraps(func)
    def do(*args, **kwargs):
        Login = Session.get_session('Login')
        print(Login)
        if Login is not None and len(Login) > 0:
            return func(*args, **kwargs)
        else:
            return apibakjson(code=0,data='',msg='Authentication failure') 
    return do
