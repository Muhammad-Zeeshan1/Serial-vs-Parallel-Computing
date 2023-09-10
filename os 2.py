import time
start_time = time.time()

List = []
for i in range (1,10000):
    List.append(i)

for i in range(len(List)):
       print(i * i)
print("--- %s seconds ---" % (time.time() - start_time))