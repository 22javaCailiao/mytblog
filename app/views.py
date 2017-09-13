# coding:utf-8

from app import app
from flask import render_template


@app.route("/")
def index():
    """
    项目入口地址
    """
    return render_template("index.html")
