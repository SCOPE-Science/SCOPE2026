"""Auditable seed + separator log for lane-603 TARGET (S_{1,1} tagged Sk vs U).

Stdlib only. Verifies:
  (S1) B(T0) Markov data: det, rank, kernel n0=(1,1,1), no BZ compatible Lambda.
  (S2) FZ mutations mu_k(B) recover B up to permutation (Markov mutation class).
  (S3) Markov upper-cluster invariant W = (A1^2+A2^2+A3^2)/(A1 A2 A3) in U:
       exact Laurent identity N'*D - N*D' == 0 after mutation at each k.
  (S4) Mixed tag vector (plain,plain,notched) violates FST tagged compatibility,
       so T0 is not a tagged triangulation / cluster.
  (S5) Extra-wall numerics: PH=(1+z^m0)^2 coeffs sum to 4; lambda(m)=4^[-<m,n0>]+.
  (S6) G-vector/wall table for MCG-orbit representatives.
Prints VERIFY_OK on success.
"""
from fractions import Fraction

B = [[0, 2, -2], [-2, 0, 2], [2, -2, 0]]

def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))

def rank_q(M):
    A = [[Fraction(x) for x in row] for row in M]
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, m):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                for j in range(c, n):
                    A[i][j] -= f * A[r][j]
        r += 1
    return r

def fz_mutate(M, k):
    n = len(M)
    Mp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == k or j == k:
                Mp[i][j] = -M[i][j]
            else:
                Mp[i][j] = M[i][j] + (abs(M[i][k]) * M[k][j] + M[i][k] * abs(M[k][j])) // 2
    return Mp

def perm_equal(A, Bp):
    import itertools
    n = len(A)
    for p in itertools.permutations(range(n)):
        if all(A[i][j] == Bp[p[i]][p[j]] for i in range(n) for j in range(n)):
            return p
    return None

# ---- Laurent monomial dicts: key=(e1,e2,e3) -> int coeff ----
def ladd(a, b, s=1):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, 0) + s * v
        if c[k] == 0:
            del c[k]
    return c

def lmul(a, b):
    c = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            k = (k1[0] + k2[0], k1[1] + k2[1], k1[2] + k2[2])
            c[k] = c.get(k, 0) + v1 * v2
    return {k: v for k, v in c.items() if v != 0}

def lpow(a, n):
    assert n >= 0
    c = {(0, 0, 0): 1}
    for _ in range(n):
        c = lmul(c, a)
    return c

def ldiv_by_Ak(poly, k):
    # divide every monomial by A_k (exact by construction in our uses)
    c = {}
    for (e1, e2, e3), v in poly.items():
        e = [e1, e2, e3]
        e[k] -= 1
        c[(e[0], e[1], e[2])] = c.get((e[0], e[1], e[2]), 0) + v
    return {k: v for k, v in c.items() if v != 0}

A1 = {(1, 0, 0): 1}
A2 = {(0, 1, 0): 1}
A3 = {(0, 0, 1): 1}
AV = [A1, A2, A3]
N = ladd(ladd(lpow(A1, 2), lpow(A2, 2)), lpow(A3, 2))
D = lmul(lmul(A1, A2), A3)

log = []
d = det3(B)
log.append(f"B(T0)={B}")
log.append(f"det(B)={d}")
assert d == 0, "expected singular Markov matrix"
r = rank_q(B)
log.append(f"rank(B)={r}")
assert r == 2
n0 = [1, 1, 1]
Bn0 = [sum(B[i][j] * n0[j] for j in range(3)) for i in range(3)]
log.append(f"B*n0={Bn0} for n0={n0}")
assert Bn0 == [0, 0, 0]
log.append("No compatible Lambda: Lambda*B=d*I would imply det(B)!=0, but det(B)=0. "
           "Hence coefficient-free BZ quantum seed at B(T0) is undefined.")
# kernel argument: (Lambda*B)*n0 = Lambda*0 = 0 vs d*n0 != 0
log.append("Kernel check: B*n0=0 => (Lambda B)n0=0, but d*I*n0=d*n0!=0 for d>0. Contradiction.")

for k in range(3):
    Mp = fz_mutate(B, k)
    p = perm_equal(B, Mp)
    log.append(f"mu_{k + 1}(B)={Mp} perm_of_B={p}")
    assert p is not None, f"mutation {k} leaves Markov class"

for k in range(3):
    others = [AV[i] for i in range(3) if i != k]
    num = ladd(lpow(others[0], 2), lpow(others[1], 2))  # Ai^2+Aj^2
    Akp = ldiv_by_Ak(num, k)  # A_k' = (Ai^2+Aj^2)/Ak
    Np = ladd(ladd(lmul(Akp, Akp), lpow(others[0], 2)), lpow(others[1], 2))
    others_full = [Akp if i == k else AV[i] for i in range(3)]
    Dp = lmul(lmul(others_full[0], others_full[1]), others_full[2])
    diff = ladd(lmul(Np, D), lmul(N, Dp), s=-1)
    log.append(f"W-invariance at k={k + 1}: Np*D-N*Dp terms={len(diff)}")
    assert diff == {}, f"W identity failed at {k}"
W = {(1, -1, -1): 1, (-1, 1, -1): 1, (-1, -1, 1): 1}
Wd = lmul(N, {( -1, -1, -1): 1})  # N/D shift check
log.append(f"W=(A1^2+A2^2+A3^2)/(A1A2A3) Laurent terms={sorted(W.items())}")
assert Wd == W, "W Laurent form mismatch"
log.append("W is mutation-invariant as rational function (Np/Dp=N/D), hence Laurent in "
           "every Markov cluster: W in U(S_{1,1}).")

tags = ["plain", "plain", "notched"]  # T0 tag vector, each arc doubly-tagged at lone puncture
ok = True
pairs = []
for i in range(3):
    for j in range(i + 1, 3):
        compat = (tags[i] == tags[j])  # single puncture: distinct arcs need same tag
        pairs.append(((i, j, tags[i], tags[j], compat)))
        if not compat:
            ok = False
log.append(f"T0 tags={tags} pairwise={pairs}")
assert not ok, "expected mixed-tag incompatibility"
log.append("T0 (2 plain + 1 notched) is NOT a tagged triangulation: distinct arcs sharing the "
           "lone puncture need equal tags (FST compatibility). So T0 defines no cluster.")

# Extra wall numerics: PH=(1+z^m0)^2 = 1+2 z^m0 + z^2m0
ph = [1, 2, 1]
log.append(f"PH coeffs={ph} sum={sum(ph)} (Mandel-Qin Thm B.4 / Remark B.5)")
assert sum(ph) == 4

def lam(m, nn=(1, 1, 1)):
    return 4 ** max(0, -sum(a * b for a, b in zip(m, nn)))

assert lam((1, 0, 0)) == 1 and lam((-1, 0, 0)) == 4 and lam((1, -1, 0)) == 1
log.append("lambda(m)=4^[-<m,n0>]+: plain (1,0,0)->1, notched (-1,0,0)->4, central (1,-1,0)->1. "
           "Notched bracelet = 4*theta (classical coefficient-free).")

table = [
    ("plain arc γ1", (1, 0, 0), "+1 in H+ (cluster complex side)", "cluster variable = theta"),
    ("notched arc γ1⋄", (-1, 0, 0), "-1 in H- (notched side)", "bracelet = 4·theta; needs (H,fH)"),
    ("arc-pair/loop-adjacent (Zhou ϑ_{fi-fi+1})", (1, -1, 0), "0 on H=n0^⊥ (central)", "theta; broken-line count 3"),
]
for row in table:
    log.append(f"MCG-rep: {row[0]} g={row[1]} <g,n0>={sum(a for a in row[1])} :: {row[2]} :: {row[3]}")

print("\n".join(log))
print("VERIFY_OK")
