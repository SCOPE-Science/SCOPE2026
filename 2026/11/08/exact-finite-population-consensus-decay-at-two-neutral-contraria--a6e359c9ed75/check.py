"""Exact finite-population checks for a three-agent majority/contrarian chain.

This code is supplementary to the analytic proof; it checks every count state for
populations of three, six and nine, averaging over all unordered triple partitions.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, factorial
from functools import lru_cache

@lru_cache(None)
def partitions(vertices):
    if not vertices:
        return ((),)
    v=vertices[0]
    return tuple(((v,)+pair,)+rest for pair in combinations(vertices[1:],2)
                 for rest in partitions(tuple(x for x in vertices[1:] if x not in pair)))

def binomial3(p):
    return {j: Q(comb(3,j))*p**j*(1-p)**(3-j) for j in range(4)}

def step_kernel(n,k,mode):
    full={j:Q(0) for j in range(n+1)}
    pp=partitions(tuple(range(n)))
    for grouping in pp:
        dist={0:Q(1)}
        for triple in grouping:
            a=sum(v<k for v in triple)
            prob=Q(a,3) if mode=='neutral' else Q(3-a,3)
            parts=binomial3(prob)
            nxt={}
            for j,v in dist.items():
                for h,b in parts.items():
                    nxt[j+h]=nxt.get(j+h,Q(0))+v*b
            dist=nxt
        for j,v in dist.items():
            full[j]+=v/Q(len(pp))
    assert sum(full.values())==1
    return full

def check():
    for n in [3,6,9]:
        q=1-Q(2,3*(n-1))
        assert len(partitions(tuple(range(n)))) == factorial(n)//(factorial(3)**(n//3)*factorial(n//3))
        for k in range(n+1):
            for mode in ['neutral','flip']:
                law=step_kernel(n,k,mode)
                mean=sum(j*p for j,p in law.items())
                second=sum(j*(n-j)*p for j,p in law.items())
                target=k if mode=='neutral' else n-k
                assert mean==target,(n,k,mode,'mean',mean,target)
                assert second == q*k*(n-k),(n,k,mode,'H',second,q*k*(n-k))
                var=sum((j-mean)**2*p for j,p in law.items())
                assert var == Q(2*k*(n-k),3*(n-1))
            # symmetry of the full one-step transition kernel under global opinion reversal
            A=step_kernel(n,k,'neutral')
            B=step_kernel(n,n-k,'flip')
            assert all(A.get(j,0)==B.get(j,0) for j in range(n+1))
            # One-step global-complement duality: K' at F is N-K' at E.
            F=step_kernel(n,k,'flip')
            assert all(F[j]==A[n-j] for j in range(n+1))
        print(f'n={n}: exact kernels, conditional means, variances, and heterozygosity checked for all {n+1} counts')
    # N=3, every transient count has one-step survival exactly 2/3.
    for mode in ['neutral','flip']:
        for k in [1,2]:
            law=step_kernel(3,k,mode)
            assert law[1]+law[2]==Q(2,3)
    # The exact mean-field polynomial of the source becomes identity/involution.
    from fractions import Fraction as F
    for p in [F(i,20) for i in range(21)]:
        def source_map(c0,c1):
            return (1-c0)*p**3+3*(1-c1)*p**2*(1-p)+3*c1*p*(1-p)**2+c0*(1-p)**3
        assert source_map(F(0),F(1,3)) == p
        assert source_map(F(1),F(2,3)) == 1-p
    print('PASS: exhaustive rational finite tests')

if __name__=='__main__':
    check()
