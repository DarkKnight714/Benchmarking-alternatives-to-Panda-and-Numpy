# Benchmarking-alternatives-to-Panda-and-Numpy
 
#### The primary goal is to compare the execution times of basic data manipulation operations across various libraries.

 ```
 We benchmark three popular data processing libraries:
- Pandas
- Modin
- Dask
using a synthetic dataset of different sizes (10,000, 100,000, and 500,000 rows).
 ```
```
We benchmark the performance of three different libraries for matrix multiplication:
- NumPy
- PyTorch
- JAX.
we perform these benchmarks for matrix sizes of 1000x1000, 5000x5000, and 10000x10000
  to compare the computational efficiency of these libraries across different problem sizes.
```
### Results
##### Pandas and it's alternatives
```
https://github.com/DarkKnight714/Benchmarking-alternatives-to-Panda-and-Numpy/blob/main/results_pandas_benchmarking.md
```
```
or check this repository for the file named results_pandas_benchmarking.md
```
#### Numpy and it's alternatives
```
https://github.com/DarkKnight714/Benchmarking-alternatives-to-Panda-and-Numpy/blob/main/results_numpy_benchmarking.md
```
```
or check this repository for the file named results_numpy_benchmarking.md
```
### Conclusion for benchmarking Pandas and it's alternatives
```
- Pandas consistently demonstrates the fastest execution times across all dataset sizes.
    It is particularly efficient for small datasets, where its single-threaded nature doesn't significantly impact performance.

- Modin, which aims to parallelize Pandas operations, shows competitive performance with Pandas for larger datasets but lags behind for smaller datasets.
    This suggests that Modin's parallelization benefits become more apparent as the dataset size grows.

- Dask, a library designed for distributed computing, performs well for larger datasets but incurs a higher overhead for smaller ones.
    It involves creating partitions and distributing work, which results in slightly longer execution times for basic operations on small datasets.
```
### Conclusion for benchmarking Numpy and it's alternatives
```
-For small matrix sizes (1000x1000), all three libraries perform matrix multiplication relatively quickly, with JAX being the fastest.

-As the matrix size increases to 5000x5000 and 10000x10000, JAX continues to outperform NumPy and PyTorch by a significant margin. This is likely due to JAX's ability to compile and optimize code for GPU execution.

-NumPy and PyTorch show a significant increase in computation time as the matrix size grows, making them less efficient for large-scale matrix multiplication compared to JAX.

-The GPU was not utilized in this benchmark, which could further accelerate computation for JAX and PyTorch if properly configured with GPU support.
```
