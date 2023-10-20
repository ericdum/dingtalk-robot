import time
import hmac
import json
import hashlib
import base64
import urllib.parse
import urllib.request



class Robot:
    def __init__(self, secret, token):
        self.secret = secret
        self.token = token

    def signature(self, timestamp):
        secret_enc = self.secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc,
                             string_to_sign_enc,
                             digestmod=hashlib.sha256).digest()
        return urllib.parse.quote_plus(base64.b64encode(hmac_code))

    def send(self, data):
        timestamp = str(round(time.time() * 1000))
        sign = self.signature(timestamp)
        req = urllib.request.Request('https://oapi.dingtalk.com/robot/send'
                                     + '?access_token=' + self.token
                                     + '&timestamp=' + timestamp
                                     + '&sign=' + sign,
                                     data=json.dumps(data).encode('utf-8'),
                                     method="POST")

        req.add_header('Content-Type', 'application/json')
        response = urllib.request.urlopen(req).read()
        print(response.decode('utf-8'))


# 其他类型
# https://open.dingtalk.com/document/robots/custom-robot-access
class MDRobot(Robot):
    def send_message(self, content, isAtAll=False):
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "公告",
                "text": content
            },
            "at": {
                "atMobiles": [],
                "atUserids": [],
                "isAtAll": isAtAll
            }
        }
        self.send(data)


class TextRobot(Robot):
    def send_message(self, content, isAtAll=False):
        data = {
            "msgtype": "text",
            "text": {
                "content": content
            },
            "at": {
                "atMobiles": [],
                "atUserids": [],
                "isAtAll": isAtAll
            }
        }
        self.send(data)


if __name__ == '__main__':
    print("this file can not be run directly")
