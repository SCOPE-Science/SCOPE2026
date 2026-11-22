"""Exact rational identities for Wachspress denominators of symmetric hexagons.

Run: python verify.py. These finite checks supplement the written universal proof.
"""
from fractions import Fraction as F
from itertools import product


def add(P, Q):
    R = P.copy()
    for k, v in Q.items():
        R[k] = R.get(k, F(0)) + v
    return {k: v for k, v in R.items() if v}


def mul(P, Q):
    R = {}
    for (i, j), v in P.items():
        for (h, k), w in Q.items():
            R[(i+h, j+k)] = R.get((i+h, j+k), F(0)) + v*w
    return {k: v for k, v in R.items() if v}


def scalar(v, P):
    return {k: v*a for k,a in P.items() if v*a}


def det(u, v):
    return u[0]*v[1]-u[1]*v[0]


def quadratic(a,b):
    s = a+b+1
    return {(0,0):2*s, (2,0):-2*a*(1+a-b),
            (1,1):-2*(1-(a-b)**2), (0,2):-2*b*(1+b-a)}


def actual(a,b):
    forms = [{(0,0):F(1),(1,0):-F(1)},
             {(0,0):F(1),(1,0):-a,(0,1):-b},
             {(0,0):F(1),(0,1):-F(1)},
             {(0,0):F(1),(1,0):F(1)},
             {(0,0):F(1),(1,0):a,(0,1):b},
             {(0,0):F(1),(0,1):F(1)}]
    ns = [(F(1),F(0)),(a,b),(F(0),F(1)),(-F(1),F(0)),(-a,-b),(F(0),-F(1))]
    weights=[]
    for j in range(6):
        factor=det(ns[(j-1)%6],ns[j])
        p={(0,0):factor}
        for k in range(6):
            if k not in ((j-1)%6,j):
                p=mul(p,forms[k])
        weights.append(p)
    total={}
    for p in weights:
        total=add(total,p)
    return total,weights


def evalpoly(p,x,y):
    return sum(c*x**i*y**j for (i,j),c in p.items())


def check(a,b):
    if not (a>0 and b>0 and a+b>1 and abs(a-b)<1):
        return 0
    q,ws=actual(a,b)
    assert q == quadratic(a,b),(a,b,q,quadratic(a,b))
    vertices=[(F(1),-F(1)),(F(1),(1-a)/b),((1-b)/a,F(1)),
              (-F(1),F(1)),(-F(1),(a-1)/b),((b-1)/a,-F(1))]
    assert sum((w!=0 for w in ws)) == 6
    # Affine precision exactly, coefficient by coefficient.
    baryx={}; baryy={}
    for w,(xv,yv) in zip(ws,vertices):
        baryx=add(baryx,scalar(xv,w))
        baryy=add(baryy,scalar(yv,w))
    assert baryx == mul(q,{(1,0):F(1)})
    assert baryy == mul(q,{(0,1):F(1)})
    alpha=a+b-1; beta=1+b-a; gamma=1+a-b
    triple=[alpha,beta,gamma]
    expected=[F(8)*beta*gamma/(beta+gamma),
              F(8)*alpha*beta/(alpha+beta),
              F(8)*alpha*gamma/(alpha+gamma)]
    got=[evalpoly(q,*v) for v in vertices[:3]]
    assert got == expected,(a,b,got,expected)
    U,V,W=sorted(triple)
    ratio=quadratic(a,b)[(0,0)] / min(got)
    assert ratio == (U+V+W)*(U+V)/(4*U*V)
    assert ratio-F(3,2) == ((V-U)*(2*V-U)+(W-V)*(U+V))/(4*U*V)
    assert ratio>=F(3,2)
    assert (ratio==F(3,2))==(a==b==1)
    return 1


def main():
    count=0
    for a,b in product((F(i,7) for i in range(1,22)),repeat=2):
        count+=check(a,b)
    assert check(F(1),F(1))
    assert count>100
    print('PASS: exact symbolic polynomial identities and affine precision for',count,'admissible rational parameter pairs')

if __name__ == '__main__':
    main()
