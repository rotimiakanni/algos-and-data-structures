# with open('sample.txt', 'w') as fil:
#     fil.write(str(100000))
#     for x in range(100000):
#         fil.write(str(x) + '\n')
#     fil.close()

import time

start = time.time()

fil = open('sample.txt')
total_sample = int(fil.readline())
number_arr = [fil.readline() for x in range(total_sample)]

begin_ = 0
end_ = total_sample - 1


start = time.time()
new_arr = []
for x in range(50000):
    new_arr.append(number_arr[x])
print(f'time taken for n2 for half array is {time.time() - start}')

start = time.time()
new_arr = []
for x in range(total_sample):
    new_arr.append(number_arr[x])
print(f'time taken for n2 is {time.time() - start}')

start = time.time()
new_arr = number_arr[::-1]
print(f'time taken for inbuilt function is {time.time() - start}')


start = time.time()

while begin_ <= end_:
    number_arr[begin_], number_arr[end_] = number_arr[end_], number_arr[begin_]
    begin_ += 1
    end_ -= 1

print(f'time taken is {time.time() - start}')