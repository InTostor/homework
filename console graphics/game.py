playerPos = [1, 1]
objects = ("-", "#", "out")
level = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1],
]


def numToSymbol(lst):
    out = []
    for i in range(0, len(lst)):
        out.append(objects[lst[i]])
    return out[::1]

def drawLevel(lvl=list,pos=list):
    out=[]
    for i in range(0,len(lvl)):
        out.append(numToSymbol(lvl[i]))
    return out



for i in range(0, len(level)):
    print("".join(str(level[i])))

for i in range(0, len(level)):
    print(" ".join(numToSymbol(level[i])))
