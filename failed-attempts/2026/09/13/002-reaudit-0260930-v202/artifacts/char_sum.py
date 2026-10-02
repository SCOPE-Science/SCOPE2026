"""Step 1: Exact S9 Frobenius-Burnside character sums for H_A and H_B.
Target: d=9, g=0, mu_A=(6,2,1) vs mu_B=(3,3,3), nu=(5,4), r=3 simple points.
H = N_trans/9!, N via Frobenius formula; transitivity is automatic (proved separately
via disjoint proper-subset-sums argument), so N_trans = N_total.
"""
from fractions import Fraction
from functools import lru_cache
from math import factorial, comb
import itertools

D = 9
FACT9 = factorial(9)

def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None:
        max_part = n
    for k in range(min(max_part, n), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest

PARTS9 = list(partitions(9))
print("num partitions of 9:", len(PARTS9))

def cells(lam):
    for i, r in enumerate(lam):
        for j in range(r):
            yield (i, j)

def is_diagram(cellset):
    """cellset (set of (i,j)) is a Ferrers diagram iff rows left-justified, top-justified, lengths nonincreasing."""
    if not cellset:
        return True
    rows = {}
    for (i, j) in cellset:
        rows.setdefault(i, []).append(j)
    maxrow = max(rows)
    if set(rows) != set(range(maxrow + 1)):
        return False
    prev = None
    for i in range(maxrow + 1):
        js = sorted(rows[i])
        if js != list(range(len(js))):
            return False
        if prev is not None and len(js) > prev:
            return False
        prev = len(js)
    return True

def connected(cellset):
    cellset = set(cellset)
    if not cellset:
        return False
    stack = [next(iter(cellset))]
    seen = set(stack)
    while stack:
        c = stack.pop()
        for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nb = (c[0] + d[0], c[1] + d[1])
            if nb in cellset and nb not in seen:
                seen.add(nb)
                stack.append(nb)
    return seen == cellset

def has_2x2(cellset):
    S = set(cellset)
    for (i, j) in S:
        if (i + 1, j) in S and (i, j + 1) in S and (i + 1, j + 1) in S:
            return True
    return False

@lru_cache(maxsize=None)
def charval(lam, mu):
    """Irreducible character of S_n: partition lam at class of cycle type mu (Murnaghan-Nakayama)."""
    lam = tuple(lam)
    mu = tuple(mu)
    if not mu:
        return 1 if not lam else 0
    if not lam:
        return 0
    k = mu[0]
    rest = mu[1:]
    L = set(cells(lam))
    if k > len(L):
        return 0
    total = 0
    for subset in itertools.combinations(sorted(L), k):
        S = set(subset)
        if not connected(S):
            continue
        if has_2x2(S):
            continue
        rem = L - S
        if not is_diagram(rem):
            continue
        # build partition of remainder
        rows = {}
        for (i, j) in rem:
            rows[i] = rows.get(i, 0) + 1
        lam2 = tuple(sorted(rows.values(), reverse=True))
        ht = len(set(i for (i, j) in S)) - 1
        total += ((-1) ** ht) * charval(lam2, rest)
    return total

def class_size(ctype, d=D):
    from collections import Counter
    c = Counter(ctype)
    z = 1
    for ln, m in c.items():
        z *= (ln ** m) * factorial(m)
    return factorial(d) // z

MU_A = (6, 2, 1)
MU_B = (3, 3, 3)
NU = (5, 4)
TAU = (2, 1, 1, 1, 1, 1, 1, 1)
ID = (1,) * 9
R = 3

# ---- self-checks on character table ----
dims = {lam: charval(lam, ID) for lam in PARTS9}
assert sum(d * d for d in dims.values()) == FACT9, "sum dim^2 != 9!"
print("self-check 1 (sum dim^2 = 9!) OK; dims:", sorted(dims.values()))

def content_sum(lam):
    return sum(j - i for (i, j) in cells(lam))

for lam in PARTS9:
    # normalized transposition character = content_sum / C(9,2)
    assert charval(lam, TAU) * comb(9, 2) == content_sum(lam) * dims[lam], f"content check fail {lam}"
print("self-check 2 (transposition chars = content sums) OK")

def hurwitz_double(mu, nu, r, d=None):
    """Disconnected (=connected if off-wall/transitive-forced) double Hurwitz number
    H = N/ d! where N = tuple count via Frobenius; caller ensures normalization context."""
    if d is None:
        d = sum(mu)
    assert sum(mu) == d and sum(nu) == d
    parts = list(partitions(d))
    ca = class_size(tuple(mu), d)
    cn = class_size(tuple(nu), d)
    ct = class_size((2,) + (1,) * (d - 2), d)
    k = 2 + r
    tot = Fraction(0)
    for lam in parts:
        a = charval(tuple(lam), tuple(mu))
        b = charval(tuple(lam), tuple(nu))
        t = charval(tuple(lam), (2,) + (1,) * (d - 2))
        dim = charval(tuple(lam), (1,) * d)
        if dim == 0:
            continue
        tot += Fraction(a * b * (t ** r), dim ** (k - 2))
    N = Fraction(ca * cn * (ct ** r), factorial(d)) * tot
    assert N.denominator == 1, f"tuple count not integral: {N}"
    return Fraction(N, factorial(d)), N

HA, NA = hurwitz_double(MU_A, NU, R)
HB, NB = hurwitz_double(MU_B, NU, R)
print("N_A =", NA, " H_A =", HA, "=", float(HA))
print("N_B =", NB, " H_B =", HB, "=", float(HB))
print("jump H_B - H_A =", HB - HA)

# ---- transitivity / off-wall check: proper subset sums ----
def proper_subsums(p):
    s = set()
    for r in range(1, len(p)):
        for c in itertools.combinations(range(len(p)), r):
            s.add(sum(p[i] for i in c))
    return s

print("subsums mu_A:", sorted(proper_subsums(MU_A)),
      "mu_B:", sorted(proper_subsums(MU_B)),
      "nu:", sorted(proper_subsums(NU)))
print("disjoint A:", proper_subsums(MU_A).isdisjoint(proper_subsums(NU)),
      "disjoint B:", proper_subsums(MU_B).isdisjoint(proper_subsums(NU)))
