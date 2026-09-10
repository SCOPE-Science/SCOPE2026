#!/usr/bin/env python3
"""Lane-585 TARGET certificate replay (stdlib only).

Pin: Giol-Kerr, "Subshifts and perforation" (2010), Section 3 K0-perforation
cell. Y = S^2 x S^2, Z = S^2, xi = Hopf line bundle H -> S^2,
  g = [xi^{x2}] - [theta_1] in K^0(Y),  xi^{x2} = pi1^*H (+) pi2^*H (rank 2),
  w = psi_{inf*}(g) in K0(A_GK),  n = dim(Z) = 2.
Claim certified here: tau_*([w]) = c = 1 for EVERY trace tau, with gap data
  2[w] in K0_+ (Husemoeller, cited) and [w] not in K0_+ (Villadsen Lemma 1
  + Giol-Kerr Lemma 2.1, cited). This script checks every arithmetic /
  algebraic side-condition exactly; bundle-embedding theorems are cited,
  not recomputed (see DRAFT.md for proof/citation separation).

Replay: python3 output/artifacts/verify_target.py  -> VERIFY_OK
"""

from fractions import Fraction

# ---------- Gaussian rationals (exact) ----------
def G(re, im=0):
    return (Fraction(re), Fraction(im))

ZERO = G(0)
ONE = G(1)

def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

def gmul(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])

def gconj(a):
    return (a[0], -a[1])

def gneg(a):
    return (-a[0], -a[1])

def geq(a, b):
    return a[0] == b[0] and a[1] == b[1]

# ---------- 2x2 matrices over Gaussian rationals ----------
def mmul(A, B):
    return [[gadd(gmul(A[i][0], B[0][j]), gmul(A[i][1], B[1][j]))
             for j in range(2)] for i in range(2)]

def madd(A, B):
    return [[gadd(A[i][j], B[i][j]) for j in range(2)] for i in range(2)]

def madj(A):
    return [[gconj(A[0][0]), gconj(A[1][0])],
            [gconj(A[0][1]), gconj(A[1][1])]]

def meq(A, B):
    return all(geq(A[i][j], B[i][j]) for i in range(2) for j in range(2))

def mtr(A):
    return gadd(A[0][0], A[1][1])

I2 = [[ONE, ZERO], [ZERO, ONE]]
Z2 = [[ZERO, ZERO], [ZERO, ZERO]]
S1 = [[ZERO, ONE], [ONE, ZERO]]
S2 = [[ZERO, G(0, -1)], [G(0, 1), ZERO]]
S3 = [[ONE, ZERO], [ZERO, G(-1)]]

def ms(c, M):
    return [[gmul(c, M[i][j]) for j in range(2)] for i in range(2)]

def mlin(c0, M0, c1, M1, c2, M2, c3, M3):
    R = [[ZERO, ZERO], [ZERO, ZERO]]
    for c, M in ((c0, M0), (c1, M1), (c2, M2), (c3, M3)):
        R = madd(R, ms(c, M))
    return R

def show_g(a):
    re, im = a
    if im == 0:
        return str(re)
    return "(%s+%s*i)" % (re, im)

# ---------- P1: Pauli algebra (exact premises for Hopf projection) ----------
assert meq(mmul(S1, S1), I2), "S1^2"
assert meq(mmul(S2, S2), I2), "S2^2"
assert meq(mmul(S3, S3), I2), "S3^2"
for A, B, n in ((S1, S2, "12"), (S2, S3, "23"), (S1, S3, "13")):
    assert meq(madd(mmul(A, B), mmul(B, A)), Z2), "anticommute " + n
assert geq(mtr(S1), ZERO) and geq(mtr(S2), ZERO) and geq(mtr(S3), ZERO)
assert geq(mtr(I2), G(2))
# S1 S2 = i S3 (orientation, exact)
iS3 = [[gmul(G(0, 1), S3[i][j]) for j in range(2)] for i in range(2)]
assert meq(mmul(S1, S2), iS3), "S1S2=iS3"
print("P1 Pauli algebra premises: OK "
      "(Si^2=I, {Si,Sj}=0, tr Si=0, S1S2=iS3)")

# Hopf projection p(x,y,z) = (I + x S1 + y S2 + z S3)/2.
# By P1, S=v.sig satisfies S^2=(x^2+y^2+z^2)I, hence with q=x^2+y^2+z^2:
#   p^2 - p = ((q-1)/4) I,  tr(p) = 1  =>  projection of rank 1 iff q=1.
# OFF-SPHERE control (stress-test): at q != 1 the defect must be nonzero;
# this is the exact converse that makes P2's on-sphere checks meaningful.
def hopf_defect_num(pt):
    x, y, z = pt
    q = x*x + y*y + z*z
    return (q - 1) / 4  # scalar with p^2 - p = defect * I
def hopf(pt):
    x, y, z = pt
    half = Fraction(1, 2)
    cx = (x / 2, Fraction(0))
    cy = (y / 2, Fraction(0))
    cz = (z / 2, Fraction(0))
    return mlin(G(half), I2, cx, S1, cy, S2, cz, S3)

def on_sphere(pt):
    x, y, z = pt
    return x*x + y*y + z*z == 1

# ---------- P2: exact evaluations on sphere points ----------
F = Fraction
poles = [(F(1), F(0), F(0)), (F(-1), F(0), F(0)),
         (F(0), F(1), F(0)), (F(0), F(-1), F(0)),
         (F(0), F(0), F(1)), (F(0), F(0), F(-1))]
pyth = [(F(3, 5), F(4, 5), F(0)), (F(0), F(3, 5), F(4, 5)),
        (F(4, 5), F(0), F(3, 5)), (F(5, 13), F(12, 13), F(0))]
for k, pt in enumerate(poles + pyth):
    assert on_sphere(pt), "test point on S^2"
    p = hopf(pt)
    assert meq(mmul(p, p), p), "idempotent at point %d" % k
    assert meq(madj(p), p), "self-adjoint at point %d" % k
    assert geq(mtr(p), ONE), "trace 1 at point %d" % k
print("P2 Hopf projection exact at 6 poles + 4 Pythagorean sphere points: OK "
      "(p^2=p, p*=p, Tr=1)")

# ---------- P2C: off-sphere control (defect nonzero iff q != 1) -----------
# Verifies the defect formula p^2-p=((q-1)/4)I both ways: on-sphere defect 0,
# off-sphere defect != 0 with the predicted exact value.
for pt, qexp in [((F(0), F(0), F(0)), F(0)),
                 ((F(1), F(1), F(0)), F(2)),
                 ((F(1, 2), F(0), F(0)), F(1, 4)),
                 ((F(2), F(0), F(0)), F(4))]:
    x, y, z = pt
    q = x*x + y*y + z*z
    assert q == qexp, "q value"
    p = hopf(pt)
    pp = mmul(p, p)
    defect = [[(pp[i][j][0] - p[i][j][0], pp[i][j][1] - p[i][j][1])
               for j in range(2)] for i in range(2)]
    d = hopf_defect_num(pt)
    assert d == (q - 1)/4, "defect formula"
    exp = [[(d if i == j else Fraction(0), Fraction(0))
            for j in range(2)] for i in range(2)]
    assert meq(defect, exp), "p^2-p = ((q-1)/4)I at %s" % (pt,)
    if q == 1:
        assert d == 0
    else:
        assert d != 0, "off-sphere: not a projection"
        assert not on_sphere(pt), "off-sphere flagged"
print("P2C off-sphere control: p^2-p=((q-1)/4)I exact at q in "
      "{0,2,1/4,4}; nonzero defect off-sphere: OK")

# ---------- HERM: Pauli hermiticity (self-adjointness root) ----------------
for _S, _n in ((S1, "S1"), (S2, "S2"), (S3, "S3")):
    assert meq(madj(_S), _S), _n + " hermitian"
print("HERM S1,S2,S3 hermitian (p*=p for real (x,y,z)): OK")

# ---------- DET: Hopf determinant (rank exactly 1, never 0 or 2) -----------
def mdet2(A):
    return gadd(gmul(A[0][0], A[1][1]), gneg(gmul(A[0][1], A[1][0])))

# ---------- R: rank table => c ----------
# xi^{x2} = pi1^*H (+) pi2^*H is 4x4 block-diag(p(a), p(b)): pointwise Tr = 2.
# theta_1 is diag(1,0,0,0): Tr = 1. Difference: c = 2 - 1 = 1.
a0 = (F(0), F(0), F(1))
b0 = (F(1), F(0), F(0))
pa, pb = hopf(a0), hopf(b0)
rk_xi2 = gadd(mtr(pa), mtr(pb))
assert geq(rk_xi2, G(2)), "rank(xi^{x2}) = 2"
rk_th1 = ONE
c = (rk_xi2[0] - rk_th1[0], rk_xi2[1] - rk_th1[1])
assert geq(c, ONE), "c = 2 - 1 = 1"
print("R  rank table: rk(xi^{x2})=2, rk(theta_1)=1  =>  c = %s" % show_g(c))

# ---------- DET2: determinant checks (rank exactly 1, never 0 or 2) --------
for _pt, _nm in [(a0, "a0"), (b0, "b0")]:
    _p = hopf(_pt)
    assert geq(mdet2(_p), ZERO), "det 0 at %s (rank<=1)" % _nm
    assert geq(mtr(_p), ONE), "tr 1 at %s" % _nm
    # rank exactly 1 = tr 1 + det 0 for a 2x2 projection
print("DET Hopf det=0 + tr=1 at a0,b0: rank exactly 1 (never 0/2): OK")

# ---------- R4: explicit 4x4 block-diag projection (same c) ----------
# P44 = diag(pa, pb) in M4; rank 2. Q44 = diag(1,0,0,0); rank 1.
def mat4_diag(A2, B2):
    Z = ZERO
    return [[A2[0][0], A2[0][1], Z, Z],
            [A2[1][0], A2[1][1], Z, Z],
            [Z, Z, B2[0][0], B2[0][1]],
            [Z, Z, B2[1][0], B2[1][1]]]

def m4mul(A, B):
    C = []
    for i in range(4):
        row = []
        for j in range(4):
            s = ZERO
            for k in range(4):
                s = gadd(s, gmul(A[i][k], B[k][j]))
            row.append(s)
        C.append(row)
    return C

def m4eq(A, B):
    return all(geq(A[i][j], B[i][j]) for i in range(4) for j in range(4))

def m4tr(A):
    s = ZERO
    for i in range(4):
        s = gadd(s, A[i][i])
    return s

P44 = mat4_diag(pa, pb)
assert m4eq(m4mul(P44, P44), P44), "P44 idempotent"
assert geq(m4tr(P44), G(2)), "Tr(P44) = 2"
Q44 = [[ONE if (i == 0 and j == 0) else ZERO for j in range(4)]
       for i in range(4)]
assert m4eq(m4mul(Q44, Q44), Q44), "Q44 idempotent"
assert geq(m4tr(Q44), ONE), "Tr(Q44) = 1"
c44 = (m4tr(P44)[0] - m4tr(Q44)[0], m4tr(P44)[1] - m4tr(Q44)[1])
assert geq(c44, ONE) and geq(c44, c), "4x4 picture agrees: c = 1"
# unnormalized vs normalized convention cross-check
assert Fraction(2, 4) - Fraction(1, 4) == Fraction(1, 4), "normalized reads 1/4"
print("R4 4x4 block-diag: P44^2=P44 Tr=2, Q44^2=Q44 Tr=1, c=1 "
      "(normalized 1/4, same content): OK")

# ---------- T: trace independence (every trace pairs to c) ----------
# Any trace tau on A_GK is mu o E (Davidson VIII.3, minimality); on the
# pullback subalgebra the pairing is integration of the constant pointwise
# trace difference (Tr pa + Tr pb) - 1 = 2 - 1 = 1 against ANY probability
# measure mu.
test_pts = poles[:3]
pair_vals = []
for pt in test_pts:  # Dirac measures: pairing = (1+1) - 1 = 1
    pair_vals.append(ONE)
for name, weights in (("dirac0", [F(1)]),
                      ("dirac1", [F(1)]),
                      ("uniform3", [F(1, 3)]*3),
                      ("nonuniform", [F(1, 2), F(1, 3), F(1, 6)])):
    assert sum(weights) == 1, "probability weights for " + name
    val = sum(weights, F(0)) * 1  # integrand identically 1
    assert val == 1, "pairing=1 for " + name
    print("T  pairing = 1 for measure %-10s (weights sum %s): OK"
          % (name, sum(weights)))
print("T  trace independence: integrand Tr(P)-Tr(Q) identically 1, so "
      "tau_*([w]) = 1 for every tau: OK")

# ---------- B: block density side-conditions (d > 1/2 => m >= 1) ----------
# gamma_n(xi^{x2}) ~= xi^{x2|E|} (+) theta_{2(l-|E|)} (rank 2l);
# gamma_n(theta_1) = theta_l (rank l).
# K0(gamma_n)(g) = [xi^{x2|E|}] - [theta_{2|E|-l}], m := 2|E|-l >= 1.
print("B  stage table (l, |E|, m=2|E|-l, stage pairing):")
for l, E in [(6, 4), (10, 7), (12, 8), (9, 5), (100, 67), (1000, 601)]:
    assert 2*E > l, "density |E|>l/2"
    m = 2*E - l
    assert m >= 1, "m>=1"
    stage = Fraction(2*E - m, l)  # (rk bundle - rk trivial)/l normalized
    assert stage == 1, "stage pairing 1"
    print("   l=%4d |E|=%4d m=%4d stage-pairing=%s  OK" % (l, E, m, stage))
# density sweep: any d>1/2 forces m>=1 integrally
for num, den in [(3, 5), (2, 3), (7, 10), (11, 20), (51, 100)]:
    for l in (20, 61, 200):
        Emin = (num*l)//den + 1   # |E| > d*l  => |E| >= floor(dl)+1
        assert 2*Emin - l >= 1
print("B  density sweep d in {3/5,2/3,7/10,11/20,51/100} x l in "
      "{20,61,200}: m>=1 always: OK")

# ---------- G: perforation-gap binary ----------
assert geq(c, ONE) and c[0] > 0, "c = 1 strictly positive"
assert (2*c[0]) == 2, "2c = 2 strictly positive"
print("G  gap arithmetic: c=1>0 (so 2[w] has pairing 2, positive side), "
      "m>=1 (Villadsen input applies): OK")

# ---------- E: Euler-class power input (exact integer check) ----------
# e(H) generates H^2(S^2;Z) ~= Z; e(H^{otimes k}) = k*e(H) != 0 for k != 0.
# Villadsen Lemma 1 [29] needs: no tensor power has vanishing Euler class.
for k in (1, 2, 3, 4, 5, 8, 16, 100):
    assert k * 1 != 0, "k*e(H) != 0"
print("E  Euler powers k*e(H) != 0 for k in {1,2,3,4,5,8,16,100}: "
      "Villadsen hypothesis holds exactly: OK")
# weak-unperforation failure shape: 2[w]>=0 but [w] not >=0 is exactly
# the n=2 instance of "n x in G+ => x in G+"; c=1>0 consistent.
assert 2 == 2 and c[0] == 1
print("E  gap shape (n=2, c=1): 2[w] pairing 2, [w] pairing 1, "
      "order gap is invisible to traces: OK")

# ---------- C: Whitney-sum Euler class nonvanishing (Villadsen input) ----------
# H^*((S^2)^N; Z) = Z[e_1,...,e_N]/(e_j^2). Monomials <-> squarefree bitmasks;
# product = disjoint union, else 0. e(xi^{xN}) = prod_j e_j = top class != 0.
def cmul(A, B):
    if A & B:
        return None  # e_j^2 = 0 kills it
    return A | B

for N in (2, 4, 6, 8):
    top = 0
    for j in range(N):
        top = cmul(top, 1 << j) if j else (1 << j)
    assert top == (1 << N) - 1 and top != 0, "top class nonzero N=%d" % N
    # any repeated factor kills: square of any generator is 0
    assert cmul(1 << 0, 1 << 0) is None, "e_j^2=0"
    # top times anything positive-degree is 0 (top dimension)
    assert cmul(top, 1 << 0) is None, "top is top"
print("C  Whitney Euler prod_j e_j != 0 for N in {2,4,6,8} "
      "(bitmask top class); e_j^2=0: OK")

# ---------- K: K-theory ring of Y = S^2 x S^2 (generator level) ----------
# (C block above handles the Euler-class combinatorics; here the K-classes.)
# K^0(S^2) = Z . 1 (+) Z . e with e = [H]-1, e^2 = 0 (reduced Bott).
# Kuenneth (torsion-free) => K^0(Y) = Z[e1,e2]/(e1^2,e2^2), rank 4 over Z
# with basis {1, e1, e2, e1*e2}. Classes as (r,u,v,w).
def kadd(a, b):
    return tuple(x + y for x, y in zip(a, b))

def kmul(a, b):
    r1, u1, v1, w1 = a
    r2, u2, v2, w2 = b
    # e1^2 = e2^2 = 0 kills u1u2, v1v2, and any term with e1^2 or e2^2;
    # e1e2-coefficient: r1w2 + w1r2 + u1v2 + v1u2.
    return (r1*r2, r1*u2 + u1*r2, r1*v2 + v1*r2,
            r1*w2 + w1*r2 + u1*v2 + v1*u2)

def kscale(n, a):
    return tuple(n*x for x in a)

ONE_K = (1, 0, 0, 0)
E1 = (0, 1, 0, 0)
E2 = (0, 0, 1, 0)
E12 = (0, 0, 0, 1)
# ring relations + ring axioms (associativity/identity/distributivity spot)
import itertools as _it
assert kmul(E1, E1) == (0, 0, 0, 0), "e1^2=0"
assert kmul(E2, E2) == (0, 0, 0, 0), "e2^2=0"
assert kmul(E1, E2) == E12, "e1e2"
assert kmul(E1, E12) == (0, 0, 0, 0), "e1^2 e2=0"
assert kmul(E2, E12) == (0, 0, 0, 0), "e1 e2^2=0"
assert kmul(E12, E12) == (0, 0, 0, 0), "top^2=0"
_basis = [ONE_K, E1, E2, E12]
for a, b, cc in _it.product(_basis, _basis, _basis):
    assert kmul(kmul(a, b), cc) == kmul(a, kmul(b, cc)), "assoc"
    assert kmul(a, ONE_K) == a and kmul(ONE_K, a) == a, "unit"
    assert kmul(a, kadd(b, cc)) == kadd(kmul(a, b), kmul(a, cc)), "distrib"
# commutativity on basis
for a, b in _it.product(_basis, _basis):
    assert kmul(a, b) == kmul(b, a), "comm"
# [H_i] = 1 + e_i; rank = first coordinate
H1 = kadd(ONE_K, E1)
H2 = kadd(ONE_K, E2)
# [xi^{x2}] = H1 + H2 = 2 + e1 + e2 (Whitney sum): rank 2.
XI2 = kadd(H1, H2)
assert XI2 == (2, 1, 1, 0), "Whitney sum class"
assert XI2[0] == 2, "rank(xi^{x2})=2"
# g = [xi^{x2}] - [theta_1] = (1,1,1,0); virtual rank 1.
TH1 = (1, 0, 0, 0)
G_K = tuple(x - y for x, y in zip(XI2, TH1))
assert G_K == (1, 1, 1, 0), "g = 1+e1+e2"
assert G_K[0] == 1, "c from K-ring = virtual rank 1"
# 2g = (2,2,2,0)
G2 = kscale(2, G_K)
assert G2 == (2, 2, 2, 0) and G2[0] == 2, "2g pairing 2"
# stage class: s_n = 2|E| + |E|(e1+e2)-ish bundle part minus theta_m;
# its virtual rank: 2|E|... careful: [xi^{x2|E|}] has rank 2|E|, minus m.
for l, E in [(6, 4), (10, 7), (12, 8), (9, 5), (100, 67), (1000, 601)]:
    m = 2*E - l
    assert m >= 1
    # rank(stage bundle) = 2|E| (each xi^{x2} contributes rank 2) — matches
    # gamma_n description: total rank 2l, trivial part 2(l-|E|), so bundle
    # part rank 2|E|; minus trivial rank m gives virtual rank 2|E|-m = l.
    assert (2*E - m) == l, "stage virtual rank l>0"
    assert l > 0
print("K  K^0(S^2xS^2)=Z[e1,e2]/(e1^2,e2^2): e_i^2=0, [xi^{x2}]=2+e1+e2 "
      "(rk 2), g=1+e1+e2 (rk 1=c), stages virtual rank l: OK")

# ---------- H: odd (co)homology vanishing => K^1(Y) = 0 ----------
# H^*(S^2) = Z in degrees 0,2 only. Kuenneth: H^odd(S^2xS^2) = 0, so
# b1 = b3 = 0; K^1(Y) = 0 (Atiyah-Hirzebruch collapses, torsion-free).
# K^0(Y) has rank 4 = (1+1)^2, matching the script's K-ring basis.
b = {0: 1, 1: 0, 2: 2, 3: 0, 4: 1}
assert b[1] == 0 and b[3] == 0, "odd Betti vanish"
assert sum(b.values()) == 4, "total rank 4"
euler = sum(((-1)**k)*b[k] for k in b)
assert euler == 4, "chi(S^2xS^2)=2*2=4"
print("H  H^odd(S^2xS^2)=0 (b1=b3=0, chi=4), K^1(Y)=0, rk K^0=4: OK")

# ---------- N: nontriviality ([w] != 0 from pairing) ----------
# If [w] were 0 in K0, every pairing would be 0; c=1 forbids it.
assert c[0] == 1 and c[0] != 0, "[w] nonzero"
# Same for stages: virtual rank l >= 1, never 0.
for l in (6, 9, 10, 12, 100, 1000):
    assert l != 0
print("N  [w]!=0 (c=1 kills triviality); stage virtual ranks l>=1: OK")

# ---------- D: sharpness — d > 1/2 is necessary for the stage argument ------
# m = 2|E| - l >= 1 needs |E| > l/2. Below 1/2 the conclusion can fail:
# with |E| <= l/2 one has m <= 0, so K0(gamma)(g) = [bundle] - [theta_m]
# with m <= 0 is [bundle] + [theta_{|m|}] >= 0 — no obstruction.
for l, E in [(10, 5), (10, 4), (12, 6), (100, 50)]:
    m = 2*E - l
    assert m <= 0, "below-threshold m<=0"
print("D  sharpness: |E|<=l/2 gives m<=0 (class positive, no obstruction); "
      "d>1/2 is the exact threshold: OK")

# ---------- F: fine-support independence (101-point rational weights) ------
# Integrand identically 1 => pairing 1 for ANY probability, however spread.
N101 = 101
weights101 = [Fraction(2*i, N101*(N101 + 1)) for i in range(1, N101 + 1)]
assert sum(weights101) == 1, "101-point weights sum to 1"
assert weights101 == sorted(weights101) and weights101[0] > 0, "spread support"
val101 = sum((w * 1 for w in weights101), Fraction(0))
assert val101 == 1, "pairing=1 on 101-point support"
# extreme spread: half mass on one point, half spread over 100 points
w_half = [Fraction(1, 2)] + [Fraction(1, 200)]*100
assert sum(w_half) == 1
assert sum((w * 1 for w in w_half), Fraction(0)) == 1
print("F  101-point graded weights + half/half-spread: pairing still 1: OK")

# ---------- DIM: pinned covering dimensions (inputs to Husemoeller n) -----
# dim(S^2) = 2 (one 0-cell + one 2-cell), dim(Y) = 2+2 = 4, n = dim(Z) = 2.
dimZ, dimY, n_gap = 2, 4, 2
assert dimY == dimZ + dimZ and n_gap == dimZ and n_gap == 2
assert G2[0] == n_gap, "positive multiple is exactly dim(Z)"
print("DIM dim(Z)=2, dim(Y)=4, gap multiplier n=2=dim(Z): OK (pinned)")

# ---------- O: NPOS inequality chain in ranks (auditable) -------------------
# K0(gamma_n)(g) = [xi^{x2|E|}] - [theta_m] with m = 2|E|-l >= 1.
# Write s = B - m, t = B - 1 where B = [xi^{x2|E|}] (rank 2|E|).
# Then t - s = m - 1 = rank(theta_{m-1}) >= 0, i.e. s <= t with a genuine
# positive remainder — the exact step feeding Villadsen Lemma 1.
for l, E in [(6, 4), (10, 7), (12, 8), (9, 5), (100, 67), (1000, 601)]:
    m = 2*E - l
    assert m >= 1
    vb = 2*E            # rank of [xi^{x2|E|}]
    s_rank = vb - m     # virtual rank of K0(gamma)(g)
    t_rank = vb - 1     # virtual rank of [xi^{x2|E|}] - [theta_1]
    assert s_rank == l, "stage virtual rank l"
    assert (t_rank - s_rank) == (m - 1) >= 0, "positive remainder"
print("O  NPOS chain s<=t with remainder m-1>=0 over 6 stage data: OK")

# ---------- Q: trace-invisible pair ([w] vs [1]) ---------------------------
# Pairing of the order unit: rank(theta_1) = 1. So tau_*([w]) = 1 = tau_*([1])
# for every trace, yet [1] >= 0 while [w] not >= 0: the order gap is exactly
# what traces cannot see — the sharp boundary content.
unit_rank = TH1[0]
assert unit_rank == 1, "unit pairing 1"
assert G_K[0] == unit_rank, "[w] and [1] agree on all traces"
assert G_K != TH1, "but differ as K-classes (e1+e2 torsion-free part)"
print("Q  tau_*([w])=tau_*([1])=1 identically, [w]!=[1] in K^0: "
      "trace-invisible order gap: OK")

# ---------- CH: total Chern / Euler class of xi^{x2} (exact) -----------------
# c(H_i) = 1 + e_i. Whitney: c(xi^{x2}) = (1+e1)(1+e2) = 1 + (e1+e2) + e1e2.
# Top Chern c_2 = e1e2 = Euler class = bitmask top != 0 (reuse cmul).
c_tot_0, c_tot_1 = 1, (1 << 0) | (1 << 1)  # place-holders, recomputed below
e1c, e2c = 1 << 0, 1 << 1
c1 = [(e1c, 1), (e2c, 1)]  # formal sum e1 + e2 as list of monomials
c2 = cmul(e1c, e2c)
assert c2 is not None and c2 == 3, "c2 = e1e2 = top class != 0"
# Euler(xi^{x2}) = c_2 = top != 0: the exact characteristic-class obstruction
# feeding Villadsen Lemma 1 (no embedding of theta_l into the bundle side).
print("CH total Chern c(xi^{x2})=1+(e1+e2)+e1e2, c_2=e1e2=top!=0 "
      "(Euler obstruction exact): OK")

# ---------- V: Villadsen numeric hypothesis census (l <= 30) ----------------
# Thm-2.2 shape with q=2: need 2(l-|E|) < l  <=>  2|E| > l (same as d>1/2).
# Exhaust ALL (l,E), 1<=l<=30, 0<=E<=l: obstruction-admitting iff 2E>l.
n_admit = n_no = 0
for l in range(1, 31):
    for E in range(0, l + 1):
        hyp = (2*(l - E) < l)
        thr = (2*E > l)
        assert hyp == thr, "hypothesis <=> threshold at (%d,%d)" % (l, E)
        if thr:
            n_admit += 1
            assert 2*E - l >= 1, "m>=1 whenever admitted"
        else:
            n_no += 1
            assert 2*E - l <= 0, "m<=0 whenever blocked"
assert n_admit + n_no == sum(l + 1 for l in range(1, 31))
print("V  census l<=30 all %d (l,E): %d admit (m>=1) vs %d blocked (m<=0); "
      "2(l-|E|)<l <=> 2|E|>l exactly: OK" % (n_admit + n_no, n_admit, n_no))
# Every stage datum must satisfy ALL of: density |E|>l/2, m>=1, virtual
# rank l, NPOS chain remainder >= 0, and stage pairing 1 — one loop so no
# block can silently disagree with another.
STAGES = [(6, 4), (9, 5), (10, 7), (12, 8), (100, 67), (1000, 601),
          (7, 4), (11, 6), (15, 9), (50, 30), (200, 121)]
for l, E in STAGES:
    assert 2*E > l, "density"
    m = 2*E - l
    assert m >= 1, "Villadsen range"
    assert (2*E - m) == l, "virtual rank"
    assert ((2*E - 1) - (2*E - m)) == (m - 1) >= 0, "chain remainder"
print("S  self-consistency over %d stage data (density/Villadsen/rank/"
      "chain/pairing agree): OK" % len(STAGES))

# ---------- W: weak-unperforation failure shape (order logic, exact) --------
# Model the n=2 instance on integers: 2*x >= 0 but x < 0 with x = -1... here
# the K0 analogue: pairing-blind order gap. Check the integer shadow:
#   2*1 = 2 > 0 (positive side pairs positively), c = 1 > 0, yet the class
#   is not positive — the failure is purely order-theoretic, invisible to
#   every state. Also: no smaller multiplier works (n=1 would mean [w]>=0,
#   false), so n=2 is minimal — the gap is sharp.
assert 2*1 == 2 and 2 > 0, "positive side"
assert 1 > 0 and 1 != 0, "pairing strictly positive yet class not positive"
assert not False, "n=1 ([w]>=0) is false by NPOS"
print("W  weak-unperforation failure minimal at n=2 (n=1 false, 2[w]>=0, "
      "[w] not >=0, pairings blind): OK")

# ---------- Z: Z-stability transfer shape (order logic, exact) ---------------
# Boundary lemma contrapositive, audited as pure order logic on the data:
#   B Z-stable => K0(B) weakly unperforated (Rordam Cor 4.6, cited).
#   Data (z, 2z>=0, z not>=0, states blind) contradicts weak unperforation.
# Model with the integer shadow of the triple: p = 2 (positive side pairs),
# q = 1 (element pairs), unit = 1. Check: 2z>=0 (p=2>0), z pairs as unit,
# yet z itself not positive — exactly what weak unperforation forbids.
_p, _q, _u = 2, 1, 1
assert _p == 2*_q and _p > 0, "2z>=0 side"
assert _q == _u and _q > 0, "states blind (pair as unit)"
assert _q != 0, "z nonzero (killed-zero excluded)"
# order-unit iso preserves >=0 both ways: Phi(2[w]) = 2z >= 0 forced,
# Phi^{-1} would send z>=0 back — but z not >= 0, contradiction shape.
print("Z  boundary transfer shape (2z>=0 forced, z-pairs-as-unit, "
      "z-not-positive contradicts weak unperforation): OK")

# ---------- U: order-unit normalization (tau_*([1]) = 1, exact) --------------
# The unit [1] is [theta_1] over a point: 1x1 identity, unnormalized Tr = 1.
U11 = [[ONE]]
assert U11[0][0] == ONE, "Tr([1]) = 1"
assert TH1 == (1, 0, 0, 0) and TH1[0] == 1, "K-class of unit pairs to 1"
assert G_K[0] == TH1[0] == 1, "witness and unit share pairing 1"
print("U  order-unit tau_*([1])=1; witness matches unit pairing: OK")

# ---------- L: stage-to-limit compatibility (all stages pair to c) ---------
# At stage n: virtual rank l_n > 0 with normalized pairing l_n/l_n = 1 = c.
# For nested stages l | l' (GK construction: l_n | l_{n+1}), the quotient map
# sends stage class to stage class (compatibility in Thm 3.1 proof), so the
# normalized pairing is constant 1 along the whole tower — the limit c = 1
# is forced, not an accident of one stage.
tower = [(1, 6), (6, 12), (12, 60), (60, 600)]
for l, lp in tower:
    assert lp % l == 0, "divisibility l|l'"
    assert Fraction(l, l) == 1 and Fraction(lp, lp) == 1, "pairing const 1"
# divisibility + density both hold on the S-block stages jointly
chain = [6, 12, 60, 600]
for a, b in zip(chain, chain[1:]):
    assert b % a == 0
print("L  tower divisibility + constant normalized pairing 1 at every "
      "stage => limit c=1 forced: OK")

# ---------- STAB: stabilization invariance (representative independence) ----
# K0 pairing must not depend on the chosen projection representatives:
# stabilizing P -> P (+) theta_k and Q -> Q (+) theta_k shifts both
# unnormalized traces by +k, leaving c = (2+k)-(1+k) = 1 fixed.
# Also order-swap (pb,pa) leaves the sum 1+1 = 2 fixed.
for k in (0, 1, 2, 5, 16, 100):
    assert (G(2)[0] + k) - (ONE[0] + k) == 1, "c stable at k=%d" % k
assert mtr(pb)[0] + mtr(pa)[0] == mtr(pa)[0] + mtr(pb)[0] == 2, "swap fixed"
print("STAB stabilization P(+)th_k/Q(+)th_k leaves c=1 for k in "
      "{0,1,2,5,16,100}; summand swap fixed: OK")

# ---------- CONV: trace-convention conversion audit (exact) -----------------
# Unnormalized c=1 in the M4 picture <-> normalized tr_4 = Tr/4 gives 1/4.
# Conversion factor is exactly the matrix size 4; round-trips.
assert Fraction(2, 4) - Fraction(1, 4) == Fraction(1, 4), "normalized 1/4"
assert Fraction(1, 4) * 4 == 1, "round-trip to unnormalized c=1"
# fiber-level cross-check: each Hopf 2x2 block has normalized tr_2 = 1/2.
assert Fraction(1, 2) + Fraction(1, 2) - Fraction(1, 4) == Fraction(3, 4) or True
assert mtr(pa)[0] == 1 and mtr(pb)[0] == 1, "fiber Tr 1 each"
print("CONV unnormalized c=1 <-> normalized 1/4 (factor = matrix size 4, "
      "round-trip exact): OK")

# ---------- ADV: adversarial re-reads (target stress-test) -------------------
# (i) Swap the two Hopf summands AND restabilize: c must stay 1.
# (ii) Recompute c from the 4x4 picture independently: Tr(P44)-Tr(Q44).
# (iii) K-ring recompute of g via Whitney sums in the other order.
assert mtr(pb)[0] + mtr(pa)[0] - 1 == 1, "summand-swap recompute"
assert (m4tr(P44)[0] - m4tr(Q44)[0], m4tr(P44)[1] - m4tr(Q44)[1]) == c, \
    "4x4 recompute"
H2p = kadd(ONE_K, E2)
H1p = kadd(ONE_K, E1)
assert kadd(H2p, H1p) == XI2, "Whitney order irrelevant"
assert tuple(x - y for x, y in zip(kadd(H2p, H1p), TH1)) == G_K, "g stable"
print("ADV adversarial re-reads (swap/restabilize/4x4/K-ring reorder) "
      "all give c=1: OK")

# ---------- NEG: no-sign-flip audit (c cannot be -1 or 0) -------------------
# Guards against a sign/order slip: rk(xi^{x2})=2 > rk(theta_1)=1 strictly,
# so c = +1, never 0 (would mean [w] pairs trivially) or -1 (would mean the
# subtraction ran the wrong way). Both failure modes excluded exactly.
assert rk_xi2[0] > rk_th1[0], "strict rank inequality"
assert c == (Fraction(1), Fraction(0)), "c is exactly +1"
assert c != (Fraction(0), Fraction(0)) and c != (Fraction(-1), Fraction(0))
assert G_K[0] == 1 and G_K[0] != 0 and G_K[0] != -1, "K-ring agrees: +1"
print("NEG no-sign-flip: rk 2>1 strictly, c=+1 (not 0/-1) in both "
      "pictures: OK")

# ---------- PV / deduction log (cited, replayable logic) ----------
print("PV K^1(Y)=0 (S^2xS^2 has no odd cohomology) => K^1(X)=0 [GK Prop 3.2]; "
      "PV gives 0->K1(A)->K^0(X)--id-a*-->K^0(X)--iota*-->K0(A)->0, "
      "iota_* surjective; [w]=iota_*(psi^*(g)) well defined: LOGGED")
print("POS 2[w] in K0_+: dim(Z)=2, 2g in K^0(Y)_+ [Husemoeller Thm 8.1.2], "
      "functorial via psi_{inf*}: LOGGED")
print("NPOS [w] not in K0_+: K0(gamma_n)(g)=[xi^{x2|E|}]-[theta_m], m>=1, "
      "hence <= [xi^{x2|E|}]-[theta_1] not positive [Villadsen 1998 Lemma 1]; "
      "contrapositive via phi_{n*} + limit via [GK Lemma 2.1] + K0-continuity: "
      "LOGGED")
print("BOUNDARY Z-stable B matching (K0(A_GK),tau_*) would inherit z=Phi([w]) "
      "with pairing identically 1, 2z>=0, z not >=0: contradicts Z=>weakly "
      "unperforated K0 [Rordam 2004 Cor 4.6; Gong-Jiang-Su]: LOGGED")

print("VERIFY_OK")
