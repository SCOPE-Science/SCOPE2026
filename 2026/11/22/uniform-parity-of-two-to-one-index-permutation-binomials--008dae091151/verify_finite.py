#!/usr/bin/env python3
"""Exact finite-field parity and square-class checks for binomial permutations.
No external dependencies; all arithmetic uses integer residue pairs or towers.
These tests supplement, but do not replace, the infinite proof.
"""
from math import gcd


def perm_sign(values):
    N=len(values)
    seen=set()
    cycles=0
    for x in range(N):
        if x not in seen:
            cycles+=1
            y=x
            while y not in seen:
                seen.add(y)
                y=values[y]
    return (-1)**(N-cycles)


def make_quadratic_prime(p):
    D=next(i for i in range(2,p) if pow(i,(p-1)//2,p)==p-1)
    def mul(x,y):
        a,b= x%p,x//p
        c,e= y%p,y//p
        return ((a*c+D*b*e)%p)+p*((a*e+b*c)%p)
    def add(x,y):
        return ((x%p+y%p)%p)+p*((x//p+y//p)%p)
    return p*p,mul,add


def make_quadratic_9():
    p=3
    def m9(x,y):
        a,b=x%3,x//3
        c,d=y%3,y//3
        return ((a*c+2*b*d)%3)+3*((a*d+b*c)%3)
    def po9(x,n):
        z=1
        while n:
            if n&1:z=m9(z,x)
            x=m9(x,x)
            n//=2
        return z
    D=next(k for k in range(1,9) if po9(k,4)!=1)
    def mul(x,y):
        a,b=x%9,x//9
        c,d=y%9,y//9
        u=m9(a,c);v=m9(m9(D,b),d)
        return (((u%3+v%3)%3)+3*((u//3+v//3)%3)) + 9*(((m9(a,d)%3+m9(b,c)%3)%3)+3*((m9(a,d)//3+m9(b,c)//3)%3))
    def add(x,y):
        a,b=x%9,x//9
        c,d=y%9,y//9
        return ((a%3+c%3)%3)+3*((a//3+c//3)%3)+9*(((b%3+d%3)%3)+3*((b//3+d//3)%3))
    return 81,mul,add


def field_power(mul,x,n):
    y=1
    while n:
        if n&1:y=mul(y,x)
        x=mul(x,x)
        n//=2
    return y


def run(q,maker):
    N,mul,add=maker()
    assert N==q*q
    exp=lambda x,n:field_power(mul,x,n)
    ps=[[exp(x,e) for x in range(N)] for e in range(2*(q-1)+1)]
    checked=permutations=zero_cases=0
    # test two distinct two-to-one exponents; repeated d modulo q+1
    ds=sorted({d for d in [2,2*q,4,2*(q+1)+2] if gcd(d,q+1)==2})
    for d in ds:
        x_d=[exp(x,d*(q-1)) for x in range(N)]
        for r in range(1,min(2*q+2,N),2):
            if gcd(r,q-1)!=1:continue
            x_r=[exp(x,r) for x in range(N)]
            for a in range(N):
                values=[mul(x_r[x],add(x_d[x],a)) for x in range(N)]
                checked+=1
                if len(set(values))==N:
                    permutations+=1
                    if a==0:zero_cases+=1
                    assert a==0 or exp(a,(N-1)//2)==1,(q,d,r,a,'nonsquare')
                    actual=perm_sign(values)
                    predicted=(-1)**((r-1)//2)
                    assert actual==predicted,(q,d,r,a,actual,predicted)
    return checked,permutations,zero_cases,len(ds)

if __name__=='__main__':
    results=[]
    for q in [3,5,7,9,11]:
        v=run(q,make_quadratic_9 if q==9 else lambda q=q:make_quadratic_prime(q))
        results.append((q,)+v)
    assert all(r[2]>0 for r in results),results
    print('ODD_Q_INDEX_TWO_PARITY_OK',results,'checked permutations inclusive of a=0')
