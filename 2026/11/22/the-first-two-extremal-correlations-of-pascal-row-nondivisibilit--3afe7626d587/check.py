"""Finite arithmetic checks for odd-prime Pascal-row shift correlations."""
from fractions import Fraction
from functools import lru_cache


def weights(p):
    B=sum((j+1)**2 for j in range(p))
    U=[sum((d+1)*((d+a)%p+1) for d in range(p) if d+a<p) for a in range(p)]
    V=[sum((d+1)*((d+a)%p+1) for d in range(p) if d+a>=p) for a in range(p)]
    return B,U,V


def digit_count(n,p):
    prod=1
    while n:
        n,d=divmod(n,p)
        prod*=d+1
    return prod


def check_p(p, L):
    B,U,V=weights(p)
    arr=[digit_count(n,p) for n in range(p**L)]
    @lru_cache(None)
    def recurrence(l,h):
        if l==0:return 1
        t,a=divmod(h,p)
        return U[a]*recurrence(l-1,t)+V[a]*recurrence(l-1,t+1)
    direct_count=0
    for h in range(min(p**L,2*p*p+9)):
        direct=sum(v*arr[(n+h)%(p**L)] for n,v in enumerate(arr))
        assert direct==recurrence(L,h),(p,L,h,direct,recurrence(L,h))
        direct_count+=1
    return direct_count


def check_fine(p, cutoff):
    # Modular Pascal recursion, without using base-p digits.
    prev=[1]
    for n in range(cutoff):
        assert sum(v%p!=0 for v in prev)==digit_count(n,p),(p,n)
        prev=[1]+[(prev[j-1]+prev[j])%p for j in range(1,len(prev))]+[1]


def check_limit(p, cutoff):
    B,U,V=weights(p)
    c1=Fraction(2*(p+1),2*p+5)
    c2=Fraction(4*p**4+4*p**3+11*p*p+11*p+18, p*(p+1)*(2*p+1)*(2*p+5))
    @lru_cache(None)
    def C(h):
        if h==0:return Fraction(1)
        if h==1:return c1
        t,a=divmod(h,p)
        return Fraction(U[a]*C(t)+V[a]*C(t+1),B)
    for h in range(1,cutoff):
        # All nonzero shifts have upper bound c1; non-power shifts <= c2.
        t=h
        while t%p==0:t//=p
        if t==1:assert C(h)==c1,(p,h,C(h),c1)
        elif t==2:assert C(h)==c2,(p,h,C(h),c2)
        else: assert C(h)<c2,(p,h,C(h),c2)
    assert c1>c2>0
    for a in range(1,p):
        assert U[a]+V[a]==B-p*a*(p-a)//2
    return str(c1),str(c2)

if __name__=='__main__':
    for p,L,maxh in [(3,7,600),(5,5,700),(7,4,500),(11,3,500)]:
        checks=check_p(p,L)
        check_fine(p,min(p**L,500))
        t=check_limit(p,maxh)
        print('PASS',p,'L',L,'direct_cyclic_shifts',checks,'direct_row_checks',min(p**L,500),'shift_bounds',maxh-1,'top',t)
