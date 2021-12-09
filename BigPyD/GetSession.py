import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getSession(url, user, password, ssl=False):
    """Use this method for basic auth, same as you'd login with the web UI
    (assuming you're not using an SSO)"""
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

def getSessionRT(url, RefreshToken, ssl=False):
    """Use this method when using a refresh token generated from the Access
    Management page"""
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "{}".format(RefreshToken)
    }

    s = requests.Session()

    r = s.request("GET", url=url+"/api/v1/refresh-access-token", headers=headers, verify=ssl)
    r.raise_for_status()

    s.headers.update({"authorization": "{}".format(r.json()['systemToken'])})
    s.url=url
    return s