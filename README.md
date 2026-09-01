# Databento Parquet Builder

This takes databento csv format and into parquet. 
## Notes:
- By default, polars uses zstd compression level 3
- Data is stored in UTC but polars which has written it reads it as ET
- Only for Nasdaq Futures (I don't know the format for options etc)
- test.parquet is a duckdb version but neither duckdb nor polars read it as ET

## Findings:

- 2010-06-06->2012-11-15: maintenance break at 17:30
- 2012-11-16->2015-09-18: maintenance break at 17:15
- 2015-09-19->Now       : maintenance break at 17:00

--- 

### Disclaimer

This was a quick small project to quickstart P6 duckdb/parquet adoption and not many tests on the data were conducted.