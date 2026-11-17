#!/usr/bin/env python3
"""Exact rational verification of convex-regression path-variation face norms.

Requires only Python 3 standard library. The mathematical proof explains why
all active faces and all unit-step perturbations suffice.
"""
from fractions import Fraction as F
from itertools import combinations

EXPECTED = {2:F(1),3:F(1),4:F(6,5),5:F(4,3),6:F(7,5),
            7:F(28,19),8:F(11,7),9:F(11,7),10:F(5,3)}

def inverse(a):
    n=len(a)
    if not n: return []
    x=[[F(v) for v in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        p=next(i for i in range(j,n) if x[i][j])
        x[j],x[p]=x[p],x[j]
        t=x[j][j]
        x[j]=[v/t for v in x[j]]
        for i in range(n):
            if i!=j and x[i][j]:
                t=x[i][j]
                x[i]=[u-t*v for u,v in zip(x[i],x[j])]
    return [row[n:] for row in x]

def face_norm(n,active):
    m=len(active)
    D=[]
    for j in active:
        row=[0]*n
        row[j:j+3]=[1,-2,1]
        D.append(row)
    if not m: return F(1),1
    G=[[sum(D[i][t]*D[j][t] for t in range(n)) for j in range(m)] for i in range(m)]
    inv=inverse(G)
    best=F(0); where=0
    for cut in range(1,n):
        h=[F(int(i>=cut)) for i in range(n)]
        dh=[sum(D[i][j]*h[j] for j in range(n)) for i in range(m)]
        u=[sum(inv[i][j]*dh[j] for j in range(m)) for i in range(m)]
        y=[h[j]-sum(D[i][j]*u[i] for i in range(m)) for j in range(n)]
        v=sum(abs(y[j+1]-y[j]) for j in range(n-1))
        if v>best:best,where=v,cut
    return best,where

def exact_n(n):
    best=F(0);arg=None; count=0
    for mask in range(1<<(n-2)):
        active=tuple(j for j in range(n-2) if mask>>j&1)
        val,cut=face_norm(n,active);count+=1
        if val>best:best,arg=val,(active,cut)
    return best,arg,count

def strict_finite_witness(n,active,cut,expected):
    # Construct fitted base on relative interior of face: selected
    # second differences are zero, all others exactly one.
    aset=set(active)
    z=[F(0),F(0)]
    for i in range(n-2):
        z.append(2*z[-1]-z[-2]+int(i not in aset))
    D=[]
    for j in active:
        row=[0]*n;row[j:j+3]=[1,-2,1];D.append(row)
    m=len(D)
    G=[[sum(D[i][t]*D[j][t] for t in range(n)) for j in range(m)] for i in range(m)]
    inv=inverse(G)
    x=[z[j]-sum(D[i][j] for i in range(m)) for j in range(n)]
    h=[F(int(j>=cut)) for j in range(n)]
    dh=[sum(D[i][j]*h[j] for j in range(n)) for i in range(m)]
    v=[sum(inv[i][j]*dh[j] for j in range(m)) for i in range(m)]
    ph=[h[j]-sum(D[i][j]*v[i] for i in range(m)) for j in range(n)]
    eps=F(1,1000000)
    zout=[z[j]+eps*ph[j] for j in range(n)]
    assert all(F(1)-eps*v[i]>0 for i in range(m))
    for i in range(n-2):
        delta=zout[i]-2*zout[i+1]+zout[i+2]
        assert (delta==0) if i in aset else (delta>0)
    # First-order optimality: x-z=-D^T 1; x+eps*h-zout=-D^T (1-eps*v).
    assert all(x[j]-z[j]==-sum(D[i][j] for i in range(m)) for j in range(n))
    assert all(x[j]+eps*h[j]-zout[j]==-sum(D[i][j]*(F(1)-eps*v[i]) for i in range(m)) for j in range(n))
    assert sum(abs(zout[j+1]-z[j+1]-zout[j]+z[j]) for j in range(n-1))/eps==expected


def boundary_spline_value(n):
    # Endpoints are unconstrained; the n-2 interior sites are fit by a line.
    # k is the split between left and right central halves.
    m=n-2
    if m<2:return F(1)
    k=n//2
    a=k-1;b=m-a
    beta=F(6*a*b,m*(m*m-1))
    alpha=F(b,m)-beta*F(m-1,2)
    return abs(alpha)+(m-1)*beta+abs(F(1)-alpha-(m-1)*beta)

def main():
    for n,val in EXPECTED.items():
        z,arg,count=exact_n(n)
        assert z==val,(n,z,val)
        assert count==2**(n-2)
        strict_finite_witness(n,arg[0],arg[1],val)
        print(f'EXACT_ALL_FACES n={n} count={count} sharp={z} active={arg[0]} cut={arg[1]}')
    for n in range(6,101):
        v=boundary_spline_value(n)
        target=F(2*n-5,n-1) if n%2==0 else F(2)-F(3,n-2)
        assert v==target,(n,v,target)
    print('EXACT_BOUNDARY_SPLINE_WITNESSES_N6_TO_N100_PASS')
    print('ALL_CONVEX_BV_CERTIFICATES_PASS')
if __name__=='__main__': main()
