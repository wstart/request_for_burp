#coding:utf-8
from requests_toolbelt import MultipartEncoder
# pip install requests_toolbelt
import requests


def getHeadArray(hstring):
    _k_vs =  hstring.split("\n")
    retunr_k_v = {}

    for _v in _k_vs:
        _v = _v.strip()
        if _v:
            _v = _v.split(":")
            print(_v)
            if _v[0].strip() == "Host":
                continue
            retunr_k_v[_v[0].strip()] =_v[1].strip()
    return  retunr_k_v


def getBody(bstirng):
    _b_s  = bstirng.split("&")
    retunr_k_v = {}
    for _b_i in  _b_s:
        print(_b_i)
        if _b_i:
            _b_i = _b_i.split("=")
            retunr_k_v[_b_i[0].strip()] =_b_i[1].strip()
    if 'multipart/form-data' in headers['Content-Type']:
        m = MultipartEncoder(
            fields= retunr_k_v
                # 'field2': ('filename', open('file.py', 'rb'), 'text/plain') 文件请自行确认 复制本行 放到 return_k 里面
        )
        headers['Content-Type'] = m.content_type
        retunr_k_v  =  m
    return  retunr_k_v


if __name__ =="__main__":
    global headers
    global bodys
    timeout = 3

    proxies = {
      "http": "http://127.0.0.1:8080",
      "https": "http://127.0.0.1:8080",
    }
    url = ""
    ispost = True
    headers_string =  '''
    header
    '''
    bodys = '''
    body
    '''
    headers  = getHeadArray(headers_string)


    bodys =  getBody(bodys)

    if ispost:
        r = requests.post(url,proxies=proxies,timeout=timeout,headers=headers,data=bodys)
    else:
        r= requests.get(url,proxies=proxies,timeout=timeout,headers=headers)


    print( r.text)
