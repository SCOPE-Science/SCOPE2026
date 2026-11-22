"""Finite corroboration of the split-coordinate-disc circumradius theorem.

Run with `python verify.py` (Python standard library only). These finite
checks do not replace the proof for arbitrary integers and real weights.
"""
from math import sqrt, isclose
from random import Random


def predicted(a, b, t):
    gap = a - b
    critical = (a - 1) / (sqrt(2) * gap) if gap > 0 else float('inf')
    if gap > 0 and t > critical:
        s = a * (a - 1)**2 / (gap * ((a - 1)**2 + 2*b*gap*t*t))
        R2 = a*a*((a - 1)**2 / (2*gap) + b*t*t)
    else:
        s = 1.0
        R2 = a * ((a - 1)/sqrt(2) + b*t)**2
    return s, R2


def support_from_squares(a, b, t, z):
    return (sum(sqrt(z[i] + z[j]) for i in range(a)
                for j in range(i+1, a))
            + t*sum(sqrt(z[i] + z[j]) for i in range(a)
                    for j in range(a,a+b)))


def reduced_support(a, b, t, s):
    return ((a-1)*sqrt(a/2)*sqrt(s)
            + t*sqrt(a*b)*sqrt(a+(b-a)*s))


def test():
    rng=Random(20261117)
    n_cases=0
    simplex_tests=0
    grid_tests=0
    worst=0.0
    for a in range(2,12):
        for b in range(1,9):
            crit=(a-1)/(sqrt(2)*(a-b)) if a>b else 1.
            for t in (0.2,0.6,1.0,1.4,2.8,crit*0.97,crit*1.03):
                s, R2=predicted(a,b,t)
                assert 0<s<=1
                z=[s/a]*a+[(1-s)/b]*b
                value=support_from_squares(a,b,t,z)
                assert isclose(value**2,R2,rel_tol=1e-11,abs_tol=1e-10)
                for k in range(1001):
                    ss=k/1000
                    f=reduced_support(a,b,t,ss)
                    worst=max(worst,f-value)
                    assert f<=value+1e-9
                    grid_tests+=1
                for _ in range(30):
                    z=[rng.expovariate(1) for _ in range(a+b)]
                    total=sum(z)
                    z=[x/total for x in z]
                    assert support_from_squares(a,b,t,z)<=value+1e-9
                    simplex_tests+=1
                n_cases+=1
    # One exact transparent integer-parameter example above the threshold.
    s,rad2=predicted(5,2,1)
    assert isclose(s,20/21,abs_tol=1e-14)
    assert isclose(rad2,350/3,abs_tol=1e-12)
    print(f'SPLIT_DISCOTOPE_PASS cases={n_cases} one_variable_grid={grid_tests} full_simplex_tests={simplex_tests} max_grid_excess={worst:.2e}')

if __name__ == '__main__':
    test()
