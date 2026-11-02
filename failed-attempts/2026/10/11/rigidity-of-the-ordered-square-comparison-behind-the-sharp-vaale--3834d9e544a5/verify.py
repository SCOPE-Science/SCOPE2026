import sympy as sp
from fractions import Fraction

# Check the source inverse/Jacobian algebra symbolically.
q, w1, w2 = sp.symbols("q w1 w2", positive=True)
z1sq = (w1**2 + (q-1)*w2**2)/q
normalized_jac_sq = sp.simplify(w1**2 / (q*z1sq))
assert sp.simplify(normalized_jac_sq - w1**2/(w1**2+(q-1)*w2**2)) == 0

# Symbolically verify the prefix summation-by-parts identity in a
# representative symbolic dimension. RESULT.md proves the arbitrary-n identity.
n = 8
qs = sp.symbols("q1:"+str(n+1))
zs = sp.symbols("z1:"+str(n+1))
r = []
s = 0
for x in qs:
    s += x
    r.append(s)
delta = [r[k]-(k+1) for k in range(n)]
lhs = sum((qs[j]-1)*zs[j]**2 for j in range(n))
rhs = sum(delta[k]*(zs[k]**2-(zs[k+1]**2 if k+1<n else 0)) for k in range(n))
assert sp.expand(lhs-rhs) == 0

# Verify the transformed prefix sums after the ordered-square substitution.
tilde = [sp.Integer(1), qs[0]+qs[1]-1] + list(qs[2:])
assert sp.simplify(tilde[0]-1) == 0
for k in range(1,n):
    assert sp.simplify(sum(tilde[:k+1]) - r[k]) == 0

# Exact rational stress tests under prefix constraints with q1=1.
tests = [
    ([Fraction(1), Fraction(3,2), Fraction(1,2)], [Fraction(5), Fraction(3), Fraction(1)]),
    ([Fraction(1), Fraction(1), Fraction(5,4), Fraction(3,4)], [Fraction(7), Fraction(5), Fraction(2), Fraction(1)]),
    ([Fraction(1), Fraction(2), Fraction(1), Fraction(1)], [Fraction(9), Fraction(6), Fraction(3), Fraction(1)]),
]
for qv, zv in tests:
    rv=[]
    s=Fraction(0)
    for x in qv:
        s += x
        rv.append(s)
    assert all(rv[k] >= k+1 for k in range(len(qv)))
    excess = sum((qv[j]-1)*zv[j]**2 for j in range(len(qv)))
    defect = sum((rv[k]-(k+1))*(zv[k]**2-(zv[k+1]**2 if k+1<len(zv) else 0)) for k in range(len(qv)))
    assert excess == defect
    assert excess > 0

# Equality of all prefix sums forces all q_j = 1.
for m in range(2, 10):
    rv = [Fraction(k) for k in range(1, m+1)]
    recovered = [rv[0]] + [rv[k]-rv[k-1] for k in range(1,m)]
    assert all(x == 1 for x in recovered)

print("VERIFY_OK")
