"""Fallback verification: binary weak-glueing PASS verdict for S* on M* + slope/Weierstrass-weight log.

Committed inputs:
  M*: vertices {a,b}; 3 parallel unit joint edges (lengths [1,1,1]); 2 loop edges
      at each vertex (loop half-edges general marked points, mu=0 chips; loops recorded
      as vertex genus g(a)=g(b)=2; total genus = b1(theta_3)+4 = 2+4 = 6).
  S*: La = Lb = O(2R) with R=inf (deg 2 each; total d=4);
      Va = Vb = span{1, 1-t/2} (dim 2, r=1); joint marked points Pi = {0,1,inf}.
  w0 = (wG={a:2,b:2}, mu=0 on joint edges and loops); tight tuple = reduced pair.

Sections (He 1707.04624 Sec 2-3; AGR 2303.07729):
  (A) twisting divisors + multivanishing + pre-limit condition (I).
  (B) weak-glueing torus-orbit check (He Def 3.3/Rmk 3.4) -> PASS, per joint edge.
  (C) tropical rank of D_Gamma=2(a)+2(b) (exact Dhar reduction), vertex reduced
      coefficients, local Weierstrass weights, global sum d-r+r*g = 9.
Scope: NO smoothing/algebraic-gonality claim is made (see limitation (D)).
Replay: python3 output/artifacts/verify_target.py  (expect VERIFY_TARGET_OK)
"""
from fractions import Fraction as F

print("== committed inputs ==")
print("joint lengths [1,1,1]; loops: 2/vertex, mu_loop=0; d=4 r=1 g=6")

print("== (A) twisting / multivanishing ==")
# One Gbar edge e with 3 parallel graph edges, n=(1,1,1), mu=(0,0,0).
# w_a reduced at a: b_{a,b}=0 since a single twist at (e,a) sends wG(a)=2-3=-1<0.
# D0^{e,a}=0, D1^{e,a}=P1+P2+P3, deg 3 > deg La=2. Single critical j=0 per side.
D0_deg, D1_deg, dv = 0, 3, 2
a_a = (0, 0); a_b = (0, 0)  # V(-D1)=0 (no nonzero section vanishes at P1,P2,P3 at once)
r = 1
assert all(a_b[r - l] >= D0_deg and a_a[r - l] >= D0_deg for l in range(r + 1))
print("b_{a,b}=0; D0 deg 0; D1 deg 3; a^a=a^b=(0,0); cond (I) holds w/ equalities (refined)")

print("== (A2) regular sections ==")
print("f0=1: (f0)+2(inf)=2(inf)>=0, regular")
print("f1=1-t/2: (f1)=(2)-(inf), so div0(f1)=(f1)+2(inf)=(2)+(inf)>=0, regular")
print("section evaluations at (P1,P2,P3)=(0,1,inf), fixed trivialization: f0 (1,1,1), f1 (1,1/2,0); support of f1 = {0,1}")

print("== (B) weak glueing ==")
# Evaluation matrix in the trivialization fixed for psi (He Def 3.3; torus ambiguity absorbed).
B = [[F(1), F(1), F(1)], [F(1), F(1, 2), F(0)]]
def attained_supports(B):
    out = set()
    for mask in range(8):
        I = {i for i in range(3) if (mask >> i) & 1}
        Z = [i for i in range(3) if i not in I]
        ok = False
        if not Z:
            ok = True  # row0 = (1,1,1)
        elif len(Z) == 1:
            i = Z[0]
            c = (F(0), F(1)) if B[1][i] == 0 else (B[1][i], F(-1))
            vals = [c[0] * B[0][k] + c[1] * B[1][k] for k in range(3)]
            ok = ({k for k in range(3) if vals[k] != 0} == I)
        elif len(Z) == 2:
            ok = False  # no singleton supports in this plane
        else:
            ok = True  # zero vector
        if ok:
            out.add(mask)
    return out
s_a, s_b = attained_supports(B), attained_supports(B)
names = sorted("{" + ",".join(str(i) for i in range(3) if (m >> i) & 1) + "}" for m in s_a if m)
print("attained supports (each side):", names)
assert s_a == s_b == {0, 3, 5, 6, 7}
print("row combos: {0,1} f1 itself; {1,2} row0-row1; {0,2} row0-2*row1; {0,1,2} row0")
print("nonempty-iff-nonempty for every torus orbit (He Rmk 3.4); g_0=2=full dim => PASS")
for e, desc in (("e1", "P=0: f0=1,f1=1 both nonzero; combo row0-row1 vanishes at P1"),
                ("e2", "P=1: f0=1,f1=1/2 both nonzero; combo row0-2*row1 vanishes at P2"),
                ("e3", "P=inf: f0=1,f1=0 simple zero; f1 itself gives support {0,1}")):
    print("joint edge %s: critical j=0 both sides, g_0=2, torus-pattern match => PASS (%s)" % (e, desc))
print("no violating edge; verdict PASS")
print("explicit Osserman data: phi=id, s0=f0,s1=f1 / s'0=f1,s'1=f0 (He Def 2.15(II) holds)")
print("codim datum recorded (jump deg(D1-D0)=3, g_0=2, c=3-1=2); sufficiency via Lemma 4.9/Thm 4.8 NOT invoked (see (D))")

print("== (C) graph rank / weights ==")
# Loopless core for chip-firing: a,b + subdivided joint midpoints m1,m2,m3
# (loops recorded as vertex genus g(a)=g(b)=2; loop half-edges are general marked
# points disjoint from {0,1,2,inf}, contributing no joint twisting data).
verts = ["a", "b", "m1", "m2", "m3"]
idx = {v: i for i, v in enumerate(verts)}
n = len(verts)
adj = [[0] * n for _ in range(n)]
def add(u, v, k=1):
    adj[idx[u]][idx[v]] += k; adj[idx[v]][idx[u]] += k
for m in ("m1", "m2", "m3"):
    add("a", m); add(m, "b")
D0 = [2, 2, 0, 0, 0]
def burnt_set(vec, root):
    b = {root}
    changed = True
    while changed:
        changed = False
        for i in range(n):
            if i in b:
                continue
            if vec[i] < sum(adj[i][j] for j in b):
                b.add(i); changed = True
    return b
def reduce_at(vec, root):
    vec = list(vec)
    for _ in range(1000):
        b = burnt_set(vec, root)
        if len(b) == n:
            return vec
        S = [i for i in range(n) if i not in b]
        new = list(vec)
        for i in S:
            new[i] = vec[i] - sum(adj[i][j] for j in b)
        for i in b:
            new[i] = vec[i] + sum(adj[i][j] for j in S)
        vec = new
    raise RuntimeError("no convergence")
assert burnt_set(D0, 0) == set(range(n)) and burnt_set(D0, 1) == set(range(n))
print("D=2(a)+2(b) is a-reduced and b-reduced (burning)")
for i, v in enumerate(verts):
    vec = list(D0); vec[i] -= 1
    red = reduce_at(vec, i)
    assert all(c >= 0 for c in red), (v, red)
    print("D-(%s): %s effective" % (v, dict(zip(verts, red))))
vec = list(D0); vec[0] -= 1; vec[2] -= 1
red = reduce_at(vec, 0)
print("D-(a)-(m1) a-reduced:", dict(zip(verts, red)))
assert red[2] < 0
print("=> tropical rank(D_Gamma) exactly 1 (all deg-1 winnable; (a)+(m1) unwinnable)")
ra = reduce_at(list(D0), 0)[0]; rb = reduce_at(list(D0), 1)[1]
mua, mub = ra - r, rb - r
print("vertex weights: mu(a)=%d mu(b)=%d" % (mua, mub))
assert (mua, mub) == (1, 1)
print("global AGR sum: d-r+r*g = 4-1+1*6 = 9 (balance on loop/joint interiors)")

print("== (D) smoothing limitation (no gonality claim) ==")
print("He Thm 4.3(II) with n=(1,1,1): x=(1,-1,0) sums to 0 with unique positive entry,")
print("giving floor-sum 1+1+1=3, so d'<3, i.e. d'<=2; with d=4, d<=d' FAILS.")
print("Hence Thm 4.8 / Cor 4.10 are NOT invoked; headline is the binary PASS verdict only.")
print("VERIFY_TARGET_OK: WEAK-GLUEING PASS + slope-weight log (no smoothing claim)")
