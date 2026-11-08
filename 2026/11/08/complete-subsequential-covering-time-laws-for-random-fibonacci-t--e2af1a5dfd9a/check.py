"""Standalone exact checks for subsequential laws of random Fibonacci tiling coverage.
Requires only Python 3's standard library.
"""
from fractions import Fraction
from itertools import product

COUNT = 0

def eq(a,b):
    global COUNT
    assert a==b, (a,b)
    COUNT += 1

def fib(d, top):
    F=[1]*d
    for n in range(d,top+1):
        F.append(F[n-1]+F[n-d])
    return F

def weights(d,r,m):
    F=fib(d,d-1+r+(m-1)*d)
    return [F[d-1+r+j*d] for j in range(m)]

def sum_rank(w, rank):
    return sum(v for j,v in enumerate(w) if rank & (1<<j))

def minimal_m(d,r,delta):
    m=0
    while sum(weights(d,r,m)) < delta:
        m+=1
    return m

def failures(d,r,delta,m):
    w=weights(d,r,m)
    return sum(sum_rank(w,rank)<delta for rank in range(1<<m))

def canonical(d,r,delta):
    m=minimal_m(d,r,delta)
    w=weights(d,r,m)
    return m, failures(d,r,delta,m)

def tail(d,r,delta,m):
    if delta==0: return Fraction(0)
    n,R=canonical(d,r,delta)
    return Fraction(1) if m<n else Fraction(R,2**m)

def cdf_point(d,delta,steps):
    return product_fraction([1-tail(d,r,delta[r],(steps+d-1-r)//d) for r in range(d)])

def product_fraction(xs):
    a=Fraction(1)
    for x in xs: a*=x
    return a

def direct_cdf(d,delta,steps):
    ws=[weights(d,r,(steps+d-1-r)//d) for r in range(d)]
    success=0
    for coin in product((0,1),repeat=steps):
        fine=True
        for r in range(d):
            if delta[r]>0:
                v=sum(w for j,w in enumerate(ws[r]) if coin[r+j*d]==1)
                if v<delta[r]: fine=False;break
        success+=fine
    return Fraction(success,2**steps)

# Independent brute counts for the canonical-rank lemma and its permanent failing count.
for d in range(2,6):
    for r in range(d):
        for m in range(1,7):
            w=weights(d,r,m)
            if m>1: eq(w[-1]>sum(w[:-1]),True)
            choices=sorted(set(x for x in [1 << (m-1),(1<<m)-1,(1<<(m-1))+1,(3*(1<<m))//4] if (1<<(m-1))<=x<(1<<m)))
            for R in choices:
                delta=sum_rank(w,R)
                eq(sum(w[:-1])<delta<=sum(w),True)
                eq(canonical(d,r,delta),(m,R))
                for n in range(m,min(m+3,9)+1):
                    eq(failures(d,r,delta,n),R)
                for n in range(max(0,m-2),m):
                    eq(failures(d,r,delta,n),1<<n)

# Directly enumerate all 2^steps placement words rather than reusing the rank formula.
for d in range(2,5):
    ds=[tuple((r+1)*z for r in range(d)) for z in (1,2,4)]
    ds += [tuple(0 if r%2 else 3 for r in range(d)),tuple(5 if r==0 else 0 for r in range(d))]
    for delta in ds:
        for steps in range(0,10):
            eq(direct_cdf(d,delta,steps),cdf_point(d,delta,steps))

# Every dyadic parameter in [1/2,1) appears EXACTLY at arbitrarily large indices.
for d in range(2,5):
    for r in range(d):
        for target in (Fraction(1,2),Fraction(5,8),Fraction(3,4),Fraction(7,8),Fraction(15,16)):
            for m in range(5,12):
                R=target * 2**m
                eq(R.denominator,1)
                delta=sum_rank(weights(d,r,m),int(R))
                eq(canonical(d,r,delta),(m,int(R)))
                for k in range(0,6):
                    eq(tail(d,r,delta,m+k),target*Fraction(1,2**k))

# Arbitrary asymptotic parameter families: construct targets with prescribed offsets and
# verify the entire centered law at every sufficiently large stage for dyadic kappa.
def make_target(d, anchor, active, params, M):
    # active maps coordinate r -> finite nonnegative offset h_r, h_anchor=0
    ms={}
    delta=[0]*d
    B=anchor+1+d*(M-1)
    for r,h in active.items():
        assert h==0 and r==anchor or (h>0 and (h-anchor+r)%d==0)
        m=(B-h-(r+1))//d+1
        assert m>=1
        ms[r]=m
        k=params[r]
        R=int(k*2**m)
        assert Fraction(R,2**m)==k
        delta[r]=sum_rank(weights(d,r,m),R)
        eq(canonical(d,r,delta[r]),(m,R))
        eq(B-(r+1+d*(m-1)),h)
    return tuple(delta),B,ms

def limiting_cdf(d,active,params,z):
    if z<0: return Fraction(0)
    return product_fraction(Fraction(1)-params[r]*Fraction(1,2**((z+h)//d)) for r,h in active.items())

for d,anchor,active,params in (
    (2,0,{0:0,1:1},{0:Fraction(3,4),1:Fraction(5,8)}),
    (2,1,{1:0,0:1},{0:Fraction(7,8),1:Fraction(1,2)}),
    (3,0,{0:0,1:2,2:1},{0:Fraction(1,2),1:Fraction(3,4),2:Fraction(7,8)}),
    (3,2,{2:0,0:2},{2:Fraction(15,16),0:Fraction(5,8)}),
    (4,1,{1:0,0:1,3:2},{1:Fraction(7,8),0:Fraction(3,4),3:Fraction(1,2)}),
):
    for M in (7,8,9,10):
        delta,B,ms=make_target(d,anchor,active,params,M)
        for z in range(0,19):
            eq(cdf_point(d,delta,B+z),limiting_cdf(d,active,params,z))
print(f"PASS: {COUNT} exact assertions")
