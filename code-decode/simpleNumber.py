# this just for benchmarking
import time

start_time = time.time()


n = 90000
lst = [2]
k = 0
for i in range(2, n+1):


    if (i > 10) and (i%10 not in [1,3,5,7,9]):
        continue

    for j in lst:

        if j*j > i + 1:
            lst.append(i)
            break
        if i % j == 0:
            k = k + 1

    if k == 0:
        lst.append(i)
        print(i)
    else:
        k = 0
    


print((time.time() - start_time))
#timing - 90k in 7.428109407424927
