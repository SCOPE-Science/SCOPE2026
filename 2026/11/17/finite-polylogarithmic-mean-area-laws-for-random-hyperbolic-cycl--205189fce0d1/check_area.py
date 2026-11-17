"""Standalone checks for exact random hyperbolic cyclic polygon mean areas.
No third-party packages required. Numerical checks corroborate the analytic proof.
"""
import math
import random

PI = math.pi


def polylog(s, z, tol=1e-14):
    assert s >= 2 and 0 <= z < 1
    if z == 0:
        return 0.0
    acc = 0.0
    power = 1.0
    for m in range(1, 200000):
        power *= z
        acc += power / m**s
        tail_bound = power*z/((m+1)**s*(1-z))
        if tail_bound < tol:
            return acc
    raise RuntimeError('Series convergence budget exceeded')


def exact_mean(n, R):
    assert n >= 3 and R > 0
    z = math.tanh(R/2)**2
    p = n-2
    return 2*n*(n-1)*sum(
        (-1)**j * math.factorial(p)/math.factorial(p-2*j)
        * polylog(2*j+2,z)/(2*PI)**(2*j+1)
        for j in range((p-1)//2+1)
    )


def area_gaps(gaps, R):
    k = 1/math.cosh(R)
    return (len(gaps)-2)*PI - 2*sum(math.atan(k/math.tan(g/2)) for g in gaps)


def random_gaps(n, rng):
    x = sorted(rng.random() for _ in range(n-1))
    return [2*PI*b for b in [x[0]]+[x[j]-x[j-1] for j in range(1,n-1)]+[1-x[-1]]]


def cosrule_triangle_area(gaps,R):
    sides = [2*math.asinh(math.sinh(R)*math.sin(g/2)) for g in gaps]
    def ang(a,b,c):
        v=(math.cosh(b)*math.cosh(c)-math.cosh(a))/(math.sinh(b)*math.sinh(c))
        return math.acos(max(-1,min(1,v)))
    a,b,c=sides
    return PI-ang(a,b,c)-ang(b,a,c)-ang(c,a,b)


def main():
    rng=random.Random(20318)
    for n in [3,4,5,6,8]:
        for R in [0.5,1.5,3.0]:
            exact=exact_mean(n,R)
            vals=[area_gaps(random_gaps(n,rng),R) for _ in range(20000)]
            mean=sum(vals)/len(vals)
            stderr=(sum((x-mean)**2 for x in vals)/len(vals)/len(vals))**0.5
            assert abs(mean-exact)<6*stderr+0.0002,(n,R,mean,exact,stderr)
            assert 0<exact<(n-2)*PI
    for R in [0.2,0.8,2.5]:
        for _ in range(30):
            gaps=random_gaps(3,rng)
            assert abs(area_gaps(gaps,R)-cosrule_triangle_area(gaps,R))<1e-9
    for R in [0.3,1.1,2.7]:
        assert abs(exact_mean(3,R)-6/PI*polylog(2,math.tanh(R/2)**2))<1e-12
        assert abs(exact_mean(4,R)-12/PI*polylog(2,math.tanh(R/2)**2))<1e-12
    print('HYPERBOLIC_CYCLIC_POLYLOG_CHECKS_OK')


if __name__=='__main__':
    main()
