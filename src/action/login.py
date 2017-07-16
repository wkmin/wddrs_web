# _*_ coding:utf-8 _*_
from flask import Blueprint, render_template,request,session,redirect

login = Blueprint('login', __name__)
@login.route('/')
def LoginPageInit():
    return render_template('login.html')

@login.route('/index')
def index():
    return render_template('index.html')
