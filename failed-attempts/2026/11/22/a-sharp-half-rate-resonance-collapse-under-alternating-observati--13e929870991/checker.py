"""Exact rational verification of a two-phase periodic threshold/reset clock.

No external dependencies. Formula proof is analytic and supplied separately.
"""
from fractions import Fraction as Q


def next_spike(t, a, b, travel):
    P = a+b
    z = t+travel
    # exact rational ceiling to the two available phases
    k = z // P
    z0 = k*P
    if z <= z0:
        return z0
    if z <= z0+a:
        return z0+a
    return (k+1)*P


def theoretical_period(a,b,travel):
    P=a+b
    q, r=divmod(travel,P)
    if r==0:
        return q*P,1
    if r <= min(a,b):
        return (2*q+1)*P,2
    return (q+1)*P,1


def check(a,b,travel):
    P=a+b
    total, spikect=theoretical_period(a,b,travel)
    # start at both possible spike phases and iterate sufficiently
    for start in (Q(0),a):
        t=start
        seen={}
        for step in range(5):
            phase=t%P
            if phase in seen:
                s, u=seen[phase]
                assert step-s==spikect,(a,b,travel,start,step,s,spikect)
                assert t-u==total,(a,b,travel,start,t,u,total)
                break
            seen[phase]=step,t
            t=next_spike(t,a,b,travel)
        else:
            raise AssertionError(('no cycle',a,b,travel))
    return True

if __name__=='__main__':
    n=0
    for a in range(1,11):
        for b in range(1,11):
            for numerator in range(1,251):
                for denominator in (1,2,3,4,5):
                    check(Q(a),Q(b),Q(numerator,denominator))
                    n+=1
    # Exact resonant examples and boundaries:
    for eps in (Q(0),Q(1,10),Q(1,100),Q(1,10000)):
        check(Q(1,2)+eps,Q(1,2)-eps,Q(1,2))
    assert next_spike(Q(0),Q(51,100),Q(49,100),Q(1,2)) == Q(51,100)
    assert next_spike(Q(51,100),Q(51,100),Q(49,100),Q(1,2)) == Q(151,100)
    print('PASS: exact two-phase transition table checked on',n,'rational parameter triples, two initial phases each')
    print('PASS: exact resonance and one-sided threshold checks')
