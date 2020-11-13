flag = True
while(flag):
    H,U,D,F = input().split()
    H = float(H)
    U = float(U)
    D = float(D)
    F = float(F)
    if H == 0 :
        break
    reduce = U*(F/100)
    high = 0
    day = 0 
    str = "success on day"
    while high <= H:
        day +=1
        high += U
        if high > H:
            break
        high -= D
        if high < 0:
            str = "failure on day"
            break
        U -= reduce
    print(str,day)