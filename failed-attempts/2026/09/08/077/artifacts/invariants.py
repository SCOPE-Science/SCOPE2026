"""Invariants + cycling/decycling for positive braids in left normal form."""
from garside import (compose, invert, identity, delta_perm, tau, proper_simples,
                     left_gcd, right_complement, start_set, finish_set)

def canonical_length(p, facs):
    return len(facs)

def summit_inf(p, facs, n):
    return p  # for positive braids inf = delta-power >= 0

def cycling(p, facs, n):
    """c(x) = Delta^p A2...Ar tau^{-p}(A1) then renormalize pass.
    Here implement on perm-factor level + sliding re-normalization."""
    if len(facs) <= 1: return p, list(facs)
    a1 = facs[0]; rest = facs[1:]
    t = a1
    for _ in range((p % 2)):
        t = tau(t, n)
    # new tail factor t appended at right then renormalize whole word
    new = rest + [t]
    # left-to-right? use right-to-left sliding passes
    from garside import left_weighted, normalize_pair
    ch = True
    while ch:
        ch = False
        for j in range(len(new)-2, -1, -1):
            x, y = new[j], new[j+1]
            if x == identity(n) or y == identity(n): continue
            if not left_weighted(x, y):
                ap, bp = normalize_pair(x, y, n)
                d = delta_perm(n)
                if ap == d:
                    # push Delta to front: Delta * bp ; tau-shift following factors
                    new[j] = d
                    # absorb: convert: remove d, apply tau to all after, p+=1
                    p += 1
                    tail = [tau(z, n) if z != d else z for z in (new[:j] + [bp] + new[j+2:])]
                    # drop identities and dups of d handled by recount
                    new = [z for z in tail if z != identity(n)]
                    dd = [z for z in new if z == d]
                    # move all Delta to front count
                    p += len(dd); new = [z for z in new if z != d]
                    ch = True
                    break
                elif bp == identity(n):
                    new[j] = ap; del new[j+1]; ch = True
                elif ap == identity(n):
                    new[j] = bp; del new[j+1]; ch = True
                else:
                    new[j], new[j+1] = ap, bp; ch = True
    new = [z for z in new if z != identity(n)]
    return p, new

def decycling(p, facs, n):
    if len(facs) <= 1: return p, list(facs)
    from garside import left_weighted, normalize_pair
    last = facs[-1]; rest = facs[:-1]
    t = last
    for _ in range((p % 2)):
        t = tau(t, n)
    new = [t] + rest
    ch = True
    while ch:
        ch = False
        for j in range(len(new)-2, -1, -1):
            x, y = new[j], new[j+1]
            if x == identity(n) or y == identity(n): continue
            if not left_weighted(x, y):
                ap, bp = normalize_pair(x, y, n)
                d = delta_perm(n)
                if ap == d:
                    p += 1
                    tail = [tau(z, n) if z != d else z for z in (new[:j] + [bp] + new[j+2:])]
                    new = [z for z in tail if z != identity(n)]
                    dd = [z for z in new if z == d]
                    p += len(dd); new = [z for z in new if z != d]
                    ch = True
                    break
                elif bp == identity(n):
                    new[j] = ap; del new[j+1]; ch = True
                elif ap == identity(n):
                    new[j] = bp; del new[j+1]; ch = True
                else:
                    new[j], new[j+1] = ap, bp; ch = True
    new = [z for z in new if z != identity(n)]
    return p, new

def summit_class_invariant(p, facs, n, max_iter=200):
    """Iterate cycling to a periodic orbit; return (inf_summit, canonical_len, orbit_min_tuple, iters)."""
    seen = {}
    cur = (p, tuple(facs))
    for t in range(max_iter):
        if cur in seen:
            cyc = cur
            break
        seen[cur] = t
        p2, f2 = cycling(cur[0], list(cur[1]), n)
        cur = (p2, tuple(f2))
    else:
        return cur[0], len(cur[1]), (cur[0], tuple(sorted(cur[1]))), max_iter
    # orbit: from first occurrence
    start = seen[cur]
    # canonical representative: min over cycle
    cyc_nodes = [k for k, v in seen.items() if v >= start]
    rep = min([(k[0], tuple(sorted(k[1]))) for k in cyc_nodes])
    return cur[0], len(cur[1]), (rep[0], rep[1]), t

def artin_perm_of_word(w, n):
    from garside import perm_of_word
    return perm_of_word(w, n)

def expsum(w):
    return len(w)

def seifert_circles_of_closure(w, n):
    """Seifert circles of closure of positive braid word: resolve each crossing
    orientation-preserving; count components via union-find on 2n strand-endpoints
    per crossing layer (standard algorithm)."""
    # model: n strands; events: for crossing of strands i,i+1 (positions), seifert smoothing
    # connects strand segments. Equivalent count: n + len(w) - rank? Use union-find:
    # nodes: (layer k, strand s) intervals. Simpler known formula for positive braid closure:
    # s = n (each strand closes to a circle, crossings join them): build DSU over n strands
    # where each crossing unions the two strands involved *at that height* — but strands
    # permute, so track labels.
    parent = list(range(n))
    def find(a):
        while parent[a] != a: parent[a] = parent[parent[a]]; a = parent[a]
        return a
    def union(a, b):
        a, b = find(a), find(b)
        if a != b: parent[a] = b
    lab = list(range(n))
    for i in w:
        a, b = lab[i], lab[i+1]
        union(a, b)
        lab[i], lab[i+1] = lab[i+1], lab[i]
    # seifert circles = number of DSU classes among strands after identification by closure perm?
    # Closure connects top s to bottom s: union lab[s] with s.
    for s in range(n):
        union(s, lab[s])
    return len({find(s) for s in range(n)})

def closure_genus(w, n):
    """Genus of closure surface via Seifert: g = (2 - mu + c - s)/2 with c=crossings, s=seifert circles, mu=components."""
    from garside import perm_of_word
    from math import gcd as _g
    # components = cycles of closure permutation
    pr = perm_of_word(w, n)
    vis = [False]*n; mu = 0
    for i in range(n):
        if not vis[i]:
            mu += 1; j = i
            while not vis[j]: vis[j] = True; j = pr[j]
    s = seifert_circles_of_closure(w, n)
    c = len(w)
    return (2 - mu + c - s)//2, mu, s
