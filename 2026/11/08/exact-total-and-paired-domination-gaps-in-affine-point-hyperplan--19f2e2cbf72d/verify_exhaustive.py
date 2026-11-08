#!/usr/bin/env python3
"""Independent direct exhaustive minimization in small affine point-line incidence graphs."""
from itertools import product,combinations

def experiment(q):
    pts=list(product(range(q), repeat=2))
    lines=[]
    for slope in range(q):
        for intercept in range(q):
            lines.append({i for i,(x,y) in enumerate(pts) if (y-slope*x)%q==intercept})
    for x in range(q):
        lines.append({i for i,(a,b) in enumerate(pts) if a==x})
    V=q*q+len(lines)
    adj=[0]*V
    for j,ll in enumerate(lines):
        for i in ll:
            adj[i]|=1<<(q*q+j);adj[q*q+j]|=1<<i
    def total(S):
        return all(adj[i]&S for i in range(V))
    def has_pm(S):
        def solve(R):
            if not R:return True
            i=(R&-R).bit_length()-1
            for j in range(V):
                if (R>>j)&1 and (adj[i]>>j)&1 and solve(R^(1<<i)^(1<<j)):
                    return True
            return False
        return solve(S)
    min_total=None; total_count=0; min_paired=None; paired_count=0
    # Direct point-line subset enumeration for total, balanced subsets for paired.
    for size in range(1, 2*(2*q-1)+1):
        cnt_t=0;cnt_p=0
        for pcount in range(max(0,size-len(lines)),min(q*q,size)+1):
            lcount=size-pcount
            # At least one vertex from each side is necessary.
            if pcount==0 or lcount==0:continue
            for pp in combinations(range(q*q),pcount):
                pb=sum(1<<v for v in pp)
                for ll in combinations(range(len(lines)),lcount):
                    s=pb|sum(1<<(q*q+v) for v in ll)
                    if total(s):
                        cnt_t+=1
                        if size%2==0 and pcount==lcount and has_pm(s):cnt_p+=1
        if min_total is None and cnt_t:
            min_total=size;total_count=cnt_t
        if min_paired is None and cnt_p:
            min_paired=size;paired_count=cnt_p
        if min_total is not None and min_paired is not None:break
    expected_total=(3*q-1)
    expected_paired=(4*q-2)
    assert min_total==expected_total and min_paired==expected_paired
    print(f'q={q} total={min_total} total_witness_count={total_count} paired={min_paired} paired_witness_count={paired_count} PASS')
for q in [2,3]: experiment(q)
print('EXHAUSTIVE_CHECKS_PASS')
