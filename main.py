import ctypes

lib = ctypes.CDLL("./libutil.so")

result = lib.sum_numbers(1000000)

print(result)
