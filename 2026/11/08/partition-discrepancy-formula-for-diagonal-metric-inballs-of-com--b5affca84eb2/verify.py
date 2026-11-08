"""Exact finite tests for diagonal-metric inballs of bipartite root polytopes.

Run with Python 3.9+ standard library only. These checks do not replace the proof.
"""
from fractions import Fraction as F
from itertools import product
from math import isclose


def sqnormal(f, weights):
    total = sum(weights)
    return sum(w*v*v for w,v in zip(weights,f)) - sum(w*v for w,v in zip(weights,f))**2 / total


def discrepancy(vals):
    return min(abs(sum(s*w for s,w in zip(signs, vals)))
               for signs in product((-1,1),repeat=len(vals)))


def formula(a,b):
    z = a + b
    t = sum(z)
    return max(sum(a)-discrepancy(a)**2/t,
               sum(b)-discrepancy(b)**2/t)


def connected_tight(f,p,q):
    n=p+q
    adj=[set() for _ in range(n)]
    for i in range(p):
        for j in range(p,n):
            if abs(f[i]-f[j])==1:
                adj[i].add(j);adj[j].add(i)
    seen={0}; todo=[0]
    while todo:
        for k in adj[todo.pop()]:
            if k not in seen: seen.add(k);todo.append(k)
    return len(seen)==n


def exhaustive(p,q,z):
    # Gauge f[0]=0. Any connected tight potential is integral with every
    # coordinate within graph-distance 2 of the first vertex.
    best=F(-1)
    contacts=0
    for rest in product(range(-2,3),repeat=p+q-1):
        f=(0,)+rest
        if any(abs(f[i]-f[j])>1 for i in range(p) for j in range(p,p+q)):
            continue
        if not connected_tight(f,p,q):continue
        v=sqnormal(f,z)
        if v>best:best=v;contacts=1
        elif v==best:contacts+=1
    assert best==formula(z[:p],z[p:]),(p,q,z,best,formula(z[:p],z[p:]))
    return contacts


def partition_equivalence(nums):
    a=list(map(F,nums)); b=[F(1)]
    x=formula(a,b)
    T=sum(a)
    is_balanced=any(sum(s*t for s,t in zip(signs,a))==0
                    for signs in product((-1,1),repeat=len(a)))
    assert (x==T)==is_balanced




def matrix_rank(rows):
    a=[[F(v) for v in row] for row in rows]
    if not a:return 0
    m=len(a);n=len(a[0]);r=0
    for c in range(n):
        k=next((j for j in range(r,m) if a[j][c]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r]
        pivot=a[r][c]
        a[r]=[v/pivot for v in a[r]]
        for j in range(m):
            if j!=r and a[j][c]:
                fact=a[j][c]
                a[j]=[u-fact*v for u,v in zip(a[j],a[r])]
        r+=1
        if r==m:break
    return r


def unweighted_center_dimension(p,q):
    n=p+q
    L=max(p,q);S=min(p,q)
    denom=L-(L%2)/F(n)
    contact=[]
    for st,ln in ((0,p),(p,q)):
        if ln!=L:continue
        for signs in product((-1,1),repeat=ln):
            f=[0]*n
            f[st:st+ln]=signs
            if sqnormal(f,[F(1)]*n)==denom:
                mean=F(sum(f),n)
                contact.append([F(v)-mean for v in f])
    dim=n-1-matrix_rank(contact)
    if p==q:
        target=1 if L%2==0 else 0
    else:
        target=S if L%2==0 else S-1
    assert dim==target,(p,q,dim,target)
    return len(contact)

def main():
    testcases=0; facets=0
    for p in range(1,5):
        for q in range(1,5):
            if p+q<3 or p+q>7:continue
            for mult in (0,1,2):
                weights=[F(1+((i+2*mult)*3+mult)%7) for i in range(p+q)]
                facets+=exhaustive(p,q,weights)
                testcases+=1
    center_profiles=0
    for p in range(1,6):
        for q in range(1,6):
            if p+q>=3:
                unweighted_center_dimension(p,q)
                center_profiles+=1
    for nums in ((1,1),(1,2,3),(2,3,4),(1,4,5,6),(5,5,1,1),
                 (11,13,17,19,20), (1,2,4,8,16)):
        partition_equivalence(nums)
    print('DIAGONAL_BICLIQUE_INBALL_CHECKS_PASSED',
          'parameter_profiles=',testcases,'maximizing_facets=',facets,
          'partition_instances=',7,'center_profiles=',center_profiles)


if __name__=='__main__':
    main()
