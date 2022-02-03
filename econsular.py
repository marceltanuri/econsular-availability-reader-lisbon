import sys
import requests

host = "https://ec-lisboa.itamaraty.gov.br"
serviceName = sys.argv[1]
_login = sys.argv[2]
_pass = sys.argv[3]


session = requests.Session()
path = '/availability'
print("Request: " + host + path)
authPage = session.get(host + path)
print("Response: " + authPage.url)
print(authPage)

host = "https://ec-lisboa.itamaraty.gov.br"
path = "/login"
_header = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
formData = "email=" + _login + "&pass="+_pass

print("Request: " + host + path)
econsularPrivatePage = session.post(
    host + path, headers=_header, data=formData)
print("Response: " + econsularPrivatePage.url)
print(econsularPrivatePage)

path = '/availability'
print("Request: " + host + path)
econsularPrivatePage = session.get(host + path)
print("Response: " + econsularPrivatePage.url)
print(econsularPrivatePage)

result = econsularPrivatePage.text.split('<td class="align-middle">'+serviceName+'</td>')[
    1].split('<td class="align-middle">')[1].split('</td></tr><tr>')[0]

print("Disponibilidade do Serviço: " + serviceName)
print(result)
