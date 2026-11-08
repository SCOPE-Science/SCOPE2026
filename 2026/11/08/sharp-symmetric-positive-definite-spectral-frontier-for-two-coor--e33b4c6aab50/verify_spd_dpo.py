"""Exact rational checks of the 2x2 symmetric DPO spectral-frontier theorem.

Reproducibility only: the all-parameter theorem is proved algebraically.
Python 3, standard library; no external packages or network access.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random

SIGNS = list(product((-1, 1), repeat=2))


def det2(a,b,c,d):
    return a*d-b*c


def solve2(m, rhs):
    a,b,c,d=m
    det=det2(a,b,c,d)
    assert det != 0
    return ((d*rhs[0]-b*rhs[1])/det,(-c*rhs[0]+a*rhs[1])/det)


def quantities(A,z,b):
    a,c,d=A
    z1,z2=z
    M=(a-z1,c,c,d-z2)
    x=solve2(M,b)
    y=solve2(M,z)
    F=z1*x[0]+z2*x[1]
    return x,y,F


def verify_flip_identity(A,b):
    for z in SIGNS:
        x,_,F=quantities(A,z,b)
        for w in SIGNS:
            _,yW,FW=quantities(A,w,b)
            S=[i for i in range(2) if z[i]!=w[i]]
            rhs=-2*sum(z[i]*x[i]*(1+yW[i]) for i in S)
            assert FW-F==rhs, (A,b,z,w,FW-F,rhs)


def assert_safe(A):
    a,c,d=A
    assert a>1 and d>1 and (a-1)*(d-1)>c*c
    detA=a*d-c*c
    assert detA>abs(a+c) and detA>abs(d+c)
    for z in SIGNS:
        D=(a-z[0])*(d-z[1])-c*c
        assert D>0
        _,y,_=quantities(A,z,(Q(1),Q(2)))
        assert 1+y[0]==(detA-z[1]*(a+c))/D>0
        assert 1+y[1]==(detA-z[0]*(d+c))/D>0


def verify_counterexample(h,t,eps):
    L=1+h
    s=1/(2*h)
    a=L+t*s*s; c=t*s; d=L+t
    assert L*(L-1)<Q(1,4)
    assert a*d-c*c-(a+c)<0
    assert a*d-c*c-(d+c)>0
    assert (a-L)*(d-L)-c*c==0 # eigenvalue L exactly
    A=(a,c,d)
    x_bad=(-eps,Q(1))
    b=((a-1)*x_bad[0]+c*x_bad[1],c*x_bad[0]+(d-1)*x_bad[1])
    xs={z:quantities(A,z,b)[0] for z in SIGNS}
    scores={z:quantities(A,z,b)[2] for z in SIGNS}
    assert xs[(1,1)]==x_bad
    assert scores[(1,1)]>max(v for z,v in scores.items() if z!=(1,1))
    assert xs[(1,1)][0]<0 and xs[(1,1)][1]>0
    verify_flip_identity(A,b)
    return A,b,scores


def main():
    # Explicit small-integer/rational counterexample: eigenvalues 11/10 and 37/10.
    A,b,scores=verify_counterexample(Q(1,10),Q(1,10),Q(1,100))
    assert A==(Q(18,5),Q(1,2),Q(6,5))
    print('RATIONAL_COUNTEREXAMPLE', 'A=',tuple(map(str,A)),
          'b=',tuple(map(str,b)),
          'potentials=',{str(z):str(v) for z,v in scores.items()})

    for h,t,e in [(Q(1,20),Q(1,5),Q(1,1000)),
                  (Q(1,10),Q(1),Q(1,100)),
                  (Q(1,5),Q(10),Q(1,1000))]:
        verify_counterexample(h,t,e)

    # Rational parametrization A=L I + t v v^T, safe at L>=5/4.
    rng=Random(20261102)
    count=0
    for _ in range(250):
        L=Q(rng.randint(5,40),4)
        t=Q(rng.randint(0,15),7)
        u=Q(rng.randint(-15,15),5)
        v=Q(rng.randint(-15,15),5)
        A=(L+t*u*u,t*u*v,L+t*v*v)
        assert_safe(A)
        b=(Q(rng.randint(-30,30),9),Q(rng.randint(-30,30),9))
        verify_flip_identity(A,b)
        allsc={z:quantities(A,z,b)[2] for z in SIGNS}
        maxsc=max(allsc.values())
        for z,F in allsc.items():
            x,_,_=quantities(A,z,b)
            consistent=all(z[i]*x[i]>=0 for i in range(2))
            assert (F==maxsc)==consistent
        count+=1
    print('EXACT_SAFE_TESTS',count)
    print('VERIFY_OK')


if __name__=='__main__':
    main()
