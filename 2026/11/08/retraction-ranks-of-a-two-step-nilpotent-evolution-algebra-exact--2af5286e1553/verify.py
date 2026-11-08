"""Standalone small-field checks of idempotent algebra endomorphism ranks.

Run: python verify.py .  Pure Python, no third-party dependencies.
"""
from itertools import product
from math import comb, lgamma, log, exp

def ops(q):
    if q in (2, 3, 5):
        return (lambda a, b: (a+b)%q), (lambda a,b: (a*b)%q)
    if q == 4:  # F_2[t]/(t^2+t+1), low bit is constant
        def mul(a,b):
            c = (a&1)*(b&1) ^ (((a>>1)&1)*(b&1) ^ (a&1)*((b>>1)&1)) * 2
            if (a&2) and (b&2): c ^= 3
            return c
        return (lambda a,b: a^b), mul
    raise ValueError('unsupported field')

def multiply(X,Y,n,add,mul):
    return tuple(tuple(reduce_add([mul(X[i][k],Y[k][j]) for k in range(n)],add) for j in range(n)) for i in range(n))

def reduce_add(vals,add):
    result=0
    for x in vals:result=add(result,x)
    return result

def matrank(X,q,add,mul):
    n=len(X); a=[list(row) for row in X]; r=0
    for c in range(n):
        pivot=next((k for k in range(r,n) if a[k][c]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=next(z for z in range(1,q) if mul(z,a[r][c])==1)
        a[r]=[mul(inv,z) for z in a[r]]
        for j in range(n):
            if j!=r and a[j][c]:
                t=a[j][c]
                a[j]=[add(a[j][k],mul(-t%q,a[r][k])) for k in range(n)] if q!=4 else [add(a[j][k],mul(t,a[r][k])) for k in range(n)]
        r+=1
    return r

def verify_direct(n,q):
    add,mul=ops(q); hist={}
    for raw in product(range(q), repeat=2*n*n):
        A=tuple(tuple(raw[i*2*n+j] for j in range(n)) for i in range(n))
        C=tuple(tuple(raw[i*2*n+n+j] for j in range(n)) for i in range(n))
        if any(mul(A[k][i],A[k][j]) for k in range(n) for i in range(n) for j in range(i+1,n)):
            continue
        B=tuple(tuple(mul(A[i][j],A[i][j]) for j in range(n)) for i in range(n))
        if multiply(A,A,n,add,mul)!=A: continue
        CA=multiply(C,A,n,add,mul); BC=multiply(B,C,n,add,mul)
        if any(add(CA[i][j],BC[i][j])!=C[i][j] for i in range(n) for j in range(n)):continue
        assert multiply(B,B,n,add,mul)==B
        r=matrank(A,q,add,mul)
        hist[r]=hist.get(r,0)+1
    formula={r:comb(n,r)*(1+r*(q-1))**(n-r)*q**(2*r*(n-r)) for r in range(n+1)}
    print('DIRECT',n,q,hist,formula)
    assert hist==formula

def verify_asymptotic(n,q):
    logs=[lgamma(n+1)-lgamma(r+1)-lgamma(n-r+1)+(n-r)*log(1+(q-1)*r)+2*r*(n-r)*log(q) for r in range(n+1)]
    t=max(logs); mass=[exp(x-t) for x in logs]; z=sum(mass);mass=[v/z for v in mass]
    mu=n/2+(1-log((q-1)*n/2))/(4*log(q))
    approx=[exp(-2*log(q)*(r-mu)**2) for r in range(n+1)]
    k=sum(approx);approx=[v/k for v in approx]
    err=sum(abs(x-y) for x,y in zip(mass,approx))/2
    print('ASYMPTOTIC',n,q,'center',round(mu,5),'TV',round(err,8))
    if n>=100:assert err<0.04

if __name__=='__main__':
    for n,q in [(1,2),(2,2),(3,2),(2,3),(2,4)]:verify_direct(n,q)
    for q in (2,3,4):
        for n in (100,300,1000):verify_asymptotic(n,q)
    print('VERIFY_OK')
