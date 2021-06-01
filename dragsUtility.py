import pandas as pd

class DragsUtility:
	def __init__(self):
		self.drags = pd.read_csv("Data/drags.csv")
		self.drags["ID"] = list(map(lambda x: str(x), list(self.drags["ID"])))
	
	def isaDrag(self, ID):
		return ID in list(map(lambda x: str(x), list(self.drags["ID"])))
	
	def getRealRanking(self):
		temp_df = self.drags
		temp_df = temp_df.sort_values(by=["Place"])
		return list(temp_df["Name"])

	def getDBRanking(self):
		temp_df = self.drags
		temp_df = temp_df.sort_values(by=["DB_scores"], ascending=False)
		return list(temp_df["Name"])
	
	def getAgeRankig(self):
		temp_df = self.drags
		temp_df = temp_df.sort_values(by=["Age"])
		return list(temp_df["Name"])
	
	def getInfoAboutQueenByName(self, name):
		temp = self.drags.loc[self.drags['Name'] == name]
		return {"ID":list(temp["ID"])[0] ,\
"Name": list(temp["Name"])[0],\
"Twitter_handler": list(temp["Twitter_handler"])[0],\
"Age": list(temp["Age"])[0],"City": list(temp["City"])[0],\
 "Episode_eliminated": list(temp["Episode_eliminated"])[0] ,\
 "Wins": list(temp["Wins"])[0] ,\
 "Bottoms": list(temp["Bottoms"])[0],\
 "DB_scores": list(temp["DB_scores"])[0] }

	def getInfoAboutQueenByID(self, ID):
		temp = self.drags.loc[self.drags['ID'] == ID]
		return {"ID":list(temp["ID"])[0] ,\
"Name": list(temp["Name"])[0],\
"Twitter_handler": list(temp["Twitter_handler"])[0],\
"Age": list(temp["Age"])[0],"City": list(temp["City"])[0],\
 "Episode_eliminated": list(temp["Episode_eliminated"])[0] ,\
 "Wins": list(temp["Wins"])[0] ,\
 "Bottoms": list(temp["Bottoms"])[0],\
 "DB_scores": list(temp["DB_scores"])[0] }
	
	def getDataFrame(self):
		return self.drags

