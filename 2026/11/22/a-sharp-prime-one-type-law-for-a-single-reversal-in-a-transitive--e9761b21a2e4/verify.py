#!/usr/bin/env python3
"""Independent direct subset-based verification of the claimed prime extensions."""

def beats(i,j,n,p,q,b):
    if i == n:
        return ((b >> j) & 1) == 0
    if j == n:
        return ((b >> i) & 1) == 1
    if (min(i,j),max(i,j)) == (p,q):
        return i > j
    return i < j

def prime(n,p,q,b):
    N=n+1
    for mask in range(1,2**N-1):
        block=[v for v in range(N) if mask & (1<<v)]
        if len(block)<2:continue
        for v in range(N):
            if v in block:continue
            if len({beats(v,w,n,p,q,b) for w in block})>1:break
        else:return False
    return True

def expected(n,p,q):
    if q==p+1:return int(n%2==0)
    return 6 if q-p==2 or (p==0 and q==n-1) else 8

def check():
    checks=0
    for n in range(4,9):
        for p in range(n):
            for q in range(p+1,n):
                actual=sum(prime(n,p,q,b) for b in range(1<<n))
                assert actual==expected(n,p,q),(n,p,q,actual)
                checks+=1
    print(f'INDEPENDENT_OK parameters={checks} n=4..8')
if __name__ == '__main__':check()
