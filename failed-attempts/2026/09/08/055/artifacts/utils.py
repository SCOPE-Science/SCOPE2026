import numpy as np
from itertools import product

def iterate(h, start='0', iters=14, cap=40000):
    s = start
    for _ in range(iters):
        s = ''.join(h[c] for c in s)
        if len(s) >= cap:
            s = s[:cap]
            break
    return s

def arr(s):
    return np.frombuffer(s.encode(), dtype=np.uint8) - 48

def has_power_at_least(s, num, den, max_p=None):
    """True if s contains a factor with exponent >= num/den (as prefix-test on s)."""
    a = arr(s)
    n = len(a)
    limit = (n * den) // num
    if max_p is not None:
        limit = min(limit, max_p)
    for p in range(1, limit + 1):
        L = (num * p + den - 1) // den  # ceil(num*p/den)
        if L > n:
            continue
        d = (a[:n - p] != a[p:n]).astype(np.int32)
        # need run of >= L zeros... window: power starting at i needs d[i..i+L-2]? length L factor with period p: need a[i..i+L-1] p-periodic => L-1... precisely need d[i..i+L-1-p-? ]: pairs (j,j+p) for j in i..i+L-1-p => L-p comparisons all equal
        w = L - p
        if w <= 0:
            return True
        c = np.cumsum(d)
        tot = c[w - 1:]
        tot[1:] = tot[1:] - c[:-w]
        if tot.min() == 0:
            return True
    return False

def first_overlap_pos(s, max_p=400):
    a = arr(s); n = len(a)
    for p in range(1, max_p + 1):
        d = (a[:n - p] != a[p:n]).astype(np.int32)
        w = p + 1
        if w > n - p:
            continue
        c = np.cumsum(d)
        tot = c[w - 1:].copy()
        tot[1:] -= c[:-w]
        z = np.nonzero(tot == 0)[0]
        if len(z):
            return int(z[0]), p
    return None

def sam_pcounts(s, nmax):
    """distinct substring counts p(n) for n=1..nmax via suffix automaton + path DP."""
    link = [-1]; length = [0]; nexts = [dict()]
    last = 0
    for ch in s:
        c = ch; cur = len(length)
        length.append(length[last] + 1); link.append(0); nexts.append({})
        p = last
        while p != -1 and c not in nexts[p]:
            nexts[p][c] = cur; p = link[p]
        if p == -1:
            link[cur] = 0
        else:
            q = nexts[p][c]
            if length[p] + 1 == length[q]:
                link[cur] = q
            else:
                cl = len(length); length.append(length[p] + 1); link.append(link[q]); nexts.append(dict(nexts[q]))
                while p != -1 and nexts[p].get(c) == q:
                    nexts[p][c] = cl; p = link[p]
                link[q] = link[cur] = cl
        last = cur
    sz = len(length)
    # dp[l] = # distinct substrings of length l; process states in decreasing length
    order = sorted(range(sz), key=lambda i: length[i], reverse=True)
    # cnt[i] = dict? use aggregated: number of distinct substrings starting... simpler: standard formula per length via DP over DAG with generating
    # Use: f[v] = polynomial; do iterative deepening: dp[v] = {1: deg...} too heavy. Instead: count substrings of each length via BFS layering on SAM is exponential.
    # Standard trick: dp over (state) counting substrings of length<=k is also hard. Use suffix array + LCP instead.
    return sam_via_sa(s, nmax)

def sam_via_sa(s, nmax):
    n = len(s)
    # suffix array via doubling
    sa = np.arange(n); r = np.frombuffer(s.encode(), dtype=np.uint8).astype(np.int32)
    idx = np.arange(n); k = 1
    while True:
        b = np.full(n, -1); ok = idx + k < n; b[ok] = r[idx[ok] + k]
        sa = sa[np.lexsort((b[sa], r[sa]))]
        nr = np.zeros(n, np.int32)
        nr[sa[0]] = 0
        for i in range(1, n):
            nr[sa[i]] = nr[sa[i-1]] + ((r[sa[i]] != r[sa[i-1]]) or (b[sa[i]] != b[sa[i-1]]))
        r = nr
        if r[sa[-1]] == n - 1:
            break
        k *= 2
    rank = np.zeros(n, np.int32); rank[sa] = np.arange(n)
    lcp = np.zeros(n - 1, np.int32)
    h = 0
    for i in range(n):
        ri = rank[i]
        if ri == 0:
            h = 0; continue
        j = sa[ri - 1]
        while i + h < n and j + h < n and s[i+h] == s[j+h]:
            h += 1
        lcp[ri - 1] = h
        if h: h -= 1
    # distinct substrings of length m: sum over suffixes max(0, min(m, n-sa[i]) - min(m, lcp... )) use standard: contribution = max(0, min(m,depth_i) - min(m, lcp_{i-1}))
    res = {}
    import numpy as _np
    depth = n - sa
    for m in range(1, nmax + 1):
        res[m] = int(_np.sum(depth >= m) - _np.sum(lcp >= m))
    return res

def all_uniform(m):
    words = [''.join(t) for t in product('01', repeat=m)]
    for w0 in words:
        if not w0.startswith('0'):
            continue
        for w1 in words:
            yield {'0': w0, '1': w1}
