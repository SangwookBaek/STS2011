def add5(x,y,*args,**kargs):
    print("local variables",locals())
    sum = sumj = 0
    sum = x + y
    for i in args:
        sum+=i
    for k,j in kargs.items():
        sumj += j
    return sum + sumj
