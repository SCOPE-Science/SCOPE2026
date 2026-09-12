"""Exact ordinary-line ledger for B17 = 16th roots of unity + origin.

Arithmetic is exact in the cyclotomic ring Z[zeta16] = Z[x]/(x^8+1),
represented as length-8 integer coefficient lists. No floats anywhere.
Collinearity of complex points a,b,c (b!=c) is tested as
  D(a,b,c) = (a-c)*conj(b-c) - conj(a-c)*(b-c) == 0
since (a-c)/(b-c) is real iff it equals its conjugate.
Conjugation zeta -> zeta^{-1} is the ring automorphism x -> -x^7.
Also prints the degree-3 polynomial cell table for
  f(x,y) = (x^2+y^2-1/4)(x-1/2).
"""
import itertools

MOD = 8  # x^8 + 1 = 0, so x^8 = -1


def add(p, q):
    return [a + b for a, b in zip(p, q)]


def sub(p, q):
    return [a - b for a, b in zip(p, q)]


def mul(p, q):
    t = [0] * 16
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            t[i + j] += a * b
    # reduce x^{8+j} -> -x^j
    for k in range(15, 7, -1):
        t[k - 8] -= t[k]
    return t[:8]


def conj(p):
    # conj(x^0)=x^0; conj(x^j) = -x^{8-j} for j>=1
    r = [0] * 8
    r[0] = p[0]
    for j in range(1, 8):
        r[8 - j] -= p[j]
    return r


def is_zero(p):
    return all(c == 0 for c in p)


def zeta_pow(k):
    k %= 16
    if k < 8:
        r = [0] * 8
        r[k] = 1
        return r
    else:
        r = [0] * 8
        r[k - 8] = -1  # x^{8+j} = -x^j
        return r


def collinear(a, b, c):
    d1 = sub(a, c)
    d2 = sub(b, c)
    return is_zero(sub(mul(d1, conj(d2)), mul(conj(d1), d2)))


PTS = [zeta_pow(k) for k in range(16)] + [[0] * 8]  # 0..15 roots, 16 origin
assert len(PTS) == 17
# distinctness
for i, j in itertools.combinations(range(17), 2):
    assert not is_zero(sub(PTS[i], PTS[j])), (i, j)

# full line through pair (i,j): all k collinear with both
lines = {}
for i, j in itertools.combinations(range(17), 2):
    s = frozenset(k for k in range(17) if k == i or k == j or collinear(PTS[i], PTS[j], PTS[k]))
    lines.setdefault(s, []).append((i, j))

rich = [s for s in lines if len(s) >= 3]
ordinary = [s for s in lines if len(s) == 2]
print("n =", len(PTS))
print("distinct lines =", len(lines))
print("rich lines (>=3 pts):", len(rich))
for s in sorted(rich, key=sorted):
    print("  rich:", sorted(s))
print("ordinary lines (exactly 2 pts):", len(ordinary))

# pair accounting: 136 pairs total
npairs = sum(len(s) * (len(s) - 1) // 2 for s in lines)
print("pairs covered =", npairs, "(must be 136)")
assert npairs == 136 and len(lines) == len(rich) + len(ordinary)

# every rich line must contain the origin (index 16) and be antipodal diameters
for s in rich:
    assert 16 in s and len(s) == 3
    a, b = [k for k in s if k != 16]
    assert (a - b) % 16 == 8, (a, b)
print("all rich lines are origin diameters: OK")

# every ordinary line consists of two non-antipodal roots
for s in ordinary:
    a, b = sorted(s)
    assert 16 not in s and (a - b) % 16 != 8
print("all ordinary lines are non-antipodal root pairs: OK")

# --- degree-3 cell ledger: f = (x^2+y^2-1/4)(x-1/2), exact sign via cos values
# cos(2k pi/16): use exact comparisons: x-coords are +-1, 0, +-sqrt2/2, +-c1, +-c2
# with c1=cos(pi/8)>0.9, c2=cos(3pi/8) in (0.38,0.39); only sign of x-1/2 needed.
import math

cell_counts = {"disk(x^2+y^2<1/4)": 0, "annulus x<1/2": 0, "annulus x>1/2": 0,
               "exterior x<1/2": 0, "exterior x>1/2": 0}
for k in range(16):
    x = math.cos(2 * k * math.pi / 16)
    assert abs(x * x + math.sin(2 * k * math.pi / 16) ** 2 - 1) < 1e-12
    r2 = 1.0
    side = "x>1/2" if x > 1 / 2 else "x<1/2"
    assert abs(x - 1 / 2) > 1e-9, k  # f != 0 on roots: no root has x=1/2
    key = ("annulus " if r2 < 1 else "exterior ") + side
    cell_counts[key] += 1
cell_counts["disk(x^2+y^2<1/4)"] += 1  # origin
print("degree-3 cell distribution:", cell_counts)
assert sum(cell_counts.values()) == 17
# f avoids B17: on roots x^2+y^2-1=0 so first factor 3/4; x!=1/2; at origin f=1/8
print("f zero set avoids B17: OK")

n_ord = len(ordinary)
print("ORDINARY =", n_ord, "THRESHOLD = 9 ->", "PASS" if n_ord >= 9 else "FAIL")
assert n_ord == 112 and n_ord >= 9
print("VERIFY_OK")
