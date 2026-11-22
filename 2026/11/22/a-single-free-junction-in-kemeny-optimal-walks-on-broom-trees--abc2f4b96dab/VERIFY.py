"""Algebraic and spectral checks for optimal Kemeny walks on broom trees.

Python 3, requires sympy and numpy. The symbolic part proves nonnegativity
of the KKT multipliers via coefficientwise nonnegative identities in
nonnegative integer indeterminates (not an extrapolation from tests).
"""
import math
import numpy as np
import sympy as sp

m,h,k,d,u,v,i=sp.symbols('m h k d u v i',integer=True)


def coeffs_nonnegative(poly,vars):
    p=sp.Poly(sp.expand(poly),*vars,domain=sp.QQ)
    assert all(a>=0 for _,a in p.terms()),[(a,b) for a,b in p.terms() if b<0]
    return len(p.terms()),min(a for _,a in p.terms())

for parity in (0,1):
    L=2*h+parity
    max_odd=h-1 if parity==0 else h
    c=lambda j:(L-j+1)*(m+j)
    Ce=sp.factor(sp.summation(c(2*i),(i,1,h)))
    Co=sp.factor(sp.summation(c(2*i+1),(i,1,max_odd)))
    Pe=sp.factor(sp.summation(c(2*i),(i,1,k)))
    Po=sp.factor(sp.summation(c(2*i+1),(i,1,k)))
    Po_before=sp.factor(sp.summation(c(2*i+1),(i,1,k-1)))
    # Feasibility of the first unsaturated path junction:
    # m^2 c0 Co > c1 Ce  for m>=2, h>=2 (even) or h>=1 (odd)
    F=sp.factor(m*m*(m+L)*Co-c(1)*Ce)
    val=coeffs_nonnegative(F.subs({m:u+2,h:v+(2 if parity==0 else 1)}),(u,v))
    assert sp.expand(F.subs({m:2,h:(2 if parity==0 else 1)}))>0
    # KKT multiplier for even junction j=2k (if internal), up to positive factor
    E=sp.factor(Pe*Co-Ce*Po_before)
    # For odd junction j=2k+1, up to positive factor
    O=sp.factor(Ce*Po-Pe*Co)
    assert coeffs_nonnegative(E.subs(h,k+d),(m,k,d))
    assert coeffs_nonnegative(O.subs(h,k+d),(m,k,d))
    print('algebraic parity',parity,'Ce=',Ce,'Co=',Co,'first-junction polynomial terms',val)

checks=0
for M in range(2,14):
    for L in range(3,21):
        N=M+L+1
        c0=N-1
        cc=lambda j:(L-j+1)*(M+j)
        Ce=sum(cc(j) for j in range(2,L+1,2))
        Co=sum(cc(j) for j in range(3,L+1,2))
        assert Ce>0 and Co>0
        x1=math.sqrt(cc(1))/(M*math.sqrt(c0)+math.sqrt(cc(1)))
        z=math.sqrt(Ce)/(math.sqrt(Ce)+math.sqrt(Co))
        a=(1-x1)/M
        x=[x1]+[(z if j%2==0 else 1-z) for j in range(2,L+1)]
        assert 0<x1 and x1+z<1 and 0<z<1
        assert abs(M*a+x1-1)<1e-12
        assert all(x[j-1]+x[j]<1+1e-12 for j in range(1,L))
        # KKT edge gradient amounts; bound multipliers positive
        H=[0]+[cc(j)/x[j-1]**2 for j in range(1,L+1)]
        lamb={1:0.0}
        for j in range(2,L+1):
            lamb[j]=H[j]-lamb[j-1]
        assert all(lamb[j]>-1e-7 for j in range(2,L))
        assert abs(lamb[L])<1e-7*max(1,H[L])
        theoretical=((M*math.sqrt(c0)+math.sqrt(cc(1)))**2+(math.sqrt(Ce)+math.sqrt(Co))**2)/N
        energy=(M*c0/a+sum(cc(j)/x[j-1] for j in range(1,L+1)))/N
        assert abs(theoretical-energy)<1e-8*max(1,theoretical)
        if M<=6 and L<=8:
            edges=[(0,i, a) for i in range(1,M+1)]
            edges.extend((0 if j==1 else M+j-1,M+j,x[j-1]) for j in range(1,L+1))
            Lap=np.zeros((N,N))
            for r,s,w in edges:
                Lap[r,r]+=w;Lap[s,s]+=w
                Lap[r,s]-=w;Lap[s,r]-=w
            ev=np.linalg.eigvalsh(Lap)
            assert abs(ev[0])<1e-9 and ev[1]>1e-9
            actual=sum(1/ev[1:])
            assert abs(actual-energy)<1e-7*max(1,energy)
        checks+=1
print('finite KKT/spectral cases:',checks, 'PASS')
