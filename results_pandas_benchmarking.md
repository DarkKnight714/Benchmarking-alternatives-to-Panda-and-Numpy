## Benchmarking Results for Pandas and it's alternatives

Here are the benchmarking results for the different dataset sizes. Each set of results represents the execution times for 10 runs of the respective operation.

### For 10,000 Rows
```
#Trail 1
- Pandas time: 0.04 seconds
- Modin time: 16.91 seconds
- Dask time: 0.80 seconds

#Trail 2
- Pandas time: 0.04 seconds
- Modin time: 30.82 seconds
- Dask time: 1.00 seconds

#Trail 3
- Pandas time: 0.04 seconds
- Modin time: 20.51 seconds
- Dask time: 0.71 seconds
```
### For 100,000 Rows
```
#Trail 1
- Pandas time: 0.45 seconds
- Modin time: 22.82 seconds
- Dask time: 1.16 seconds

#Trail 2
- Pandas time: 0.42 seconds
- Modin time: 16.55 seconds
- Dask time: 1.13 seconds

#Trail 3
- Pandas time: 0.43 seconds
- Modin time: 33.07 seconds
- Dask time: 0.98 seconds
```
### For 500,000 Rows
```
#Trail 1
- Pandas time: 2.55 seconds
- Modin time: 50.89 seconds
- Dask time: 3.11 seconds

#Trail 2
- Pandas time: 2.62 seconds
- Modin time: 54.95 seconds
- Dask time: 2.77 seconds

#Trail 3
- Pandas time: 2.59 seconds
- Modin time: 59.38 seconds
- Dask time: 3.07 seconds
```
