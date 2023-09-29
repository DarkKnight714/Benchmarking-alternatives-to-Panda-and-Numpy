## Benchmarking Results for Numpy and it's alternatives

Here are the benchmarking results for the different matrix sizes. Each set of results represents the execution times for 10 runs of the respective operation.

```
Libraries used for benchmarking are 
1.Numpy
2.PyTorch
3.JAX
```
### For Matrix size 1000 x 1000
```
#Trial 1
- Numpy time: 0.19 seconds
- PyTorch time: 0.26 seconds
- JAX time: 0.10 seconds

#Trial 2
- Numpy time: 0.18 seconds
- PyTorch time: 0.21 seconds
- JAX time: 0.10 seconds

#Trial 3
- Numpy time: 0.25 seconds
- PyTorch time: 0.27 seconds
- JAX time: 0.10 seconds
```
### For Matrix size 5000 x 5000
```
#Trial 1
- Numpy time: 16.69 seconds
- PyTorch time: 26.57 seconds
- JAX time: 8.13 seconds

#Trial 2
- Numpy time: 16.57 seconds
- PyTorch time: 26.94 seconds
- JAX time: 7.79 seconds

#Trial 3
- Numpy time: 16.57 seconds
- PyTorch time: 26.15 seconds
- JAX time: 7.96 seconds
```
### For Matrix size 10000 x 10000
```
#Trial 1
- Numpy time: 133.41 seconds
- PyTorch time: 202.40 seconds
- JAX time: 56.87 seconds

#Trial 2
- Numpy time: 129.54 seconds
- PyTorch time: 203.92 seconds
- JAX time: 57.47 seconds

#Trial 3
- Numpy time: 146.85 seconds
- PyTorch time: 217.88 seconds
- JAX time: 63.08 seconds
```
