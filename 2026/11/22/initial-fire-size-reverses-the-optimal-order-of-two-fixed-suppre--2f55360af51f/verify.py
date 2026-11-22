"""Independent symbolic and numerical diagnostics for a two-level suppression-order theorem.

Run: python verify.py
Requires sympy, numpy, scipy. The analytical proof is in RESULT.md;
finite randomized tests are not an exhaustive mathematical proof.
"""
import numpy as np
import sympy as sp
from scipy.linalg import expm

birth, lowdeath, highdeath, high, low = sp.symbols(
    'birth lowdeath highdeath high low', positive=True, finite=True
)

def symbolic_generator(s):
    return sp.Matrix([[-(birth + lowdeath + s), birth],
                      [highdeath + s, -(highdeath + s)]])

strong = symbolic_generator(high)
weak = symbolic_generator(low)
comm = sp.simplify(strong * weak - weak * strong)
expected = (high - low) * sp.Matrix([
    [-birth, 0], [highdeath - birth - lowdeath, birth]
])
assert (comm-expected).applyfunc(sp.simplify) == sp.zeros(2)
assert sp.simplify((comm * sp.ones(2, 1))[0] - (low-high)*birth) == 0
assert sp.simplify((comm * sp.ones(2, 1))[1] - (high-low)*(highdeath-lowdeath)) == 0

# Distinct real eigenvalues guarantee b_s(t)>0 for every t>0.
rate = sp.symbols('rate', nonnegative=True)
M = symbolic_generator(rate)
disc = sp.factor((sp.trace(M))**2 - 4*M.det())
assert sp.simplify(disc - ((birth + lowdeath - highdeath)**2 +
                           4*birth*(highdeath+rate))) == 0
assert sp.factor(M.det() - (lowdeath+rate)*(highdeath+rate)) == 0

rng = np.random.default_rng(20230721)
checks = 5
for _ in range(1800):
    b, m, d = rng.uniform(.04, 6, 3)
    x, y = np.sort(rng.uniform(0, 8, 2))[::-1]
    u, v = rng.uniform(.005, 3, 2)
    p = rng.uniform(0, 1)
    def Q(gamma):
        return np.array([[-(b+m+gamma), b], [d+gamma, -(d+gamma)]], dtype=float)
    H, L = Q(x), Q(y)
    diff_matrix = expm(u*H) @ expm(v*L) - expm(v*L) @ expm(u*H)
    eigH = np.linalg.eigvals(H)
    eigL = np.linalg.eigvals(L)
    bh = np.exp(max(eigH)*u)*(-np.expm1(-(max(eigH)-min(eigH))*u)) / (max(eigH)-min(eigH))
    bl = np.exp(max(eigL)*v)*(-np.expm1(-(max(eigL)-min(eigL))*v)) / (max(eigL)-min(eigL))
    assert bh>0 and bl>0
    predicted = bh*bl*(x-y)*np.array([[-b, 0], [d-b-m, b]])
    assert np.allclose(diff_matrix, predicted, rtol=1e-7, atol=3e-13), (diff_matrix,predicted)
    mixture = np.array([p,1-p])
    signed = mixture @ diff_matrix @ np.ones(2)
    target = bh*bl*(x-y)*((1-p)*(d-m)-p*b)
    assert np.isclose(signed, target, rtol=1e-7, atol=4e-13)
    if abs(target)>1e-11:
        assert np.sign(signed)==np.sign(target)
    checks+=4

# Concrete witness: one burning unit favors early strong suppression;
# two burning units favor late strong suppression.
b,m,d,x,y,u,v = 1.,1.,2.,3.,0.,1.,1.
Q = lambda g: np.array([[-(b+m+g),b], [d+g,-(d+g)]],float)
E = (expm(Q(x)*u)@expm(Q(y)*v)-expm(Q(y)*v)@expm(Q(x)*u))@np.ones(2)
assert E[0]<-0.007 and E[1]>0.007
assert abs(E[0]+E[1])<1e-13
print(f'PASSED {checks+3} checks; exemplar survival differences [{E[0]:.12f}, {E[1]:.12f}].')
