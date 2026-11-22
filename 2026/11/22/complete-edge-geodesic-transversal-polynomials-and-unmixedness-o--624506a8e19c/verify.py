"""Independent exhaustive check of edge-geodesic-transversal matching-block characterization."""
from itertools import combinations, product
from math import comb, factorial
from collections import Counter

def graph(parts):
    labels=[i for i,n in enumerate(parts) for _ in range(n)]
    v=len(labels)
    edges=[(i,j) for i in range(v) for j in range(i+1,v) if labels[i]!=labels[j]]
    return labels,edges

def direct_geodesics(labels,edges):
    v=len(labels); E=set(edges)
    paths=[]
    # diameter <= 2 for connected complete multipartite with r>=2.
    for a,b in edges:
        if labels.count(labels[a])==1 and labels.count(labels[b])==1:
            paths.append({(a,b)})
    for a,b in combinations(range(v),2):
        if labels[a]!=labels[b]:continue
        for x in range(v):
            if labels[x]==labels[a]:continue
            paths.append({tuple(sorted((a,x))),tuple(sorted((b,x)))})
    return paths

def independent_block(labels, edges, omitted):
    for u,v in omitted:
        if labels.count(labels[u])==labels.count(labels[v])==1:
            return False
    for (a,b),(c,d) in combinations(omitted,2):
        if a==c or a==d or b==c or b==d:
            # both unselected cross edges belong to the SAME pair of parts
            if {labels[a],labels[b]}=={labels[c],labels[d]}:
                return False
    return True

def expected_poly(parts):
    ans={0:1}
    for i,j in combinations(range(len(parts)),2):
        a,b=parts[i],parts[j]
        if a==b==1: fac={1:1}
        else: fac={a*b-k:comb(a,k)*comb(b,k)*factorial(k) for k in range(min(a,b)+1)}
        tmp=Counter()
        for x,y in ans.items():
            for w,z in fac.items():tmp[x+w]+=y*z
        ans=dict(tmp)
    return ans

def audit(parts):
    labels,edges=graph(parts); P=direct_geodesics(labels,edges); m=len(edges)
    cnt=Counter(); min_sets=[]; inclusion_min=[]
    for mask in range(1<<m):
        S={edges[k] for k in range(m) if mask>>k&1}
        good=all(S&x for x in P)
        omission=set(edges)-S
        assert good==independent_block(labels,edges,omission),(parts,mask)
        if good:
            cnt[len(S)]+=1
            if all(not all((S-{e})&x for x in P) for e in S):inclusion_min.append(mask)
    assert dict(cnt)==expected_poly(parts),(parts,cnt,expected_poly(parts))
    low=min(cnt)
    assert len(inclusion_min)==cnt[low] and all(mask.bit_count()==low for mask in inclusion_min)
    return (parts,m,len(P),sum(cnt.values()),low,cnt[low],len(inclusion_min))

if __name__=='__main__':
    for parts in [(1,1),(1,2),(1,1,2),(1,2,2),(1,2,3),(2,2),(2,3),(2,2,2),(1,1,1,2)]:
        print('EXHAUSTIVE',*audit(parts))
    print('VERIFY_OK')
