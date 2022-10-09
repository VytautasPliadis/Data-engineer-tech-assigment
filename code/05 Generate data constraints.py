import os
import pandas as pd
from tdda.constraints import discover_df

def main():
	# change current directory
	os.chdir('..')
	path=os.getcwd()
	
	# #read csv file
	df = pd.read_csv(path+'\\raw_data\\yellow_tripdata_2020-01.csv')

	#generate constraints based on yellow_tripdata_2020-01.csv
	constraints = discover_df(df)
	with open('reports\\yellow_tripdata_2020-01.tdda', 'w') as f:
		f.write(constraints.to_json())
	print('OK')

if __name__ == "__main__":
	main()