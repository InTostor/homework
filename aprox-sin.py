from math import *
import string

pi = 3.1415926535897932384626433832795


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def aprSin2(inp=float):
    inp = inp - pi * (inp // pi)
    t = inp / pi
    yw = 2 * t
    yj = 2 - yw

    out = yw + (yj - yw) * t

    return float(out)


def aprSin3(x=float):
    t = x / pi
    B = 3 * pi / 7
    E = B * t
    F = B * (1 - t)
    H = E + (B - E) * t
    I = F + (B - F) * (1 - t)
    J = H + (I - H) * t
    out = J - 0.01
    return out


def stringNormalizer(string, tgtlen):
    string = str(string)
    return str(string + "0" * (tgtlen - len(string)))


print("x, lib,sin2,sin3 delta2, delta3")
for i in range(1, 314):
    ms = round(sin(i / 100), 5)
    asi2 = round(aprSin2(i / 100), 5)
    asi3 = round(aprSin3(i / 100), 5)
    io = stringNormalizer(i / 100, 5)
    mso = stringNormalizer(ms, 7)
    asi2o = stringNormalizer(asi2, 7)
    asi3o = stringNormalizer(asi3, 7)
    print(io, "|", end=" ")
    print(mso, "|", end=" ")
    print(asi2o, "|", end=" ")
    print(asi3o, "|", end=" ")
    delta2 = stringNormalizer(round((asi2 - ms), 3), 4)
    print(delta2, "|", end=" ")
    delta3 = stringNormalizer(round((asi3 - ms), 3), 4)
    print(delta3, "|")


print(aprSin2(6 / 5))
print(aprSin3(6 / 5))
