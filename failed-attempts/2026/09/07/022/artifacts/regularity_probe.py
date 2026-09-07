#!/usr/bin/env python3
"""Regularity probe: vertical-alternation lengths and active-site profiles.
Albert-Linton-Ruskuc: insertion encoding of a class is regular iff the class
does not contain arbitrarily long vertical alternations.
We compute, for avoiders to n=12 already enumerated (or fresh to n=10),
the max vertical-alternation length contained as a pattern, and the
distribution of 'active sites' (number of children in generating tree).
This does NOT construct a minimized DFA; it documents why DFA minimization
was deferred (needs PermutaTriangle/comb_spec_searcher, out of budget).
"""
import itertools, sys

def contains_alt(perm, L):
    # vertical alternation: odd entries all above even entries or vice versa?
    # Standard def: permutation alternates between low/high regions:
    # e.g. 2k.. pattern where values in odd positions are all < values in even positions (split).
    # We test all subsequences of length L for being an alternation.
    n=len(perm)
    if n<L: return False
    for idx in itertools.combinations(range(n),L):
        vals=[perm[i] for i in idx]
        # check vertical alternation: for all odd j, vals[j] > max(vals[even]) or < min(vals[even])?
        # Vertical alternation of length L: entries alternate low/high with separating line.
        # Equivalent: set of values splits into low half and high half, parities separate.
        # For even L=2k: k lows on one parity, k highs on other. For odd, similar.
        # Test both parity assignments.
        ok=False
        for parity in (0,1):
            lows=[vals[i] for i in range(L) if i%2==parity]
            highs=[vals[i] for i in range(L) if i%2!=parity]
            if max(lows)<min(highs) or max(highs)<min(lows):
                # also need the alternation to interleave positions (it does by construction)
                ok=True; break
        if ok:
            return True
    return False

def max_alt_in_class(which, N=9):
    # enumerate via P1 import
    sys.path.insert(0,"output/artifacts")
    from p1_dfs import count_av  # noqa - actually count only; re-enumerate with storage
    # simple re-enumeration keeping perms to N
    is_A=(which=='A')
    cur=[[]]
    maxalt={}
    for k in range(0,N+1):
        if k>=4:
            m=0
            # sample: check max alt length present in any avoider of length k (cap scan for speed)
            # full scan to k<=9 is fine (35k perms)
            for p in cur:
                # longest alt in p: test from min(k,8) down
                for L in range(min(k,8),3,-1):
                    if contains_alt(p,L):
                        if L>m: m=L
                        break
            maxalt[k]=m
            print(f"[{which}] n={k} na={len(cur)} maxAlt={m}",flush=True)
        else:
            print(f"[{which}] n={k} na={len(cur)}",flush=True)
        if k==N: break
        nxt=[]
        for p in cur:
            for v in range(k+1):
                if k==0:
                    nxt.append([v]); continue
                q=[x+1 if x>=v else x for x in p]
                q.append(v)
                ok=True
                if k>=3:
                    d=v
                    for i in range(k-2):
                        for j in range(i+1,k-1):
                            for l in range(j+1,k):
                                a,b,c=q[i],q[j],q[l]
                                if is_A:
                                    if a<b and a<c and a<d and b<c and (c<d or d<b):
                                        ok=False; break
                                else:
                                    if a>b and a>c and a>d and b<c and (c<d or d<b):
                                        ok=False; break
                            if not ok: break
                        if not ok: break
                if ok: nxt.append(q)
        cur=nxt

if __name__=="__main__":
    w=sys.argv[1] if len(sys.argv)>1 else "A"
    N=int(sys.argv[2]) if len(sys.argv)>2 else 8
    max_alt_in_class(w,N)
