"""Finite checks from direct partition definitions for the Bell-three graph formulas."""
from collections import defaultdict,deque
from math import factorial, comb
from itertools import combinations

def partitions(v,k=3):
    # restricted-growth strings: every unordered set partition exactly once
    if v<=0: return
    def rec(arr,maximum):
        if len(arr)==v:
            yield tuple(frozenset(i for i,x in enumerate(arr) if x==b) for b in range(maximum+1)); return
        for b in range(min(maximum+1,k-1)+1):
            arr.append(b)
            yield from rec(arr,max(maximum,b))
            arr.pop()
    yield from rec([0],0)

def rkey(parts): return frozenset(parts)
def remove(parts,i):return frozenset(frozenset(p-{i}) for p in parts if len(p-{i})>0)

def observed(m,n):
    V=m+n
    ps=[rkey(p) for p in partitions(V) if all(not (any(v<m for v in part) and any(v>=m for v in part)) for part in p)]
    inv={p:i for i,p in enumerate(ps)}
    # adjacency under the 'remove-one vertex' definition, not by formula
    buckets=defaultdict(list)
    for i,p in enumerate(ps):
        for v in range(V):buckets[(v,remove(p,v))].append(i)
    E=set()
    for indices in buckets.values():
        for i,j in combinations(indices,2): E.add((min(i,j),max(i,j)))
    return ps,E

def key_part(parts,m,n):
    A=set(range(m));B=set(range(m,m+n))
    Ablocks=[p for p in parts if p<=A]; Bblocks=[p for p in parts if p<=B]
    if len(Ablocks)==1 and len(Bblocks)==1:return ('root',0)
    if len(Ablocks)==2 and len(Bblocks)==1:
        mask=sum(1<<x for x in Ablocks[0]); mask=min(mask,((1<<m)-1)^mask)
        return ('A',mask)
    if len(Ablocks)==1 and len(Bblocks)==2:
        mask=sum(1<<(x-m) for x in Bblocks[0]);mask=min(mask,((1<<n)-1)^mask)
        return ('B',mask)
    raise AssertionError((parts,Ablocks,Bblocks))

def pcedges(s):
    if s<3:raise AssertionError
    full=(1<<s)-1
    nodes=range(1<<(s-1))
    def canon(x):return min(x,x^full)
    E=set()
    for v in nodes:
        for i in range(s):
            u=canon(v^(1<<i))
            if u!=v:E.add(tuple(sorted((v,u))))
    return E

def predicted(m,n):
    idx=[('root',0)] + [('A',i) for i in range(1,1<<(m-1))]+[('B',i) for i in range(1,1<<(n-1))]
    pos={v:i for i,v in enumerate(idx)}
    E=set()
    for lab,s in [('A',m),('B',n)]:
        for u,v in pcedges(s):
            a=pos[('root',0)] if u==0 else pos[(lab,u)]
            b=pos[('root',0)] if v==0 else pos[(lab,v)]
            E.add(tuple(sorted((a,b))))
    return idx,E

def dist_cnt(N,E,src):
    neighbors=[set() for _ in range(N)]
    for i,j in E:neighbors[i].add(j);neighbors[j].add(i)
    dist={src:0}; count={src:1}; queue=deque([src])
    while queue:
        x=queue.popleft()
        for y in neighbors[x]:
            if y not in dist:dist[y]=dist[x]+1;count[y]=0;queue.append(y)
            if dist[y]==dist[x]+1:count[y]+=count[x]
    return dist,count

def single_distance_count(s,u,v):
    h=(u^v).bit_count();d=min(h,s-h)
    return d,factorial(d)*(2 if 2*h==s else 1)

def formula(m,n,x,y):
    def info(lab,mask):
        return m if lab=='A' else n,mask
    if x[0]==y[0] and x[0]!='root':
        return single_distance_count(m if x[0]=='A' else n,x[1],y[1])
    if x[0]=='root':
        return single_distance_count(n if y[0]=='B' else m,0,y[1]) if y[0]!='root' else (0,1)
    if y[0]=='root':return formula(m,n,y,x)
    s,u=info(*x);t,v=info(*y)
    d1,c1=single_distance_count(s,0,u);d2,c2=single_distance_count(t,0,v)
    return d1+d2,c1*c2

def tau_formula(s):
    assert s>=3
    result=1
    for j in range(2,s+1,2):result*=(2*j)**comb(s,j)
    assert result%(2**(s-1))==0
    return result//(2**(s-1))

def det_bareiss(a):
    # Division-free (until exact elimination) integer determinant, standard library only.
    a=[row[:] for row in a]
    n=len(a)
    if n==0:return 1
    sign=1
    prev=1
    for k in range(n-1):
        if a[k][k]==0:
            rr=next((i for i in range(k+1,n) if a[i][k]),None)
            if rr is None:return 0
            a[k],a[rr]=a[rr],a[k]
            sign=-sign
        piv=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*piv-a[i][k]*a[k][j]
                assert num%prev==0
                a[i][j]=num//prev
        for i in range(k+1,n):a[i][k]=0
        prev=piv
    return sign*a[n-1][n-1]

def tau_by_laplacian(N,E):
    L=[[0]*N for _ in range(N)]
    for a,b in E:L[a][a]+=1;L[b][b]+=1;L[a][b]-=1;L[b][a]-=1
    return det_bareiss([r[:-1] for r in L[:-1]])

def main():
    for m,n in [(3,3),(3,4),(4,4),(3,5),(4,5)]:
        ps,ob=observed(m,n);idx,pr=predicted(m,n)
        assert len(set(ps))==len(ps)==len(idx)
        keyed={key_part(p,m,n):i for i,p in enumerate(ps)}
        assert set(keyed)==set(idx)
        ob_as_idx={tuple(sorted((idx.index(key_part(ps[a],m,n)),idx.index(key_part(ps[b],m,n))))) for a,b in ob}
        assert ob_as_idx==pr,(m,n,ob_as_idx^pr)
        N=len(idx)
        if N<=24:
            for s in range(N):
                d,c=dist_cnt(N,pr,s)
                for t in range(N):
                    assert (d[t],c[t])==formula(m,n,idx[s],idx[t]),(m,n,s,t,(d[t],c[t]),formula(m,n,idx[s],idx[t]))
        expect=tau_formula(m)*tau_formula(n)
        if N<=16:assert tau_by_laplacian(N,pr)==expect
        print('BELLPARTITION_AND_GEODESIC_OK',m,n,N,len(pr),'tau',expect)
    for s in range(3,7):
        N=2**(s-1);E=pcedges(s)
        if N<=16:assert tau_by_laplacian(N,E)==tau_formula(s)
        print('PROJECTIVE_CUBE_TREE_COUNT_OK',s,N,tau_formula(s))
    print('VERIFY_OK')
if __name__=='__main__':main()
