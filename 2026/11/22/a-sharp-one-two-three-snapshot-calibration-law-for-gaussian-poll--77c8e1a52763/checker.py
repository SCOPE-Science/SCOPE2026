"""Finite reproducibility checks for a single calibrated free-space diffusion puff.
No external dependencies. Analytic global statements are proved in RESULT.md.
"""
from fractions import Fraction as F
from math import exp, log, pi, isclose
import random

checks = 0

def ok(condition, why=''):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(f'check {checks} failed: {why}')


def rank(a):
    b = [[F(v) for v in row] for row in a]
    m = len(b)
    n = len(b[0])
    r = 0
    for j in range(n):
        k = next((k for k in range(r, m) if b[k][j] != 0), None)
        if k is None: continue
        b[r], b[k] = b[k], b[r]
        scale = b[r][j]
        b[r] = [v / scale for v in b[r]]
        for i in range(m):
            if i != r:
                scale = b[i][j]
                b[i] = [b[i][c] - scale*b[r][c] for c in range(n)]
        r += 1
        if r == m: break
    return r


def linear_solve(A, B):
    n = len(B)
    M = [list(map(float, row)) + [float(b)] for row, b in zip(A, B)]
    for j in range(n):
        k = max(range(j, n), key=lambda i: abs(M[i][j]))
        ok(abs(M[k][j]) > 1e-14, 'invertible design')
        M[j], M[k] = M[k], M[j]
        v = M[j][j]
        for t in range(j, n+1): M[j][t] /= v
        for i in range(n):
            if i == j: continue
            v = M[i][j]
            for t in range(j, n+1): M[i][t] -= v*M[j][t]
    return [M[j][-1] for j in range(n)]


def sites(d):
    e = []
    for j in range(d):
        e.append(tuple(F(int(j==i)) for i in range(d)))
    return [e[0], tuple(-x for x in e[0])] + e[1:]


def squared(a, b):
    return sum((x-y)**2 for x,y in zip(a,b))


def concentration(s, z, mass, D, age):
    return mass*(4*pi*D*age)**(-len(s)/2)*exp(-float(squared(s,z))/(4*D*age))

# Exactly d+1 affinely spanning sites on a unit sphere, and a full-rank
# quadratic array with one additional site in the interior.
for d in range(1, 6):
    S = sites(d)
    A = [[F(1), *s] for s in S]
    H = [[F(1), *s, squared(s,(F(0),)*d)] for s in S]
    ok(len(S) == d+1)
    ok(rank(A) == d+1)
    ok(rank(H) == d+1)
    ok(all(squared(s,(F(0),)*d) == 1 for s in S))
    extra = (F(0),)*d
    ok(rank([[F(1), *s, squared(s,extra)] for s in S+[extra]]) == d+2)
    if d>=2:
        # Hyperplane reflection gives exact distance twin for every point.
        flat = [tuple([F(0)]+list(s[1:])) for s in S]
        z1 = tuple([F(2)] + [F(j+1,3) for j in range(d-1)])
        z2 = tuple([-F(2)] + [F(j+1,3) for j in range(d-1)])
        ok(rank([[F(1), *s] for s in flat]) < d+1)
        for s in flat:
            ok(squared(s,z1) == squared(s,z2))

# Radial age profiles are peaked and ratios of shifted profiles have an
# interior strict minimum; the example has an exact two-time ambiguity.
def g(u, p=1, a=1):
    return u**(-p)*exp(-a/u)

def ratio(u, h=1):
    return g(u+h)/g(u)

u1=1.0
r1=ratio(u1)
ok(ratio(2.0) < r1 < ratio(4.0))
lo,hi=2.0,4.0
for _ in range(95):
    md=(lo+hi)/2
    if ratio(md)<r1: lo=md
    else: hi=md
u2=(lo+hi)/2
ok(u2>2)
ok(isclose(ratio(u2),r1,rel_tol=1e-13))
M1=1.0
M2=M1*g(u1)/g(u2)
ok(abs(M2-M1)>1e-4)
for delta in (0,1):
    ok(isclose(M1*g(u1+delta), M2*g(u2+delta), rel_tol=2e-13))
ok(not isclose(M1*g(u1+2), M2*g(u2+2), rel_tol=1e-7))

# Known mass, one snapshot is ambiguous on an affinely spanning sphere.
target=g(.5)
lo,hi=1.,15.
for _ in range(95):
    md=(lo+hi)/2
    if g(md) > target: lo=md
    else: hi=md
u3=(lo+hi)/2
ok(u3>1)
ok(isclose(g(u3),g(.5),rel_tol=1e-13))
ok(not isclose(g(u3+1),g(1.5),rel_tol=1e-7))

# Quadratic polynomial interpolation reconstructs parameters from ONE
# snapshot for nonspherical arrays in 1-5 dimensions, without knowing M.
rng = random.Random(20261121)
for d in range(1, 6):
    S=sites(d)+[(F(0),)*d]
    Q=[[1.,*[float(v) for v in s], float(squared(s,(F(0),)*d))] for s in S]
    for trial in range(320):
        z = [rng.uniform(-1.5,1.5) for _ in range(d)]
        D = rng.uniform(.20,1.5)
        age = rng.uniform(.8,4.)
        mass = rng.uniform(.4,3.)
        ys = [concentration(s,z,mass,D,age) for s in S]
        coeff = linear_solve(Q,[log(y) for y in ys])
        c=coeff[-1]
        recovered_age = -1/(4*D*c)
        z2=[-coeff[1+j]/(2*c) for j in range(d)]
        M = exp(coeff[0]+sum(v*v for v in z2)/(4*D*recovered_age))*(4*pi*D*recovered_age)**(d/2)
        ok(isclose(recovered_age,age,rel_tol=1e-9,abs_tol=1e-9))
        ok(isclose(M,mass,rel_tol=1e-9,abs_tol=1e-9))
        for a,b in zip(z,z2):
            ok(isclose(a,b,rel_tol=1e-9,abs_tol=1e-9))

# Two-time spatial-ratio reconstruction on co-spherical arrays away from
# the circumcenter. One snapshot is at time t1=3 and second at t2=4.
for d in range(1,6):
    S=sites(d)
    x0=S[0]
    A=[[float(s[j]-x0[j]) for j in range(d)] for s in S[1:]]
    for trial in range(400):
        z = [rng.uniform(-.7,.7) for j in range(d)]
        if max(map(abs,z))<.04: z[0]=.3
        D=rng.uniform(.15,1.5)
        age=rng.uniform(.9,3.2)
        mass=rng.uniform(.5,6.)
        y1=[concentration(s,z,mass,D,age) for s in S]
        y2=[concentration(s,z,mass,D,age+1) for s in S]
        delta1=[log(v/y1[0]) for v in y1[1:]]
        delta2=[log(v/y2[0]) for v in y2[1:]]
        j=max(range(d),key=lambda j: abs(delta1[j]))
        ok(abs(delta1[j])>1e-8)
        r=delta1[j]/delta2[j]
        age2=1/(r-1)
        ok(isclose(age2,age,rel_tol=2e-7,abs_tol=2e-7))
        # Equal-radius sensors yield delta_i=(s_i-s0).z/(2 D age).
        z2=linear_solve(A, [2*D*age2*v for v in delta1])
        for a,b in zip(z,z2):
            ok(isclose(a,b,rel_tol=2e-7,abs_tol=2e-7))
        M=y1[0]*(4*pi*D*age2)**(d/2)*exp(float(squared(x0,z2))/(4*D*age2))
        ok(isclose(M,mass,rel_tol=2e-7,abs_tol=2e-7))

# Scalar calculus sign statements for 2 vs 3 observations in the exact
# circumcenter case: a derivative with at most one zero, sharp two-time fold.
for d in range(1,8):
    p=d/2
    a=rng.uniform(.1,3.)
    h=rng.uniform(.1,2.)
    # Derivative of log(g(u+h)/g(u)) changes sign precisely once.
    def sign_derivative(u):
        return p-a*(1/u+1/(u+h))
    lo,hi=1e-6,100.
    ok(sign_derivative(lo)<0<sign_derivative(hi))
    for _ in range(75):
        md=(lo+hi)/2
        if sign_derivative(md)<0: lo=md
        else: hi=md
    u0=(lo+hi)/2
    ok(u0>0)
    for u in [u0*.3,u0*.7,u0*1.3,u0*3]:
        ok((sign_derivative(u)<0) == (u<u0))
print(f'PASS: {checks} deterministic numerical/exact assertions; analytic bounds in RESULT.md')
