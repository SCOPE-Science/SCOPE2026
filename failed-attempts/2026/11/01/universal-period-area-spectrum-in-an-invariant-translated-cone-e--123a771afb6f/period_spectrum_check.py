"""Exact rational finite tests for a translated-cone-exchange interval model.

The theorem in the companion mathematical note is proved independently of
these tests, using an explicit rotation tower and exact area integration.
"""
from fractions import Fraction as Q
from math import floor, gcd


def map_f(x, lam, delta):
    # x in the translated invariant horizontal interval [0,1+delta)
    if not Q(0) <= x < 1 + delta:
        raise ValueError('domain')
    if x < 1 - lam + delta:
        return x + lam
    if x < 1:
        return x + lam - 1
    return x - 1


def model_period(p, q, delta, x):
    lam=Q(p,q)
    assert gcd(p,q)==1 and 0<lam<1 and 0<=delta<=lam
    if x >=1:
        x-=1
    assert Q(0)<=x<1
    # base rotation by p/q, roof=2 on [1-lam,1-lam+delta)
    n=sum(1 for j in range(q) if 1-lam <= (x+j*lam)%1 < 1-lam+delta)
    return q+n


def check_orbits():
    tests=0
    for q in range(2,11):
        for p in range(1,q):
            if gcd(p,q)!=1:continue
            lam=Q(p,q)
            for d in range(0,9):
                delta=lam*Q(d,8)
                L=1+delta
                for k in range(29):
                    x=L*Q(2*k+1,58)
                    period=model_period(p,q,delta,x)
                    assert period == q+int(q*delta) or period == q+(q*delta).__ceil__()
                    y=x
                    for _ in range(period):
                        y=map_f(y,lam,delta)
                    assert y==x,(p,q,delta,x,period,y)
                    for k2 in range(1,period):
                        z=x
                        for _ in range(k2): z=map_f(z,lam,delta)
                        assert z!=x,(p,q,delta,x,k2)
                    tests+=1
    return tests


def exact_area_formula(p,q):
    lam=Q(p,q)
    values=[Q(q+j, q*q)* (Q(1,2) if j==0 or j==p else 1) for j in range(p+1)]
    full=lam+lam*lam/2
    assert sum(values)==full
    return [v/full for v in values]


def direct_integrated_class_area(p,q):
    # The distribution of q equally spaced grid points in an interval
    # of length delta has two adjacent integer counts. Integrate its
    # linearly varying class masses exactly across delta in [0,p/q].
    total={q+j:Q(0) for j in range(p+1)}
    for j in range(p):
        # Set t=q*delta = j+u, 0<=u<=1;
        # lower period q+j has x-length (q+j)(1-u)/q.
        # higher period q+j+1 has x-length (q+j+1)u/q.
        total[q+j]+=Q(q+j,2*q*q)
        total[q+j+1]+=Q(q+j+1,2*q*q)
    return total


def main():
    n=check_orbits()
    n_area=0
    for q in range(2,36):
        for p in range(1,q):
            if gcd(p,q)!=1:continue
            exact=exact_area_formula(p,q)
            direct=direct_integrated_class_area(p,q)
            lam=Q(p,q);full=lam+lam*lam/2
            assert [direct[q+j]/full for j in range(p+1)]==exact
            n_area+=1
    print('PASS exact rational orbit/least-period tests:',n)
    print('PASS exact integrated period-area spectra:',n_area)
    print('Example lambda=2/5 (periods 5,6,7):',exact_area_formula(2,5))

if __name__=='__main__':main()
