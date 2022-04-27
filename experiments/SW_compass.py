for x in range(0, 360):
    compass = (x / 360) * ((x - 180.1) / abs(x - 180.1))
    print(x, compass)
