import requests
from bs4 import BeautifulSoup

S = requests.Session()

url = "https://openedu.ru/"

headers = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User_Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}
params = {
    "next" : "/"
}

S.get(url, headers=headers)
responce = S.get("https://openedu.ru/login/npoedsso/?next=/", headers=headers, params=params)
params = {}
a = responce.text.find("execution")
params["execution"] = responce.text[a+13:a+49]
a = responce.text.find("session_code")
params["session_code"] = responce.text[a+13:a+56]
a = responce.text.find("tab_id")
params["tab_id"] = responce.text[a+7:a+18]
params["client_id"] = "plp"

data = {
    "username" : "itmo413395",
    "password" : "qazwsx1234",
    "rememberMe" : "on"
}
url = f"https://sso.openedu.ru/realms/openedu/login-actions/authenticate?session_code={params['session_code']}&execution={params['execution']}&client_id=plp&tab_id={params['tab_id']}"

responce = S.post(url,params=params,headers=headers,data=data)
responce = S.get("https://openedu.ru/my/", headers=headers)
print(responce.text)