"""Independent exact series census and forward iterates; standard library only."""
from collections import Counter
from math import comb

N = 14

def mul(a,b):
    c = [0]*(N+1)
    for i,x in enumerate(a):
        if not x: continue
        for j in range(N+1-i):
            c[i+j] += x*b[j]
    return c

def add(*arrays):
    return [sum(a[j] for a in arrays) for j in range(N+1)]

def cumulative_series(t):
    one = [1]+[0]*N
    zrun = [0]+[1]*N
    uniform = [0]+[2]*N
    if t == 0: return uniform
    ones = [int(1 <= j <= t) for j in range(N+1)]
    pair = [(j-1) if 2<=j<=t+1 else 0 for j in range(N+1)]
    triple = [comb(j-1,2) if 3<=j<=t+1 else 0 for j in range(N+1)]
    denominator_p = mul(ones,zrun)
    inverse = [0]*(N+1)
    inverse[0]=1
    for j in range(1,N+1):
        inverse[j]=sum(denominator_p[k]*inverse[j-k] for k in range(1,j+1))
    numerator = mul(zrun, add(mul(ones, add(one,zrun)),pair,triple))
    return add(uniform,mul(zrun,zrun),mul(numerator,inverse))

def update(x,n):
    b=[int(c) for c in format(x,f'0{n}b')[::-1]]
    for i in range(n):
        l=b[i-1] if i else b[n-1]
        r=b[i+1] if i<n-1 else b[0]
        b[i]=r if b[i] else l
    return sum(v<<i for i,v in enumerate(b))

if __name__ == '__main__':
    series=[cumulative_series(t) for t in range(N+1)]
    checks=0
    for n in range(3,N+1):
        depths=Counter()
        for x in range(1<<n):
            y=x
            t=0
            while True:
                nxt=update(y,n)
                if nxt==y:
                    assert y in (0,(1<<n)-1)
                    break
                t+=1;y=nxt
                assert t<n
            depths[t]+=1
        for t in range(n):
            predicted=series[t][n]-(series[t-1][n] if t else 0)
            assert predicted==depths[t],(n,t,predicted,depths[t])
            checks+=1
        assert series[n-1][n]==(1<<n)
        print(f'n={n} shell_check={n} total={series[n-1][n]}')
    print(f'PASS census_coefficients={checks}')
