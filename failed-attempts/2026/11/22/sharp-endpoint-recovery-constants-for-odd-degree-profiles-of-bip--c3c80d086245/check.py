#!/usr/bin/env python3
"""Independent exact-integer finite checks of the accompanying parity-Fourier theorem."""
from fractions import Fraction
from itertools import combinations
from math import comb

def tree_parity_profiles(m,n):
    N=m+n
    edges=[(i,m+j) for i in range(m) for j in range(n)]
    profile={}
    number=0
    for edge_ids in combinations(range(m*n),N-1):
        parent=list(range(N))
        def find(a):
            while parent[a]!=a:
                a=parent[a]
            return a
        par=0
        valid=True
        for eid in edge_ids:
            u,v=edges[eid]
            fu,fv=find(u),find(v)
            if fu==fv:
                valid=False
                break
            parent[fu]=fv
            par^=(1<<u)|(1<<v)
        if not valid: continue
        assert len({find(i) for i in range(N)})==1
        profile[par]=profile.get(par,0)+1
        number+=1
    return profile, number

def direct_multiplier(profiles,mask):
    return sum((-1 if (mask&v).bit_count()&1 else 1)*t for v,t in profiles.items())

def predicted_multiplier(m,n,s):
    a=(s & ((1<<m)-1)).bit_count()
    b=(s>>m).bit_count()
    return (-1 if (a+b)&1 else 1)*(m-2*a)**(n-1)*(n-2*b)**(m-1)

def fwht(v):
    v=list(v)
    step=1
    while step<len(v):
        for i in range(0,len(v),2*step):
            for j in range(i,i+step):
                a,b=v[j],v[j+step]
                v[j],v[j+step]=a+b,a-b
        step*=2
    return v

def kraw(d,r,t):
    return sum((-1)**j*comb(t,j)*comb(d-t,r-j) for j in range(max(0,r-(d-t)),min(r,t)+1))

def phi(d):
    if d%2:return Fraction(1)
    r=d//2
    return Fraction(1)+Fraction(comb(d,r),2**r)-Fraction(2*comb(d,r),2**d)

def projector_kernel_from_support(m,n):
    N=m+n
    flags=[int(predicted_multiplier(m,n,s)!=0) for s in range(1<<N)]
    vals=fwht(flags)
    return [Fraction(v,1<<N) for v in vals]

def main():
    assertions=0
    for d in range(2,18,2):
        r=d//2
        for t in range(d+1):
            val=kraw(d,r,t)
            if t%2: assert val==0
            else:
                j=t//2
                assert val*comb(d,t)==(-1)**j*comb(d,r)*comb(r,j)
            assertions+=1
        avg=sum(comb(d,t)*abs(kraw(d,r,t)) for t in range(d+1))
        assert avg==comb(d,r)*2**r
        assertions+=1
    for m,n in [(2,2),(2,3),(3,3),(2,4),(3,4),(4,4)]:
        profiles,ct=tree_parity_profiles(m,n)
        assert ct==m**(n-1)*n**(m-1)
        N=m+n
        flags=[]
        for freq in range(1<<N):
            a=direct_multiplier(profiles,freq)
            b=predicted_multiplier(m,n,freq)
            assert a==b,(m,n,freq,a,b)
            flags.append(int(a!=0))
            assertions+=1
        signal=[profiles.get(j,0) for j in range(1<<N)]
        assert fwht(signal)==[predicted_multiplier(m,n,i) for i in range(1<<N)]
        assertions+=1
        expected_rank=(2**m-(comb(m,m//2) if m%2==0 else 0))*(2**n-(comb(n,n//2) if n%2==0 else 0))
        assert sum(flags)==expected_rank
        ker=projector_kernel_from_support(m,n)
        assert sum(abs(c) for c in ker)==phi(m)*phi(n),(m,n)
        assert sum(ker)==1
        assertions+=3
    print('PASS: {} integer/rational assertions; direct labelled-tree enumeration, Walsh-Hadamard transforms, Krawtchouk identities, projection kernels'.format(assertions))
if __name__=='__main__':main()
