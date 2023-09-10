import time
start_time = time.time()

import multiprocessing

List = []
for i in range (1,10000):
    List.append(i)

def square(x):
	return x * x
if __name__ == '__main__':
	pool = multiprocessing.Pool()
	pool = multiprocessing.Pool(processes=4)
	inputs = List
	outputs = pool.map(square, inputs)
	print("Output: {}".format(outputs))

print("--- %s seconds ---" % (time.time() - start_time))
