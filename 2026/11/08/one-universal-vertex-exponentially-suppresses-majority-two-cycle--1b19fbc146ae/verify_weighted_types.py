#!/usr/bin/env python3
"""Independent compressed pair-type verification with multinomial weights."""
from math import factorial, comb


def weighted_types(n):
    fac=[factorial(i) for i in range(n+1)]
    for a in range(n+1):
        for b in range(n-a+1):
            h=n-a-b
            # 00-pairs a; 11-pairs b; mixed pairs h, each of two orientations
            yield a,b,h,fac[n]//(fac[a]*fac[b]*fac[h])*2**h


def compressed_step(n, extra, a,b,h,c):
    total=2*b+h+(c if extra else 0)
    if not extra:
        if total < n: return n,0,0,0
        if total > n: return 0,n,0,0
        return b,a,h,c  # 00 and 11 exchange, mixed stay
    if total < n: return n,0,0,0
    if total > n+1: return 0,n,0,1
    if total == n:
        return n-a,a,0,0  # old 00 become 11
    return b,n-b,0,1       # old 11 become 00; others become 11


def main():
    total_weight=0
    for n in range(2,61):
        for extra in (False,True):
            fixed=two=unperiodic=0
            for a,b,h,w in weighted_types(n):
                for c in ((0,1) if extra else (0,)):
                    s=(a,b,h,c)
                    f=compressed_step(n,extra,*s)
                    ff=compressed_step(n,extra,*f)
                    N=2*n+int(extra)
                    total=2*b+h+(c if extra else 0)
                    is_fixed = (total==0 or total==N or (not extra and h==n))
                    is_two = ((not extra and total==n and h<n)
                              or (extra and h==0 and total in (n,n+1)))
                    if is_fixed: fixed+=w
                    elif is_two: two+=w
                    else: unperiodic+=w
                    fff=compressed_step(n,extra,*ff)
                    ffff=compressed_step(n,extra,*fff)
                    assert (ffff==ff if extra else fff==f)
            assert fixed==(2 if extra else 2+2**n), (n,extra,'fixed',fixed)
            assert two==(2*comb(n,(n+1)//2) if extra else comb(2*n,n)-2**n),(n,extra,'two',two)
            assert fixed+two+unperiodic==2**(2*n+int(extra))
            total_weight+=fixed+two+unperiodic
        if n in (2,3,4,5,8,16,32,60):
            print('compressed type census passed at n=',n)
    print('PASS; all n=2..60; both families; total formal configuration weights=',total_weight)

if __name__=='__main__':main()
