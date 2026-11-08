"""Exact finite-state and equilibrium checks for unequal-fidelity two-memory walks.
No simulations or finite checks purport to prove the infinite-time limit.
"""
from fractions import Fraction as F
from itertools import product


def channels(p1,p2,plus,minus,zero):
    n=plus+minus+zero
    assert n>0
    a,b=2*p1-1,2*p2-1
    x=F(plus-minus,n); q=F(plus+minus,n); c=F(zero,n)
    ua=(q+a*x)/2; va=(q-a*x)/2
    ub=(q+b*x)/2; vb=(q-b*x)/2
    pp=ua*ub+c*(ua+ub)
    pm=va*vb+c*(va+vb)
    p0=c*c+ua*vb+va*ub
    return x,q,c,a,b,pp,pm,p0


def check():
    t=0
    for p1,p2 in product((F(1,2),F(2,3),F(3,4),F(9,10),F(19,20)),repeat=2):
        a=2*p1-1; b=2*p2-1; s=(a+b)/2
        for n in range(1,13):
            for plus in range(n+1):
                for minus in range(n-plus+1):
                    zero=n-plus-minus
                    x,q,c,_,_,pp,pm,p0=channels(p1,p2,plus,minus,zero)
                    assert pp>=0 and pm>=0 and p0>=0 and pp+pm+p0==1
                    assert pp-pm==s*(1+c)*x
                    assert p0==c*c+(q*q-a*b*x*x)/2
                    assert (pp+pm)-q==q-F(3,2)*q*q+a*b*x*x/2
                    t+=4
        if s>F(3,4) and a*b>0:
            qstar=2-1/s
            v2=(2*s-1)*(4*s-3)/(a*b*s*s)
            assert 0<v2<qstar*qstar
            assert qstar-F(3,2)*qstar*qstar+a*b*v2/2==0
            assert s*(2-qstar)-1==0
            recovered=s*s-(a-b)**2/4
            assert recovered==a*b
            assert v2*a*b*s*s==(2*s-1)*(4*s-3)
            t+=5
    print(f'{t} exact rational assertions passed')

if __name__=='__main__': check()
