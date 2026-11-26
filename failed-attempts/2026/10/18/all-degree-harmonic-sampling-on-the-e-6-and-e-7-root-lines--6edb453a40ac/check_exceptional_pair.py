#!/usr/bin/env python3
"""Exact root-line geometry and all-degree harmonic sampling certificate.
Requires Python 3 and SymPy; no source downloads or external files.
"""
import itertools
from fractions import Fraction
from math import comb
from sympy import Matrix, Rational, Symbol, gegenbauer, eye, ones, zeros


def e8_roots_scaled():
    roots=[]
    for i in range(8):
        for j in range(i+1,8):
            for a,b in itertools.product((-1,1),repeat=2):
                v=[0]*8;v[i]=2*a;v[j]=2*b
                roots.append(tuple(v))
    for v in itertools.product((-1,1),repeat=8):
        if sum(x<0 for x in v)%2==0:roots.append(v)
    assert len(roots)==240
    return roots


def make_lines(rank):
    roots=e8_roots_scaled()
    if rank==6: filtered=[v for v in roots if v[5]==v[6]==v[7]]
    else: filtered=[v for v in roots if v[6]==v[7]]
    assert len(filtered)=={6:72,7:126}[rank]
    L=sorted({max(v,tuple(-x for x in v)) for v in filtered})
    assert len(L)=={6:36,7:63}[rank]
    return L


def dot(u,v):return sum(x*y for x,y in zip(u,v))


def spectral_levels(rank,degree):
    N,k,r,s,kap={6:(36,20,2,-4,10),7:(63,32,4,-4,16)}[rank]
    la=Rational(rank-2,2)
    t=Symbol('t')
    P=gegenbauer(degree,la,t)
    a=P.subs(t,Rational(1,2))/P.subs(t,1)
    b=P.subs(t,0)/P.subs(t,1)
    if degree%2:
        return (1+kap*a,1-2*a)
    return (1+k*a+(N-1-k)*b, 1-b+r*(a-b),1-b+s*(a-b))


def check():
    count=0
    for n in (6,7):
        N,k,r,s,kap={6:(36,20,2,-4,10),7:(63,32,4,-4,16)}[n]
        L=make_lines(n)
        S=Matrix(N,N,lambda i,j:0 if i==j else dot(L[i],L[j])//4)
        assert all(dot(v,v)==8 for v in L)
        assert all(S[i,j] in (-1,0,1) for i in range(N) for j in range(N))
        A=S.applyfunc(abs)
        assert A*ones(N,1)==k*ones(N,1)
        assert S*S-(kap-2)*S-2*kap*eye(N)==zeros(N)
        assert S.trace()==0
        mu={6:12,7:16}[n]
        lam={6:10,7:16}[n]
        assert A*A==(k-mu)*eye(N)+(lam-mu)*A+mu*ones(N)
        assert A.trace()==0
        # Orthogonality/commutativity after symmetrization is not assumed.
        # Symmetry plus the two polynomial identities and traces determine
        # all eigenvalues and multiplicities, without matrix elimination.
        count+=4
        for ell in range(80):
            levels=spectral_levels(n,ell)
            if ell==0:
                assert levels[0]==N and levels[1:]==(0,0)
            elif ell==1:
                assert levels[0]>0 and levels[1]==0
            elif ell==2:
                assert levels[0]==0 and levels[1]>0 and levels[2]==0
            elif ell==3:
                assert levels[0]==0 and levels[1]>0
            elif ell==4:
                assert levels[0]==0 and levels[1]>0 and levels[2]>0
            else:
                assert all(x>0 for x in levels)
            count+=1
        # For ell>=80, the elementary normalized-Gegenbauer bound from the
        # integral representation and pi^2<10 guarantees strict diagonal dominance
        # for even ell, and strict positivity of both S-eigenvalues for odd ell.
        if n==6:
            row_bound=Rational(k*100,3)+Rational((N-1-k)*75,4)
            odd_bound=Rational(kap*100,3)
        else:
            row_bound=Rational(k*800,9)+Rational((N-1-k)*50,1)
            odd_bound=Rational(kap*800,9)
        assert row_bound < 80**2 and odd_bound < 80**2
        count+=2
        print('RANK',n,'ROOT_LINES',N,'FINITELY_VERIFIED_DEGREES',80,
              'HIGH_DEGREE_ROW_BOUND',row_bound,'OVER_ELL_SQUARED',
              'ODD_EIGEN_BOUND',odd_bound,'OVER_ELL_SQUARED')
    print('ALL_CHECKS_OK',count)
if __name__=='__main__':check()
