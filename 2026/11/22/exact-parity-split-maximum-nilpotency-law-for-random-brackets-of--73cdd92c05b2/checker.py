#!/usr/bin/env python3
"""Direct finite-field checks for powers of additive brackets in strictly triangular algebras.
Only prime fields are needed for these independent tests. Standard library only.
"""
from itertools import product
from fractions import Fraction


def predicted(n,q):
    a=Fraction((q*q-1)*(q-1),q**3)
    h=n//2
    if n%2:
        return a**h
    if n==2:
        return Fraction(1,1)
    v=Fraction(q*q-1,q*q)*Fraction(q-1,q)**(2*h-2)
    w=a**(h-2)*(a+(h-1)*(1-a-Fraction(1,q**4)))
    uv=2*a**(h-1)-v
    return (1-Fraction(1,q))*w+Fraction(1,q)*uv


def truncated_bracket_nonzero(n,q,vs,us):
    # vs[i]=(A_{i,i+1},B_{i,i+1}), us[i]=(A_{i,i+2},B_{i,i+2}).
    c=[(vs[i][0]*vs[i+1][1]-vs[i][1]*vs[i+1][0])%q for i in range(n-2)]
    h=n//2
    if n%2:
        z=1
        for i in range(0,n-2,2): z=z*c[i]%q
        return z!=0
    if n==2:return False
    u=1;v=1
    for i in range(0,n-2,2):u=u*c[i]%q
    for i in range(1,n-2,2):v=v*c[i]%q
    if u or v:return True
    d=[]
    for i in range(n-3):
        a,b=vs[i]; ap,bp=vs[i+2]; e,f=us[i]; g,k=us[i+1]
        d.append((a*k-b*g+e*bp-f*ap)%q)
    total=0
    for j in range(h-1):
        x=d[2*j]
        for r in range(j): x=x*c[2*r]%q
        for r in range(j+1,h-1): x=x*c[2*r+1]%q
        total=(total+x)%q
    return total!=0


def verify(n,q):
    counts=[0,0]
    # Full independent enumeration of first and second superdiagonal coefficients.
    # Full matrices have irrelevant higher coefficients with equal multiplicities.
    for raw in product(range(q),repeat=2*(n-1)):
        vs=list(zip(raw[::2],raw[1::2]))
        if n%2:
            counts[truncated_bracket_nonzero(n,q,vs,[])]+=1
        else:
            for u_raw in product(range(q),repeat=2*(n-2)):
                us=list(zip(u_raw[::2],u_raw[1::2]))
                counts[truncated_bracket_nonzero(n,q,vs,us)]+=1
    actual=Fraction(counts[1],sum(counts))
    expect=predicted(n,q)
    assert actual==expect,(n,q,actual,expect)
    print(f'n={n} q={q} checked={sum(counts)} nonzero={counts[1]} probability={actual} PASS')

if __name__=='__main__':
    for n,q in ((3,2),(4,2),(4,3),(5,2),(6,2),(7,2)):
        verify(n,q)


def direct_full_matrix(n,q):
    # An independent full-matrix bracket and power calculation, without using superdiagonal reductions.
    idx=[(i,j) for i in range(n) for j in range(i+1,n)]
    matrices=[]
    for vals in product(range(q),repeat=len(idx)):
        m=[[0]*n for _ in range(n)]
        for (i,j),v in zip(idx,vals):m[i][j]=v
        matrices.append(m)
    def mul(a,b):
        return [[sum(a[i][k]*b[k][j] for k in range(n))%q for j in range(n)] for i in range(n)]
    h=(n-1)//2 if n%2 else n//2-1
    success=0
    for a in matrices:
        for b in matrices:
            ab=mul(a,b); ba=mul(b,a)
            c=[[(ab[i][j]-ba[i][j])%q for j in range(n)] for i in range(n)]
            p=c
            for _ in range(1,h):p=mul(p,c)
            success+=any(t for row in p for t in row)
    actual=Fraction(success,len(matrices)**2)
    expected=predicted(n,q)
    assert actual==expected,(n,q,actual,expected)
    print(f'full-matrix n={n} q={q} pairs={len(matrices)**2} success={success} probability={actual} PASS')

if __name__=='__main__':
    direct_full_matrix(4,2)
    direct_full_matrix(4,3)
