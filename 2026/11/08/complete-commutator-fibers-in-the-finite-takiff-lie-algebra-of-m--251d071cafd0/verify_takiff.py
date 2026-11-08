#!/usr/bin/env python3
"""Direct finite-field linear-algebra census of commutator fibres in the six-dimensional Takiff Lie algebra of sl2.
All arithmetic uses independent coefficient matrices, no identities from the proposed proof.
"""
from itertools import product
from collections import Counter

def rank(M,p):
    if not M: return 0
    a=[[x%p for x in row] for row in M]
    n=len(a); m=len(a[0]); r=0
    for c in range(m):
        piv=next((i for i in range(r,n) if a[i][c]),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        inv=pow(a[r][c],-1,p)
        a[r]=[v*inv%p for v in a[r]]
        for i in range(n):
            if i!=r and a[i][c]:
                f=a[i][c]
                a[i]=[(u-f*v)%p for u,v in zip(a[i],a[r])]
        r+=1
        if r==n: break
    return r

def bracket(x,y,p):
    # sl2 basis E=[[0,1],[0,0]], F=[[0,0],[1,0]], H=[[1,0],[0,-1]].
    # [E,F]=H, [H,E]=2E, [H,F]=-2F.
    a,b,c=x; d,e,f=y
    return ((2*(c*d-a*f))%p, (2*(b*f-c*e))%p, (a*e-b*d)%p)

def columns(A,C,p):
    standard=((1,0,0),(0,1,0),(0,0,1))
    return [bracket(v,C,p) for v in standard]+[bracket(A,v,p) for v in standard]

def theory(Z,W,q):
    if any(Z): return q**4*(q*q-1)
    if any(W): return q**4*(q*q-1)*(q+1)
    return q**4*(q*q-1)*(q*q+q+1)+q**6

def check(p, exhaustive=True):
    vecs=list(product(range(p),repeat=3)); actual=Counter()
    if exhaustive:
      for A in vecs:
        for C in vecs:
          Z=bracket(A,C,p)
          cols=columns(A,C,p)
          M=[[v[i] for v in cols] for i in range(3)]
          r=rank(M,p)
          for W in vecs:
            aug=[row+[W[i]] for i,row in enumerate(M)]
            if rank(aug,p)==r: actual[(Z,W)]+=p**(6-r)
      assert len(actual)==p**6,(p,len(actual))
      assert sum(actual.values())==p**12
      for (Z,W),n in actual.items():
        assert n==theory(Z,W,p),(p,Z,W,n,theory(Z,W,p))
      print('FULL_TARGET_FIBERS_PASS',p,'targets',len(actual),'total_pairs',sum(actual.values()))
    else:
      import random
      rng=random.Random(219431+p)
      # direct evaluate every (A,C) for 3 selected targets
      for Z,W in [((0,0,0),(0,0,0)),((0,0,0),(1,0,0)),((1,0,0),(1,2%p,0))]:
        n=0
        for A in vecs:
          for C in vecs:
            if bracket(A,C,p)!=Z: continue
            cols=columns(A,C,p)
            M=[[v[i] for v in cols] for i in range(3)]
            r=rank(M,p)
            if rank([row+[W[i]] for i,row in enumerate(M)],p)==r: n+=p**(6-r)
        assert n==theory(Z,W,p),(p,Z,W,n,theory(Z,W,p))
      print('SELECTED_TARGET_FIBERS_PASS',p,'three_targets')
    # independent ad-rank brute force on the full Lie algebra, each element represented by A,B
    ar=Counter()
    for A in vecs:
      for B in vecs:
        basis6=[(v,(0,0,0)) for v in [(1,0,0),(0,1,0),(0,0,1)]]+[((0,0,0),v) for v in [(1,0,0),(0,1,0),(0,0,1)]]
        cols=[]
        for C,D in basis6:
          U=bracket(A,C,p)
          V=tuple((v+w)%p for v,w in zip(bracket(A,D,p),bracket(B,C,p)))
          cols.append(U+V)
        ar[rank([[v[i] for v in cols] for i in range(6)],p)]+=1
    assert ar=={0:1,2:p**3-1,4:(p**3-1)*p**3},(p,ar)
    print('ALL_ADJOINT_RANKS_PASS',p,dict(sorted(ar.items())))

if __name__=='__main__':
    check(3,True)
    check(5,False)
    print('TAKIFF_SL2_COMMUTATOR_FIBERS_PASS')
