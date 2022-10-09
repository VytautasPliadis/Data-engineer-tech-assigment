import os
import pandas as pd

def main():

	path=input('Enter (.parquet) file path:')
	f_name, f_ext = os.path.splitext(path)

	df = pd.read_parquet(path)
	print('Running script...')

	df.to_csv(f_name+'.csv',index=False)
	print('OK')

if __name__ == "__main__":
    main()