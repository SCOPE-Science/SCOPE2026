#!/usr/bin/env python3
"""Exact tests for the minimal-dominating-set Fourier theorem on bicliques.

Run: python3 check.py
Only the standard library is needed. No floating-point arithmetic is used.
"""
from math import comb


def predicted(m, n, i, j):
    return (m - 2*i)*(n - 2*j) + (-1)**i + (-1)**j


def predicted_zeros(m, n):
    if m % 2 and n % 2:
        return 0
    if m % 2 == 0 and n % 2 == 0:
        a,b=m//2,n//2
        return comb(m,a)*2**(n-1) + comb(n,b)*2**(m-1) - (comb(m,a)*comb(n,b) if (a+b)%2 else 0)
    if m % 2 == 0:
        a,b=m//2,(n-1)//2
        return comb(m,a)*2**(n-1) + comb(m,a-1)*comb(n,b)
    return predicted_zeros(n,m)


def dominates(mask, m, n):
    left=mask & ((1<<m)-1)
    right=mask >> m
    return (left and right) or left == ((1<<m)-1) or right == ((1<<n)-1)


def enumerate_minimal(m,n):
    return [x for x in range(1<<(m+n))
            if dominates(x,m,n) and all(not dominates(x ^ (1<<k),m,n)
                                            for k in range(m+n) if x & (1<<k))]


def run():
    total=0
    for m in range(2,7):
        for n in range(2,7):
            support=enumerate_minimal(m,n)
            expected={((1<<m)-1), (((1<<n)-1)<<m)}
            expected.update((1<<i)|(1<<(m+j)) for i in range(m) for j in range(n))
            assert set(support)==expected,(m,n,"classification")
            freq=[]
            for w in range(1<<(m+n)):
                explicit=sum(1 if ((x&w).bit_count()%2==0) else -1 for x in support)
                i=(w&((1<<m)-1)).bit_count()
                j=(w>>m).bit_count()
                predicted_w=predicted(m,n,i,j)
                assert explicit==predicted_w, (m,n,w,explicit,predicted_w)
                freq.append(explicit)
                total+=1
            z=sum(1 for v in freq if v==0)
            assert z==predicted_zeros(m,n), (m,n,z,predicted_zeros(m,n))
            assert min(abs(x) for x in freq if x) == (2 if m%2==0 or n%2==0 else 1)
            assert max(abs(x) for x in freq) == m*n+2
    # Larger parameters use a separate integer weighted-frequency census.
    for m in range(2,41):
        for n in range(2,41):
            z=sum(comb(m,i)*comb(n,j) for i in range(m+1) for j in range(n+1)
                  if predicted(m,n,i,j)==0)
            assert z==predicted_zeros(m,n), (m,n,z,predicted_zeros(m,n))
            least=min(abs(predicted(m,n,i,j)) for i in range(m+1) for j in range(n+1)
                      if predicted(m,n,i,j))
            assert least==(1 if m%2 and n%2 else 2), (m,n,least)
    print('MINIMAL_DOMINATION_BICLIQUE_WALSH_PASS', 'exact_coefficients=',total,
          'weighted_parameter_pairs=',39**2)


if __name__=='__main__':
    run()
