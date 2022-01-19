def multsum():
    ins, out, out1 = [], 0, 1
    while True:
        inp = input(">")
        if inp=="break": 
            break
        else:
            ins.append(inp)
    try: 
        for i in range(0,len(ins)):
            out = out + int(ins[i])
            
    except ValueError:
        ""       
    try:
        for i in range(0,len(ins)):
            out1 = out1 * int(ins[i])
            
    except ValueError:        
        print("[error] inputs after (",i,") not counting: wrong type")
    
        
    return(out,out1)


def medium():
    ins, out = [], 0 
    while True:
        inp = input(">")
        if inp=="break": 
            break
        else:
            ins.append(inp)
    try:
        for i in range(0,len(ins)):
            out = out + int(ins[i])
    except ValueError:         
        print("[error] inputs after (",i,") not counting: wrong type")
        
        
    # catching zero dividing
    try:
        return(out/len(ins))
    except ZeroDivisionError:
        print("no input")



print(multsum())
print(medium())