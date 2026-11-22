"""Exact finite checks for the fixed-set partial-transformation idempotent theorem.
Use Python 3.10 or later; no external dependencies.
"""
from itertools import product, permutations
from collections import Counter
from math import factorial, comb


def partition_profiles(b, a):
    """Generate (rank, stabilizer, signature) of all abstract unit-conjugacy classes."""
    def multiset_parts(rem, minimum=1):
        yield ()
        for first in range(minimum, rem + 1):
            for rest in multiset_parts(rem - first, first):
                yield (first,) + rest

    for active_mask in product((False, True), repeat=a):
        active = tuple(y for y, yes in enumerate(active_mask) if yes)
        for leaves in product(range(b + 1), repeat=len(active)):
            used = sum(leaves)
            if used > b:
                continue
            for parts in multiset_parts(b - used):
                size = used + sum(parts)
                idle = b - size
                if idle < 0:
                    continue
                counts = Counter(parts)
                stabilizer = factorial(idle)
                for l in leaves:
                    stabilizer *= factorial(l)
                for m, t in counts.items():
                    stabilizer *= factorial(m - 1) ** t * factorial(t)
                signature = (active, leaves, parts, idle)
                yield (len(active) + len(parts), stabilizer, signature)


def profile_of(f, a, b):
    n = a + b
    image = {x for x in f if x >= 0}
    assert all(f[x] == x for x in image)
    active = tuple(y for y in range(a) if f[y] >= 0)
    leaves = tuple(sum(1 for z in range(a,n) if f[z] == y) for y in active)
    parts = tuple(sorted(1 + sum(1 for z in range(a,n) if z != root and f[z] == root)
                         for root in sorted(image) if root >= a))
    idle = sum(f[z] < 0 for z in range(a,n))
    return (active, leaves, parts, idle)


def brute(a, b):
    n = a + b
    pred = list(partition_profiles(b, a))
    pred_signatures = {x[2] for x in pred}
    assert len(pred) == len(pred_signatures)
    choices = [[-1, y] for y in range(a)] + [[-1, *range(n)] for _ in range(b)]
    labeled_by_rank = Counter()
    by_sign = Counter()
    by_sign_rank = {}
    all_maps = []
    for tup in product(*choices):
        if any(tup[x] < 0 or tup[x] != x for x in (v for v in tup if v >= 0)):
            continue
        s = profile_of(tup, a, b)
        by_sign[s] += 1
        rank = len({x for x in tup if x >= 0})
        by_sign_rank[s] = rank
        labeled_by_rank[rank] += 1
        all_maps.append(tup)
    assert set(by_sign) == pred_signatures, (a, b, set(by_sign)^pred_signatures)
    for r, stab, sign in pred:
        assert by_sign[sign] == factorial(b)//stab, (a,b,r,stab,sign,by_sign[sign])
        assert by_sign_rank[sign] == r
    for r in range(a+b+1):
        expected = sum(comb(a,j)*comb(b,r-j)*(r+1)**(b-r+j)
                       for j in range(max(0,r-b),min(a,r)+1))
        assert labeled_by_rank[r] == expected, (a,b,r,labeled_by_rank[r],expected)
    if b <= 4:
        # Independently recompute actual orbits under all units (permutations of free points).
        seen = set()
        ranks = Counter()
        for f in all_maps:
            if f in seen: continue
            orbit = set()
            for q in permutations(range(a,n)):
                sigma = tuple(range(a))+q
                inv = [0]*n
                for i,v in enumerate(sigma): inv[v]=i
                transformed = tuple(-1 if f[inv[x]] < 0 else sigma[f[inv[x]]] for x in range(n))
                orbit.add(transformed)
            assert len(orbit) == by_sign[profile_of(f,a,b)]
            assert all(profile_of(g,a,b)==profile_of(f,a,b) for g in orbit)
            seen.update(orbit)
            ranks[len({x for x in f if x>=0})] += 1
        assert len(seen) == len(all_maps)
        assert ranks == Counter(r for r,_,_ in pred)
    return len(pred), len(all_maps)


def classes_from_series(a,b):
    # Compute coefficients of (1-z)^(-1)*(1+1/(1-z))^a*prod(1-z^j)^(-1)
    arr=[1]+[0]*b
    for _ in range(a+1):
        nxt=[]
        for i in range(b+1): nxt.append(sum(arr[:i+1]))
        arr=nxt
    # multiply by (2-z)^a
    p=[sum(comb(a,j)*(-1)**j*2**(a-j)*arr[i-j] for j in range(min(a,i)+1)) for i in range(b+1)]
    # Euler partition product
    for j in range(1,b+1):
        for i in range(j,b+1): p[i]+=p[i-j]
    return p[b]

if __name__=='__main__':
    for a in range(0,4):
        for b in range(0,5):
            c, e = brute(a,b)
            assert c == classes_from_series(a,b)
            print(f'a={a} b={b} classes={c} labeled={e}')
    print('FIXED_POINT_PARTIAL_RETRACTION_ORBITS_VERIFIED')
