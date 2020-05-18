import requests

def get_hmac_variables(AppInstanceID,proxy):
    url = "https://api.regmovies.com/v1/CrownClub/HMAC/"
    headers = {"AppInstanceID": "d30d28f7-518a-4827-a019-ff6f6c8f079d",
               "X-UA-Channel-ID": "16fc8b4e-231f-47e3-bdfb-044494fa6b8f",
               "AuthUser": "MobileApp2003a_780015146E282D5A4AAA9384C242D778",
               "X-App-Version": "7.8.0",
               "X-AppBuild": "830",
               "X-Device-OS": "Android 8.0.0",
               "X-Device-Model": "Samsung Galaxy S7",
               "Ocp-Apim-Subscription-Key": "80a7b5d4349044539f533545abf8001a",
               "Host": "api.regmovies.com",
               "Connection": "Keep-Alive",
               "Accept-Encoding": "gzip",
               "User-Agent": "okhttp/3.12.1"}
    try:
        sent_request = requests.get(url=url,headers=headers,proxies=proxy)
    except:
        print("Error while calling /v1/CrownClub/HMAC/")
        return None
    sent_request_json = sent_request.json()
    hmac_id = sent_request_json["Id"]
    hmac_algorithm = sent_request_json["Algorithm"]
    hmac_iterations = sent_request_json["Iterations"]
    hmac_keynonce = sent_request_json["KeyNonce"]
    hmac_messagenonce = sent_request_json["MessageNonce"]
    return [hmac_id,hmac_algorithm,hmac_iterations,hmac_keynonce,hmac_messagenonce]

def login_request(username,password,sig,proxy):
    url = "https://api.regmovies.com/v1/CrownClub/Member/Login"
    headers = {"AppInstanceID": "d30d28f7-518a-4827-a019-ff6f6c8f079d",
               "X-UA-Channel-ID": "16fc8b4e-231f-47e3-bdfb-044494fa6b8f",
               "AuthUser": "MobileApp2003a_780015146E282D5A4AAA9384C242D778",
               "X-App-Version": "7.8.0",
               "X-AppBuild": "830",
               "X-Device-OS": "Android 8.0.0",
               "X-Device-Model": "Samsung Galaxy S7",
               "Ocp-Apim-Subscription-Key": "80a7b5d4349044539f533545abf8001a",
               "X-Signature": str(sig),
               "Accept-Encoding": "gzip",
               "User-Agent": "okhttp/3.12.1",
               "Content-Type": "application/json; charset=UTF-8"}
    post_data = '{"credential1":"'+username+'","credential2":"'+password+'"}'
    print(headers)
    print(post_data)
    try:
        sent_request = requests.post(url=url,headers=headers,data=post_data,proxies=proxy)
    except:
        return None
    print(sent_request.text)