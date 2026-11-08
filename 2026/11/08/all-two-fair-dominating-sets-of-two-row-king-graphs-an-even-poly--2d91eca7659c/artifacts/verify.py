"""Independent finite checks of the 2-fair polynomial for two-row king graphs.
Only finite samples are checked; the unrestricted conclusion uses the accompanying proof.
Run with: python3 artifacts/verify.py
"""
from itertools import combinations, product
from math import comb


def formula(n):
    assert n >= 1
    out = {}
    for k in range(1, n + 1):
        ways = 0
        for a in range(k):
            for b in (0, 1):
                for c in (0, 1):
                    if n == 3*k - 2 - 2*a + b + c:
                        ways += comb(k-1, a)
        if ways:
            out[2*k] = out.get(2*k, 0) + ways
    if n % 3 == 2:
        k = (n+1)//3
        out[2*k] = out.get(2*k, 0) + 4**k
    return out


def word_census(n):
    out={}
    for s in product((0,1,2), repeat=n):
        if all(s[i] == 2 or (s[i-1] if i else 0)+s[i]+(s[i+1] if i+1<n else 0)==2 for i in range(n)):
            size=sum(s)
            weight=2**sum(i==1 for i in s)
            out[size]=out.get(size,0)+weight
    return out


def graph_census(n):
    vert=[(r,j) for j in range(n) for r in range(2)]
    out={}
    for mask in range(1<<(2*n)):
        chosen=[v for i,v in enumerate(vert) if mask>>i&1]
        valid=True
        for i,(r,j) in enumerate(vert):
            if mask>>i&1: continue
            count=sum(abs(r-a)<=1 and abs(j-b)<=1 for a,b in chosen)
            if count!=2:
                valid=False;break
        if valid:
            k=mask.bit_count(); out[k]=out.get(k,0)+1
    return out


def minimum_count(n):
    m=(n+2)//3
    if n%3==0:return 1
    if n%3==1:return (n-1)//3+1
    return 4**m+2


def main():
    for n in range(1,10):
        a=formula(n); b=graph_census(n)
        assert a==b,(n,a,b)
        print('DIRECT_GRAPH_OK',n,sorted(a.items()))
    for n in range(1,13):
        a=formula(n);b=word_census(n)
        assert a==b,(n,a,b)
    print('ALL_TERNARY_WORDS_OK n=1..12')
    for n in range(1,201):
        p=formula(n)
        m=(n+2)//3
        assert min(p)==2*m
        assert p[2*m]==minimum_count(n)
        assert all(k%2==0 for k in p)
    print('MINIMUM_RESIDUE_AND_PARITY_OK n=1..200')
    print('VERIFY_OK')

if __name__=='__main__': main()
