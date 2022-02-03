import sys
import requests
import winsound
import sched, time

host = "https://ec-lisboa.itamaraty.gov.br"
duration = 2000  # milliseconds
freq = 840  # Hz
    
serviceName = sys.argv[1]
_login = sys.argv[2]
_pass = sys.argv[3]

print(serviceName)

def econsular():
    session = requests.Session()
    path = '/availability'
    print("Request: " + host + path)
    authPage = session.get(host + path)
    print("Response: " + authPage.url)
    print(authPage)

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

    if result.find("mais tarde") < 0:
        winsound.Beep(freq, duration)

econsular()

s = sched.scheduler(time.time, time.sleep)

def sched_method(sc): 
    econsular()
    s.enter(60, 1, sched_method, (sc,))

s.enter(60, 1, sched_method, (s,))
s.run()