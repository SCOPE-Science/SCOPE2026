#!/usr/bin/env python3
"""Verify the exact two-terminal theta-graph dark-projector formula."""
import itertools
from collections import defaultdict
from fractions import Fraction
from math import gcd
import numpy as np


def build(lengths):
    n=sum(lengths)-1
    H=np.zeros((n,n),float)
    vertices={}
    ptr=2
    for i,L in enumerate(lengths):
        chain=[0]+list(range(ptr,ptr+L-1))+[1]
        for j,v in enumerate(chain[1:-1],1):vertices[(i,j)]=v
        ptr+=L-1
        for x,y in zip(chain,chain[1:]):H[x,y]=H[y,x]=1
    assert ptr==n
    return H,vertices


def analytic(lengths):
    H,vertices=build(lengths)
    N=H.shape[0]; proj=np.zeros((N,N),float)
    keys=sorted({Fraction(k,L) for L in lengths for k in range(1,L)})
    dim=0
    for t in keys:
        groups=defaultdict(list)
        for i,L in enumerate(lengths):
            k=t*L
            if k.denominator==1:
                groups[int(k)%2].append(i)
        for g,inds in groups.items():
            if len(inds)<2: continue
            dim+=len(inds)-1
            U=np.zeros((N,len(inds)))
            w=np.array([np.sqrt(2/lengths[i])*np.sin(np.pi*float(t)) for i in inds])
            for column,i in enumerate(inds):
                for j in range(1,lengths[i]):
                    U[vertices[(i,j)],column]=np.sqrt(2/lengths[i])*np.sin(np.pi*float(t)*j)
            proj+=U@(np.eye(len(inds))-np.outer(w,w)/(w@w))@U.T
    return dim,proj


def spectral(H):
    lam,V=np.linalg.eigh(H)
    P=np.zeros_like(H)
    n=H.shape[0]
    at=0
    while at<n:
        end=at+1
        while end<n and abs(lam[end]-lam[at])<5e-9:end+=1
        E=V[:,at:end]
        B=E[:2,:]
        u,s,vh=np.linalg.svd(B,full_matrices=True)
        rank=int(np.sum(s>2e-8))
        if rank<end-at:
            Z=E@vh[rank:,:].T
            P+=Z@Z.T
        at=end
    return P


def closed_dimension(lengths):
    def overlap(sub):
        g=0
        for v in sub:g=gcd(g,v)
        reduced=[v//g for v in sub]
        if len(set(v%2 for v in reduced))==1:
            return g-1
        return (g-1)//2
    return sum(overlap(pair) for pair in itertools.combinations(lengths,2))-overlap(lengths)


def run():
    tested=0; comparisons=0; zero=0
    for lengths in itertools.product(range(2,9),repeat=3):
        H,vertices=build(lengths)
        d,P=analytic(lengths)
        Q=spectral(H)
        assert d==closed_dimension(lengths),(lengths,'closed dimension')
        assert abs(np.trace(P)-d)<5e-8,(lengths,'dim')
        assert np.linalg.norm(P@P-P)<2e-8,(lengths,'projector')
        assert np.linalg.norm(H@P-P@H)<2e-8,(lengths,'commutes')
        assert np.max(np.abs(P-Q))<3e-8,(lengths,'spectral')
        assert np.max(np.abs(P[:2,:]))<2e-8,(lengths,'hub')
        pairgood=False
        for a,b in itertools.combinations(lengths,2):
            g=gcd(a,b)
            pairgood|=(g>1 and not(g==2 and (a%4,b%4) in [(2,0),(0,2)]))
        assert (d>0)==pairgood,(lengths,d,pairgood)
        comparisons+=len(vertices)
        tested+=1
        if d==0:zero+=1
    for lengths,want in [((2,4,3),0),((2,2,3),1),((4,4,5),3),((3,3,3),4),((4,4,4),6)]:
        d,P=analytic(lengths)
        assert d==want,(lengths,d,want)
    print('PASS full spectral projector for',tested,'theta graphs; localized sites',comparisons,'; full-capture cases',zero)
    print('PASS closed gcd/parity dimension, zero-capture criterion, all cases, plus five exact examples')

if __name__=='__main__':run()
