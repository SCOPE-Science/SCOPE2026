"""Independent exact Gaussian-integer and Walsh tensor transforms of proper colourings."""
from collections import Counter
from itertools import product

def times(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def plus(a,b): return (a[0]+b[0],a[1]+b[1])

def transform(n, edges, group):
    dims=4**n
    f=[(0,0)]*dims
    for x in product(range(4),repeat=n):
        if all(x[u]!=x[v] for u,v in edges):
            i=sum(x[k]*4**k for k in range(n));f[i]=(1,0)
    if group=='cyclic':
        base=[[(1,0),(1,0),(1,0),(1,0)],
              [(1,0),(0,1),(-1,0),(0,-1)],
              [(1,0),(-1,0),(1,0),(-1,0)],
              [(1,0),(0,-1),(-1,0),(0,1)]]
    else:
        base=[[(1,0) if (bin(a&b).count('1')%2==0) else (-1,0) for b in range(4)] for a in range(4)]
    for ax in range(n):
        gap=4**ax
        f2=f.copy()
        for start in range(0,dims,4*gap):
            for offset in range(gap):
                vals=[f[start+offset+t*gap] for t in range(4)]
                for a in range(4):
                    total=(0,0)
                    for t in range(4): total=plus(total,times(base[a][t],vals[t]))
                    f2[start+offset+a*gap]=total
        f=f2
    assert all(im==0 for re,im in f)
    return Counter(z[0] for z in f)

def cychist(q,n):
    c=Counter()
    for tail in product(range(q),repeat=n-1):
        nums=Counter((0,)+tail)
        c[((-1)**n*sum((1-q)**nums[a] for a in range(q)))//q]+=1
    return c

def mult(h,k):
    d=Counter()
    for a,x in h.items():
        for b,y in k.items():d[a*b]+=x*y
    return d

def predicted(n, cycle_lengths):
    h=Counter({1:1})
    for x in cycle_lengths:h=mult(h,cychist(4,x))
    ans=Counter({4*k:v for k,v in h.items()})
    ans[0]+=4**n-4**(n-1)
    return ans

for n,edges,cycles in [
    (6,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,5),(5,0)],[3,4]),
    (7,[(0,1),(1,2),(2,3),(3,0),(0,4),(4,5),(5,6),(6,0)],[4,4]),
]:
    pred=predicted(n,cycles)
    for group in ('cyclic','klein'):
        h=transform(n,edges,group)
        assert h==pred,(n,group,h,pred)
        print('verified',group,'vertices',n,'nonzero',sum(c for z,c in h.items() if z!=0),'zeros',h[0],'PASS')
