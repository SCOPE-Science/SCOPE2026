"""Exact incidence test for the type-D root-polytope illumination construction."""
from itertools import combinations, product

def vertices(n):
    for i,j in combinations(range(n),2):
        for a,b in product((-1,1),repeat=2):
            v=[0]*n;v[i]=a;v[j]=b
            yield tuple(v)

def directions(n):
    if n==3:
        return ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
    ans=[]
    for i in range(n):
        s=tuple(-1 if j<i else (n if j==i else 1) for j in range(n))
        for t in (-1,1):ans.append(tuple(t*x for x in s))
    return tuple(ans)

def illuminated(v,d):
    supp=[i for i,x in enumerate(v) if x]
    i,j=supp
    return v[i]*d[i]<0 and v[j]*d[j]<0 and -v[i]*d[i]-v[j]*d[j]>sum(abs(d[k]) for k in range(len(d)) if k not in supp)

for n in range(3,16):
    vv=list(vertices(n)); dd=directions(n)
    count=[sum(illuminated(v,d) for d in dd) for v in vv]
    assert all(x==1 for x in count),(n,{x:count.count(x) for x in set(count)})
    counts=[sum(illuminated(v,d) for v in vv) for d in dd]
    assert all(x==(3 if n==3 else n-1) for x in counts)
    print('n',n,'vertices',len(vv),'directions',len(dd),'exact_partition',True)
print('ROOT_FAMILY_EXACT_OK')
