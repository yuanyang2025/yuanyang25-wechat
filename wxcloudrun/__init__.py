from flask import Flask

import config


# 初始化web应用
app = Flask(__name__, instance_relative_config=True)
app.config['DEBUG'] = config.DEBUG
app.config['JSON_AS_ASCII'] = False  # 保留汉字

# 加载控制器
from wxcloudrun import views

# 加载配置
app.config.from_object('config')
