# coding:utf-8

from flask import Flask

# 应用定义声明
app = Flask(__name__)

# 这个import语句放在这里, 防止views, models import发生循环import
from app import views
