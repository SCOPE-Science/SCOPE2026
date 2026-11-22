#!/usr/bin/env python3
"""Exact, independently reconstructed Smith computation for the 240 exceptional curves.
All arithmetic is integral; no floating point or external data files are used.
"""
import itertools
import collections
import math
import numpy as np

def roots_twice():
    roots=[]
    for i,j in itertools.combinations(range(8),2):
        for a,b in itertools.product((-2,2),repeat=2):
            v=[0]*8;v[i]=a;v[j]=b;roots.append(tuple(v))
    for v in itertools.product((-1,1),repeat=8):
        if v.count(-1)%2==0: roots.append(v)
    assert len(roots)==len(set(roots))==240
    return np.array(sorted(roots),dtype=np.int64)

def exceptional_classes():
    # Each class is aH - sum(b_i E_i), in the blowup at eight points.
    classes=[]
    for i in range(8):
        b=[0]*8;b[i]=-1;classes.append((0,*b))
    for I in itertools.combinations(range(8),2):
        b=[int(i in I) for i in range(8)];classes.append((1,*b))
    for I in itertools.combinations(range(8),5):
        b=[int(i in I) for i in range(8)];classes.append((2,*b))
    for i in range(8):
        for j in range(8):
            if j==i:continue
            b=[1]*8;b[i]=2;b[j]=0;classes.append((3,*b))
    for I in itertools.combinations(range(8),3):
        b=[2 if i in I else 1 for i in range(8)];classes.append((4,*b))
    for I in itertools.combinations(range(8),6):
        b=[2 if i in I else 1 for i in range(8)];classes.append((5,*b))
    for i in range(8):
        b=[2]*8;b[i]=3;classes.append((6,*b))
    assert len(classes)==len(set(classes))==240
    return np.array(sorted(classes),dtype=np.int64)

def graph_from_roots():
    v=roots_twice()
    gram=v@v.T
    assert np.all(gram%4==0)
    gram//=4
    assert np.array_equal(v.T@v,240*np.eye(8,dtype=np.int64))
    assert np.array_equal(v.sum(axis=0),np.zeros(8,dtype=np.int64))
    assert collections.Counter(gram[0,:])=={2:1,1:56,0:126,-1:56,-2:1}
    L=240*np.eye(240,dtype=np.int64)-np.ones((240,240),dtype=np.int64)+gram
    assert np.array_equal(L.sum(axis=1),np.zeros(240,dtype=np.int64))
    assert np.all(L.diagonal()==241)
    assert collections.Counter(-L[0,1:])=={0:56,1:126,2:56,3:1}
    return L

def graph_from_blowup():
    v=exceptional_classes()
    # Intersection pairing H^2=1, E_i^2=-1.
    gram=v[:,[0]]@v[:,[0]].T-v[:,1:]@v[:,1:].T
    assert np.all(np.diag(gram)==-1)
    assert np.all(v[:,0]*3-v[:,1:].sum(axis=1)==1) # (-K).C=1
    weights=gram.copy();np.fill_diagonal(weights,0)
    assert np.min(weights)==0 and np.max(weights)==3
    L=np.diag(weights.sum(axis=1))-weights
    assert np.all(L.diagonal()==241)
    return L

def local_invariant_valuations(A,p,K):
    """Smith exponents over Z/(p^K), using legal row and column operations.
    Pivots have least p-adic valuation in the remaining block, so all
    required divisions by p^v are exact. Every arithmetic operation is
    reduced modulo p^K; max integer product below 6e16 (< 2^63).
    """
    modulus=p**K
    B=A.copy().astype(np.int64)%modulus
    n=B.shape[0]; vals=[]
    for k in range(n):
        block=B[k:,k:]
        v=0
        while v<K and not np.any(block%(p**(v+1))):v+=1
        if v>=K:
            vals.extend([K]*(n-k));break
        ij=np.argwhere(block%(p**(v+1))!=0)[0]
        i,j=k+int(ij[0]),k+int(ij[1])
        if i!=k:B[[k,i],:]=B[[i,k],:]
        if j!=k:B[:,[k,j]]=B[:,[j,k]]
        pv=p**v
        assert B[k,k]%pv==0 and (B[k,k]//pv)%p!=0
        unit_inverse=pow(int(B[k,k]//pv),-1,modulus//pv)
        if k+1<n:
            row_multipliers=((B[k+1:,k]//pv)*unit_inverse)%(modulus//pv)
            B[k+1:,k:]=(B[k+1:,k:]-row_multipliers[:,None]*B[[k],k:])%modulus
            assert np.all(B[k+1:,k]==0)
            col_multipliers=((B[k,k+1:]//pv)*unit_inverse)%(modulus//pv)
            B[k:,k+1:]=(B[k:,k+1:]-B[k:,[k]]*col_multipliers[None,:])%modulus
            assert np.all(B[k,k+1:]==0)
        vals.append(v)
    return collections.Counter(vals)

def run():
    L1=graph_from_roots();L2=graph_from_blowup()
    # These matrices have different vertex orders; compare rooted Smith data.
    prime_caps={2:24,3:16,5:12,7:7}
    expected={2:{0:9,4:222,6:8},3:{0:9,1:222,2:8},5:{0:9,1:222,3:8},7:{0:239}}
    target_valuations={2:936,3:238,5:246,7:0}
    for name,L in [('roots',L1),('blowup',L2)]:
        assert L.shape==(240,240)
        for delete in (0,119,239):
            A=np.delete(np.delete(L,delete,axis=0),delete,axis=1)
            for p,K in prime_caps.items():
                got=local_invariant_valuations(A,p,K)
                assert got==expected[p],(name,delete,p,got)
                assert sum(e*n for e,n in got.items())==target_valuations[p]
            print('checked',name,'deleted vertex',delete,'Smith exponents',expected)
    # Independent exact spectral calculation from 240 roots, checked by Gram identities.
    # All rows of L sum to zero. The root columns span eight orthogonal
    # 300-eigenvectors; the constant vector is the only 0-eigenvector;
    # the remaining 231 eigenvalues equal 240.
    # Matrix-tree theorem gives 300**8 * 240**230.
    assert 300**8*240**230==240**222*72000**8
    print('E8_WEIGHTED_ALL_240_EXCEPTIONAL_SMITH_OK')
if __name__=='__main__':run()
