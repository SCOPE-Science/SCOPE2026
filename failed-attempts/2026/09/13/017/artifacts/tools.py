"""Exact tools for even-hole / clique / chromatic analysis (bitmask based)."""
import itertools, sys

def adj_to_masks(adj, n):
    m = [0]*n
    for i in range(n):
        b = 0
        for j in adj[i]:
            b |= (1 << j)
        m[i] = b
    return m

def induced_degrees_ok(mask, masks, n):
    # check every v in mask has exactly 2 neighbors within mask
    mm = mask
    vs = []
    v = 0
    while mm:
        if mm & 1:
            vs.append(v)
        v += 1; mm >>= 1
    for v in vs:
        d = bin(masks[v] & mask).count('1')
        if d != 2:
            return False
    # connectivity over mask
    seen = 1 << vs[0]
    stack = [vs[0]]
    while stack:
        x = stack.pop()
        nb = masks[x] & mask & ~seen
        while nb:
            lsb = nb & (-nb); nb ^= lsb
            y = lsb.bit_length()-1
            seen |= (1 << y); stack.append(y)
    return seen == mask

def find_even_hole(masks, n, limit=0):
    """Return an even hole vertex-mask, or 0 if none. limit: max holes to count (0 = existence)."""
    count = 0
    # iterate sizes 4,6,8,... (even)
    for s in range(4, n+1, 2):
        for combo in itertools.combinations(range(n), s):
            mask = 0
            for v in combo:
                mask |= (1 << v)
            if induced_degrees_ok(mask, masks, n):
                if limit == 0:
                    return mask
                count += 1
                if count >= limit:
                    return mask
    return 0

def count_even_holes(masks, n, cap=50):
    c = 0
    for s in range(4, n+1, 2):
        for combo in itertools.combinations(range(n), s):
            mask = 0
            for v in combo:
                mask |= (1 << v)
            if induced_degrees_ok(mask, masks, n):
                c += 1
                if c >= cap:
                    return c
    return c

def max_clique_size(masks, n):
    best = [0]
    # branch and bound (Tomita-style simple)
    def expand(cand, depth):
        # bound
        i = 0
        while cand:
            # prune by popcount
            if depth + bin(cand).count('1') <= best[0]:
                return
            v = (cand & (-cand)).bit_length() - 1 if False else None
            # pick lowest set bit
            lsb = cand & (-cand)
            vv = lsb.bit_length() - 1
            cand ^= lsb
            expand(cand & masks[vv], depth+1)
            if depth+1 > best[0]:
                best[0] = depth+1
    expand((1 << n) - 1, 0)
    return best[0]

def is_k_colorable(masks, n, k):
    # DSATUR branch and bound decision
    nbr = masks
    color = [-1]*n
    # order: saturation
    def select():
        bestv = -1; bestsat = -1; bestdeg = -1
        for v in range(n):
            if color[v] >= 0:
                continue
            used = set()
            for w in range(n):
                if (nbr[v] >> w) & 1 and color[w] >= 0:
                    used.add(color[w])
            s = len(used)
            d = bin(nbr[v]).count('1')
            if s > bestsat or (s == bestsat and d > bestdeg):
                bestsat = s; bestdeg = d; bestv = v
        return bestv
    # forward: try
    import sys
    sys.setrecursionlimit(10000)
    def rec(colored):
        if colored == n:
            return True
        v = select()
        forbidden = 0
        for w in range(n):
            if ((nbr[v] >> w) & 1) and color[w] >= 0:
                forbidden |= (1 << color[w])
        for c in range(k):
            if not (forbidden >> c) & 1:
                color[v] = c
                if rec(colored+1):
                    return True
                color[v] = -1
        return False
    return rec(0)

def chromatic_number(masks, n, lo=1, hi=None):
    if hi is None:
        hi = n
    # quick lower bound: max clique
    w = max_clique_size(masks, n)
    lo = max(lo, w)
    for k in range(lo, hi+1):
        if is_k_colorable(masks, n, k):
            return k
    return hi+1

def greedy_upper(masks, n):
    order = sorted(range(n), key=lambda v: bin(masks[v]).count('1'), reverse=True)
    col = [-1]*n
    for v in order:
        used = set(col[w] for w in range(n) if ((masks[v] >> w) & 1) and col[w] >= 0)
        c = 0
        while c in used:
            c += 1
        col[v] = c
    return max(col)+1

def edges_of(masks, n):
    E = []
    for i in range(n):
        for j in range(i+1, n):
            if (masks[i] >> j) & 1:
                E.append((i, j))
    return E

def from_edges(n, E):
    m = [0]*n
    for i, j in E:
        m[i] |= (1 << j); m[j] |= (1 << i)
    return m
