def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10))

def func_two(n):
    return list(map(str, range(n)))

print(func_two(10))

import time

# Grab current time code
start_time = time.time()
# Run code
result = func_one(1000000)
# Grab current time after code
end_time = time.time()

elapsed_time = end_time - start_time
print(elapsed_time)

# Grab current time code
start_time = time.time()
# Run code
result = func_two(1000000)
# Grab current time after code
end_time = time.time()

elapsed_time = end_time - start_time
print(elapsed_time)

import timeit
stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup, number=100000))

stmt = '''
func_two(100)
'''

setup = '''
def func_two(n):
    return list(map(str, range(n)))
'''

print(timeit.timeit(stmt, setup, number=100000))