"""Fast generating-tree enumeration for Av(4123,31524) and Av(4123,1324)."""
import sys, time
from itertools import permutations

def lis_len_atleast(arr, k):
    """Check if LIS length of arr >= k. Patience with small k."""
    # tails[i] = min tail of increasing subseq of length i+1
    tails = []
    for x in arr:
        # binary search
        lo, hi = 0, len(tails)
        while lo < hi:
            mid = (lo+hi)//2
            if tails[mid] < x:
                lo = mid+1
            else:
                hi = mid
        if lo == len(tails):
            tails.append(x)
            if len(tails) >= k:
                return True
        else:
            tails[lo] = x
    return len(tails) >= k

def child_avoids_4123_31524(parent, pos, m):
    """parent: tuple/list length m-1 avoiding; child inserts m at index pos.
    Returns True iff child avoids {4123,31524}."""
    n = m-1
    # Build suffix and prefix views without materializing full list
    # suffix = parent[pos:] (elements after insertion point), prefix = parent[:pos]
    # Check 4123: need increasing subseq of length 3 in suffix
    if m-1-pos >= 3:
        suf = parent[pos:]
        if lis_len_atleast(suf, 3):
            return False
    # Check 31524 with max at pos. Need p1<p2<pos<p4<p5 (in child coords),
    # values a=parent-part: v2 < v4 < v1 < v5 where v1 at p1, v2 at p2 (prefix), v4 at p4, v5 at p5 (suffix).
    # Brute force over pairs; lengths small.
    pre = parent[:pos]
    suf = parent[pos:]
    lp, ls = len(pre), len(suf)
    if lp >= 2 and ls >= 2:
        # For each pair (p4,p5) with p4<p5 in suffix and suf[p4]<suf[p5] (need v4<v5),
        # record min possible v4? Actually need existence of p1,p2 with v2<v4 and v4<v1<v5.
        # Precompute for suffix pairs: list of (v4,v5).
        # For prefix pairs p1<p2: (v1,v2).
        # Naive double loop is fine: |pre|*|suf| pairs.
        # Optimize: precompute prefix pair minima/maxima.
        # Simple approach: iterate over middle split.
        # For each (i1<i2) in pre, each (j1<j2) in suf with pre[i2]<suf[j1] and suf[j1]<pre[i1]<suf[j2].
        # Loop with early exit.
        for i1 in range(lp):
            v1 = pre[i1]
            for i2 in range(i1+1, lp):
                v2 = pre[i2]
                if v2 >= v1:
                    continue  # need v2 < v1 (since v2<v4<v1)
                # need suf pair j1<j2 with v2 < suf[j1] < v1 < suf[j2]
                for j1 in range(ls):
                    w4 = suf[j1]
                    if not (v2 < w4 < v1):
                        continue
                    for j2 in range(j1+1, ls):
                        w5 = suf[j2]
                        if v1 < w5:
                            return False
    return True

def child_avoids_4123_1324(parent, pos, m):
    n = m-1
    if m-1-pos >= 3:
        suf = parent[pos:]
        if lis_len_atleast(suf, 3):
            return False
    # 1324 with max last: need 132 pattern in prefix parent[:pos]
    pre = parent[:pos]
    lp = len(pre)
    if lp >= 3:
        # check contains 132: exists i1<i2<i3 with v1<v3<v2
        # O(lp^2) quick
        for i2 in range(1, lp):
            v2 = pre[i2]
            # min of pre[:i2]
            mn = min(pre[:i2])
            if mn >= v2:
                continue
            for i3 in range(i2+1, lp):
                v3 = pre[i3]
                if mn < v3 < v2:
                    return False
    return True

def enumerate_tree(checker, nmax):
    """BFS/DFS over insert-max tree. Returns counts[0..nmax]."""
    counts = [0]*(nmax+1)
    counts[0] = 1
    cur = [()]  # perms of current length as tuples
    # store as lists for speed? tuples fine
    for m in range(1, nmax+1):
        nxt = []
        for p in cur:
            # try each insertion position
            for pos in range(m):
                if checker(p, pos, m):
                    # build child tuple
                    c = p[:pos] + (m,) + p[pos:]
                    nxt.append(c)
        counts[m] = len(nxt)
        cur = nxt
        print(f"n={m}: {counts[m]} (parents {len(cur)})", flush=True)
    return counts

def brute_contains(perm, pat):
    from itertools import combinations
    n, k = len(perm), len(pat)
    for idx in combinations(range(n), k):
        vals = [perm[i] for i in idx]
        # normalize
        s = sorted(vals)
        rank = {v:i+1 for i,v in enumerate(s)}
        if tuple(rank[v] for v in vals) == pat:
            return True
    return False

def brute_count(n, basis):
    c = 0
    for p in permutations(range(1, n+1)):
        ok = True
        for b in basis:
            if len(b) <= n and brute_contains(p, b):
                ok = False; break
        c += 1 if ok else 0
    return c

if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv)>1 else 10
    which = sys.argv[2] if len(sys.argv)>2 else "31524"
    t0=time.time()
    if which == "31524":
        counts = enumerate_tree(child_avoids_4123_31524, nmax)
    else:
        counts = enumerate_tree(child_avoids_4123_1324, nmax)
    print(counts)
    print("time", time.time()-t0)
