"""Explore 1-hole 2-adic Toeplitz candidates: complexity + complement symmetry."""
import math
from collections import defaultdict

def v2(k):
    assert k != 0
    k = abs(k)
    c = 0
    while k % 2 == 0:
        k //= 2
        c += 1
    return c

def build_word(a, M, x0=None):
    # positions -M..M, x_m = a[v2(m)] for m != 0
    x = {}
    for m in range(-M, M + 1):
        if m == 0:
            x[m] = a[0] if x0 is None else x0
        else:
            x[m] = a[v2(m) % len(a)] if v2(m) < len(a) else a[-1]
    return [x[m] for m in range(-M, M + 1)]

def factor_set(word, n):
    s = set()
    L = len(word)
    for i in range(L - n + 1):
        s.add(tuple(word[i:i + n]))
    return s

def complexity(word, nmax):
    out = {}
    for n in range(1, nmax + 1):
        out[n] = len(factor_set(word, n))
    return out

def complement_closed(word, nmax):
    # check: every factor's complement is also a factor (within same word approx)
    for n in range(1, nmax + 1):
        F = factor_set(word, n)
        for w in F:
            c = tuple(1 - b for b in w)
            if c not in F:
                return False, n, w
    return True, None, None

M = 2**15
NCODE = 32
cands = {
    "alt": [i % 2 for i in range(NCODE)],
    "sparse_pow2": [1 if (i > 0 and (i & (i - 1)) == 0) else 0 for i in range(NCODE)],
    "per3": [1 if i % 3 == 0 else 0 for i in range(NCODE)],
    "per3b": [(i % 3) % 2 for i in range(NCODE)],
    "zeros_tail": [1 if i < 6 and i % 2 == 0 else 0 for i in range(NCODE)],  # eventually const -> periodic, control
    "beatty": [1 if int((i + 1) * math.sqrt(2)) - int(i * math.sqrt(2)) > 0 else 0 for i in range(NCODE)],
}
for name, a in cands.items():
    # need coding defined for valuations up to v2(M)~15; extend periodically? No:
    # use a as function of valuation index directly (length NCODE covers v<=31)
    w = build_word(a, M)
    comp = complexity(w, 200)
    print(f"=== {name}: a[:16]={a[:16]}")
    for n in [10, 20, 40, 80, 160, 200]:
        print(f"  p({n})={comp[n]}  p/(n log2 n)={comp[n]/(n*math.log2(n)):.3f}")
    ok, n0, wit = complement_closed(w, 25)
    print(f"  complement-closed to 25: {ok}" + (f" fail at n={n0} wit={wit}" if not ok else ""))
