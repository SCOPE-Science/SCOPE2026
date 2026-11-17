"""Reproduce finite diagnostics for planar Kaczmarz angle identities.

The proofs of universal statements are analytic, not based on these checks.
This file uses only the Python standard library.
"""
from math import acos, cos, sin, hypot, sqrt, isclose, lgamma, log
from random import Random


def dot(u, v):
    return u[0]*v[0] + u[1]*v[1]


def vecsub(u, v, k=1.0):
    return (u[0]-k*v[0], u[1]-k*v[1])


def norm(u):
    return hypot(*u)


def check_angle_sequence(rs, tol=5e-10):
    angle = 0.0
    ev = [(1.0, 0.0)]
    for r in rs:
        angle += acos(r)
        ev.append((cos(angle), sin(angle)))
    # Independent auxiliary-vector recursion.
    gs = []
    for n, en in enumerate(ev):
        gn = en
        for j in range(n):
            gn = vecsub(gn, gs[j], dot(en, ev[j]))
        gs.append(gn)
    product, total = 1.0, 0.0
    for n, r in enumerate(rs, 1):
        prediction = product * sqrt(1-r*r)
        assert abs(norm(gs[n]) - prediction) < tol*(1+prediction)
        assert abs(dot(gs[n], ev[0])) < tol
        total += prediction
        product *= r
        # Independent residual: iterated projections of two basis vectors.
        vectors = [(1.0, 0.0), (0.0, 1.0)]
        for en in ev[:n+1]:
            vectors = [vecsub(v, en, dot(v, en)) for v in vectors]
        # Projection product is rank one: two column Euclidean Frobenius norm = op norm.
        residual = sqrt(sum(dot(v, v) for v in vectors))
        assert abs(residual - product) < tol*(1+product)
        # Independent direct max of coefficient weights achieved at vector (1,total).
        x = (1.0 / sqrt(1+total*total), total / sqrt(1+total*total))
        directly = sum(abs(dot(x,g)) for g in gs[:n+1])
        assert abs(directly - sqrt(1+total*total)) < tol*(1+total)
    return len(rs)


def power_r(n, a, b):
    return sqrt(1-a/(n+b))


def power_p_exact(n, a, b):
    return sqrt(__import__('math').exp(lgamma(b+1)+lgamma(n+b+1-a)-lgamma(b+1-a)-lgamma(n+b+1)))


def log_p(n, b, sigma):
    return sqrt(b/(n+b)) * (log(b)/log(n+b))**sigma


def main():
    rng = Random(1169)
    assertions = 0
    for count in range(1,17):
        for _ in range(4):
            rs = [0.08+0.90*rng.random() for _ in range(count)]
            assertions += check_angle_sequence(rs)
    for a,b in ((0.5,3.0),(1.,3.),(2.,4.)):
        prod=1.0
        for n in range(1,1001):
            prod*=power_r(n,a,b)
            if n in (1,2,3,10,50,100,500,1000):
                assert isclose(prod,power_p_exact(n,a,b),rel_tol=1e-11)
                assertions += 1
        # convergence to predicted constant using n^-a/2
        C = sqrt(__import__('math').exp(lgamma(b+1)-lgamma(b+1-a)))
        assert abs(prod/(C*1000**(-a/2))-1)<0.005
        assertions += 1
    for sigma in (0.,0.5,1.,2.):
        b=3.0
        for n in (20,1000,100000):
            pn=log_p(n,b,sigma)
            pprev=log_p(n-1,b,sigma)
            an=sqrt(pprev*pprev-pn*pn)
            C=sqrt(b)*log(b)**sigma
            asym=C/(n*log(n)**sigma)
            assert 0.75<an/asym<1.3
            assertions+=1
    print('PLANAR_KACZMARZ_EXACT_OK', assertions, 'finite checks')

if __name__=='__main__':
    main()
