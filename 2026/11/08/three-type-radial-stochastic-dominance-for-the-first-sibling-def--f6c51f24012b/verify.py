"""Exact verification of the three-type first-sibling tail inequalities.

Run with Python 3 and SymPy (tested with SymPy 1.13). The symbolic
certificate is finite; it proves a polynomial identity and the
nonnegativity of every integer coefficient, not merely a grid test.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import sympy as sp

p, q, r = sp.symbols('p q r', positive=True)
x, y, z = sp.symbols('x y z', nonnegative=True)
S = p + q + r
pair = [(p, q), (p, r), (q, r)]
H = 2 * sum(a * b / (a + b)**2 for a, b in pair) \
    - 2 * (p*q + p*r + q*r) / S**2 - 6*p*q*r/S**3
K = 6*p*q*r / S**3
assert sp.factor(H.subs({p:1,q:1,r:1})-sp.Rational(11,18)) == 0
assert sp.factor(K.subs({p:1,q:1,r:1})-sp.Rational(2,9)) == 0

# The radial derivative is -R/theta, where R = -(p_i-S/3) grad_i H.
R = sp.factor(-sum((v-S/3)*sp.diff(H,v) for v in (p,q,r)))
num, den = sp.fraction(R)
expected_den = 3*S**3 * sp.prod((a+b)**3 for a,b in pair)
assert sp.expand(den-expected_den) == 0
Q = sp.Poly(sp.expand(num.subs({p:x+y+z,q:y+z,r:z})),x,y,z)
assert Q.is_homogeneous
assert Q.total_degree() == 12
assert len(Q.terms()) == 79
assert all(coef > 0 for mon,coef in Q.terms())
# The z^10 term is strictly positive as soon as x+y>0 and z>0.
assert sp.expand(Q.as_expr().coeff(z,10) - 8448*(x*x+x*y+y*y)) == 0
assert sp.Poly(Q.as_expr().subs({x:0,y:0}),z).is_zero

# Check the distinct Poissonized formulas against an independent exact
# state-space recursion for the original iid coupon draws.
def distribution(probs):
    n = 3
    @lru_cache(None)
    def rec(state):
        if 0 not in state:
            output=[F(0) for _ in range(n)]
            output[state.count(1)-1] = F(1)
            return tuple(output)
        denominator = sum(probs[i] for i in range(n) if state[i]<2)
        output=[F(0) for _ in range(n)]
        for i in range(n):
            if state[i] == 2:
                continue
            nxt = list(state); nxt[i] += 1
            child = rec(tuple(nxt))
            for k in range(n):
                output[k] += probs[i]/denominator * child[k]
        return tuple(output)
    return rec((0,0,0))

cases = 0
for a,b,c in product(range(1,7),repeat=3):
    t=a+b+c
    prob=(F(a,t),F(b,t),F(c,t))
    distribution_exact=distribution(prob)
    h=sum(distribution_exact[1:])
    k=distribution_exact[2]
    H_exact=(2*sum(prob[i]*prob[j]/(prob[i]+prob[j])**2
                   for i,j in ((0,1),(0,2),(1,2)))
             -2*sum(prob[i]*prob[j] for i,j in ((0,1),(0,2),(1,2)))
             -6*prob[0]*prob[1]*prob[2])
    K_exact=6*prob[0]*prob[1]*prob[2]
    assert h==H_exact and k==K_exact
    assert sum(distribution_exact)==1
    cases+=1

# Verify strict ordered tails along a small exact-rational ray sample.
for target in ((F(1,2),F(1,3),F(1,6)),(F(3,5),F(1,5),F(1,5)),(F(7,10),F(1,5),F(1,10))):
    last=None
    for theta in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
        current=tuple(F(1,3)+theta*(v-F(1,3)) for v in target)
        d=distribution(current)
        tails=(sum(d[1:]),d[2])
        if last is not None:
            assert tails[0]<last[0] and tails[1]<last[1]
        last=tails
print('PASS: 79 positive exact certificate coefficients; 216 rational state recurrences; 12 strict ray comparisons')
