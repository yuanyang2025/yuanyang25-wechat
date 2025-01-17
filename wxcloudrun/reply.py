from . import token_generator


REGISTER = "注册"
VERICODE = "验证码"


DEFAULT_REPLY = "且看太极圆"

def add_space_every_4_chars(s):
    return ' '.join(s[i:i+4] for i in range(0, len(s), 4))

def reply(content: str, openid: str):
    
    openid_num = int(openid, 16)
    
    if content == REGISTER:
        return token_generator.get_token(2, 0, openid_num).hex()
    
    if content == VERICODE:
        return add_space_every_4_chars(token_generator.vericode(openid, 16))
    
    return DEFAULT_REPLY
    