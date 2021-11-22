class Scan:

    def __init__(self, session):
        self.s = session

        r = session.get(url=session.url + "/api/v1/scanProfiles")
        self.profile = r.json()['scanProfiles'][0]['name']
        self.scanProfiles = r.json()['scanProfiles']

    def getProfileDetails(self, scanProfile):
        return next((profile for profile in self.scanProfiles if profile["name"] == "{}".format(scanProfile)), None)

    def run(self, scanProfile=None):
        if scanProfile == None:
            scanProfile = self.profile
        
        scanDetails = self.getProfileDetails(scanProfile)

        if scanDetails == None:
            raise ValueError("""Scan profile does not exist. 
                If you are trying to run a scan profile you just added, 
                try using getScanProfiles to update the scan profiles.""")

        else:
            data = {"scanType":"{}".format(scanDetails['scanType']),
            "scanProfileName":"{}".format(scanProfile),
            "scanOrigin":"Invoked manually"
            }

            r = self.s.post(url=self.s.url + '/api/v1/scans', json=data)
            return r.json()

    def setScan(self, data):
        r = self.s.post(url=self.s.url + "/api/v1/scanProfiles", json=data)
        return r.json()

    def getScanProfiles(self):
        r = self.s.get(url=self.s.url + "/api/v1/scanProfiles")
        self.scanProfiles = r.json()['scanProfiles']
        return r.json()
