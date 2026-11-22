#!/usr/bin/env python3
"""Standalone finite checks of shattering of Arf-parity quadratic refinements.
Coordinate order (u_1,...,u_m,v_1,...,v_m), over F2.
"""
import itertools, math, random

def q0(x,m):
    return sum(((x>>i)&1)*((x>>(m+i))&1) for i in range(m))%2

def B(x,y,m):
    return (sum(((x>>i)&1)*((y>>(m+i))&1) + ((y>>i)&1)*((x>>(m+i))&1) for i in range(m)))%2

def rank(vecs,dim):
    basis={}
    for x in vecs:
        y=x
        while y:
            p=y.bit_length()-1
            if p in basis: y ^=basis[p]
            else: basis[p]=y; break
    return len(basis)

def isotropic_perp(S,m):
    dim=2*m
    K=[v for v in range(1<<dim) if all(B(v,s,m)==0 for s in S)]
    # K isotropic iff every pair of vectors in K has zero polar pairing
    return all(B(u,v,m)==0 for u,v in itertools.combinations(K,2)),len(K)

def algebra_prediction(S,m,epsilon):
    if rank(S,2*m)!=len(S): return False
    iso,nK = isotropic_perp(S,m)
    return not iso or (epsilon==0 and nK==(1<<m))

def empirical(S,m,epsilon):
    vectors=range(1<<(2*m)); concepts=[a for a in vectors if q0(a,m)==epsilon]
    target=1<<len(S)
    traces=set()
    for a in concepts:
        bits=sum((q0(s,m)^B(a,s,m))<<i for i,s in enumerate(S))
        traces.add(bits)
        if len(traces)==target:return True
    return False

def iso_count(m,r):
    if r<0 or r>m:return 0
    num=den=1
    for i in range(r):
        num*= 2**(2*m-i)-2**i
        den*= 2**r-2**i
    assert num%den==0
    return num//den

def gaussian(n,k):
    if k<0 or k>n:return 0
    num=den=1
    for i in range(k):
        num*= 2**n-2**i
        den*= 2**k-2**i
    assert num%den==0
    return num//den

def unordered_bases(k):
    prod=1
    for i in range(k):prod*=2**k-2**i
    return prod//math.factorial(k)

def polynomial(m,epsilon):
    out=[]
    for k in range(2*m+1):
        r=2*m-k
        tot=gaussian(2*m,k)
        bad=iso_count(m,r)
        if epsilon==0 and r==m:bad=0
        out.append((tot-bad)*unordered_bases(k))
    return out

def run():
    print('m=2 even/odd polynomial',polynomial(2,0),polynomial(2,1))
    print('m=3 even/odd polynomial',polynomial(3,0),polynomial(3,1))
    print('m=4 even/odd polynomial',polynomial(4,0),polynomial(4,1))
    # Entire nonempty support enumeration for dimension four: 15 point domain.
    for e in (0,1):
        counts=[0]*16
        for k in range(0,16):
            if k>3:break  # size bound: at most 10 forms
            for S in itertools.combinations(range(1,16),k):
                prediction=algebra_prediction(S,2,e)
                brute=empirical(S,2,e)
                assert prediction==brute,(S,e,prediction,brute)
                counts[k]+=brute
        assert counts[:5]==polynomial(2,e) + [0]*(5-len(polynomial(2,e)))
        print('EXHAUSTIVE m=2 parity',e,counts[:5])
    # All supports up to k=3 in dimension six, and a reproducible sample at k=4,5.
    rng=random.Random(1729)
    for e in (0,1):
        for k in (0,1,2,3):
            ct=0
            for S in itertools.combinations(range(1,64),k):
                prediction=algebra_prediction(S,3,e)
                brute=empirical(S,3,e)
                assert prediction==brute,(S,e)
                ct+=brute
            assert ct==polynomial(3,e)[k],(e,k,ct,polynomial(3,e)[k])
            print('EXHAUSTIVE m=3 parity',e,'k=',k,'count=',ct)
        for k in (4,5,6):
            sample=[tuple(sorted(rng.sample(range(1,64),k))) for _ in range(150)]
            for S in sample: assert algebra_prediction(S,3,e)==empirical(S,3,e),(e,k,S)
            print('SAMPLED m=3 parity',e,'k=',k,'tested=',len(sample))
    print('QUADRATIC_PARITY_SHATTER_PASS')
if __name__=='__main__':run()
