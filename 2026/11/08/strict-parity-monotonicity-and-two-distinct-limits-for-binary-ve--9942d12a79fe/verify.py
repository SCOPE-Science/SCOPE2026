#!/usr/bin/env python3
"""Direct finite-field checks for exact Fourier norms of binary Veronese cones."""
from itertools import product
from fractions import Fraction
from math import prod

def mul(a,b,q):
    # GF(2), GF(4)=F2[t]/(t²+t+1), GF(8)=F2[t]/(t³+t+1)
    polys={2:0b11,4:0b111,8:0b1011}
    poly=polys[q];deg=q.bit_length()-1
    out=0
    while b:
        if b&1:out^=a
        b>>=1;a<<=1
        if a&q:a^=poly
    return out

def field_trace(a,q):
    out=0;x=a
    for i in range(q.bit_length()-1):
        out^=x;x=mul(x,x,q)
    assert out in (0,1)
    return out

def rk(M,q):
    M=[list(row) for row in M];r=0;m=len(M);n=len(M[0])
    for j in range(n):
        i=next((i for i in range(r,m) if M[i][j]),None)
        if i is None:continue
        M[i],M[r]=M[r],M[i]
        inv=next(x for x in range(1,q) if mul(x,M[r][j],q)==1)
        M[r]=[mul(x,inv,q) for x in M[r]]
        for t in range(m):
            if t==r:continue
            c=M[t][j]
            if c:M[t]=[a^mul(c,b,q) for a,b in zip(M[t],M[r])]
        r+=1
        if r==m:break
    return r

def count_alternating(m,j,q):
    # Number of alternating m×m matrices with rank 2j.
    n=2*j
    if n==0:return 1
    numer=prod(q**(m-i)-1 for i in range(n))
    den=prod(q**(n-i)-1 for i in range(n))
    assert numer%den==0
    gaussian=numer//den
    nondeg=q**(j*(j-1))*prod(q**(2*i-1)-1 for i in range(1,j+1))
    return gaussian*nondeg

def exact_norm(m,q):
    dim=m*(m+1)//2
    weighted=sum(count_alternating(m,j,q)*q**j for j in range(m//2+1))
    return Fraction(weighted,q**(dim-m))

def direct_check(m,q):
    coords=[(i,j) for i in range(m) for j in range(i,m)]
    vectors=list(product(range(q),repeat=m))
    feature=[]
    for v in vectors:
        feature.append(tuple(mul(v[i],v[j],q) for i,j in coords))
    assert len(set(feature))==q**m
    spec_sum=0
    hist={}; rank_hist={}
    for coeff in product(range(q),repeat=len(coords)):
        terms=[field_trace(_xor_mul(coeff, feat, q),q) for feat in feature]
        s=len(terms)-2*sum(terms)
        spec_sum+=abs(s)
        B=[[0]*m for _ in range(m)]
        for a,(i,j) in zip(coeff,coords):
            if i!=j:B[i][j]=B[j][i]=a
        r=rk(B,q)
        assert r%2==0
        assert abs(s) in (0,q**(m-r//2)),(m,q,r,s)
        hist[abs(s)]=hist.get(abs(s),0)+1
        rank_hist.setdefault(r,{}).setdefault(abs(s),0)
        rank_hist[r][abs(s)]+=1
    for r in range(0,m+1,2):
        num=count_alternating(m,r//2,q)
        assert rank_hist[r][q**(m-r//2)]==num*q**r
        assert rank_hist[r].get(0,0)==num*(q**m-q**r)
    norm=Fraction(spec_sum,q**len(coords))
    assert norm==exact_norm(m,q),(m,q,norm,exact_norm(m,q))
    print('PASS',f'q={q}',f'm={m}',f'ambient={q**len(coords)}',f'cone={q**m}',f'A_norm={norm}',f'nonzero_hist={hist}')

def _xor_mul(a,b,q):
    val=0
    for x,y in zip(a,b):val^=mul(x,y,q)
    return val

if __name__=='__main__':
    for m,q in [(2,2),(3,2),(4,2),(5,2),(2,4),(3,4),(2,8)]:
        direct_check(m,q)
    print('BINARY_VERONESE_FOURIER_CHECKS_PASS')

# Reconstruct each parity subsequence by two-step exact birth/death transitions.
def markov_norms(q,hmax=14):
    for parity in (0,1):
        state={0: Fraction(1)}
        for h in range(hmax+1):
            m=2*h+parity
            hnorm=sum(Fraction(1,q**k)*v for k,v in state.items())
            assert hnorm==exact_norm(m,q)/q**h,(q,m,hnorm,exact_norm(m,q)/q**h)
            if h<hmax:
                nextstate={}
                for k,p in state.items():
                    if parity==0:
                        birth=Fraction(1,q**(4*k+1))
                        death=(1-Fraction(1,q**(2*k)))*(1-Fraction(1,q**(2*k-1))) if k else Fraction(0)
                    else:
                        birth=Fraction(1,q**(4*k+3))
                        death=(1-Fraction(1,q**(2*k+1)))*(1-Fraction(1,q**(2*k))) if k else Fraction(0)
                    for dest,weight in ((k+1,birth),(k-1,death),(k,1-birth-death)):
                        if weight:
                            nextstate[dest]=nextstate.get(dest,Fraction(0))+p*weight
                state=nextstate
                assert sum(state.values())==1
                new_norm=sum(Fraction(1,q**k)*v for k,v in state.items())
                assert new_norm<hnorm
    print('PASS',f'q={q}', 'strict parity monotonicity and 2-step transition through dimension 29')

if __name__=='__main__':
    for q in (2,4,8): markov_norms(q)
    print('BINARY_VERONESE_MARKOV_CHECKS_PASS')
