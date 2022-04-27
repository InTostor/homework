# Дан список числовых значений в файле.
# Необходимо найти только четные и нечетные значения в нем
# и возвести эти значения в квадрат. Получившийся результат
# необходимо вернуть обратно в файл
# четные и нечетные числа - все числа. Т.е сохранить в файл квадрат данного числа


path1 = str(__file__).replace("main.py", "") + "data1.txt"  # first problem
path2 = str(__file__).replace("main.py", "") + "data2.txt"  # second problem
# this required to start program from any place. just a path normalizer
# this just for benchmarking
import time

# problem functions
def firstProblem():
    f = open(path1, "r")
    fArr = (
        str(str(f.readlines()).replace("'", "").replace("\n", " "))
        .replace("[", "")
        .replace("]", "")
    )
    fArr = fArr.split(",")
    f.close()
    print(fArr)

    for i in range(0, len(fArr)):
        fe = float(fArr[i])
        fArr[i] = fe * fe

    fArr = str(fArr)
    fArr = fArr.replace("[", "").replace("]", "")
    f = open(path1 + ".solved.txt", "w")
    f.write(fArr)

    print(fArr)


def secondProblem():
    f = open(path2, "r")
    fArr = (
        str(str(f.readlines()).replace("'", "").replace("\n", " "))
        .replace("[", "")
        .replace("]", "")
    )
    fArr = fArr.split(",")
    print(fArr)
    fArr = list(map(int, fArr))

    sm = sum(fArr)
    mid = sm / len(fArr)

    out = "sum: " + str(sm) + "\n" + "mid: " + str(mid) + "\n"

    f = open(path2 + ".solved.txt", "w")
    f.write(out)


start_time = time.time()
# begin of program

firstProblem()
secondProblem()

# end of program
print((time.time() - start_time), "s")


#  # # # # # # # # # # # # # # # # # # # # # # # # # #
#  % % % % % % % # % % % % % # % # # % # % % % % % % %
#  # # # % # # # # % # # # # # % # # % # # # # % # # #
#  # # # % # # # # % # # # # # # % % # # # # # % # # #
#  # # # % # # # # % % % % % # # % % # # # # # % # # #
#  # # # % # # # # % # # # # # % # # % # # # # % # # #
#  # # # % # # # # % % % % % # % # # % # # # # % # # #
