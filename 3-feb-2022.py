def cubes(num=1,start=1):
    out,n=[],0
    for i in range(start,start+num):
        out.append(i*i*i)
        n=n+1
    return out

def EvenCounter(num):
    out=[int(a) for a in str(num)]
    uneven,even=0,0
    for i in range(0,len(out)):
        if ((out[i]%2) ==0):
            even+=1
        else:
            uneven+=1

    return even,uneven

print(cubes(40,2)) # оба аргумента (массив)
print(cubes(50)) # только количество (начало - 1) (массив)
print(cubes()) # без аргументов. Возвращает 1 (массив)

print("----------------------------")
print(EvenCounter(25467)) # возвращает количество четных и не четных чисел (два числа)