#!/usr/bin/env python3
"""Exact integer-checker for the four-colour surjection Walsh theorem.

No dependencies outside Python standard library.  The test constructs the set
of onto words directly and independently transforms its indicator; the
closed formula is evaluated separately for every character.
"""
from math import factorial

def predicted(n, b):
    z = b.count(0)
    k = n-z
    s = 0
    for v in b: s ^= v
    if s: return 0
    if not k: return 4**n - 4*3**n + 6*2**n - 4
    v = -4*(1 + (-1)**k * 3**z)
    if len(set(b)-{0}) == 1: v += 2**(n+1)
    return v

def fast_walsh(a):
    step=1
    N=len(a)
    while step<N:
        for p in range(0,N,2*step):
            for j in range(p,p+step):
                u=a[j];v=a[j+step]
                a[j]=u+v; a[j+step]=u-v
        step*=2

def test(n):
    N=1<<(2*n)
    a=[0]*N
    for x in range(N):
        w=x; seen=0
        for _ in range(n):
            seen |= 1 << (w & 3)
            w >>= 2
        a[x] = int(seen == 15)
    fast_walsh(a)
    rank=0; min_gap=None
    for f,actual in enumerate(a):
        w=f; b=[]
        for _ in range(n):
            b.append(w & 3); w >>= 2
        expected=predicted(n,b)
        assert actual == expected,(n,f,actual,expected)
        if actual:
            rank+=1
            av=abs(actual)
            min_gap=av if min_gap is None else min(av,min_gap)
    extras=(3**n-3)//4 if n%2 else 0
    assert rank==4**(n-1)-extras,(n,rank)
    assert min_gap==(16 if n%2 else 8),(n,min_gap)
    print('n=%d frequencies=%d rank=%d sharp_gap=%d surjections=%d' %(n,N,rank,min_gap,a[0]))

def check_projection(n):
    N=4**n
    e=[0]*N
    for b in range(N):
        digits=[]; v=b
        for _ in range(n):
            digits.append(v & 3); v >>= 2
        counts=[digits.count(x) for x in range(4)]
        e[b] = int(counts[0]==0 and all(counts[x]%2==1 for x in (1,2,3)))
    Ecount=sum(e)
    fast_walsh(e)
    diag={sum(c<<(2*j) for j in range(n)) for c in range(4)}
    projection_numerator=[(N//4 if x in diag else 0)-e[x] for x in range(N)]
    abs_sum=sum(abs(v) for v in projection_numerator)
    from fractions import Fraction
    norm=Fraction(abs_sum,N)
    if n%2:
        x=1 | (2<<2)
        assert e[x] == (3**(n-2)+5)//4,(n,e[x])
        assert projection_numerator[x]<0
        assert norm>1
    else:
        assert Ecount==0 and norm==1
    print('projection n=%d norm=%s E=%d'%(n,norm,Ecount))
    if n==5:assert norm==Fraction(91,16)
    if n==7:assert norm==Fraction(14107,1024)

if __name__=='__main__':
    for n in range(4,10): test(n)
    for n in range(4,8): check_projection(n)
    print('QUATERNARY_SURJECTION_WALSH_EXACT_PASS')
