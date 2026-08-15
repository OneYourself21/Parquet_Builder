import polars as pl

if __name__ == '__main__':
    q = pl.scan_csv("E-mini_Nasdaq-100_Futures/E-mini_Nasdaq-100_Futures.csv").select(
        pl.col("ts_event").str.to_datetime(time_zone="EST"), "instrument_id", "symbol", "open", "high", "low", "close", "volume")


    df = q.collect()
    df.write_parquet(file = "E-mini_Nasdaq-100_Futures.parquet")
