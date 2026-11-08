#!/usr/bin/env python3
"""Direct finite checks for extremal Kneser total-cut topology and symmetry."""
from itertools import combinations
from math import comb
from collections import Counter
from functools import lru_cache
import math

def sign_perm(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return (-1)**inv

def sign_action_on_ordered_subset(p,inds):
    vals=[p[i] for i in inds]
    return sign_perm([sorted(vals).index(v) for v in vals])

def original_family(n,k):
    vertices=tuple(combinations(range(n),k))
    return vertices

def max_intersecting_sets(n,k):
    import networkx as nx
    v=original_family(n,k)
    h=nx.Graph()
    h.add_nodes_from(range(len(v)))
    h.add_edges_from((i,j) for i in range(len(v)) for j in range(i+1,len(v)) if set(v[i]) & set(v[j]))
    allmax=list(nx.find_cliques(h))
    m=max(len(c) for c in allmax)
    full=[frozenset(c) for c in allmax if len(c)==m]
    return v,m,full

def check_nerve(n,k):
    v,alpha,full=max_intersecting_sets(n,k)
    N=len(v)
    assert alpha==comb(n-1,k-1)
    if n>2*k:
        star=[frozenset(j for j,s in enumerate(v) if i in s) for i in range(n)]
        assert set(full)==set(star),(n,k,len(full))
        facets=[set(range(N))-s for s in star]
        for r in range(1,n+1):
            for t in combinations(range(n),r):
                actual=bool(set.intersection(*(facets[i] for i in t)))
                expected=r<=n-k
                assert actual==expected,(n,k,t)
        print('NERVE',n,k,'graph_vertices',N,'alpha',alpha,'maximal_independent_sets',len(full),'nerve_skeleton_dimension',n-k-1,'sphere_rank',comb(n-1,k-1))
    else:
        pairs={frozenset([i,v.index(tuple(sorted(set(range(n))-set(e))))]) for i,e in enumerate(v)}
        assert len(pairs)==N//2
        assert len(full)==2**(N//2)
        print('BOUNDARY',n,k,'graph_vertices',N,'alpha',alpha,'matching_pairs',len(pairs),'cross_polytope_sphere_dimension',len(pairs)-1)

def transposition_orientation(k):
    n=2*k
    v=original_family(n,k)
    idx={s:i for i,s in enumerate(v)}
    visited=set(); axes=[]
    for i,s in enumerate(v):
        if i not in visited:
            j=idx[tuple(sorted(set(range(n))-set(s)))]
            assert i!=j
            axes.append((i,j));visited.update((i,j))
    perm=list(range(n));perm[0],perm[1]=perm[1],perm[0]
    def image_id(i):return idx[tuple(sorted(perm[x] for x in v[i]))]
    axes_img=[]; flip=[]
    mp={u:p for p,(u,w) in enumerate(axes)}
    mp.update({w:p for p,(u,w) in enumerate(axes)})
    for a,b in axes:
        a1=image_id(a)
        axes_img.append(mp[a1]);flip.append(1 if axes[mp[a1]][0]==a1 else -1)
    assert sorted(axes_img)==list(range(len(axes)))
    det=sign_perm(axes_img)*math.prod(flip)
    exponent=comb(2*k-2,k-1)//2
    predicted=(-1)**exponent
    assert det==predicted,(k,det,predicted)
    from_bin=int((k-1).bit_count()==1)
    assert det==(-1 if from_bin else 1)
    print('ORIENTATION',k,'axes',len(axes),'negative_eigenvalue_count',exponent,'determinant',det,'k_minus_one_power_of_two',bool(from_bin))

def partition(n):
    if n==0:yield ()
    else:
      for a in range(1,n+1):
       for b in partition(n-a):
        if not b or a<=b[0]:yield (a,)+b

def representative(lens):
    p=[];start=0
    for L in lens:
        p.extend([start+i+1 for i in range(L-1)]+[start]);start+=L
    return p

def std_ext_character(p,q):
    n=len(p)
    C=[0]*(q+1)
    for r in range(q+1):
      z=0
      for I in combinations(range(n),r):
        if set(p[i] for i in I)==set(I):z+=sign_action_on_ordered_subset(p,I)
      C[r]=z
    u=0
    for i in range(q+1):u=C[i]-u
    return u

def nerve_lefschetz(p,q):
    n=len(p)
    # augmented Euler trace: sum_{r=0}^{q+1} (-1)^{r-1} trace C_{r-1}
    alt=0
    for r in range(q+2):
      z=0
      for I in combinations(range(n),r):
       if set(p[i] for i in I)==set(I):z+=sign_action_on_ordered_subset(p,I)
      alt+=(-1)**(r-1)*z  # float due r=0: still exact integer result
    return int(round((-1)**q*alt))

def check_character(n,k):
    q=n-k-1
    for ls in partition(n):
        p=representative(ls)
        c=std_ext_character(p,q+1)
        l=nerve_lefschetz(p,q)
        assert c==l,(n,k,ls,c,l)
    print('CHARACTER',n,k,'conjugacy_classes',len(list(partition(n))),'degree',q,'rank',comb(n-1,q+1))

if __name__=='__main__':
    for n,k in [(4,2),(5,2),(6,2),(6,3),(7,2)]:check_nerve(n,k)
    for k in range(2,10):transposition_orientation(k)
    for n,k in [(5,2),(6,2),(7,2),(7,3),(8,2),(8,3)]:check_character(n,k)
    print('ALL_VERIFY_OK')
