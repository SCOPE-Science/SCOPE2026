"""Reproducible finite tests for expansive relations on reflexive chains.

No external packages. Run: python checker.py
"""
from collections import Counter
from itertools import combinations_with_replacement
from math import comb


def expansive(m, n, mask):
    """Definition: forward confluence and inverse forward confluence."""
    for i in range(m):
        for j in range(n):
            if not (mask >> (i*n+j)) & 1:
                continue
            for ii in range(i, m):
                if not any((mask >> (ii*n+jj)) & 1 for jj in range(j+1)):
                    return False
            for jj in range(j, n):
                if not any((mask >> (ii*n+jj)) & 1 for ii in range(i+1)):
                    return False
    return True


def row_col_total(m,n,mask):
    return all(any((mask >> (i*n+j)) & 1 for j in range(n)) for i in range(m)) and all(any((mask >> (i*n+j)) & 1 for i in range(m)) for j in range(n))


def profiles(m, n):
    """Exact weighted enumerator of all bi-total expansive correspondences."""
    out = Counter()
    alpha_options = list(combinations_with_replacement(range(n), m))
    beta_options = list(combinations_with_replacement(range(m), n))
    for alpha_forward in alpha_options:
        alpha = alpha_forward[::-1]
        for beta_forward in beta_options:
            beta = beta_forward[::-1]
            mandatory = {(i,alpha[i]) for i in range(m)} | {(beta[j],j) for j in range(n)}
            region = {(i,j) for i in range(m) for j in range(n) if j>=alpha[i] and i>=beta[j]}
            if not mandatory <= region:
                continue
            base=len(mandatory)
            for k in range(len(region)-base+1):
                out[base+k] += comb(len(region)-base,k)
    return out


def brute(m,n):
    d=Counter()
    for mask in range(1<<(m*n)):
        if row_col_total(m,n,mask) and expansive(m,n,mask):
            d[mask.bit_count()]+=1
    return d


def chain(m,n):
    """Build all edge counts by adding one edge at each step."""
    if m<n:
        raise ValueError("chain(m,n) requires m >= n; transpose when m < n")
    f=[n-1] * (m-n+1) + list(range(n-2,-1,-1))
    assert len(f)==m and f[0]==n-1 and f[-1]==0
    S={(i,f[i]) for i in range(m)}
    chain=[set(S)]
    for i in range(m):
        for j in range(f[i]+1,n):
            S.add((i,j))
            chain.append(set(S))
    for i in range(m-1,-1,-1):
        for j in range(f[i]-1,-1,-1):
            S.add((i,j))
            chain.append(set(S))
    assert len(chain)==m*n-m+1
    return chain


def transpose(coords,m,n):
    return {(j,i) for i,j in coords}


for m in range(1,5):
    for n in range(1,5):
        if m*n>16: continue
        expected=profiles(m,n)
        observed=brute(m,n)
        assert expected==observed, (m,n,expected,observed)
        assert set(expected)==set(range(max(m,n),m*n+1)), (m,n,expected)
        assert expected[max(m,n)]==comb(max(m,n)-1,min(m,n)-1)
        if m*n>max(m,n):
            assert expected[m*n-1]==m*n-m-n+2
        if m>=n:
            ch=chain(m,n)
        else:
            ch=[transpose(v,n,m) for v in chain(n,m)]
        assert len(ch)==m*n-max(m,n)+1
        for k,coords in enumerate(ch):
            assert len(coords)==max(m,n)+k
            mask=sum(1<<(i*n+j) for i,j in coords)
            assert row_col_total(m,n,mask) and expansive(m,n,mask)
print('Counts for square chains:', [(n,sum(profiles(n,n).values())) for n in range(1,5)])
print('FULL_CHECKS_OK')
