#!/usr/bin/env python3
"""Direct exact matching-count enumeration versus independent run formulas."""
from collections import Counter
from math import comb
from functools import lru_cache


def literal_graph(n):
    # hub is vertex n
    adj=[set() for _ in range(n+1)]
    for a in range(n):
        for b in ((a+1)%n,n):
            adj[a].add(b); adj[b].add(a)
    return adj


def matching_count(adj, mask):
    @lru_cache(None)
    def f(m):
        if not m: return 1
        v=(m & -m).bit_length()-1
        rem=m & ~(1<<v)
        return sum(f(rem & ~(1<<w)) for w in adj[v] if (rem>>w)&1)
    return f(mask)


def brute(n):
    adj=literal_graph(n); ans=Counter()
    for mask in range(1,1<<(n+1)):
        if mask.bit_count()%2: continue
        if any(not ((mask>>v)&1) and not any((mask>>w)&1 for w in adj[v]) for v in range(n+1)): continue
        mm=matching_count(adj,mask)
        if mm: ans[(mask.bit_count(),mm)]+=1
    return ans


def formula(n):
    out=Counter()
    # full rim and hub-containing full rim
    if n%2==0: out[(n,2)]+=1
    else: out[(n+1,n)]+=1
    # direct run generation, different from graph-level pair counting
    # one positive even run followed by one or two omitted vertices (proper hub-free)
    def Q(s,z):
        if s==0:
            if z==0: return 1
            return 0
        if s<0 or z<0:return 0
        # s runs, sum of half-selected lengths = z; zero-gap sum n-2z
        N=n-2*z
        if N<s or N>2*s or z<s: return 0
        return n*comb(z-1,s-1)*comb(s,N-s)//s # each /s divisible only AFTER multiplication
    for z in range(1,n//2+1):
        for s in range(1,z+1):
            # use exact rational to avoid floor for each term
            N=n-2*z
            if s<=N<=2*s:
                val=n*comb(z-1,s-1)*comb(s,N-s)
                assert val%s==0
                out[(2*z,1)]+=val//s
    # hub-present: unique odd run 2a+1, a+1 matchings; s extra even runs
    # s extra runs with total half lengths k>=s; zero gaps s+1, total zero N>=s+1
    for a in range((n-2)//2+1):
        mu=a+1
        for s in range(0,n//2+1):
            for k in range(s,n//2+1):
                if s==0 and k>0: continue
                if s>0 and k==0: continue
                N=n-(2*a+1)-2*k
                if N<s+1:continue
                ways_even=1 if s==0 else comb(k-1,s-1)
                ways_zero=comb(N-1,s)
                out[(2+2*a+2*k,mu)] += n*ways_even*ways_zero
    return +out

if __name__=='__main__':
    totals=[]
    for n in range(3,16):
        b=brute(n); f=formula(n)
        if b!=f:
            print('MISMATCH',n, 'missing',b-f,'excess',f-b)
            raise SystemExit(1)
        totals.append(sum(b.values()))
    print('VERIFY_OK wheel_rim_n=3..15 all_nonempty_vertex_masks_scanned=131043 matches_direct_perfect_matching_count_to_run_formula=PASS')
    print('matching_set_totals='+str(totals))
    print('n=10 multiplicity_distribution='+str(dict(sorted(Counter({m:sum(v for (s,mm),v in brute(10).items() if m==mm) for (s,m) in brute(10)}).items()))))
