"""Exact count of connected outer-EF1 allocations on complete bipartite graphs.

Public reproducibility code. Python 3 standard library only.
Each agent receives a nonempty connected bundle; all vertices allocated.
All agents share the same binary additive valuation.
"""
from functools import lru_cache
from itertools import product
from math import comb, factorial


def connected(v):
    # counts (A+, A0, B+, B0)
    sa=v[0]+v[1]; sb=v[2]+v[3]
    return sa+sb==1 or (sa>0 and sb>0)


def removable_positive(v):
    sa=v[0]+v[1]; sb=v[2]+v[3]
    if sa+sb==1:
        return v[0]+v[2]==1
    return ((v[0]>0 and (sa>=2 or sb==1)) or
            (v[2]>0 and (sb>=2 or sa==1)))


def exact_count(counts,k):
    """Number of allocations to k labeled nonempty bundles, exact integer."""
    assert len(counts)==4 and all(isinstance(x,int) and x>=0 for x in counts)
    n=sum(counts)
    assert counts[0]+counts[1]>0 and counts[2]+counts[3]>0 and 1<=k<=n
    nt=counts[0]+counts[2]
    # enumerate all possible local bundle profiles, with combinatorial labels handled later
    possible=[]
    for t in product(*(range(a+1) for a in counts)):
        if sum(t) and connected(t):
            possible.append((t,t[0]+t[2],removable_positive(t)))
    @lru_cache(None)
    def rec(rem, agents_left, low, seen_low):
        if agents_left==0:
            return int(all(v==0 for v in rem) and seen_low)
        s=0
        for b,val,outer in possible:
            if val not in (low,low+1) or (val==low+1 and not outer):
                continue
            if any(x>y for x,y in zip(b,rem)):continue
            multiplicity=1
            for x,y in zip(b,rem):multiplicity*=comb(y,x)
            rr=tuple(x-y for x,y in zip(rem,b))
            s+=multiplicity*rec(rr,agents_left-1,low,seen_low or val==low)
        return s
    return sum(rec(counts,k,h,False) for h in range(nt+1))


def direct_count(counts,k):
    """Completely independent per-labeled-vertex exhaustive verifier."""
    n=sum(counts)
    colors=[(0,1)]*counts[0]+[(0,0)]*counts[1]+[(1,1)]*counts[2]+[(1,0)]*counts[3]
    ans=0
    for alloc in product(range(k),repeat=n):
        blocks=[[idx for idx,x in enumerate(alloc) if x==j] for j in range(k)]
        if any(not z for z in blocks):continue
        if any(len(z)>1 and len(set(colors[i][0] for i in z))==1 for z in blocks):continue
        vals=[sum(colors[i][1] for i in z) for z in blocks]
        if max(vals)-min(vals)>1:continue
        if max(vals)==min(vals):ans+=1;continue
        low=min(vals);good=True
        for z,v in zip(blocks,vals):
            if v==low:continue
            can=False
            for i in z:
                if not colors[i][1]:continue
                zz=[j for j in z if j!=i]
                if len(zz)<=1 or len(set(colors[j][0] for j in zz))>1:
                    can=True;break
            if not can:good=False;break
        ans+=good
    return ans


def unit_formula(a,b,k):
    # coefficient H_q^(k-r) H_(q+1)^r by truncated polynomial multiplication
    n=a+b;q,r=divmod(n,k)
    def hd(d):
        if d==1:return [1,1]
        return [0]+[comb(d,j) for j in range(1,d)]+[0]
    poly=[1]
    for d in [q]*(k-r)+[q+1]*r:
        new=[0]*min(a+1,len(poly)+d)
        for i,v in enumerate(poly):
            for j,w in enumerate(hd(d)):
                if i+j<len(new):new[i+j]+=v*w
        poly=new
    coef=poly[a] if a<len(poly) else 0
    den=factorial(q)**(k-r)*factorial(q+1)**r
    val=comb(k,r)*factorial(a)*factorial(b)*coef
    assert val%den==0
    return val//den


def run():
    comparisons=0
    for a in range(1,4):
        for b in range(1,4):
            n=a+b
            for plus_a in range(a+1):
                for plus_b in range(b+1):
                    counts=(plus_a,a-plus_a,plus_b,b-plus_b)
                    for k in range(1,min(n,4)+1):
                        got=exact_count(counts,k)
                        expected=direct_count(counts,k)
                        assert got==expected,(counts,k,got,expected)
                        comparisons+=1
    extra=0
    for a in range(1,7):
        for b in range(1,7):
            for k in range(1,a+b+1):
                want=unit_formula(a,b,k)
                got=exact_count((a,0,b,0),k)
                pred=(k<=min(a,b) or k>=max(a,b))
                assert got==want,(a,b,k,got,want)
                assert (got>0)==pred,(a,b,k,got,pred)
                extra+=1
    sufficient=0
    for a in range(1,6):
        for b in range(a,6):
            for pa in range(a+1):
                for pb in range(b+1):
                    for k in range(1,a+b+1):
                        if k<=a or k>=b:
                            assert exact_count((pa,a-pa,pb,b-pb),k)>0
                            sufficient+=1
    print('PASS',comparisons,'independent exhaustive comparisons;',extra,'unit-count and threshold comparisons;',sufficient,'binary universal-existence checks')
    for a,b in [(2,4),(3,7),(4,4)]:
        print('unit K_%d,%d:'%(a,b),[(k,unit_formula(a,b,k)) for k in range(1,a+b+1)])

if __name__=='__main__':run()
