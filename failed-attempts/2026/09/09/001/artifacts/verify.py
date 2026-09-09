"""Independent replay verifier (stdlib + numpy only).
Usage: python3 verify.py
Checks every headline witness from its committed matrix file."""
import numpy as np, json
from fractions import Fraction
from math import comb

def load(p):
    return np.loadtxt(p, dtype=int)

def hist_gray(G):
    k, n = G.shape
    N = 1 << k
    h = [0]*(n+1); cur = np.zeros(n, dtype=int); h[0] = 1
    for i in range(1, N):
        gi = i ^ (i >> 1); gm = (i-1) ^ ((i-1) >> 1)
        b = (gi ^ gm).bit_length() - 1
        cur ^= G[b]; h[int(cur.sum())] += 1
    return h

def rank2(M):
    A = M.copy() % 2; r = 0; row = 0
    R, C = A.shape
    for c in range(C):
        p = -1
        for i in range(row, R):
            if A[i, c]: p = i; break
        if p < 0: continue
        A[[row, p]] = A[[p, row]]
        for i in range(R):
            if i != row and A[i, c]: A[i] ^= A[row]
        row += 1; r += 1
    return r

def nullbasis(G):
    k, n = G.shape
    R = G.copy() % 2
    where = [-1]*n; row = 0
    for c in range(n):
        s = -1
        for i in range(row, k):
            if R[i, c]: s = i; break
        if s == -1: continue
        R[[row, s]] = R[[s, row]]
        for i in range(k):
            if i != row and R[i, c]: R[i] ^= R[row]
        where[c] = row; row += 1
    free = [c for c in range(n) if where[c] == -1]
    B = np.zeros((len(free), n), dtype=int)
    for j, f in enumerate(free):
        B[j, f] = 1
        for c in range(n):
            if where[c] != -1: B[j, c] = R[where[c], f]
    return B

def mwdual(A, n, k):
    out = []
    for j in range(n+1):
        s = Fraction(0)
        for i, a in enumerate(A):
            if a:
                s += a*sum(Fraction(((-1)**t)*comb(i, t)*comb(n-i, j-t))
                           for t in range(max(0, j-(n-i)), min(j, i)+1))
        q, r = divmod(s, 2**k)
        assert r == 0, (j, s)
        out.append(int(q))
    return out

cert = json.load(open("cert.json"))
ok = True
for name, e in cert.items():
    G = load(e["file"].split("/")[-1])
    n, k = G.shape[1], G.shape[0]
    assert (n, k) == (e["n"], e["k"]), name
    assert rank2(G) == e["k"] == e["rank"], name
    h = hist_gray(G)
    assert h == e["hist"], name
    assert sum(h) == 2**k, name
    d = next(i for i in range(1, n+1) if h[i])
    assert d == e["d"], (name, d)
    Bd = mwdual(h, n, k)
    assert Bd == e["MW_dual"], name
    assert sum(Bd) == 2**(n-k), name
    if e["dual_enumerated"]:
        dh = hist_gray(nullbasis(G))
        assert dh == Bd, name
        assert dh == e["dual_hist"], name
    print(f"{name}: OK [{n},{k},{d}] tally={sum(h)} MWsum={sum(Bd)}" +
          (f" dual-enumerated d_perp={e['dual_d']}" if e["dual_enumerated"] else " MW-integral-only"))
print("VERIFY_OK")
