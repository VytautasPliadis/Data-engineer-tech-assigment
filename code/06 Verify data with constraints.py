import os
import pandas as pd

from tdda.constraints import verify_df


def main():
	# change current directory
	os.chdir('..')
	path=os.getcwd()
		
	df = pd.read_csv(path+'\\raw_data\\yellow_tripdata_2020-01.csv')
	# print(df)	
	
	v1 = verify_df(df,path+'\\reports\\yellow_tripdata_2020-01.tdda', type_checking='strict', epsilon=0)
	print(v1)

if __name__ == "__main__":
	main()