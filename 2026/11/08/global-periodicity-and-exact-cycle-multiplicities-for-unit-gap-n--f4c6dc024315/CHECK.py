"""Integer-only reproduction of the explicit section return cycles and plane periods."""
from math import isqrt


def offset(b, m):
    return (m-1)*(m+2*b*(m-1))//2


def layer(b, x):
    assert x >= 0
    a = 2*b+1
    m = (isqrt(1+8*a*x)-1)//(2*a)+1
    while x < offset(b,m):
        m -= 1
    while x >= offset(b,m+1):
        m += 1
    return m, x-offset(b,m)


def exact_return(b, x):
    a = 2*b+1
    X,Y=x,0
    for t in range(1, 20000):
        sign=1 if X>=0 else -1
        Y-=sign
        X+=a*Y+b
        if Y==0 and X>=0:
            return X,t
    raise AssertionError((b,x))


def formula_return(b,x):
    m,u=layer(b,x)
    return ((x+4*b*m,4*m) if u<m else (x-(2*m-1),4*m-2))


def exact_period(b, x):
    a = 2*b+1
    X,Y=x,0
    for t in range(1, 30000):
        sign=1 if X>=0 else -1
        Y-=sign
        X+=a*Y+b
        if (X,Y)==(x,0): return t
    raise AssertionError((b,x))


def verify():
    assertions=0
    for b in [1,2,3,4,5,6,10,17]:
        a=2*b+1
        for m in range(1, 20):
            base=offset(b,m)
            end=offset(b,m+1)
            assert end-base==a*m-b;assertions+=1
            for x in range(base,end):
                assert exact_return(b,x)==formula_return(b,x);assertions+=1
            for t in range(m):
                x=base+t
                orbit=[x]
                for j in range(a):
                    x=formula_return(b,x)[0]
                    orbit.append(x)
                assert x==base+t and len(set(orbit[:-1]))==a; assertions+=1
                assert sum(formula_return(b,z)[1] for z in orbit[:-1])==4*a*m;assertions+=1
                if m<=5:
                    assert exact_period(b,base+t)==4*a*m;assertions+=1
            for j in range(a):
                pass
    print('EXACT_INTEGER_RETURN_AND_CYCLE_CHECK_OK', assertions)


if __name__=='__main__': verify()
