import numpy as np
import torch
import jax
import jax.numpy as jnp
import timeit

# Define the size of the matrices
matrix_size = 10000

# Create a random key for JAX
rng = jax.random.PRNGKey(0)

# Create random matrices
numpy_matrix = np.random.rand(matrix_size, matrix_size)
torch_matrix = torch.rand(matrix_size, matrix_size)
jax_matrix = jax.random.normal(rng, (matrix_size, matrix_size))

def benchmark_numpy():
    result = np.dot(numpy_matrix, numpy_matrix)
    return result

def benchmark_pytorch():
    result = torch.mm(torch_matrix, torch_matrix)
    return result

def benchmark_jax():
    result = jnp.dot(jax_matrix, jax_matrix)
    return result

numpy_time = timeit.timeit(benchmark_numpy, number=10)
pytorch_time = timeit.timeit(benchmark_pytorch, number=10)
jax_time = timeit.timeit(benchmark_jax, number=10)


print(f"Numpy time: {numpy_time:.2f} seconds")
print(f"PyTorch time: {pytorch_time:.2f} seconds")
print(f"JAX time: {jax_time:.2f} seconds")
