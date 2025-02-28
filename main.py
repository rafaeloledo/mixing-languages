import ctypes

lib = ctypes.CDLL("./libutil.so")

lib.sum_numbers.argtypes = [ctypes.c_long]
lib.sum_numbers.restype = ctypes.c_long

result = lib.sum_numbers(1000000)

print(result)
