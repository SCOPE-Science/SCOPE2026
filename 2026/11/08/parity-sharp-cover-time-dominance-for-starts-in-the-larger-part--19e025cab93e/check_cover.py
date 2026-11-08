"""Exact cover-time checks for bipartite walks; Python standard library only."""
from fractions import Fraction
from functools import lru_cache
from math import factorial, comb

@lru_cache(None)
def stirling(k,n):
    if k==n==0:return 1
    if k==0 or n==0 or n>k:return 0
    return n*stirling(k-1,n)+stirling(k-1,n-1)

def F(n,k):
    return Fraction(factorial(n)*stirling(k,n),n**k)

def exact_cdf(a,b,start_in_A,t_end):
    n=a+b; full=(1<<n)-1
    start=0 if start_in_A else a
    d={(start,1<<start):Fraction(1)}
    out=[]
    for t in range(t_end+1):
        out.append(sum((p for (_,mask),p in d.items() if mask==full),Fraction(0)))
        nd={}
        for (u,mask),p in d.items():
            if u<a:
                other=range(a,a+b)
                denom=b
            else:
                other=range(a)
                denom=a
            for v in other:
                key=(v,mask|1<<v)
                nd[key]=nd.get(key,Fraction(0))+p/denom
        d=nd
    return out

def predicted(a,b,seed_A,t):
    k=t//2
    if t%2: return F(a,k+1)*F(b,k+1)
    return F(a,k+1)*F(b,k) if seed_A else F(a,k)*F(b,k+1)

def expected_gap_exact(a,b):
    # Inclusion-exclusion for the sum of two coupon CDF products.
    s=Fraction(0)
    for i in range(a+1):
        for j in range(b+1):
            if i==0 and j==0: continue
            x=Fraction(a-i,a); y=Fraction(b-j,b)
            s+=(-1)**(i+j)*comb(a,i)*comb(b,j)*(x-y)/(1-x*y)
    return s

def check():
    compared=0; strict=0
    for a in range(1,6):
        for b in range(1,6):
            da=exact_cdf(a,b,True,16)
            db=exact_cdf(a,b,False,16)
            for t in range(17):
                pa=predicted(a,b,True,t)
                pb=predicted(a,b,False,t)
                assert da[t]==pa,(a,b,t,da[t],pa)
                assert db[t]==pb,(a,b,t,db[t],pb)
                compared+=2
                if a>b and t%2==0 and t//2>=a-1:
                    assert da[t]>db[t],(a,b,t)
                    strict+=1
                if a>=b:assert da[t]>=db[t],(a,b,t)
                if t%2:assert da[t]==db[t],(a,b,t)
    for k in range(2,30):
        A=[factorial(n)*stirling(k,n) for n in range(k+1)]
        for n in range(2,k):
            assert A[n]*A[n]>A[n-1]*A[n+1]
    assert expected_gap_exact(3,2)==Fraction(7,10)
    for a in range(1,8):
        for b in range(1,a+1):
            gap=expected_gap_exact(a,b)
            if a==b: assert gap==0
            elif b==1: assert gap==1
            else: assert 0<gap<1
    print('PASS',compared,'direct Markov distribution comparisons,',strict,'strict parity checks, ordered-Bell coefficients through k=29, exact mean differences')
    print('K(3,2) first parity gap t=4:',predicted(3,2,True,4)-predicted(3,2,False,4))
if __name__=='__main__':check()
