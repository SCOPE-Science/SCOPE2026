#!/usr/bin/env python3
"""Exact finite ridge and dihedral-angle checks for general parking-function polytopes.

Vertices and halfspaces are independently generated using cumulative parking bounds;
ridge detection uses affine rank of the common active vertex set.
"""
from itertools import combinations,permutations
from math import comb,acos,pi,sqrt
import numpy as np

def verts(b):
    n=len(b);cum=np.cumsum(b).tolist();vset=set()
    for k in range(n+1):
        v=tuple([1]*k+cum[k:]);vset.update(permutations(v))
    return np.array(sorted(vset),dtype=np.int64)

def facets(b):
    n=len(b);cum=np.cumsum(b).tolist();out=[]
    for i in range(n):
        normal=np.zeros(n,dtype=np.int64);normal[i]=-1
        out.append(('L',frozenset((i,)),normal,-1))
    for s in range(1,n+1):
        if b[0]==1 and s==n-1:continue
        cap=sum(cum[-s:])
        for Ss in combinations(range(n),s):
            normal=np.zeros(n,dtype=np.int64);normal[list(Ss)]=1
            out.append(('U',frozenset(Ss),normal,cap))
    return out

def test(b):
    n=len(b);points=verts(b);planes=facets(b);f=len(planes)
    active=[]
    for _,_,normal,cap in planes:
        vals=points@normal
        assert np.max(vals)<=cap
        active.append(vals==cap)
    nested=right=acute=0
    for i,j in combinations(range(f),2):
        ki,Si,ni,ci=planes[i];kj,Sj,nj,cj=planes[j]
        common=points[active[i]&active[j]]
        is_ridge=len(common)>0 and np.linalg.matrix_rank(common[1:]-common[0],tol=1e-9)==n-2
        predicted=(ki==kj=='L' or ki==kj=='U' and (Si<Sj or Sj<Si) or
                   ki!=kj and ((not Si.intersection(Sj)) or (b[0]==1 and
                   (ki=='U' and len(Si)==n or kj=='U' and len(Sj)==n))))
        assert is_ridge==predicted,(b,ki,Si,kj,Sj,is_ridge,predicted)
        if not is_ridge: continue
        c=float(ni@nj)/(np.linalg.norm(ni)*np.linalg.norm(nj))
        observed=pi-acos(max(-1.,min(1.,c)))
        if ki==kj=='U':
            nested+=1;expected=pi-acos(sqrt(min(len(Si),len(Sj))/max(len(Si),len(Sj))))
        elif ki!=kj and b[0]==1 and (ki=='U' and len(Si)==n or kj=='U' and len(Sj)==n):
            acute+=1;expected=acos(1/sqrt(n))
        else:
            right+=1;expected=pi/2
        assert abs(observed-expected)<1e-12,(b,ki,Si,kj,Sj,observed,expected)
    U=3**n-2**(n+1)+1
    if b[0]==1:
        U-=n*(2**(n-1)-1);R=n*(2**(n-1)-2)+comb(n,2);A=n
    else:
        R=n*(2**(n-1)-1)+comb(n,2);A=0
    assert (nested,right,acute)==(U,R,A),(b,(nested,right,acute),(U,R,A))
    print('PASS',b, 'vertices',len(points),'facets',f,'ridges',sum((nested,right,acute)),'types',(nested,right,acute))

if __name__=='__main__':
    cases=[]
    for n in (3,4,5):
        for b0 in (1,2):
            for variant in (0,1,2):
                b=(b0,)+tuple([1]*(n-1)) if variant==0 else (b0,)+tuple(range(1,n)) if variant==1 else (b0,)+tuple((2+i%3) for i in range(n-1))
                cases.append(b)
    for b in cases:test(b)
    print('PARKING_GENERAL_ANGLE_SPECTRUM_PASS',len(cases),'cases')
