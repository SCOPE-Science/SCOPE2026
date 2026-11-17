#!/usr/bin/env python3
"""Exact checks for Euclidean facet geometry of cycle root polytopes.
Requires only the Python standard library. No probabilistic simulation is a proof.
"""
from itertools import combinations, product
from math import comb
from fractions import Fraction

def words(n):
    if n%2==0:
        m=n//2
        for pos in combinations(range(n),m):
            chosen=set(pos)
            yield tuple(1 if i in chosen else -1 for i in range(n))
    else:
        m=(n-1)//2
        for z in range(n):
            inds=[i for i in range(n) if i!=z]
            for pos in combinations(inds,m):
                chosen=set(pos)
                yield tuple(0 if i==z else 1 if i in chosen else -1 for i in range(n))

def centered_num(d):
    n=len(d)
    heights=[0]
    for s in d[:-1]:
        heights.append(heights[-1]+s)
    assert heights[-1]+d[-1]==0
    total=sum(heights)
    return tuple(n*x-total for x in heights)

def test():
    word_checks=0; normal_checks=0; covariance_checks=0
    for n in range(3,16):
        expected=comb(n,n//2) if n%2==0 else n*comb(n-1,(n-1)//2)
        count=0; sF=0; minF=10**100; min_count=0
        numer_cov=[[0]*n for _ in range(n)] if n<=9 else None
        for d in words(n):
            assert d.count(0)==(n%2) and sum(d)==0
            f=centered_num(d)
            F=sum(v*v for v in f) # n^2 ||normal||^2
            count+=1;sF+=F
            if F<minF:minF=F;min_count=1
            elif F==minF:min_count+=1
            if numer_cov is not None:
                for i in range(n):
                    for j in range(n):
                        numer_cov[i][j]+=f[i]*f[j]
        assert count==expected
        pred_min=Fraction(n,4) if n%2==0 else Fraction(n*n-1,4*n)
        pred_mult=2 if n%2==0 else 2*n
        pred_mean=Fraction(n*(n+1),12) if n%2==0 else Fraction(n*n-1,12)
        assert Fraction(minF,n*n)==pred_min, (n,minF,pred_min)
        assert min_count==pred_mult,(n,min_count)
        assert Fraction(sF,count*n*n)==pred_mean,(n,sF,pred_mean)
        if numer_cov is not None:
            c=Fraction(n,n-1) if n%2==0 else Fraction(1)
            for i in range(n):
                for j in range(n):
                    k=abs(i-j)
                    Lplus=Fraction(n*n-1,12*n)-Fraction(k*(n-k),2*n)
                    assert Fraction(numer_cov[i][j],count*n*n)==c*Lplus,(n,i,j)
                    covariance_checks+=1
        normal_checks+=count
        print(f'n={n} facets={count} min_norm_sq={pred_min} outermost_count={min_count} mean_norm_sq={pred_mean}')
    for n in range(3,10):
        brute=[]
        for d in product((-1,0,1),repeat=n):
            if sum(d)!=0:continue
            if sum(z!=0 for z in d)<n-1:continue
            brute.append(d)
        assert set(brute)==set(words(n)),n
        word_checks+=len(brute)
    print(f'CYCLE_FACET_WATSON_PASS exact_facets={normal_checks} brute_word_facets={word_checks} exact_covariance_entries={covariance_checks}')
if __name__=='__main__': test()
