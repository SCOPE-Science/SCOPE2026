#!/usr/bin/env python3
"""Exact finite-arithmetic verification for the 45-line Wiman stable boundary.

Requires Python 3 and NumPy (int64). The four Valentiner generators are
from Bauer et al., arXiv:1609.08648, Section 2.3. Their reduction at a
prime above 19 has delta = 9 and omega = 7. All matrices and reductions
below use integers; floating-point arithmetic is never used.
"""
from collections import Counter, defaultdict
from itertools import combinations
import numpy as np

P=19

def normalize(v):
    v=tuple(int(a)%P for a in v)
    first=next(a for a in v if a)
    u=pow(first,-1,P)
    return tuple(a*u%P for a in v)

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])

def minor2(A,ii,jj):
    rows=[i for i in range(3) if i!=ii]
    cols=[j for j in range(3) if j!=jj]
    return A[rows[0]][cols[0]]*A[rows[1]][cols[1]]-A[rows[0]][cols[1]]*A[rows[1]][cols[0]]

def inverse3(A):
    det=sum((-1)**j*A[0][j]*minor2(A,0,j) for j in range(3))%P
    assert det
    c=pow(det,-1,P)
    return [[c*((-1)**(i+j))*minor2(A,j,i)%P for j in range(3)] for i in range(3)]

def orbit_lines():
    delta=9; omega=7
    assert (delta*delta)%P==5 and (omega*omega+omega+1)%P==0
    mu1=((delta-1)*pow(2,-1,P))%P
    mu2=(-(1+delta)*pow(2,-1,P))%P
    half=pow(2,-1,P)
    generators=[
        [[0,0,1],[1,0,0],[0,1,0]],
        [[1,0,0],[0,-1,0],[0,0,-1]],
        [[-half,half*mu2,half*mu1],
         [half*mu2,half*mu1,-half],
         [half*mu1,-half,half*mu2]],
        [[-1,0,0],[0,0,-omega*omega],[0,-omega,0]],
    ]
    inverse_generators=[inverse3(A) for A in generators]
    seen={(1,0,0)}; todo=[(1,0,0)]
    while todo:
        v=todo.pop()
        for A in inverse_generators:
            w=normalize([sum(v[i]*A[i][j] for i in range(3)) for j in range(3)])
            if w not in seen:
                seen.add(w); todo.append(w)
    assert len(seen)==45
    return sorted(seen)

def intersection_data(lines):
    incidences=defaultdict(set)
    for i,j in combinations(range(len(lines)),2):
        pt=normalize(cross(lines[i],lines[j]))
        incidences[pt].update((i,j))
    assert len(incidences)==201
    assert Counter(map(len,incidences.values()))=={3:120,4:45,5:36}
    assert sum(len(s)*(len(s)-1)//2 for s in incidences.values())==990
    assert all(sum(i in s for s in incidences.values())==16 for i in range(45))
    return [tuple(sorted(v)) for k,v in sorted(incidences.items())]

def build_graph(inc):
    n=45+len(inc)
    L=np.zeros((n,n),dtype=np.int64)
    Q={m:np.zeros((45,45),dtype=np.int64) for m in (3,4,5)}
    for idx,ss in enumerate(inc):
        u=45+idx; m=len(ss)
        for i in ss:
            L[i,i]+=1;L[u,u]+=1
            L[i,u]-=1;L[u,i]-=1
            for j in ss:Q[m][i,j]+=1
    assert n==246 and np.count_nonzero(np.triu(L<0,1))==720
    assert (L.sum(axis=1)==0).all()
    assert (np.diag(L)[:45]==16).all()
    assert Counter(map(int,np.diag(L)[45:]))=={3:120,4:45,5:36}
    B=960*np.eye(45,dtype=np.int64)-sum((60//m)*Q[m] for m in Q)
    assert (B.sum(axis=1)==0).all()
    return L,Q,B

def mm(A,B):
    # NumPy integer products; largest exact intermediate here is below 2^63.
    return A@B

def joint_certificate(Q,B):
    """Integer matrix identities certify the full rational spectral splitting."""
    eigs=[0,665,705,720,729]
    dims={0:1,665:9,705:9,720:16,729:10}
    values={0:(24,16,20),665:(14,1,0),705:(6,9,0),
            720:(6,4,5),729:(6,1,8)}
    I=np.eye(45,dtype=np.int64)
    # For possibly large powers, use arbitrary-precision Python integers.
    X=B.astype(object); E=np.eye(45,dtype=object)
    powers=[E]
    for k in range(1,5): powers.append(powers[-1]@X)
    for k,M in enumerate(powers):
        trace=sum(int(M[i,i]) for i in range(45))
        assert trace==sum(dims[l]*(l**k) for l in eigs)
    annihilator=E.copy()
    for l in eigs:annihilator=annihilator@(X-l*E)
    assert not any(v for row in annihilator for v in row)
    for m in Q:
        for n in Q:
            assert np.array_equal(Q[m]@Q[n],Q[n]@Q[m])
    for l in eigs:
        projnumerator=E.copy()
        for u in eigs:
            if u!=l:projnumerator=projnumerator@(X-u*E)
        assert any(v for row in projnumerator for v in row)
        for m,sc in zip((3,4,5),values[l]):
            R=(Q[m].astype(object)-sc*E)@projnumerator
            assert not any(v for row in R for v in row)
    return dims,values

def pol_mul(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):C[i+j]+=a*b
    return C

def pol_add(A,B):
    C=[0]*max(len(A),len(B))
    for i,a in enumerate(A):C[i]+=a
    for i,b in enumerate(B):C[i]+=b
    return C

def schur_blocks(values):
    # Increasing-order coefficients of (t-16)*prod(t-m)
    den=[1]
    for m in (3,4,5):den=pol_mul(den,[-m,1])
    polys={}
    for eig,val in values.items():
        F=pol_mul(den,[-16,1])
        for m,q in zip((3,4,5),val):
            tmp=[1]
            for r in (3,4,5):
                if r!=m:tmp=pol_mul(tmp,[-r,1])
            F=pol_add(F,[-q*x for x in tmp])
        polys[eig]=F
    expected={
      0:[0,-328,179,-28,1],
      665:[665,-(133+5*109),109+5*23,-(23+5),1],
      705:[705,-(141+5*109),109+5*23,-(23+5),1],
      720:[720,-691,224,-28,1],
      729:[729,-694,224,-28,1],
    }
    for k,v in expected.items():assert polys[k]==v,(k,polys[k],v)
    return polys

def bareiss_det(A):
    C=[list(map(int,row)) for row in A]
    n=len(C); prev=1
    for k in range(n-1):
        pivot=C[k][k]
        assert pivot!=0
        for i in range(k+1,n):
            for j in range(k+1,n):
                w=C[i][j]*pivot-C[i][k]*C[k][j]
                assert w%prev==0
                C[i][j]=w//prev
            C[i][k]=0
        prev=pivot
    return C[-1][-1]

def padic_smith(A,prime,depth):
    """Legal row/column operations over Z/(prime**depth); returns valuations."""
    modulus=prime**depth
    A=A.copy()%modulus
    n=A.shape[0]
    result=[]
    for k in range(n):
        block=A[k:,k:]
        valuation=0
        while valuation<depth:
            filt=((block//(prime**valuation))%prime)!=0
            if filt.any():break
            valuation+=1
        assert valuation<depth, ('precision exhausted',prime,depth,k)
        i,j=np.argwhere(filt)[0];i+=k;j+=k
        if i!=k:A[[i,k]]=A[[k,i]]
        if j!=k:A[:,[j,k]]=A[:,[k,j]]
        q=prime**valuation
        assert (A[k:,k:]%q==0).all()
        inverse=pow(int(A[k,k]//q),-1,modulus//q)
        if k+1<n:
            factors=((A[k+1:,k]//q)*inverse)%(modulus//q)
            A[k+1:,k:]=(A[k+1:,k:]-factors[:,None]*A[k,k:])%modulus
            assert not A[k+1:,k].any()
            factors=((A[k,k+1:]//q)*inverse)%(modulus//q)
            A[k:,k+1:]=(A[k:,k+1:]-A[k:,k,None]*factors[None,:])%modulus
            assert not A[k,k+1:].any()
        result.append(valuation)
    assert len(result)==n
    assert result==sorted(result)
    return Counter(result)

def main():
    lines=orbit_lines()
    inc=intersection_data(lines)
    L,Q,B=build_graph(inc)
    dims,values=joint_certificate(Q,B)
    schur_blocks(values)
    # Full 246-degree polynomial is the stated factorization, from Schur blocks.
    # Its nonzero-eigenvalue product divided by 246 is a tree count.
    tau=(5**9)*(3**75)*328*(141**9)*(133**9)*(729**10)*(720**16)//246
    expected_tau=(2**66)*(3**175)*(5**25)*(7**9)*(19**9)*(47**9)
    assert tau==expected_tau
    # A second independent exact Kirchhoff cofactor via a 44x44 Schur complement.
    d=bareiss_det(B[1:,1:])
    num=d*(3**120)*(4**45)*(5**36)
    assert num%(60**44)==0 and num//(60**44)==tau
    local_expected={
      2:{0:228,2:1,4:16},
      3:{0:169,1:42,2:17,3:7,7:2,8:8},
      5:{0:228,1:9,2:8},
      7:{0:236,1:9},
      19:{0:236,1:9},
      47:{0:236,1:9},
    }
    depths={2:9,3:10,5:6,7:3,19:3,47:3}
    for root in (0,15,46,200):
        C=np.delete(np.delete(L,root,axis=0),root,axis=1)
        for p,ex in local_expected.items():
            result=padic_smith(C,p,depths[p])
            assert dict(result)==ex,(root,p,result)
    assert {p:sum(v*c for v,c in ex.items()) for p,ex in local_expected.items()} == {
        2:66,3:175,5:25,7:9,19:9,47:9}
    factors=[3]*42+[9]*17+[540]+[2160]*6+[174960]+[1093674960]+[16405124400]*8
    assert len(factors)==76
    assert all(b%a==0 for a,b in zip(factors,factors[1:]))
    from math import prod
    assert prod(factors)==tau
    assert 720-246+1==475
    print('WIMAN_45_STABLE_BOUNDARY_FULL_SMITH_AND_SPECTRUM_OK')
    print('components=246 nodes=720 genus=475; tree order=',tau)
    print('nontrivial invariant factors=',Counter(factors))

if __name__=='__main__':main()
