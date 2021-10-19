class DSAR:

    def __init__(self, session):
        self.s = session

        r = session.get(url=session.url + "/api/v1/sar/profiles")
        self.profileId = r.json()['profiles'][0]['_id']


    def search(self, userName="", userId="", allAttributes="true"):
        r = self.s.get(url=self.s.url + "/api/v1/sar/search/entity-sources?profileId=" + self.profileId + "&userName=" + userName + "&userId=" + userId + "&allAttributes=" + allAttributes)
        return r.json()


    def run(self, userId, displayName, attributes={}):
        data = {"profileId":"{}".format(self.profileId),
            "userDetails": {
                "userId": "{}".format(userId),
                "displayName": "{}".format(displayName),
                "attributes": attributes
            }
        }

        r = self.s.post(url=self.s.url + "/api/v1/sar/reports", json=data)
        return r.json()


    def bulk(self, data):
        r = self.s.post(url=self.s.url + "/api/v1/sar/reports/bulk", json=data)
        return r.json()

    def scans(self, limit="100", state="Completed"):
        """The other option here for state would be "Started" """
        r = self.s.get(url=self.s.url + "/api/v1/sar/scans?limit=" + limit + "&state=" + state)
        return r.json()


    def scanDetail(self, requestId):
        r = self.s.get(url=self.s.url + "/api/v1/sar/scans/" + requestId)
        return r.json()


    def delete(self, requestId):
        r = self.s.post(url=self.s.url + "/api/v1/sar/reports/" + requestId + "/request-for-remove")
        return r.json()


    def profiles(self):
        r = self.s.get(url=self.s.url + "/api/v1/sar/profiles")
        return r.json()
