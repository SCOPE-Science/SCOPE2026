"""Exact rational cross-energy cumulant checks for common-reset harmonic diffusions.

Run with Python 3, no third-party dependencies.
"""
from fractions import Fraction as F
from itertools import combinations
import random


def stat_moments(rate, omega, temperature):
    """Stationary moment recursion from the diffusion-reset generator."""
    n = len(omega)
    moments = {0: F(1)}
    for cardinality in range(1, n + 1):
        for index_set in combinations(range(n), cardinality):
            mask = sum(1 << i for i in index_set)
            rhs = sum(omega[i] * temperature[i] * moments[mask & ~(1 << i)]
                      for i in index_set)
            moments[mask] = rhs / (rate + sum(omega[i] for i in index_set))
    return moments


def exact_cov(rate, omega, temperature, i, j):
    a, b = omega[i], omega[j]
    return (temperature[i]*temperature[j]*rate*a*b /
            ((rate+a)*(rate+b)*(rate+a+b)))


def exact_triple(rate, omega, temperature):
    a, b, c = omega
    p = a+b+c
    e2 = a*b+a*c+b*c
    e3 = a*b*c
    denominator = ((rate+a)*(rate+b)*(rate+c)*(rate+a+b)
                   *(rate+a+c)*(rate+b+c)*(rate+p))
    return (temperature[0]*temperature[1]*temperature[2]
            *a*b*c*rate*(2*rate**3+2*p*rate**2-p*e2+e3)/denominator)


def raw_cumulant(m):
    a, b, c = 1,2,4
    return (m[7] - m[3]*m[4] - m[5]*m[2] - m[6]*m[1]
            + 2*m[1]*m[2]*m[4])


def threshold_numerator(rate, omega):
    a,b,c = omega
    p=a+b+c
    return 2*rate**3+2*p*rate**2-p*(a*b+a*c+b*c)+a*b*c


def check():
    rng = random.Random(60821)
    total = 0
    for _ in range(550):
        omega = [F(rng.randint(1, 22), rng.randint(1, 15)) for i in range(3)]
        temp = [F(rng.randint(1, 20), rng.randint(1, 8)) for i in range(3)]
        rate = F(rng.randint(1, 40), rng.randint(1, 22))
        M = stat_moments(rate, omega, temp)
        for i,j in combinations(range(3),2):
            c = M[(1<<i)|(1<<j)]-M[1<<i]*M[1<<j]
            assert c == exact_cov(rate, omega,temp,i,j) > 0
            total += 1
        k = raw_cumulant(M)
        assert k == exact_triple(rate, omega, temp)
        assert (k>0)-(k<0) == ((threshold_numerator(rate,omega)>0)-
                               (threshold_numerator(rate,omega)<0))
        total += 2
        for perm in ((1,0,2),(2,1,0),(1,2,0)):
            w=[omega[i] for i in perm]
            v=[temp[i] for i in perm]
            assert exact_triple(rate,w,v)==k
            total+=1
        lower=min(omega)
        upper=sum(omega)/3
        assert threshold_numerator(lower, omega) <=0
        assert threshold_numerator(upper, omega) >=0
        total+=2
        # A balancing transfer from larger a to smaller b (same sum)
        a,b,c=sorted(omega)
        middle=(a+b)/2
        before = (a+b+c)*(a*b+b*c+a*c)-a*b*c
        after = (a+b+c)*(middle**2+middle*c*2)-middle*middle*c
        assert after>=before
        total+=1
    # Scalar equality boundary for the isotropic rate, all temperatures
    for q in range(1,31):
        v=F(q,q+2)
        assert exact_triple(v,[v]*3,[F(1),F(2),F(3)])==0
        total+=1
    # Critical simple anisotropic rational case: (1,1,10), r=... positive tests
    omega=[F(1),F(1),F(10)]
    assert threshold_numerator(F(2),omega)<0
    assert threshold_numerator(F(3),omega)>0
    total+=2
    print('PASS:',total,'exact-rational assertions; 550 rational parameter instances')

if __name__ == '__main__':
    check()
