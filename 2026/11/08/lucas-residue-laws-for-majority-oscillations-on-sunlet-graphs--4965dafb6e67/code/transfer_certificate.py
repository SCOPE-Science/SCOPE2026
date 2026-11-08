#!/usr/bin/env python3
"""Exact finite transfer and characteristic-polynomial checks (Python stdlib)."""

def mult(a,b):
    n=len(a); p=len(b[0]);mid=len(b)
    return [[sum(a[i][k]*b[k][j] for k in range(mid)) for j in range(p)] for i in range(n)]

def ident(n): return [[int(i==j) for j in range(n)] for i in range(n)]

def tr(a): return sum(a[i][i] for i in range(len(a)))

def charpoly(a):
    # Newton identities: c[k]=-(1/k)*sum(c[k-j]*trace(A^j)).
    n=len(a); power=ident(n); ps=[0]
    for k in range(1,n+1):
        power=mult(power,a);ps.append(tr(power))
    c=[1]
    for k in range(1,n+1):
        numerator=-sum(c[k-j]*ps[j] for j in range(1,k+1))
        assert numerator%k==0
        c.append(numerator//k)
    return c

def pmul(p,q):
    a=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):a[i+j]+=x*y
    return a

def ppow(p,k):
    a=[1]
    for _ in range(k):a=pmul(a,p)
    return a

def transfer4(test):
    # De Bruijn graph of triples of binary values, test(prev,cur,next).
    m=[[0]*4 for _ in range(4)]
    for p in range(2):
        for c in range(2):
            for n in range(2):
                if test(p,c,n):m[2*p+c][2*c+n]+=1
    return m

def transfer16():
    # q=(a,b); compatibility at site i of time-(a,b) and time-(b,a).
    symbols=[(a,b) for a in range(2) for b in range(2)]
    m=[[0]*16 for _ in range(16)]
    for p,(ap,bp) in enumerate(symbols):
        for c,(a,b) in enumerate(symbols):
            for ne,(an,bn) in enumerate(symbols):
                if (b==ap or b==an) and (a==bp or a==bn):
                    m[4*p+c][4*c+ne]+=1
    return m

def lucas(n):
    a,b=2,1
    for i in range(n):a,b=b,a+b
    return a

def P(n):
    if n%2:return lucas(2*n)+(2 if n%3==0 else -1)
    if n%6==0:return lucas(2*n)+6+4*lucas(n)
    return lucas(2*n)+3-2*lucas(n)

def F(n):return lucas(n)+[2,1,-1,-2,-1,1][n%6]

def Q(n):return lucas(n)+(2 if n%3==0 else -1)

def trace_checks(m,fn):
    p=ident(len(m))
    for n in range(1,31):
        p=mult(p,m)
        if n>=3:assert tr(p)==fn(n),(n,tr(p),fn(n))

if __name__=='__main__':
    m=transfer16();f=transfer4(lambda p,c,n: c==p or c==n)
    q=transfer4(lambda p,c,n: not(p==c==n))
    # Coefficients are in descending powers.
    expectedF=pmul([1,-1,-1],[1,-1,1])
    expectedQ=pmul([1,-1,-1],[1,1,1])
    expectedP=pmul(pmul(pmul(ppow([1,-1],2),ppow([1,1],2)),
                            pmul([1,-3,1],[1,1,1])),
                            [1,0,3,0,8,0,3,0,1])
    assert charpoly(f)==expectedF
    assert charpoly(q)==expectedQ
    assert charpoly(m)==expectedP
    trace_checks(f,F);trace_checks(q,Q);trace_checks(m,P)
    for n in range(3,31):
        assert P(n)>=F(n)
        assert (P(n)-F(n))%2==0
        assert Q(n)%2==0
        assert Q(n)<=P(n)-F(n)
    print('F_4_charpoly:',charpoly(f))
    print('Q_4_charpoly:',charpoly(q))
    print('P_16_charpoly:',charpoly(m))
    print('verified all three trace identities n=3..30; cycle integrality and containment OK')
