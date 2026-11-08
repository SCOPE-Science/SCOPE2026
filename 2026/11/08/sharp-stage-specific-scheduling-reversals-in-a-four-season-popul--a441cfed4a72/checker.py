"""Exact checks for two-environment, four-phase, two-stage Leslie projection result.

Requires SymPy. No simulation is used for the algebraic identities.
"""
from itertools import product
from fractions import Fraction as F
from collections import defaultdict
import sympy as sp


def L(f, g, s):
    return sp.Matrix([[f, g], [s, 0]])


def cyclic(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


a, u, v, d, w, z = sp.symbols("a u v d w z", positive=True)
A, B = L(a, u, v), L(d, w, z)
cluster, alternating = A*A*B*B, A*B*A*B
D = sp.factor(sp.trace(cluster) - sp.trace(alternating))
expected = a*a*w*z-a*d*u*z-a*d*v*w+d*d*u*v-u*u*z*z+2*u*v*w*z-v*v*w*w
assert sp.expand(D-expected) == 0
assert sp.factor(D-(A*B-B*A).det()) == 0
assert sp.factor(cluster.det()-alternating.det()) == 0
assert sp.factor(D.subs({w:u,z:v})-u*v*(a-d)**2) == 0
assert sp.factor(D.subs({d:a,z:v})+v*v*(u-w)**2) == 0
assert sp.factor(D.subs({d:a,w:u})+u*u*(v-z)**2) == 0

for n in range(1, 5):
    for count_a in range(n+1):
        classes = {cyclic(t) for t in product("AB", repeat=n) if t.count("A") == count_a}
        if n <= 3:
            assert len(classes) == 1, (n, count_a, classes)
        if n == 4 and count_a == 2:
            assert len(classes) == 2 and classes == {tuple("AABB"), tuple("ABAB")}

examples = [
    ("fecundity", L(F(8,5),F(4,5),F(2,5)), L(F(4,25),F(4,5),F(2,5)),
        F(-98079,390625),F(161121,390625)),
    ("maturation", L(F(33,50),F(11,10),F(11,20)), L(F(33,50),F(11,10),F(11,100)),
        F(1468416481,40000000000), F(-7901823519,40000000000)),
]
for label, X,Y,expect_cluster,expect_alt in examples:
    assert 0 < X[1,0] <= 1 and 0 < Y[1,0] <= 1
    U,V = X*X*Y*Y, X*Y*X*Y
    assert U.det() == V.det() and U.det() < 1
    assert (sp.eye(2)-U).det() == expect_cluster
    assert (sp.eye(2)-V).det() == expect_alt
    assert U.trace()>0 and V.trace()>0
    print(label, "traces", U.trace(), V.trace(), "determinant", U.det(),
          "det(I-M)",expect_cluster,expect_alt)
print("PASS: symbolic identity, universal signs, minimal word classes, two exact persistence reversals")
