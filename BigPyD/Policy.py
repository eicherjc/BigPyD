from pandas import json_normalize
import os

class Policy:

    def __init__(self, session):
        self.s = session

        r = session.get(url=session.url + "/api/v1/compliance-rules")
        self.policies = r.json()

    def exportPolicies(self, fileName="policies.csv"):
        policiesDF = json_normalize(self.policies)

        with open(os.getcwd() + os.path.sep + fileName, "w") as file:
            file.write(policiesDF.to_csv(index=False))

        return print("Policies written to " + os.getcwd() + os.path.sep + fileName)

    def setPolicy(self, data):
        r = self.s.post(url=self.s.url + "/api/v1/compliance-rules", json=data)
        return r.json()
