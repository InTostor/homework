# this just for benchmarking
import time

start_time = time.time()
run = []

# n = abs(int(input()))
for nums in range(0, 12):
    for n in range(1, 80):

        sqn = n * n
        for a in range(1, n):
            sqa = a * a
            for b in range(a - 1, n):
                sqb = sqa + b * b
                if sqb > sqn:
                    break
                for c in range(b - 1, n):
                    sq = sqb + c * c
                    if sq > sqn:
                        break
                    if sq == sqn:
                        print(a, b, c, n)

    run.append((time.time() - start_time))
    start_time = time.time()

print("timings")
print("1  ", run[0])
print("2  ", run[1])
print("3  ", run[2])
print("4  ", run[3])
print("5  ", run[4])
print("6  ", run[5])
print("7  ", run[6])
print("8  ", run[7])
print("9  ", run[8])
print("10  ", run[9])
print("11  ", run[10])
print("12  ", run[11])
print("avg", sum(run) / 12)

# original
# --- 7.862524747848511 seconds ---
# --- 7.8851892948150635 seconds ---
# --- 8.068974256515503 seconds ---
