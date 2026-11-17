"""Exact, reproducible finite verification of a two-class first-return construction.

Only finite rational calculations are tested; the unrestricted theorem requires its proof.
"""
from fractions import Fraction as Q
from math import log


def f(d, state):
    x,y=state
    if x <= 0:
        return (x+y+1,Q(0))
    return (y+1,-d*x)


def iterate_return(d,x):
    cur=(x,Q(0))
    for t in range(1,2*d+4):
        cur=f(d,cur)
        if cur[1]==0 and 0<cur[0]<1:
            return t,cur[0]
    raise AssertionError(('no return',d,x,cur))


def one(d):
    # Every cell is checked at four interior rational fractions.
    checks=0
    distribution=[]
    for j in range(d):
        for u in (Q(1,7),Q(2,7),Q(4,7),Q(6,7)):
            x=(Q(j)+u)/(d*d)
            t,out=iterate_return(d,x)
            assert (t,out)==(2*d+2-j,u),(d,j,'A',x,t,out,u)
            checks+=1
        distribution.append((Q(1,d*d),2*d+2-j))
    for j in range(d-1):
        for u in (Q(1,7),Q(2,7),Q(4,7),Q(6,7)):
            x=(Q(j+1)+u)/d
            t,out=iterate_return(d,x)
            assert (t,out)==(d+3+j,1-u),(d,j,'B',x,t,out,u)
            checks+=1
        distribution.append((Q(1,d),d+3+j))
    assert sum((p for p,r in distribution),Q(0))==1
    mean=sum((p*r for p,r in distribution),Q(0))
    var=sum((p*(r-mean)**2 for p,r in distribution),Q(0))
    assert mean==Q((d+1)*(3*d+1),2*d)
    assert var==Q((d-1)*(d+1)*(d*d-2*d+3),12*d*d)
    # A full branch of slope d^2, another of slope -d.
    entropy=sum((-float(p)*log(float(p)) for p,r in distribution))
    assert abs(entropy/float(mean)-2*log(d)/(3*d+1))<1e-12
    return checks


def main():
    total=sum(one(d) for d in range(2,25))
    print('VERIFY_OK exact_rational_orbit_checks=%d integer_parameters=23'%(total,))
    print('return_probabilities, mean, variance: exact rational checks')
    print('entropy_formula: finite numerical cross-check')


if __name__=='__main__':
    main()
