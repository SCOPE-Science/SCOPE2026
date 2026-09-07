"""Method A: max-insertion generating tree, independent checker via direct comparisons.
Stdlib only. Usage: python3 methodA.py [shard_start shard_end] or all.
Writes work/countsA.json when run as driver.
"""
import itertools, json, sys, time

def contains_with_newmax(child, pos_new, p1, p2):
    # child: tuple length n, pos_new: index of value n (the max)
    # Only check quadruples containing pos_new. Independent impl: direct rank via counts.
    n = len(child)
    if n < 4:
        return False
    # iterate triples of other positions
    others = [i for i in range(n) if i != pos_new]
    # triple nested loops
    L = len(others)
    for a in range(L):
        for b in range(a+1, L):
            for c in range(b+1, L):
                idx = sorted([others[a], others[b], others[c], pos_new])
                i1,i2,i3,i4 = idx
                v1,v2,v3,v4 = child[i1],child[i2],child[i3],child[i4]
                # rank via counting greater (python comparisons, no sort/table)
                r1 = 1+(v1>v2)+(v1>v3)+(v1>v4)
                r2 = 1+(v2>v1)+(v2>v3)+(v2>v4)
                r3 = 1+(v3>v1)+(v3>v2)+(v3>v4)
                r4 = 1+(v4>v1)+(v4>v2)+(v4>v3)
                # need careful: (v1>v2) is bool->int; rank = 1 + #smaller
                # Actually #smaller = sum(v1>v? no: v1>v2 means v2 smaller, count it)
                # so above is correct.
                if (r1,r2,r3,r4)==p1 or (r1,r2,r3,r4)==p2:
                    return True
    return False

def count_pair_A(p1, p2, nmax=9):
    # returns list a[0..nmax], profiles dict n -> {nsites: freq}
    Av = [()]  # Av_{0}
    counts = [1]  # a0
    profiles = {}
    # handle n=0 already; iterate n=1..nmax
    # Av holds perms of current length n-1
    for n in range(1, nmax+1):
        if n < 4:
            # all insertions avoid; Av_n size = n!
            import math
            # generate explicitly for next iteration (small)
            newAv = []
            for par in Av:
                for pos in range(n):
                    child = par[:pos]+(n,)+par[pos:]
                    newAv.append(child)
            Av = newAv
            counts.append(len(Av))
            # profile: each parent has n active sites
            profiles[n] = {n: len(Av)//n if Av else 0}
            continue
        newAv = []
        prof = {}
        for par in Av:
            nsites = 0
            for pos in range(n):
                child = par[:pos]+(n,)+par[pos:]
                if not contains_with_newmax(child, pos, p1, p2):
                    newAv.append(child)
                    nsites += 1
            prof[nsites] = prof.get(nsites, 0)+1
        Av = newAv
        counts.append(len(Av))
        profiles[n] = prof
    return counts, profiles

if __name__ == "__main__":
    # quick self-test on target pair to n=8
    t0=time.time()
    c,pr = count_pair_A((1,3,4,2),(2,1,4,3),8)
    print(c, f"{time.time()-t0:.2f}s")
    print(pr)
