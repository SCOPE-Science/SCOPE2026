"""Step 18: Jacobi polynomial + Griesmer/Plotkin bound screens for shortened family.
(a) Split/Jacobi distribution for fixed coordinate (balanced): n0(w)=A_w-t_w,
n1(w)=t_w. Jacobi J(z0,z1,x0,x1) identity vs dual split m0(B),m1(B) from punctured
code cosets. Verify polarized MacWilliams identity exactly (Bonnecaze-Mourrain-Sole):
J_{C^perp}(z0,z1,x0,x1) = (1/|C|) J_C(z0+z1, z0-z1, x0+x1, x0-x1) evaluated as
coefficient identity on the (w,i) table. Check exactly.
(b) Griesmer + Plotkin + Hamming sanity for [71,35,16],[70,34,16],[69,33,16],
[68,32,16],[67,31,16].
"""
from math import comb
from fractions import Fraction
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]

# (a) split table
t = {w: Fraction(w * A[w], 72) for w in range(73)}
n0 = {w: A[w] - t[w] for w in range(73)}
n1 = dict(t)
# dual split: punctured code P=C_p [71,36]: words classified by deleted bit?
# m0(j) = #{punctured words wt j from parent wt j, coord 0} = A_j - t_j
# m1(j) = #{from parent wt j+1, coord 1} = t_{j+1}
m0 = {j: A[j] - t[j] for j in range(72)}
m1 = {j: (t[j + 1] if j + 1 <= 72 else Fraction(0)) for j in range(72)}
# Polarized MW check: for each (j,e) in {0,1}x weights of dual split:
# m_e(j) =? (1/2^36) sum_{w,i} (-1)^{e*i} K_j^{(71)}(w - i*?) ... use direct
# bivariate identity: evaluate J at enough points and compare. Take variables
# (z0,z1,x0,x1) = small integer tuples, compare LHS/RHS exactly.
import itertools
pts = [(2, 1, 3, 1), (1, 1, 1, 0), (3, 2, 1, 1), (1, 0, 2, 1), (2, 0, 1, 3)]
ok = True
for (z0, z1, x0, x1) in pts:
    # J_C = sum_{w,i} n_i(w) z_{i}?? convention: J = sum n0(w) z0 x0^{71-w} x1^w... use
    # J_C(z0,z1,x0,x1) = sum_w n0(w) z0 x0^{71-w} x1^w + n1(w) z1 x0^{71-w} x1^w
    # with w indexed on punctured length (parent wt w -> punctured wt w or w-1).
    # Careful: n1(w) words have punctured weight w-1. So:
    JC = sum(n0[w] * z0 * x0 ** (71 - w) * x1 ** w for w in range(72)) + \
        sum(n1[w] * z1 * x0 ** (72 - w) * x1 ** (w - 1) for w in range(73) if w >= 1 and n1[w])
    # J_{Cperp}: Cperp = C itself (self-dual parent); dual split for punctured dual
    # uses same formula with m0,m1 and length 71:
    JD = sum(m0[j] * z0 * x0 ** (71 - j) * x1 ** j for j in range(72)) + \
        sum(m1[j] * z1 * x0 ** (71 - j) * x1 ** j for j in range(72))
    RHS = JC  # placeholder; real identity: JD(z,x) = (1/|C|) JC(z0+z1,z0-z1,x0+x1,x0-x1)
    JCt = sum(n0[w] * (z0 + z1) * (x0 + x1) ** (71 - w) * (x0 - x1) ** w for w in range(72)) + \
        sum(n1[w] * (z0 - z1) * (x0 + x1) ** (72 - w) * (x0 - x1) ** (w - 1) for w in range(73) if w >= 1 and n1[w])
    RHS = JCt / 2 ** 36
    match = (JD == RHS)
    ok &= match
    print(f"  pt(z={z0},{z1},x={x0},{x1}): JD={JD} RHS={RHS} {'=' if match else 'NEQ'}")
print("Jacobi polarized identity holds:", ok)
assert ok

# (b) bounds
def griesmer(n, k, d):
    return sum((d + (1 << i) - 1) // (1 << i) for i in range(k))

for (n, k, d) in [(71, 35, 16), (70, 34, 16), (69, 33, 16), (68, 32, 16), (67, 31, 16)]:
    g = griesmer(n, k, d)
    print(f"[{n},{k},{d}]: Griesmer need {g} <= {n}: {'pass' if g <= n else 'VIOLATION'}")
    # Plotkin (d even, 2d<n? 32<71 yes -> A<= 2*floor(d/(2d-n))... binary Plotkin:
    # if 2d>n: A(n,d)<=2*floor(d/(2d-n)))
    print(f"  Plotkin n/a (2d={2*d} < n={n}, no bound)")
json.dump({"jacobi_ok": ok}, open(os.path.join(HERE, "s18_jacobi.json"), "w"), indent=1)
print("wrote s18_jacobi.json")
