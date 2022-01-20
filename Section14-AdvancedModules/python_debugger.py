x = [1,2,3]
y = 2
z = 3

result = y + z
result2 = x + y

import pdb

result_one = y + z

# Set trace before error line
pdb.set_trace()
result_two = y + x