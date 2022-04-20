path = str(__file__).replace("xyzCounter.py", "")+"data.txt"
# this required to start program from any place. just a path normalizer


# this just for benchmarking
import time
start_time = time.time()
# begin of program

f = open(path,"r")
fStr = str(f.readlines())

print(" X  Y  Z\n",fStr.count("X"),fStr.count("Y"),fStr.count("Z"))
f.close()

# end of program
print((time.time() - start_time),"s")