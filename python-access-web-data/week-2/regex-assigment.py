import re
from functools import reduce

file_handle = open('regex-sum.txt', 'r')
num_str_list = re.findall('[0-9]+', file_handle.read())

print(reduce(lambda x, y: int(x) + int(y), num_str_list))
