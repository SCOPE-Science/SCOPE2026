"""Exact rational tests for pendant-trap hitting-time theorem.

Usage: python pendant_hitting_checker.py
Independent full-generator inversion is compared with the core local-time
resolvent formula. No simulation or numerical approximations are used.
"""
import sympy as S

CHECKS = 0

def check(flag, message):
    global CHECKS
    if flag is not True and flag != S.true:
        raise AssertionError(message)
    CHECKS += 1

def generator(n, edges):
    q = S.zeros(n)
    for (u, v, c) in edges:
        c = S.sympify(c)
        q[u, v] += c
        q[v, u] += c
        q[u, u] -= c
        q[v, v] -= c
    return q

def killed(q, y):
    ix = [i for i in range(q.rows) if i != y]
    return ix, q.extract(ix, ix), q.extract(ix, [y])

def full_moments(q, x, y):
    ix, qt, _ = killed(q, y)
    N = (-qt).inv()
    ones = S.ones(len(ix), 1)
    mean = N*ones
    second = 2*N*N*ones
    k = ix.index(x)
    return S.factor(mean[k]), S.factor(second[k]-mean[k]**2)

def direct_lt(q, x, y, s):
    ix, qt, out = killed(q, y)
    return S.factor(((s*S.eye(len(ix))-qt).inv()*out)[ix.index(x)])

def test(n, edges, x, y, v):
    q0 = generator(n, edges)
    ix, qt, out = killed(q0, y)
    N = (-qt).inv()
    m = len(ix)
    reward = S.ones(m, 1)
    if v != y: reward[ix.index(v)] += 1
    mean0 = (N*reward)[ix.index(x)]
    second0 = (2*N*S.diag(*reward)*N*reward)[ix.index(x)]
    var0 = S.factor(second0-mean0**2)
    Lv = S.factor((N*S.eye(m)[:,ix.index(v)])[ix.index(x)])
    for w in [S.Rational(1,4), S.Rational(2,3), S.Rational(1), S.Rational(4), S.Rational(11)]:
        qw = generator(n+1, edges+[(v, n, w)])
        mean, var = full_moments(qw, x, y)
        check(S.simplify(mean-mean0)==0, 'mean invariance')
        check(S.simplify(var-var0-2*Lv/w)==0, 'variance reciprocal law')
        for s in [S.Rational(1,3), S.Rational(1), S.Rational(5,2)]:
            theta = S.factor(w*s/(w+s))
            diagonal = S.zeros(m)
            diagonal[ix.index(v),ix.index(v)] = theta
            pred = S.factor(((s*S.eye(m)-qt+diagonal).inv()*out)[ix.index(x)])
            direct = direct_lt(qw, x, y, s)
            check(S.simplify(pred-direct)==0, 'Laplace formula')
    check(Lv>0, 'local time positive')

# Several nontrivial nonconstant-conductance cores and attachments
cases = [
    (2, [(0, 1, 1)], 0, 1, 0),
    (3, [(0, 1, 2), (1, 2, 3)], 0, 2, 1),
    (3, [(0, 1, 2), (1, 2, 3)], 0, 2, 0),
    (3, [(0, 1, 1), (1, 2, 2), (0, 2, 3)], 0, 1, 2),
    (4, [(0, 1, 2), (1, 2, 1), (2, 3, 4), (0, 3, 3), (0, 2, 2)], 0, 3, 1),
    (4, [(0, 1, 2), (1, 2, 1), (2, 3, 4), (0, 3, 3), (0, 2, 2)], 3, 1, 0),
]
for c in cases:
    test(*c)

s, w = S.symbols('s w', positive=True)
q3 = generator(3, [(0, 1, 1), (0, 2, w)])
phi = direct_lt(q3, 0, 1, s)
check(S.factor(phi-(s+w)/(s*s+s*(1+2*w)+w))==0,'two-edge exact transform')
check(S.simplify(S.diff(phi,w) + s*s/(s*s+s*(1+2*w)+w)**2)==0, 'strict Laplace derivative')
check(S.factor(-S.diff(phi,s).subs(s,0)) == 2, 'example mean')
check(S.simplify(S.diff(phi,s,2).subs(s,0)-8-2/w)==0,'example variance')
check(S.simplify(S.limit(phi,w,0,dir='+') - 1/(1+s))==0,'rare trap Laplace limit')
check(S.simplify(S.limit(phi,w,S.oo) - 1/(1+2*s))==0,'fast trap Laplace limit')
# The compound-Poisson/exponential transition kernels have the
# Chapman-Kolmogorov composition law of a mean-preserving Markov family.
t, u, z = S.symbols('t u z', positive=True)
check(S.simplify((s/(1+s*t))/(1+u*s/(1+s*t))-s/(1+s*(t+u)))==0, 'kernel semigroup')
# An attachment behind an already absorbing target is never visited.
q = generator(4, [(0,1,1),(1,2,2),(2,3,3)])
for w0 in [S.Rational(1,5), S.Rational(7)]:
    qbig = generator(5, [(0,1,1),(1,2,2),(2,3,3),(3,4,w0)])
    check(full_moments(q,0,1)==full_moments(qbig,0,1), 'unvisited branch moments')
    check(direct_lt(q,0,1,S.Rational(2,3))==direct_lt(qbig,0,1,S.Rational(2,3)), 'unvisited branch LT')
print(f'VERIFY_OK {CHECKS} exact rational and symbolic assertions')
