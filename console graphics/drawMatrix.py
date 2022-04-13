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


def drawMatrix(arr):
    width = len(arr)
    out = arr
    for i in range(0, width):
        out[i] = "".join(str(arr[i]))
        out[i] = str(out[i]).replace("[", "").replace("]", "")
        print(out[i])


drawMatrix(level)
