import polars as pl
import duckdb

def write_db():
    q = pl.scan_csv("E-mini_Nasdaq-100_Futures/E-mini_Nasdaq-100_Futures.csv").select(
        pl.col("ts_event").str.to_datetime(time_zone="America/New_York"), "instrument_id", "symbol", "open", "high", "low", "close",
        "volume")

    df = q.collect()
    df.write_parquet(file="E-mini_Nasdaq-100_Futures.parquet")

    duckdb.sql("CREATE TABLE temp AS "
               "SELECT * FROM df;")

    duckdb.sql("COPY "
               "(SELECT * FROM temp)"
               "TO 'test.parquet' "
               "(FORMAT parquet, COMPRESSION zstd, COMPRESSION_LEVEL 3);")

    duckdb.sql("DROP TABLE temp;")



def read_db():
    q = pl.scan_parquet("E-mini_Nasdaq-100_Futures.parquet")
    df = q.collect()
    return df


if __name__ == '__main__':
    write_db()
