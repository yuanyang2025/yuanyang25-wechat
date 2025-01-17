import hashlib
from random import SystemRandom
import time


from config import vericode_token, register_token
# version: 8 bits
# openid: ￼28 * 6 = 168 bits
# time: in minutes, 32bit￼
# mark: 8bits
# nonce: ￼40bits
# Hash: SHA256 256


print("############## vericode token in use", vericode_token)
print("############## register token in use", register_token)


def get_time():
    t = int(time.time() / 60) & 0xffffffff
    return t
    

def get_nonce():
    c = SystemRandom()
    return c.getrandbits(40)

def get_token(version, mark, openid):
    version = version & 0xff
    mark = mark & 0xff
    
    token = version
    
    token <<= 168
    token |= openid # 168bits
    
    token <<= 32
    token |= get_time() # 32bits
    
    token <<= 8
    token |= mark #8bits
    
    token <<= 40
    token |= get_nonce() #40bits
    
    byte_array = token.to_bytes(32, byteorder='big', signed=False)
    
    
    # print("raw ", byte_array.hex())
    
    hash = hashlib.sha256(byte_array)
    hash.update(register_token.encode("utf-8"))
    hash = hash.digest()
    
    # print("hash", hash.hex())
    
    result =bytes(a ^ b for a, b in zip(byte_array, hash)) + hash
 
    return result
    



#openid: lower case hex humber, which length is 168 bits or 42 hexadecimal digits
def vericode(openid: str, len: int) -> str:
    hash = hashlib.sha512()
    hash.update(openid.encode())
    hash.update(vericode_token.encode())
    
    t = int(time.time()) // 120
    byte_array = (t & 0xFFFFFFFFFFFFFFFF).to_bytes(8, byteorder='little')
    hash.update(byte_array)
    
    hash = hash.digest()
    return hash.hex()[:len]