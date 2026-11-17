"""Finite supplementary diagnostics for a Bell-diagonal operator-mean extremum.
The universal inequality is proved analytically in RESULT.md. This file does
not certify it by sampling.
"""
from fractions import Fraction
from math import sqrt
import numpy as np

E = np.eye(4)
BELL = np.column_stack([
    np.array([1,0,0,1])/sqrt(2),
    np.array([1,0,0,-1])/sqrt(2),
    np.array([0,1,1,0])/sqrt(2),
    np.array([0,1,-1,0])/sqrt(2),
])


def negative_mass(w):
    rho=BELL@np.diag(w/np.sum(w))@BELL.T
    pt=rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
    return float(sum(max(0.,-float(t)) for t in np.linalg.eigvalsh(pt)))


def harmonic(a,b,t):
    if t==0: return a
    if t==1: return b
    out=np.zeros_like(a,dtype=float)
    mask=(a>0)&(b>0)
    out[mask] = a[mask]*b[mask]/((1-t)*b[mask]+t*a[mask])
    return out


def weighted_mean(a,b,atoms):
    out=np.zeros_like(a,dtype=float)
    for t,m in atoms:
        out += m*harmonic(a,b,t)
    return out


def random_separable(rng):
    # Convex hull of the six Bell-octahedron edge vertices.
    coeff=rng.dirichlet(np.ones(6))
    pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    v=np.zeros(4)
    for z,(i,j) in zip(coeff,pairs):
        v[i]+=z/2;v[j]+=z/2
    return v


def main():
    rng=np.random.default_rng(20261109)
    models=[
        [(0.,.18),(1.,.12),(.3,.7)],
        [(0.,.0),(1.,.0),(.5,1.)],
        [(0.,.4),(1.,.5),(.2,.1)],
        [(0.,.5),(1.,.5)],
        [(0.,0.03),(1.,0.01),(.25,.41),(.73,.55)],
    ]
    assertions=0
    for atoms in models:
        c=sum(m for t,m in atoms if t==0)
        d=sum(m for t,m in atoms if t==1)
        bound=(1-c-d)/(2*(1+c+d))
        a=np.array([.5,.5,0.,0.]);b=np.array([.5,0.,.5,0.])
        w=weighted_mean(a,b,atoms)
        expected=np.array([.5,c/2,d/2,0.])
        assert np.allclose(w, expected, atol=1.e-13)
        assertions+=1
        assert abs(negative_mass(w)-bound)<1.e-12
        assertions+=1
        for _ in range(2000):
            a=random_separable(rng);b=random_separable(rng)
            w=weighted_mean(a,b,atoms)
            assert max(w)/sum(w) <= 1/(1+c+d)+3.e-12
            assertions+=1
            assert negative_mass(w) <= bound+3.e-12
            assertions+=1
    # Independent exact rational test of a mixture of weighted harmonic means.
    def hrat(a,b,t):
        if t==0: return a
        if t==1: return b
        if a==0 or b==0: return Fraction(0)
        return a*b/((1-t)*b+t*a)
    rational_atoms=[(Fraction(0),Fraction(1,7)),
        (Fraction(1),Fraction(2,7)),
        (Fraction(2,5),Fraction(4,7))]
    A=list(map(Fraction,['1/2','1/2','0','0']))
    B=list(map(Fraction,['1/2','0','1/2','0']))
    W=[sum(m*hrat(A[i],B[i],t) for t,m in rational_atoms) for i in range(4)]
    assert W==[Fraction(1,2),Fraction(1,14),Fraction(1,7),Fraction(0)]
    assertions+=1
    expected=Fraction(1,2)/sum(W)-Fraction(1,2)
    assert expected==Fraction(1,5)
    assertions+=1
    print('PASS:',assertions,'supplementary assertions; proof is independent of finite tests')
if __name__=='__main__': main()
