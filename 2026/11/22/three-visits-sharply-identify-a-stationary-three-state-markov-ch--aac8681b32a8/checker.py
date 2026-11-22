"""Exact-arithmetic reproducibility checks for three-visit Markov count inversion.

Requires only Python 3.10+ standard library. This samples rational stationary
flow matrices and verifies the theorem's reconstruction identities; it is not
a replacement for the universal algebraic proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import isqrt

CHECKS = 0

def assert_equal(a, b):
    global CHECKS
    assert a == b, (a, b)
    CHECKS += 1

def rational_root(x):
    assert x >= 0
    a, b = isqrt(x.numerator), isqrt(x.denominator)
    assert a*a == x.numerator and b*b == x.denominator, x
    return Q(a, b)

def count_law(P, pi, n=3):
    d = len(P)
    ans = {}
    for path in product(range(d), repeat=n):
        pr = pi[path[0]]
        for a, b in zip(path, path[1:]):
            pr *= P[a][b]
        c = tuple(path.count(i) for i in range(d))
        ans[c] = ans.get(c, Q(0)) + pr
    return ans

def reverse(P, pi):
    return [[pi[j]*P[j][i]/pi[i] for j in range(3)] for i in range(3)]

def reconstructions(law):
    e = [tuple(3 if k == i else 0 for k in range(3)) for i in range(3)]
    pi = [sum(Q(c[i])*prob for c, prob in law.items())/3 for i in range(3)]
    q = [rational_root(law.get(e[i],Q(0))/pi[i]) for i in range(3)]
    u = [2*pi[i]*(1-q[i]) for i in range(3)]
    s = {}
    rho = {}
    for i in range(3):
        for j in range(i+1, 3):
            k = 3-i-j
            s[i,j] = (u[i]+u[j]-u[k])/2
            cnt = tuple(2 if a == i else 1 if a == j else 0 for a in range(3))
            b = law.get(cnt, Q(0))
            rho[i,j] = (b-q[i]*s[i,j])/pi[i]
            cnt2 = tuple(2 if a == j else 1 if a == i else 0 for a in range(3))
            assert_equal(b-q[i]*s[i,j], (law.get(cnt2,Q(0))-q[j]*s[i,j])*pi[i]/pi[j])
    magnitude = []
    for (i,j), sij in s.items():
        magnitude.append(rational_root(sij*sij-4*pi[i]*pi[j]*rho[i,j]))
    assert_equal(magnitude[0], magnitude[1])
    assert_equal(magnitude[1], magnitude[2])
    out = []
    for sign in (1,-1):
        J = sign*magnitude[0]
        flow = [[Q(0) for _ in range(3)] for _ in range(3)]
        for i in range(3):
            flow[i][i]=pi[i]*q[i]
        for i,j in ((0,1),(1,2),(2,0)):
            z = s[min(i,j),max(i,j)]
            flow[i][j]=(z+J)/2
            flow[j][i]=(z-J)/2
        trial = [[flow[i][j]/pi[i] for j in range(3)] for i in range(3)]
        assert_equal([sum(row) for row in trial], [Q(1)]*3)
        assert_equal(count_law(trial, pi), law)
        out.append(trial)
    return pi, out

def test_flow(diags, edges, current):
    weights = [[Q(0) for _ in range(3)] for _ in range(3)]
    for i in range(3): weights[i][i]=Q(diags[i])
    for (i,j), e in zip(((0,1),(1,2),(2,0)),edges):
        assert e>=abs(current)
        weights[i][j]=Q(e+current)
        weights[j][i]=Q(e-current)
    total=sum(map(sum, weights), Q(0))
    F=[[a/total for a in row] for row in weights]
    pi=[sum(row) for row in F]
    P=[[F[i][j]/pi[i] for j in range(3)] for i in range(3)]
    assert_equal([sum(F[i][j] for i in range(3)) for j in range(3)], pi)
    law=count_law(P,pi)
    pi2, options=reconstructions(law)
    assert_equal(pi2, pi)
    assert_equal(P in options, True)
    assert_equal(reverse(P,pi) in options, True)

# Includes directed cycles, asymmetric stationary distributions, zero diagonals,
# zero off-diagonal entries, symmetric and nonreversible transition structures.
for d in ((0,0,0), (1,2,3), (3,0,7), (2,5,9), (1,1,1)):
    for edges in ((2,2,2),(2,3,4),(1,5,2),(3,4,6),(0,3,2)):
        for c in range(-min(edges),min(edges)+1):
            if sum(edges)==0: continue
            test_flow(d, edges, c)

p0=[[Q(1,2),Q(1,4),Q(1,4)], [Q(1,4),Q(1,2),Q(1,4)], [Q(1,4),Q(1,4),Q(1,2)]]
p1=[[Q(1,2),Q(3,8),Q(1,8)], [Q(1,8),Q(1,2),Q(3,8)], [Q(3,8),Q(1,8),Q(1,2)]]
pi=[Q(1,3)]*3
assert_equal(count_law(p0,pi,n=2), count_law(p1,pi,n=2))
assert_equal(Q(1,4)-p0[0][1]*p0[1][0],Q(3,16))
assert_equal(Q(1,4)-p1[0][1]*p1[1][0],Q(13,64))
print(f'PASS: {CHECKS} exact-rational assertions')
