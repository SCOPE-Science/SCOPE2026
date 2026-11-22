#!/usr/bin/env python3
"""Standalone exact/finite checks for an affine interval Markov family.

All finite checks are supplementary to the all-n analytic proof in RESULT.md.
Requires Python 3.9+ standard library only.
"""
from itertools import product
from collections import Counter
from math import comb, log


def counts(word):
    n = len(word)
    a = sum(word[j-1] == -1 and word[j] == 1 for j in range(1,n))
    b = sum(word[j-1] == 1 and word[j] == -1 for j in range(1,n))
    up = int(word[-2] == -1 and word[-1] == 1)
    down = int(word[-2] == 1 and word[-1] == -1)
    return a,b,up,down


def matrix(word):
    n = len(word)
    a = [[1]*n for _ in range(n)]
    for j in range(1,n):
        if word[j-1] == -1 and word[j] == 1:
            a[j][0] = 0
        elif word[j-1] == 1 and word[j] == -1:
            a[j][-1] = 0
    return a


def determinant_bareiss(A):
    a=[list(row) for row in A]
    n=len(a)
    sign=1; last=1
    for k in range(n-1):
        if a[k][k] == 0:
            for j in range(k+1,n):
                if a[j][k]:
                    a[k],a[j]=a[j],a[k]
                    sign=-sign
                    break
            else:
                return 0
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot - a[i][k]*a[k][j]
                assert numerator % last == 0
                a[i][j]=numerator//last
        for i in range(k+1,n):a[i][k]=0
        last=pivot
    return sign*a[-1][-1]


def poly(word,z):
    n=len(word)
    A,B,up,down=counts(word)
    return z**3-(n-down)*z**2+(A+B-n*down)*z+A*down-B*up


def perron(word):
    n=len(word)
    A,B,up,down=counts(word)
    def gap(lam):
        r = (1-1/lam) if up else (lam/(lam+1) if down else 1.0)
        return lam*(n-lam)-A-B*r
    lo=float(n-1);hi=float(n)
    assert gap(lo)>-1e-10 and gap(hi)<1e-10, (word,gap(lo),gap(hi))
    for _ in range(58):
        m=(lo+hi)/2
        if gap(m)>0:lo=m
        else:hi=m
    return (lo+hi)/2


def main():
    exact=0
    for n in range(3,9):
        for word in product((-1,1),repeat=n):
            M=matrix(word)
            for z in (n-1,n,n+2):
                direct=determinant_bareiss([[(z if i==j else 0)-M[i][j] for j in range(n)] for i in range(n)])
                assert direct == z**(n-3)*poly(word,z),(n,word,z,direct,poly(word,z))
                exact+=1
    print('Exact characteristic-polynomial determinant checks:',exact)
    seen=0
    for n in range(2,15):
        freq=Counter()
        best=(float('inf'),None)
        largest=(-float('inf'),None)
        for word in product((-1,1),repeat=n):
            k=sum(word[j]!=word[j-1] for j in range(1,n))
            typ='up' if word[-2:] == (-1,1) else ('down' if word[-2:] == (1,-1) else 'none')
            freq[(typ,k)]+=1
            lam=perron(word)
            if n>=3:
                A,B,up,down=counts(word)
                r=(1-1/lam) if up else (lam/(lam+1) if down else 1.0)
                vec=[1-(int(word[j-1]==-1 and word[j]==1)+int(word[j-1]==1 and word[j]==-1)*r)/lam for j in range(1,n)]
                vec=[1.0]+vec
                assert min(vec)>0
                assert abs(sum(vec)-lam)<1e-9
                M=matrix(word)
                assert max(abs(sum(M[i][j]*vec[j] for j in range(n))-lam*vec[i]) for i in range(n))<1e-8
            if lam<best[0]-1e-9:best=(lam,word)
            if lam>largest[0]+1e-9:largest=(lam,word)
            if n>=3:
                delta=n-lam
                entropy_loss=log(n/lam)
                assert abs(entropy_loss-k/n**2)<=2/n**2+1e-12,(n,word)
            seen+=1
        for k in range(n):
            if k<=n-2:assert freq[('none',k)]==2*comb(n-2,k)
            if k>=1:
                assert freq[('up',k)]==comb(n-2,k-1)
                assert freq[('down',k)]==comb(n-2,k-1)
        expected=tuple(-1 if j%2==0 else 1 for j in range(n))
        assert best[1]==expected, (n,best)
        assert abs(largest[0]-n)<1e-8
        print('n=%d min_root=%.10f max_root=%.10f unique_min=%s' % (n,best[0],largest[0],''.join('-' if v==-1 else '+' for v in best[1])))
    print('Exhaustive orientation-word checks:',seen)
    print('All finite tests passed (not a replacement for the infinite-n proof).')

if __name__=='__main__':main()
