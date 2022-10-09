import os
import pandas as pd
from pandas_profiling import ProfileReport

def main():
	# change current directory
	os.chdir('..')
	path=os.getcwd()
		
	#generate report for yellow_tripdata_2020-01.csv
	df = pd.read_csv(path+'\\raw_data\\yellow_tripdata_2020-01.csv')
	profile = ProfileReport(df, title="Data Profiling Report (yellow_tripdata_2020-01)")
	profile.to_file("Data profiling.html")

	
if __name__ == "__main__":
	main()