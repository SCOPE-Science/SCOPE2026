"""Independent symbolic pair-type census and exact conditional moment verification."""
from collections import defaultdict
from fractions import Fraction
from math import comb

def C(n,r):return comb(n,r) if 0<=r<=n else 0

def by_types(m,k):
    A=defaultdict(int)
    # counts r11, r00, rmixed for k deleted pairs; unpaired vertices weight b
    for mixed in range(k+1):
      for both11 in range(k-mixed+1):
        both00=k-mixed-both11
        ways=C(k,mixed)*C(k-mixed,both11)*2**mixed
        b=m-mixed-2*both11
        if 0<=b<=2*m-2*k:
            A[mixed]+=ways*C(2*m-2*k,b)
    return A

for m in range(2,61):
 for k in range(m+1):
    dist=by_types(m,k)
    assert sum(dist.values())==C(2*m,m),(m,k)
    mean=Fraction(sum(j*c for j,c in dist.items()),C(2*m,m))
    assert mean==Fraction(k*m,2*m-1),(m,k,mean)
    var=Fraction(sum(j*j*c for j,c in dist.items()),C(2*m,m))-mean**2
    p=Fraction(m,2*m-1)
    covariance=Fraction(m,(2*m-1)**2*(2*m-3))
    assert var==k*p*(1-p)+k*(k-1)*covariance,(m,k,var)
    if k==m: assert dist[m]==2**m,(m,k)
    else: assert dist.get(m,0)==0,(m,k)
print('PASS: pair-type generating coefficient sums and exact first two moments for all 1888 cases m=2..60, 0<=k<=m')
