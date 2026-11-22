"""Numerical and exact-rational checks for Pareto minCF power-weight identities.
Run: python check.py  (Python 3 standard library only).
Finite checks corroborate, but do not prove, the all-parameter theorem.
"""
from fractions import Fraction as Q
from math import exp, log, isclose


def truncated_moment(alpha, p, t):
    if alpha == p:
        return t**p * (1 + p * log(1/t))
    return (p * t**alpha - alpha * t**p)/(p-alpha)


def trace(alpha, beta):
    return 2*alpha / ((alpha-beta)*(2*alpha-beta)*(2-beta)*(alpha+1-beta))


def integral_direct(alpha, beta, upper_u=120.0, pieces=40000):
    # t=exp(-u), and t^(-1-beta) dt = exp(beta*u) du.
    assert pieces % 2 == 0
    h=upper_u/pieces
    total=0.0
    for i in range(pieces+1):
        u=i*h
        t=exp(-u)
        m1=truncated_moment(alpha,1.0,t)
        m2=truncated_moment(alpha,2.0,t)
        vari=max(0.0, m2-m1*m1)
        f=vari*exp(beta*u)
        total+= (1 if i in (0,pieces) else 4 if i%2 else 2)*f
    return total*h/3


def algebraic_integral(a,b):
    # The two truncated moments and their square are integrated term-by-term.
    if a==1:
        r=2/(1-b)-2/(2-b)-2/(2-b)**2-2/(2-b)**3
    elif a==2:
        r=-3/(2-b)+2/(2-b)**2+4/(3-b)-1/(4-b)
    else:
        r=(2/(2-a)/(a-b) - a/(2-a)/(2-b)
           -(a*a/(2-b)-2*a/(a+1-b)+1/(2*a-b))/(a-1)**2)
    return r


def main():
    checks=0
    for a in [Q(1,3),Q(1,2),Q(3,4),Q(1),Q(5,4),Q(3,2),Q(2),Q(3),Q(5)]:
        for f in [Q(1,5),Q(1,3),Q(1,2),Q(3,4)]:
            b=f*min(a,Q(2))
            assert algebraic_integral(a,b)==trace(a,b), (a,b)
            checks+=1
    # Compare an independent direct Simpson integral of the variance with exact value.
    samples=[(.5,.25),(1.,.5),(1.5,1.),(2.,1.),(3.,1.),(.75,.4),(2.5,1.5)]
    for a,b in samples:
        got=integral_direct(a,b)
        target=trace(a,b)
        assert isclose(got,target,rel_tol=2e-6,abs_tol=2e-7),(a,b,got,target)
        checks+=1
    # The second truncated moment indeed matches a direct Pareto integral in x.
    for a in [.5,1.,1.5,2.,3.]:
        for p in [1.,2.]:
            for t in [.05,.2,.7]:
                # Integrate over x in [1,1/t], then add Pareto survival t^alpha.
                # Polynomial integration formula as independent density check.
                cutoff=1/t
                if a==p:
                    integrate=a*t**p*log(cutoff)
                else:
                    integrate=a*t**p*(cutoff**(p-a)-1)/(p-a)
                got=integrate+t**a
                expected=truncated_moment(a,p,t)
                assert isclose(got,expected,rel_tol=1e-12,abs_tol=1e-12)
                checks+=1
    # Representative boundary exponents (small-t comparison, not proof).
    for a in [.5,1.,1.5,2.,3.]:
        for t in [1.e-4,1.e-6]:
            p1=truncated_moment(a,1.,t)
            p2=truncated_moment(a,2.,t)
            assert p2+1e-13 >= p1*p1
            checks+=1
    print(f'PASS: {checks} algebraic, integral, and distribution-moment checks')
    for a,b in samples:
        print(f'alpha={a:g}, beta={b:g}, exact trace={trace(a,b):.12g}')

if __name__=='__main__': main()
