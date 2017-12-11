def tower(x):
    if x>59:
        print('數字太大囉！')
    else:  
        for i in range(1,x):
            print(' '*(x-i+1),"*"*(i*2-1))

def ninenine(x1,x2):
    x2=x2+1
    for i in range(1,10):
        a=list(range(x1,x2))
        b=[a[0]*i,a[1]*i,a[2]*i]
        print('%s x %s = %s' % (a[0], i, b[0]),"\t",
          '%s x %s = %s' % (a[1], i, b[1]),'\t',
          '%s x %s = %s' % (a[2], i, b[2]))
    print('\n')