"""Independent exact and numerical checks for the inhomogeneous hard-core cycle circle-rigidity theorem.
Run with Python 3.11+; only standard-library modules are required.
"""
from itertools import product
from math import cos, pi, sqrt
import cmath


def add(p, q):
    r = [0] * max(len(p), len(q))
    for k, a in enumerate(p): r[k] += a
    for k, a in enumerate(q): r[k] += a
    return trim(r)


def mul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q): r[i + j] += a * b
    return trim(r)


def trim(p):
    while len(p)>1 and p[-1] == 0: p.pop()
    return p


def multiply(A, B):
    return [[add(mul(A[i][0],B[0][j]),mul(A[i][1],B[1][j])) for j in (0,1)] for i in (0,1)]


def transfer_poly(bs):
    P = [[[1],[0]],[[0],[1]]]
    for b in bs:
        M = [[[1+b],[1]],[[0,1],[0,1]]]
        P = multiply(P, M)
    return add(P[0][0],P[1][1])


def independent_poly(bs):
    n = len(bs)
    coeff = [0] * (n+1)
    for mask in range(1<<(2*n)):
        if any(((mask>>j)&1) and ((mask>>((j+1)%(2*n)))&1) for j in range(2*n)):
            continue
        k = sum((mask>>(2*i))&1 for i in range(n))
        weight = 1
        for i, b in enumerate(bs):
            if (mask>>(2*i+1))&1: weight *= b
        coeff[k] += weight
    return coeff


def numerical_even_factor_roots(b, c, n):
    assert n % 2 == 0
    m = n//2
    r2 = (1+b)*(1+c)
    roots=[]
    for j in range(m):
        theta=(2*j+1)*pi/(2*m)
        a=2-2*sqrt(b*c)*cos(theta)
        discr=a*a-4*r2
        assert discr < 0
        roots.extend([(-a+cmath.sqrt(discr))/2,(-a-cmath.sqrt(discr))/2])
    return roots


def numerical_odd_factor_roots(b,n):
    assert n%2
    R=1+b
    roots=[complex(-R)]
    for j in range((n-1)//2):
        theta=(2*j+1)*pi/(2*n)
        a=2*R-4*b*cos(theta)**2
        discr=a*a-4*R*R
        assert discr < 0
        roots.extend([(-a+cmath.sqrt(discr))/2,(-a-cmath.sqrt(discr))/2])
    return roots


def evaluate(p,z):
    v=0j
    for c in reversed(p): v=v*z+c
    return v


def verify():
    checks=0
    for n in range(2,8):
        tests=[tuple(1+(i+j*j)%5 for i in range(n)) for j in range(6)]
        tests.extend([(1,)*n,tuple((2 if i%2==0 else 5) for i in range(n)),tuple((1 if i%2==0 else 4) for i in range(n))])
        for bs in tests:
            p1=transfer_poly(bs)
            p2=independent_poly(bs)
            assert p1 == p2, (n,bs,p1,p2)
            assert p1[-1] == 1 and p1[-2] == n
            W=1
            for b in bs: W*=1+b
            assert p1[0] == W
            assert p1[1] == sum(W//((1+bs[i])*(1+bs[(i-1)%n])) for i in range(n))
            checks += 1
    for n in range(2,16):
        if n%2:
            bs=(3,)*n
            roots=numerical_odd_factor_roots(3,n)
            R=4
        else:
            bs=tuple((2 if i%2==0 else 5) for i in range(n))
            roots=numerical_even_factor_roots(2,5,n)
            R=sqrt(18)
        p=transfer_poly(bs)
        assert len(roots)==n
        for z in roots:
            assert abs(abs(z)-R) < 1e-10
            assert abs(evaluate(p,z)) / (1+abs(z))**n < 1e-8, (n, z, evaluate(p,z))
        checks += n
    # The exact necessity condition is equal adjacent products. For all enumerated
    # non-2-periodic samples the coefficient identity required by a root circle fails.
    for n in range(3,9):
        for bs in product((1,2,3),repeat=n):
            if all(bs[i]==bs[(i+2)%n] for i in range(n)):
                continue
            w=[b+1 for b in bs]
            P=transfer_poly(bs)
            # By strict arithmetic-geometric mean, (c1/n) > geometric mean(w)^(n-2).
            assert (P[1]/n) > (P[0])**((n-2)/n) - 1e-10
            checks += 1
    print('VERIFIED', checks, 'exact transfer/coefficient, root-modulus, and rigidity-witness cases')

if __name__=='__main__':
    verify()
