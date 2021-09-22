class DSAR:

    def __init__(self, session):
        self.s = session

        r = session.get(url=session.url + "/api/v1/sar/profiles", headers=session.headers, verify=False)
        self.profileId = r.json()['profiles'][0]['_id']

    def search(self, userName="", userId="", allAttributes="true"):
        r = self.s.get(url=self.s.url + "/api/v1/sar/search/entity-sources?profileId=" + self.profileId + "&userName=" + userName + "&userId=" + userId + "&allAttributes=" + allAttributes, headers=self.s.headers, verify=False)
        return r.json()

    def run(self, userId, displayName, attributes={}):
        data = {"profileId":"{}".format(self.profileId),
            "userDetails": {
                "userId": "{}".format(userId),
                "displayName": "{}".format(displayName),
                "attributes": attributes
            }
        }

        r = self.s.post(url=self.s.url + "/api/v1/sar/reports", headers=self.s.headers, json=data)
        return r.json()

    # def bulk(self):


    def delete(self, requestId):
        r = self.s.post(url=self.s.url + "/api/v1/sar/reports/" + requestId + "/request-for-remove", headers=self.s.headers, verify=False)
        return r.json()

    def profiles(self):
        r = self.s.get(url=self.s.url + "/api/v1/sar/profiles", headers=self.s.headers, verify=False)
        return r.json()
