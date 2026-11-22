"""Finite checks for prescribed graphical-cycle Lie-bracket fibers."""
from itertools import product
from collections import Counter

def formula(n,q,mask):
    E=[(i,(i+1)%n) for i in range(n)]
    forced={v for i,(u,v) in enumerate(E) if mask>>i&1 for v in (u,v)}
    ans=0
    for zeros in range(1<<n):
        if any(zeros>>v&1 for v in forced):continue
        surviving=[i for i in range(n) if not (zeros>>i&1)]
        p=list(range(n))
        def find(x):
            while p[x]!=x:x=p[x]
            return x
        def union(a,b):p[find(a)]=find(b)
        for i,(u,v) in enumerate(E):
            if not(mask>>i&1) and u in surviving and v in surviving:union(u,v)
        classes={find(v) for v in surviving}
        cp={a:j for j,a in enumerate(sorted(classes))}
        edges=set(); bad=False
        for i,(u,v) in enumerate(E):
            if mask>>i&1:
                a,b=cp[find(u)],cp[find(v)]
                if a==b:bad=True;break
                edges.add(tuple(sorted((a,b))))
        if bad:continue
        k=len(classes)
        colorings=0
        for cs in product(range(q+1),repeat=k):
            if all(cs[a]!=cs[b] for a,b in edges):colorings+=1
        ans+=(q-1)**len(surviving)*colorings
    assert ans%(q-1)**mask.bit_count()==0
    return ans//(q-1)**mask.bit_count()

def direct(n,q):
    vec=list(product(range(q),repeat=2)); counts=Counter()
    for vs in product(vec,repeat=n):
        cc=tuple((vs[i][0]*vs[(i+1)%n][1]-vs[i][1]*vs[(i+1)%n][0])%q for i in range(n))
        counts[cc]+=1
    assert sum(counts.values())==q**(2*n)
    mask_counts={}
    for c,num in counts.items():
        mask=sum((1<<i) for i,x in enumerate(c) if x)
        if mask in mask_counts: assert mask_counts[mask]==num,(n,q,mask,mask_counts[mask],num)
        else:mask_counts[mask]=num
    for mask in range(1<<n):
        expected=formula(n,q,mask)
        got=mask_counts.get(mask,0)
        assert expected==got,(n,q,mask,expected,got)
    assert counts[(1,)*n]==q**n-q
    return len(counts), len(mask_counts), counts[(1,)*n]
if __name__=='__main__':
    for n,q in [(3,2),(3,3),(3,5),(5,2),(5,3),(7,2),(9,2)]:
        a,b,c=direct(n,q)
        print('PASS',n,q,'reachable_targets',a,'support_masks',b,'full_support_fiber',c,flush=True)
    print('ODD_CYCLE_ALL_FIBERS_CHECKED')
