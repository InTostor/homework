# n = abs(int(input()))
# for a in range(1, n):
#     for b in range(1, n):
#         for c in range(1, n):
#             if (n >= c) & (c >= b) & (b >= a) & (a > 0):
#                 if a**2 + b**2 + c**2 == n**2:
#                     print(f"{a} {b} {c} {n}")
#                     continue
#                 else:
#                     continue
#             continue


# this just for benchmarking
import time

start_time = time.time()
run = []

# n = abs(int(input()))
for nums in range(0, 3):
    for n in range(1, 80):

        for a in range(1, n):
            for b in range(1, n):
                for c in range(1, n):
                    if (n >= c) & (c >= b) & (b >= a) & (a > 0):
                        if a**2 + b**2 + c**2 == n**2:
                            print(f"{a} {b} {c} {n}")
                            continue
                        else:
                            continue
                    continue

    run.append((time.time() - start_time))
    start_time = time.time()


print(run[0])
print(run[1])
print(run[2])
print("avg", sum(run) / 3)

# original
# --- 7.862524747848511 seconds ---
# --- 7.8851892948150635 seconds ---
# --- 8.068974256515503 seconds ---
