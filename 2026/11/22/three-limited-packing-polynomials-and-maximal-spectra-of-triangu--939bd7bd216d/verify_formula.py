"""Exact symbolic coefficient calculation for three-limited packings of L(K_n).
Uses labelled component counts, without graph subset enumeration.
"""
from math import comb, factorial

def matchings(n):
    return {k: factorial(n)//(factorial(n-2*k)*2**k*factorial(k)) for k in range(n//2+1)}

def add_poly(target, factor, extra, offset, n):
    for k,val in matchings(n-extra).items():
        target[k+offset] = target.get(k+offset,0)+factor*val

def all_counts(n):
    c={}
    add_poly(c,1,0,0,n)
    if n>=3:
        add_poly(c,3*comb(n,3),3,2,n) # P3, center chosen among 3
        add_poly(c,comb(n,3),3,3,n) # triangle
    if n>=4:
        add_poly(c,12*comb(n,4),4,3,n) # P4, 4!/2
        c[3]=c.get(3,0)+4*comb(n,4) # K1,3, no matching
    return c

def maximal_counts(n):
    if n==3:return {3:1}
    counts={}
    def add(k,v): counts[k]=counts.get(k,0)+v
    add(3,n*comb(n-1,3))
    if n%2:
        m=(n-1)//2
        add(m+2, factorial(n)//(6*2**(m-1)*factorial(m-1)))
        add(m+1, factorial(n)//(2**(m-1)*factorial(m-2)))
    else:
        m=n//2
        add(m+1, 4*factorial(n)//(6*2**(m-2)*factorial(m-2)))
    return {k:v for k,v in counts.items() if v}

for n in range(3,12):
    a=all_counts(n); b=maximal_counts(n)
    print(f'{n}\t'+','.join(f'{k}:{v}' for k,v in sorted(a.items()))+'\t'+','.join(f'{k}:{v}' for k,v in sorted(b.items())))
