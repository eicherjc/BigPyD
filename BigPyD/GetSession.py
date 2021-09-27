import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getSession(url, user, password, ssl=False):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "username": "{}".format(user),
        "password": "{}".format(password)
    }

    s = requests.Session()

    r = s.request("POST", url=url+"/api/v1/sessions", headers=headers, verify=ssl, json=data)
    r.raise_for_status()

    s.headers.update({"authorization": "{}".format(r.json()['auth_token'])})
    s.url=url
    return s
