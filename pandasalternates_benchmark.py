import pandas as pd
import numpy as np
import dask.dataframe as dd
import timeit
import modin.pandas as mpd
import ray
ray.init(runtime_env={'env_vars': {'__MODIN_AUTOIMPORT_PANDAS__': '1'}})

# Create a sample DataFrame
data = {'A': np.random.rand(500000),
        'B': np.random.rand(500000),
        'C': np.random.rand(500000)}
df = pd.DataFrame(data)

# Benchmark pandas
def benchmark_pandas():
    df['D'] = df['A'] + df['B']
    result = df.groupby('C')['D'].mean()
    return result

# Benchmark Modin
def benchmark_modin():
    df_modin = mpd.DataFrame(data)
    df_modin['D'] = df_modin['A'] + df_modin['B']
    result = df_modin.groupby('C')['D'].mean()
    return result

# Benchmark Dask
ddf = dd.from_pandas(df, npartitions=4)
def benchmark_dask():
    ddf['D'] = ddf['A'] + ddf['B']
    result = ddf.groupby('C')['D'].mean().compute()
    return result


# Run and time the benchmarks
pandas_time = timeit.timeit(benchmark_pandas, number=10)
modin_time = timeit.timeit(benchmark_modin, number=10)
dask_time = timeit.timeit(benchmark_dask, number=10)

print(f"Pandas time: {pandas_time:.2f} seconds")
print(f"Modin time: {modin_time:.2f} seconds")
print(f"Dask time: {dask_time:.2f} seconds")
