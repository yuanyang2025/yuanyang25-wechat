import base64
import binascii
from datetime import datetime
from flask import jsonify, render_template, request
from run import app

from wxcloudrun.reply import reply



def trunc_open_id(open_id: str) -> str:
    if len(open_id) == 28:
        return open_id
    if len(open_id) > 28:
        return open_id[-28:]
    
    return "0" * (28 - len(open_id)) + open_id
    

@app.route('/', methods=['GET', 'POST'])
def index():
    
    data = request.get_json()

    # 解析字段
    to_user_name = data.get("ToUserName")
    from_user_name = data.get("FromUserName")
    create_time = data.get("CreateTime")
    msg_type = data.get("MsgType")
    content = data.get("Content")
    msg_id = data.get("MsgId")

    openid = trunc_open_id(from_user_name)  # 保证长度是28字符， 即168位
    byte_id = base64.urlsafe_b64decode(openid)
    openid = binascii.hexlify(byte_id).decode("utf-8")
    
    # 返回解析结果
    response = {
        "ToUserName": from_user_name,
        "FromUserName": to_user_name,
        "CreateTime": create_time,
        "MsgType": "text",
        "Content": reply(content, openid),
    }
    
    return jsonify(response), 200


