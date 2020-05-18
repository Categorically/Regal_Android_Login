import hmac
import hashlib
from regal_requests import get_hmac_variables,login_request
import time
class debug:
    on = True
def debug_print(string):
    if debug.on == True:
        print(f"[DEBUG] {string}")

def byte_to_string(bArray):
    cArr2 = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    cArr = []
    i = 0
    while i < len(bArray):
        b = bArray[i] & 255
        cArr.append(cArr2[b >> 4])
        cArr.append(cArr2[b & 15])
        i += 1
    string = "".join(list(cArr))
    return string.lower()
def keynonce_hash(timestamp, keynonce):
    """KeyNonce: uuid\n
       timestamp: length = 13"""
    # timestamp = round(int(timestamp)/1000) & -64
    message = str(timestamp) + str(keynonce)
    message = bytes(message, 'UTF-8')
    digest_output = hashlib.sha512(message).hexdigest()
    return digest_output

def get_sig(keynonce_hashed,app_instance_id,message_nonce,i,alg):
    """keynonce_hash: sha512 hexdigest\n
       app_instance_id: uuid\n
       message_nonce: uuid"""
    key = bytes(keynonce_hashed,'ascii')
    message = str(app_instance_id) + str(message_nonce)
    message = bytes(message,'ascii')
    i2 = 0
    while 1:
        if i2 == i:
            break
        if alg == "SHA384":
            hmac_digest = hmac.new(key, message, hashlib.sha384).digest()
        elif alg == "SHA256":
            hmac_digest = hmac.new(key, message, hashlib.sha256).digest()
        elif alg == "SHA512":
            hmac_digest = hmac.new(key, message, hashlib.sha512).digest()
        message = hmac_digest
        i2 += 1 
    return byte_to_string(message)
        
app_instance_id = "d30d28f7-518a-4827-a019-ff6f6c8f079d" # Static doesn't change
proxy = None
hmac_id,hmac_algorithm,hmac_iterations,hmac_keynonce,hmac_messagenonce = get_hmac_variables(app_instance_id,proxy)
print(hmac_algorithm)

timestamp = str(time.time())
keynonce_hashed = keynonce_hash(timestamp,hmac_keynonce)
hmac_hexdigest = get_sig(keynonce_hashed,app_instance_id,hmac_messagenonce,hmac_iterations,hmac_algorithm)
signature = hmac_id + ":" + hmac_hexdigest
print(signature)

login_request("USERNAME","PASSWORD",signature,proxy)