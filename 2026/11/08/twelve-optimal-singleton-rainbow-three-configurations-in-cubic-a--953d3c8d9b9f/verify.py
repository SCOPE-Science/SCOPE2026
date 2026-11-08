"""Standalone checks for exact equality-level rainbow-3 configurations.
Uses graph neighborhoods, not the theorem's cyclic recurrence.
Usage: python verify.py
"""
from itertools import product, combinations, permutations


def prism(m):
    # vertices (row,index), encoded by row*m+index
    V=2*m
    adj=[set() for _ in range(V)]
    for r in (0,1):
        for i in range(m):
            x=r*m+i
            for y in (r*m+(i-1)%m, r*m+(i+1)%m, (1-r)*m+i):
                adj[x].add(y);adj[y].add(x)
    return adj


def mobius(n):
    adj=[set() for _ in range(n)]
    for i in range(n):
        for j in ((i-1)%n,(i+1)%n,(i+n//2)%n):
            adj[i].add(j); adj[j].add(i)
    return adj


def valid(adj,f):
    return all(f[v]!=0 or {f[u] for u in adj[v]} >= {1,2,3} for v in range(len(f)))


def count_on_bipartitions(adj):
    n=len(adj)
    color=[-1]*n
    for start in range(n):
        if color[start]>=0:continue
        color[start]=0;pending=[start]
        while pending:
            v=pending.pop()
            for u in adj[v]:
                if color[u]<0:color[u]=1-color[v];pending.append(u)
                else:assert color[u]!=color[v]
    counts=[]; witnesses=[]
    for parity in (0,1):
        side=[i for i,x in enumerate(color) if x==parity]
        assert len(side)==n//2
        comp=[i for i in range(n) if color[i]!=parity]
        ct=0; ex=None
        f=[0]*n
        for labs in product((1,2,3),repeat=len(side)):
            for v,c in zip(side,labs):f[v]=c
            if all(len({f[u] for u in adj[v]})==3 for v in comp):
                ct+=1
                if ex is None: ex=tuple(f)
        counts.append(ct); witnesses.append(ex)
    return counts,witnesses


def orbit_test(adj,kind,param):
    n=len(adj)
    # Use direct adjacency to build two shore classes.
    parity=[-1]*n; parity[0]=0; todo=[0]
    while todo:
        v=todo.pop()
        for u in adj[v]:
            if parity[u]<0:parity[u]=1-parity[v];todo.append(u)
    optimal=set()
    for k in (0,1):
        side=[v for v in range(n) if parity[v]==k]
        other=[v for v in range(n) if parity[v]!=k]
        for colors in product((1,2,3), repeat=len(side)):
            f=[0]*n
            for v,c in zip(side,colors):f[v]=c
            if all(set(f[u] for u in adj[v])=={1,2,3} for v in other):optimal.add(tuple(f))
    assert len(optimal)==12
    exemplar=next(iter(optimal))
    orbit=set()
    for sh in range(param):
        for perm in permutations((1,2,3)):
            new=[0]*n
            for i,c in enumerate(exemplar):
                j= i//param*param + (i%param+sh)%param if kind=='prism' else (i+sh)%param
                new[j]=0 if c==0 else perm[c-1]
            orbit.add(tuple(new))
    assert orbit==optimal,(kind,param,len(orbit),len(optimal))
    print('EXACT_AUTOMORPHISM_COLOR_ORBIT_OK',kind,param,len(orbit))


def full_weight_count(adj,wt):
    n=len(adj); count=0;lower=0
    for w in range(wt+1):
        for supp in combinations(range(n),w):
            for colors in product((1,2,3),repeat=w):
                a=[0]*n
                for v,c in zip(supp,colors):a[v]=c
                if valid(adj,a):
                    if w==wt:count+=1
                    else:lower+=1
    return count,lower


def main():
    for m in (6,12):
        counts,_=count_on_bipartitions(prism(m))
        assert counts==[6,6],('prism',m,counts)
        print('PRISM_BIPARTITION_ENUM_OK',m,counts)
    for n in (6,18):
        counts,_=count_on_bipartitions(mobius(n))
        assert counts==[6,6],('mobius',n,counts)
        print('MOBIUS_BIPARTITION_ENUM_OK',n,counts)
    for kind,p,adj in [('prism',6,prism(6)),('mobius',6,mobius(6))]:
        count,lower=full_weight_count(adj,len(adj)//2)
        assert (count,lower)==(12,0),(kind,p,count,lower)
        print('DIRECT_SUBSET_ENUM_OK',kind,p,count,lower)
    orbit_test(prism(6),'prism',6)
    orbit_test(mobius(6),'mobius',6)
    # For the first non-equality cases, no equality-level function can exist.
    for kind,p,adj in [('prism',4,prism(4)),('prism',8,prism(8)),('mobius',10,mobius(10))]:
        counts,_=count_on_bipartitions(adj)
        assert counts==[0,0],(kind,p,counts)
        print('EQUALITY_OBSTRUCTION_OK',kind,p)
    print('VERIFY_OK')

if __name__=='__main__':main()
