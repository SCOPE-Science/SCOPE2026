"""Standalone exact checks for the dyadic valuation-covariance theorem.
Run with Python 3, no third-party modules: python3 CHECK.py
"""
from fractions import Fraction
from math import comb, factorial

def nu2(n):
    assert n>0
    return (n & -n).bit_length()-1

def local_kernel(d):
    if d==0:
        return Fraction(2)
    return Fraction(2)-Fraction(3,2**nu2(abs(d)))

def overlap(w,q,h):
    a,r=divmod(w,q)
    t=h%q
    intersect=max(0,r-t)+max(0,r-(q-t))
    return q*a*a+2*a*r+intersect

def corr(w,h):
    return sum((w-abs(t))*local_kernel(h+t) for t in range(1-w,w))

def covariance_from_arcs(w,h):
    M=(h+w).bit_length()+1
    out=Fraction(-w*w)
    for k in range(1,M):
        out+=Fraction(3*overlap(w,1<<k,h),1<<k)
    out+=Fraction(3*max(0,w-h),1<<(M-1))
    return out

checks=0
for w in range(1,81):
    P=1<<(1+(w-1).bit_length())
    var=corr(w,0)
    assert var>0
    assert corr(w,w)==-var/2
    checks+=2
    for h in range(1,2*P+1):
        co=covariance_from_arcs(w,h)
        assert co>=-var/2,(w,h,co,var)
        assert (co==-var/2)==(h%P in {w%P,(-w)%P}),(w,h,co,var)
        checks+=2
    for h in [0,1,w,w+1,2*w+3,P-1,P,P+w]:
        assert covariance_from_arcs(w,h)==corr(w,h),(w,h)
        checks+=1
    for k in range(1,(2*w+1).bit_length()+3):
        q=1<<k
        assert overlap(w,q,w)==min(overlap(w,q,h) for h in range(q))
        checks+=1

# Check the supplied integral-coefficient definition and its valuation identity
# at a small grid, without using the cited theorem in the numerical computation.
for l in range(1,7):
    for m in range(l,13):
        S=sum(2**k*comb(2*m-2*k,m-k)*comb(m+k,m)*comb(k,l)
              for k in range(l,m+1))
        A=Fraction(factorial(l)*factorial(m)*S,2**(m-l))
        assert A.denominator==1
        val=nu2(A.numerator)
        target=l+sum(nu2(j) for j in range(m-l+1,m+l+1))
        assert val==target,(l,m,val,target)
        checks+=1
print('ALL EXACT CHECKS PASS',checks)
for l in [1,3,5,11,15]:
    w=2*l;P=1<<(1+(w-1).bit_length())
    print('l',l,'P',P,'variance',corr(w,0),'minimum covariance',corr(w,w),'equality shifts modulo P',sorted({w,P-w}))
