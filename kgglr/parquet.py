# coding: utf-8

import pyarrow.parquet as pq
import pyarrow as pa


def to_parquet(data_df, filename):
    print(f'Saving {filename}')
    table = pa.Table.from_pandas(data_df)
    pq.write_table(table, filename)

def read_parquet(filename):
    print(f'Loading {filename}')
    table = pq.read_table(filename)
    return table.to_pandas()
