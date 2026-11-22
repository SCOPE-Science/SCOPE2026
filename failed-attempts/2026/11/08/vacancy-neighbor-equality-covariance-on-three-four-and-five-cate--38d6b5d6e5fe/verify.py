"""Exact independent checks for the vacancy/adjacent-equality covariance in uniform weak compositions."""
from fractions import Fraction
from math import comb

def stars(n,r):
    if r == 0:
        return int(n == 0)
    return comb(n+r-1,r-1) if n>=0 else 0

def equal_pair(n,r):
    return sum(stars(n-2*j,r-2) for j in range(n//2+1))

def theoretical(n,r):
    total=stars(n,r)
    return Fraction(r*(total*(2*stars(n,r-2)+(r-2)*equal_pair(n,r-1))-r*stars(n,r-1)*equal_pair(n,r)),total**2)

def closed(n,r):
    if r==3:
        return Fraction(0) if n%2==0 else Fraction(-6*(n-1),(n+1)*(n+2)**2)
    if r==4:
        return Fraction(24*n,(n+1)*(n+2)*(n+3)**2) if n%2==0 else Fraction(0)
    if r==5:
        return Fraction(10*n,(n+4)*(n+1)*(n+3)) if n%2==0 else Fraction(10*(n-1)*(n+6),(n+3)*(n+2)*(n+4)**2)
    raise ValueError

def compositions(n,m):
    if m==1:
        yield (n,)
    else:
        for k in range(n+1):
            for tail in compositions(n-k,m-1):
                yield (k,)+tail

def exhaustive(n,m):
    z=a=za=cnt=0
    for row in compositions(n,m):
        x=sum(v==0 for v in row)
        y=sum(row[i]==row[(i+1)%m] for i in range(m))
        z+=x;a+=y;za+=x*y;cnt+=1
    assert cnt==stars(n,m)
    return Fraction(za,cnt)-Fraction(z*a,cnt*cnt)

assertions=0
for m in range(3,6):
    for n in range(0,501):
        assert theoretical(n,m)==closed(n,m), (n,m)
        assertions+=1
        if 0<=n<=12:
            assert exhaustive(n,m)==theoretical(n,m), (n,m)
            assertions+=1
for m in range(6,9):
    for n in range(0,7):
        assert theoretical(n,m)==exhaustive(n,m), (n,m)
        assertions+=1
for n in range(2,501):
    assert (closed(n,3)<0 if n%2 else closed(n,3)==0)
    assert (closed(n,4)>0 if n%2==0 else closed(n,4)==0)
    assert closed(n,5)>0
    assertions+=3
print('PASS',assertions,'exact arithmetic and independently enumerated assertions')
