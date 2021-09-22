from pandas import json_normalize
import os

class Policy:

    def __init__(self, session):
        self.s = session

        r = session.get(url=session.url + "/api/v1/compliance-rules", headers=session.headers, verify=False)
        self.policies = r.json()

    def exportPolicies(self, fileName="policies.csv"):
        policiesDF = json_normalize(self.policies)

        with open(os.getcwd() + os.path.sep + fileName, "w") as file:
            file.write(policiesDF.to_csv(index=False))

        return print("Policies written to " + os.getcwd() + os.path.sep + fileName)

    def setPolicy(self, name, desc, ptype, query, threshold, owner=""):
        data = {
            "name": "{}".format(name),
            "type": "{}".format(ptype),
            "description": "{}".format(desc),
            "owner": "{}".format(owner),
            "complianceRuleCalc":
            {
                "bigidQuery": "{}".format(query),
                "maxFindings": "{}".format(threshold)
            },
            "taskSettings":
            {
                "includeObjectsReport": True,
                "includeLinkToInventory": True
            },
            "is_enabled": True,
            "apps":
            [],
            "actions":
            [],
            "tpaAdditionalParams": ""
        }