"""Finite consistency checks for local Hardy--Littlewood stability.
Run with: python CHECK.py (requires mpmath).
Analytic proofs are supplied in RESULT.md; finite checks are not proofs of universal claims.
"""
from fractions import Fraction as Q
from math import factorial
import mpmath as mp

mp.mp.dps=65
checks=0

def coef(a,k):
    z=Q(1)
    for j in range(k):
        z *= (a+j)/Q(j+1)
    return z

for a,b,p in [(Q(1,2),Q(3,4),Q(1)),(Q(1,2),Q(2),Q(4,5)),(Q(17,20),Q(23,20),Q(31,10)),(Q(1,5),Q(6,5),Q(7))]:
    q=p*b/a
    g=p*Q(1,2)*(b-a)/(b+1)
    assert g>0; checks+=1
    assert Q(p,2)*(1-(b/a)*coef(a,2)/coef(b,2))==g; checks+=1
    assert Q(p,2)*(1-(b/a)*coef(a,1)/coef(b,1))==0; checks+=1
    last=Q(0)
    for k in range(2,101):
        lam=Q(p,2)*(1-(b/a)*coef(a,k)/coef(b,k))
        assert lam>=g and lam>last and lam<p/Q(2); checks+=1
        last=lam
    for k in range(2,21):
        r=(b/a)*coef(a,k)/coef(b,k)
        rn=(b/a)*coef(a,k+1)/coef(b,k+1)
        assert rn/r == (a+k)/(b+k); checks+=1


def norm_power(s,p,k,t):
    # For f=1+t*z**k, the binomial expansion of f**(p/2) gives an
    # EXACT Hilbert-norm series, truncated here with an explicit small t.
    s=mp.mpf(s.numerator)/s.denominator
    p=mp.mpf(p.numerator)/p.denominator
    t=mp.mpf(t)
    return mp.fsum([abs(mp.binomial(p/2,j)*t**j)**2 * mp.factorial(k*j)/mp.rf(s,k*j)
                    for j in range(64)])

for a,b,p in [(Q(1,2),Q(3,4),Q(1)),(Q(1,2),Q(2),Q(4,5)),(Q(17,20),Q(23,20),Q(31,10))]:
    q=p*b/a
    for k in (1,2,3,4):
        target=mp.mpf(p.numerator)/(2*p.denominator)*(1-mp.mpf(b.numerator)*a.denominator/(b.denominator*a.numerator)*
                  (mp.mpf(coef(a,k).numerator)/coef(a,k).denominator)/
                  (mp.mpf(coef(b,k).numerator)/coef(b,k).denominator))
        estimates=[]
        for t in ('0.003','0.0003'):
            na=norm_power(a,p,k,t)**(mp.mpf(2)*p.denominator/p.numerator)
            nb=norm_power(b,q,k,t)**(mp.mpf(2)*q.denominator/q.numerator)
            sa=mp.mpf(coef(a,k).numerator)/coef(a,k).denominator
            v=(na-nb)*sa/mp.mpf(t)**2
            estimates.append(v)
            assert abs(v-target)<mp.mpf('0.005'); checks+=1
        assert abs(estimates[1]-target)<abs(estimates[0]-target); checks+=1

print('PASS finite checks:',checks)
