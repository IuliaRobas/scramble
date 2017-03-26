def a(x):
    r=""
    i=len(x)-1
    while i>=0:
        r+=x[i]
        i-=1
    return r

def b(x):
    r=x[len(x)-1]
    for i in range(0,len(x)-1):
        r+=x[i]
    return r

print(a(b(b(b('.redmoc'))))+a(a(a(a('noY-SS'))))+b(b('pihsnrT@'))+a(b('reatinteg')))