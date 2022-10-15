# Beyond Analysis - Data Engineer Technical assignment - 2022-10-09
 
## Dependencies
- Language: Python 3.10.2
- Python Packages / Libraries: pandas, pandas-profiling, tdda

## Dataset
- [2020 January Yellow Taxi Trip Records (parquet).](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet)
- To convert .parquet file to .csv please use `00 Convert parquet to csv.py` script and move into `raw_data` directory

## Directory
- `code`: Contains scripts for assignment
- `raw_data`: Contains main cvs file
   - `splitted_csv`: Contains splited parts of the main csv file
   - `sqlite`: Contains SQLite database with loaded files from above
- `reports`: Contains data profiling, data quality raport and data constraint file
   - `AWS Glue DataBrew report`: Contains screenshots of custom data sample statistic/profile overwiev made by AWS
- `processed_data`: Contains data entity relationship diagram

## Summary and week points
- After spliting by date `yellow_tripdata_2020-01.csv` file, found that file has invalid timeframe values (2003, 2008, 2009...) 
- Data profiling and constraints validation showed that `yellow_tripdata_2020-01.csv` has additional quality issues, check `Quality Raport.pdf` 
- `06 Verify data with constraints.py` script cannot validate the timeliness metric (invalid timeframe values mentioned above)

