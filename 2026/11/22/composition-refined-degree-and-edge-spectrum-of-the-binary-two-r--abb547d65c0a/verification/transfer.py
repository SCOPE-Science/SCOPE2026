"""Formal two-state block expansion, independent of deletion-set enumeration."""
from collections import Counter, defaultdict
from math import comb
from itertools import product


def matrix_histograms(max_n):
    # Paths of maximal alternating blocks: the next block begins with the previous block's final symbol.
    paths = [defaultdict(int) for _ in range(max_n + 1)]
    for first in (0, 1):
        for length in range(1, max_n + 1):
            bits = [first ^ (j & 1) for j in range(length)]
            paths[length][(sum(bits), length * length // 4, bits[-1])] += 1
    # Paths here are built in increasing total length, always appending one whole block.
    for size in range(1, max_n + 1):
        for (weight, degree, last), multiplicity in list(paths[size].items()):
            for length in range(1, max_n - size + 1):
                bits = [last ^ (j & 1) for j in range(length)]
                paths[size + length][(weight + sum(bits), degree + length * length // 4, bits[-1])] += multiplicity
    return [Counter({(k, d): sum(v for (kk, dd, last), v in hist.items() if (kk, dd) == (k,d))
                     for (k,d,last) in hist}) for hist in paths]


def edges(n,k):
    return sum((n - 2*t + 1) * comb(n - 2*t, k-t) for t in range(1,n//2+1) if 0<=k-t<=n-2*t)


def cross(n,k):
    return sum((n - 2*t) * comb(n-2*t-1,k-t) for t in range(1,(n-1)//2+1) if 0<=k-t<=n-2*t-1)


def main():
    fs=matrix_histograms(24)
    for n in range(1,25):
        dist=fs[n]
        assert sum(dist.values()) == 2**n, (n,sum(dist.values()))
        for k in range(n+1):
            assert sum(ct for (w,d),ct in dist.items() if w==k) == comb(n,k),(n,k,'weight')
            total=sum(d*ct for (w,d),ct in dist.items() if w==k)
            assert total == 2*edges(n,k),(n,k,'degree sum')
            r,s=min(k,n-k),max(k,n-k)
            assert max(d for (w,d),ct in dist.items() if w==k and ct>0) == r*min(s,r+1)
        assert sum(edges(n,k) for k in range(n+1))+sum(cross(n,k) for k in range(n)) == (0 if n==1 else 1+(n-2)*2**(n-1))
        print(f'n={n:2d} distribution-cells={len(dist):4d} total={2**n:8d} verified')
    # Independent direct enumeration of words and even alternating intervals.
    for n in range(1, 14):
        observed=Counter()
        for bits in product((0,1),repeat=n):
            d=0
            for i in range(n):
                for j in range(i+1,n,2):  # even substring lengths
                    if all(bits[h] != bits[h+1] for h in range(i,j)):
                        d+=1
            observed[(sum(bits),d)] +=1
        assert observed==fs[n], (n,'histogram mismatch')
    print('PASS formal block coefficients through length 24 and independent direct histograms through length 13')

if __name__=='__main__':main()
