"""Myhill-Nerode state-complexity lower bound for insertion-encoding DFAs of
Av(4231,3124) and Av(4231,3214).

For max-insertion languages, two permutations share an IE-state only if their
future extension languages agree; in particular the depth-2 signature
(#children, #grandchildren) must agree. Distinct (e1,e2) signatures among
n-avoiders hence lower-bound the number of DFA states. We also count distinct
length<=3 occurrence profiles to show coarse profiles saturate while true
state complexity grows.

Run: python3 sig_complexity.py  (takes a few minutes; prints table)
"""
from itertools import combinations
from collections import defaultdict

def pat_of(seq):
    order = sorted(range(len(seq)), key=lambda t: seq[t])
    rank = [0] * len(seq)
    for r, t in enumerate(order):
        rank[t] = r + 1
    return tuple(rank)

def bases(which):
    return {(4, 2, 3, 1), (3, 1, 2, 4)} if which == 'A' else {(4, 2, 3, 1), (3, 2, 1, 4)}

def avoids(p, F):
    n = len(p)
    if n < 4:
        return True
    return not any(pat_of([p[i] for i in idx]) in F
                   for idx in combinations(range(n), 4))

def kids(p, F):
    n = len(p)
    out = []
    for x in range(n + 1):
        c = p[:x] + (n + 1,) + p[x:]
        if avoids(c, F):
            out.append(c)
    return out

def prof3(p):
    s = set()
    for L in (1, 2, 3):
        for idx in combinations(range(len(p)), L):
            s.add(pat_of([p[i] for i in idx]))
    return frozenset(s)

def main():
    print("which,n,perms,distinct_sig2,distinct_prof3")
    for which in ['A', 'B']:
        F = bases(which)
        live = [()]
        for m in range(1, 9):
            new = []
            for q in live:
                for x in range(m):
                    c = q[:x] + (m,) + q[x:]
                    if avoids(c, F):
                        new.append(c)
            live = new
            if m >= 5:
                S2, P = set(), set()
                for p in live:
                    k1 = kids(p, F)
                    S2.add((len(k1), sum(len(kids(c, F)) for c in k1)))
                    P.add(prof3(p))
                print(f"{which},{m},{len(live)},{len(S2)},{len(P)}", flush=True)

if __name__ == '__main__':
    main()
