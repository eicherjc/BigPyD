import pandas

class SarReports:

	def __init__(self, session):
		self.s = session
		self.records = []

	# Get all individual Sar IDs based on a Sar profile ID. The Sar profile ID for a retention Sar is in the "Display Name"
	def getSarIDs(self, profileID, state="Completed", limit=100):
		sars = self.s.get(url=self.s.url + "/api/v1/sar/scans?state=" + state + "&skip=0&limit=" + str(limit))

		sarids = []

		for x in sars.json()['scans']:
			if x['profile_id'] == profileID:
				sarids.append(x['_id'])

		return sarids

	# Get the actual records for an individual Sar, filtering for the specific attribute you want
	def getSarRecords(self, sarid, attribute, limit=20000, offset=0):
		sar = self.s.get(url=self.s.url + "/api/v1/sar/reports/" + sarid + "?limit=" + str(limit) + "&offset=" + str(offset))

		records = []

		for x in sar.json()['records']:
			if x['attribute'] == attribute:
				records.append(x)

		return records

	# Feed all the Sar IDs into the getSarRecords function to get one list of all records from all Sars of a given Retention Policy evaluation
	def getRetentionRecords(self, profileID, attribute):
		self.profileID = profileID
		self.attribute = attribute

		records = []

		for x in self.getSarIDs(profileID):
			records.extend(self.getSarRecords(x, attribute))

		self.records = records

	def exportRetentionRecordsFull(self):
		if not self.records:
			return print("You need to run the getRetentionRecords method first")

		df = pandas.DataFrame(self.records)
		df.to_csv("full_retention_report_" + self.profileID + "_" + self.attribute + ".csv", index=False)

		return print("Retention Records Full Report of " + self.profileID + " profile for the " + self.attribute + " attribute written to current directory.")

	def exportRetentionRecordsCounts(self):
		if not self.records:
			return print("You need to run the getRetentionRecords method first")

		df = pandas.DataFrame(self.records)
		countdf = df.groupby("fullObjectName").count()
		countdf.to_csv("count_retention_report_" + self.profileID + "_" + self.attribute + ".csv")

		return print("Retention Records Count Report of " + self.profileID + " profile for the " + self.attribute + " attribute written to current directory.")