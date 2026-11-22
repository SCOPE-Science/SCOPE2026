"""Exact diagnostic checks for parallel power-law drainage and recession curvature.

Requires Python >=3.9, standard library only. Diagnostics do not replace the proof.
"""
from fractions import Fraction as F
from itertools import product

def value(p, A, B, a, b, t):
    u = F(1, 1) / (t+a)
    v = F(1, 1) / (t+b)
    q = A*u**p + B*v**p
    q1 = -p*(A*u**(p+1)+B*v**(p+1))
    q2 = p*(p+1)*(A*u**(p+2)+B*v**(p+2))
    q3 = -p*(p+1)*(p+2)*(A*u**(p+3)+B*v**(p+3))
    beta = q*q2/q1**2
    derivative = (q1*q2+q*q3)/q1**2 - 2*q*q2**2/q1**3
    r = (t+a)/(t+b)
    excess = F(p+1,p)*A*B*r**p*(1-r)**2/(A+B*r**(p+1))**2
    factor = A*(p-(p+2)*r)-B*r**(p+1)*(p+2-p*r)
    return beta, derivative, excess, factor, r

def main():
    checks = 0
    for p, A, B, a, b, t in product(
         (2,3,4,5), (F(1), F(2), F(5), F(27)),
         (F(1), F(3), F(10), F(1000)),
         (F(1,2), F(1), F(2)), (F(3), F(4), F(10)),
         (F(0), F(1,7), F(1,2), F(1), F(5))):
        assert a<b
        beta,derivative,excess,factor,r = value(p,A,B,a,b,t)
        assert beta == F(p+1,p) + excess
        assert excess > 0
        assert (derivative > 0) == (factor > 0)
        assert (derivative < 0) == (factor < 0)
        assert (derivative == 0) == (factor == 0)
        checks += 5
    # Known simple-reservoir benchmark and exact sharp extremal point.
    p,A,B,a,b,t = 2,F(5),F(27),F(1),F(4),F(1,2)
    beta,derivative,_,factor,r = value(p,A,B,a,b,t)
    assert r==F(1,3) and derivative==0 and factor==0
    assert beta==F(16,9)
    checks+=5
    # For p=2, offset ratio b/a>3 is sharp for the *possibility*,
    # over all amplitudes, of b_app exceeding 2 at some positive time.
    p,A,B,a,b,t = 2,F(27),F(1000),F(1),F(4),F(2,7)
    beta,_,_,_,r = value(p,A,B,a,b,t)
    assert r==F(3,10)
    assert beta==F(169,80), (beta,F(169,80))
    assert beta>2
    checks+=3
    # For offsets a/b >= 1/3 and p=2, optimized envelope never exceeds 2.
    for r in (F(1,3), F(2,5), F(1,2), F(9,10)):
        upper=F(3,2)*(1+ (1-r)**2/(4*r))
        assert upper<=2
        checks+=1
    print('PASS',checks,'exact assertions')

if __name__=='__main__':main()
