import json

import requests

url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww9c07d84e2ca4943b&' \
      'corpsecret=jmr79mSC5_CGJOVTjlUwGmql4Up_wtqB6a4i5KodMvY'
r = requests.get(url)
response = r.json()
access_token = response['access_token']
post_data ={
      "touser":"96143",
      "msgtype" : "text",
      "agentid":1000031,
      "text":{
            "content":"我就试一下",
      },
      "safe": 0,
}
post_msges=(bytes(json.dumps(post_data), 'utf-8'))
print(access_token)
post_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+ access_token
r2 = requests.post(post_url, post_msges)
response2 = r2.json()
print(response2)