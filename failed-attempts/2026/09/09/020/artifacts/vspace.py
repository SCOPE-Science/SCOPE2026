"""Vector-space groups C2^6 and C3^4: exact CD data via linear algebra (stdlib).

Abelian theorem (proved in DRAFT): CD(G) = full subgroup lattice, m = |G|^2,
CD-subgroup = {1}. Subspaces enumerated via independent-tuple canonical keys;
rank sizes checked against Gaussian binomials; width = middle Gaussian number
(Sperner for subspace lattices) with explicit full-middle-rank witness,
pairwise incomparability brute-force checked.
"""
import json, os, sys, itertools
from math import comb

def gauss(p, n, k):
    num = den = 1
    for i in range(k):
        num *= p**(n-i)-1
        den *= p**(k-i)-1
    return num // den

def addv(p, a, b): return tuple((x+y) % p for x, y in zip(a, b))
def mulv(p, c, a): return tuple((c*x) % p for x in a)

def span(p, vecs, zero):
    S = {zero}
    for v in vecs:
        S = S | {addv(p, s, w) for s in S for w in (v, mulv(p, p-1, v)) }
        # closure under all scalar multiples: iterate
        changed = True
        while changed:
            changed = False
            cur = list(S)
            for s in cur:
                for t in cur:
                    u = addv(p, s, t)
                    if u not in S:
                        S.add(u); changed = True
    return frozenset(S)

def indep(p, vecs, zero):
    seen = []
    for v in vecs:
        if v == zero: return False
        # v in span of seen?
        S = {zero}
        for w in seen:
            S = S | {addv(p, s, w2) for s in S for w2 in [w]+[mulv(p,c,w) for c in range(2,p)]}
            cl = True
            while cl:
                cl = False
                cur = list(S)
                for s in cur:
                    for t in cur:
                        u = addv(p, s, t)
                        if u not in S: S.add(u); cl = True
        if v in S: return False
        seen.append(v)
    return True

def subspaces_of_dim(p, n, k, nums):
    """nums: list of nonzero vectors as tuples. Enumerate k-spaces via
    independent k-tuples with canonical span key."""
    zero = tuple([0]*n)
    found = {}
    for tup in itertools.combinations(nums, k):
        if not indep(p, tup, zero):
            continue
        S = span(p, list(tup), zero)
        assert len(S) == p**k
        found.setdefault(S, tup)
    return list(found)

def run(p, n, name):
    nums = [v for v in itertools.product(range(p), repeat=n) if any(v)]
    to_idx = {v: i+1 for i, v in enumerate(nums)}  # 1-based; 0 = zero
    zero = tuple([0]*n)
    ranks = {}
    for k in range(n+1):
        if k == 0:
            ranks[0] = [frozenset([zero])]
        elif k == n:
            ranks[n] = [frozenset([zero]+nums)]
        else:
            ranks[k] = subspaces_of_dim(p, n, k, nums)
        g = gauss(p, n, k)
        assert len(ranks[k]) == g, f"rank {k}: {len(ranks[k])} != gauss {g}"
    mid = n//2
    W = gauss(p, n, mid)
    wit = ranks[mid]
    # pairwise incomparability (equal dimension => automatic, but check)
    for a in range(len(wit)):
        for b in range(a+1, len(wit)):
            assert not (wit[a] < wit[b]) and not (wit[b] < wit[a])
    # every subspace comparable structure sanity: chain through ranks exists
    N = p**n
    cd_size = sum(gauss(p, n, k) for k in range(n+1))
    # encode members as sorted index lists
    enc = lambda S: sorted([0]+[to_idx[v] for v in S if v != zero])
    return {
        "group": name, "family": "vspace", "n": N,
        "abelian_theorem": True,
        "m": N*N,
        "cd_size": cd_size,
        "nsub": cd_size,
        "cd_subgroup": [0],
        "width": W,
        "width_rank": mid,
        "rank_sizes": [len(ranks[k]) for k in range(n+1)],
        "gauss_sizes": [gauss(p, n, k) for k in range(n+1)],
        "width_witness": [enc(S) for S in wit],
        "is_chain": cd_size <= 2,
        "is_quasi_antichain": False,
        "note": "CD = full subgroup lattice by abelian theorem; width by Sperner + explicit middle-rank witness",
    }

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    rd = os.path.join(here, "results")
    os.makedirs(rd, exist_ok=True)
    which = sys.argv[1] if len(sys.argv) > 1 else "ALL"
    jobs = {"C2x6": (2, 6), "C3x4": (3, 4)}
    for name, (p, n) in jobs.items():
        if which != "ALL" and which != name:
            continue
        import time
        t0 = time.time()
        r = run(p, n, name)
        r["time_s"] = round(time.time()-t0, 2)
        with open(os.path.join(rd, name + ".json"), "w") as f:
            json.dump(r, f)
        print(f"{name}: nsub={r['nsub']} m={r['m']} width={r['width']} "
              f"ranks={r['rank_sizes']} t={r['time_s']}s", flush=True)
