import pandas as pd 
import os

def splitCsv(fileName,data_path):
    # read the csv and add a 'data_filters' column for indexing
    df=pd.read_csv(fileName)
    df['date_filters'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    df['date_filters'] = df['date_filters'].dt.strftime('%Y-%m-%d') 
    
    # iterate over the days present
    for day in df['date_filters'].unique():
        # split the days
        day_df = df[df['date_filters'] == day]
        # drop the additional 'date_filters' column
        day_df.drop('date_filters', inplace=True, axis=1)
        # make the path and save
        day_path = os.path.join(data_path, fileName+'_splited_'+day +'.csv')
        print(day_path)
        day_df.to_csv(day_path, index=False)
        
def main():
    # make dir for splitted csv
    os.chdir('..')
    path=os.getcwd()
    if not os.path.exists(path+'\\raw_data\\splitted_csv'):
        os.mkdir(path+'\\raw_data\\splitted_csv')
    
    # change current directory
    os.chdir(path+'\\raw_data')
    #split all csv in a folder
    for count, f in enumerate(os.listdir()):
        if f.split('.')[-1] =='csv':
            print(f)
            splitCsv(f,path+'\\raw_data\\splitted_csv')
                
if __name__ == "__main__":
    main()
