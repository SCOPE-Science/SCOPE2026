"""Standalone checks for exact min-plus ranks of Hamming spheres and balls.

All computations use integers. Finite tests complement, but do not replace,
the parametric proof in RESULT.md.
"""
from itertools import combinations, permutations, product


def hinge(s, r):
    return max(0, s - r)


def vshape(s, r):
    return abs(s - r)


def target(l, t, r):
    return 1 + min(l, t, r, l + t - r)


def rank_tropical(a):
    n, m = len(a), len(a[0])
    for size in range(min(n, m), 0, -1):
        for ii in combinations(range(n), size):
            for jj in combinations(range(m), size):
                best, multiplicity = None, 0
                for sig in permutations(range(size)):
                    val = sum(a[ii[i]][jj[sig[i]]] for i in range(size))
                    if best is None or val < best:
                        best, multiplicity = val, 1
                    elif val == best:
                        multiplicity += 1
                if multiplicity == 1:
                    return size
    return 0


def matrix_terms(l, t, r, fun):
    lo, hi = max(0, r-t), min(l, r)
    reps = range(lo, hi+1)
    large = l+t+5
    def u(p, a):
        if p < lo and a == lo:
            return lo-p if fun is vshape else 0
        if lo <= p <= hi and a == p:
            return 0
        if p > hi and a == hi:
            return p-hi
        return large
    def v(q, a):
        return fun(a+q,r)
    return reps, u, v


def word_weight(s):
    return sum(x != 0 for x in s)


def direct_distance(s, words):
    return min(sum(x!=y for x,y in zip(s,c)) for c in words)


stats = {"param_cases":0, "entry_checks":0, "full_decoding_checks":0,
         "tropical_rank_checks":0, "tropical_nonsingular_witness_checks":0}
for l in range(0, 6):
    for t in range(0, 6):
        for r in range(0, l+t+1):
            k=target(l,t,r)
            for f in (hinge,vshape):
                stats["param_cases"]+=1
                reps,u,v = matrix_terms(l,t,r,f)
                assert len(reps) == k
                A=[[f(p+q,r) for q in range(t+1)] for p in range(l+1)]
                for p in range(l+1):
                    for q in range(t+1):
                        assert A[p][q] == min(u(p,a)+v(q,a) for a in reps)
                        stats["entry_checks"] += 1
                chosen=list(reps)
                sub=[[f(p+r-z,r) for z in chosen] for p in chosen]
                assert len(sub)==k and all(sub[i][i]==0 for i in range(k))
                for sig in permutations(range(k)):
                    val=sum(sub[i][sig[i]] for i in range(k))
                    assert (val==0) == (sig==tuple(range(k)))
                    stats["tropical_nonsingular_witness_checks"] += 1
                if l+t<=6:
                    assert rank_tropical(A)==k
                    stats["tropical_rank_checks"] += 1

# Independence: exhaustive nearest-neighbour distance, not just the
# radial closed formula, for q-ary alphabets and small full lengths.
for alphabet in (2, 3, 4):
    max_size={2:6,3:4,4:3}[alphabet]
    for n in range(max_size+1):
        universe=list(product(range(alphabet),repeat=n))
        for r in range(n+1):
            sphere=[c for c in universe if word_weight(c)==r]
            ball=[c for c in universe if word_weight(c)<=r]
            for w in universe:
                assert direct_distance(w,sphere)==vshape(word_weight(w),r)
                assert direct_distance(w,ball)==hinge(word_weight(w),r)
                stats["full_decoding_checks"] += 2

assert target(2, 2, 2) == 3
print("VERIFY_OK", stats)
