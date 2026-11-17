"""Exact labelled occupancy enumeration versus closed exponential generating function."""
from math import factorial
from itertools import product
from fractions import Fraction
from collections import defaultdict

def coeff_exponential(q,r,n):
    # Polynomial in u; each term (power, h-power, product of factors E^m, E-1, E-1-h)
    f=[0]*(2*q-1)
    F=factorial
    h=Fraction(1,F(r))
    def e(k,m):
        if m<0 or k<0:return Fraction(0)
        if m==0:return Fraction(int(k==0))
        return Fraction(m**k,F(k))
    def H(j): return h**j if j*r<=n else Fraction(0)
    def base(j,m):return H(j)*e(n-j*r,m)
    f[0]+=1 # e^z (all-zero configuration)
    for s in range(2,q):
        t=q-s
        f[t]+=F(n)*(e(n,t+1)-e(n,t))
    f[q-1]+=F(n)*(e(n,q)-e(n,q-1)-h*e(n-r,q-1))
    for j in range(1,q):
        f[j+q-2]+=F(n)*base(j,q-j-1)
        f[j+q-1]+=F(n)*(base(j,q-j)-base(j,q-j-1)-base(j+1,q-j-1))
    f[0]+=F(n)*H(q)*e(n-q*r,0)
    assert all(x.denominator==1 and x>=0 for x in f),(q,r,n,f)
    return tuple(map(int,f))

def occupancy_counts(q,r,n):
    d=defaultdict(int)
    f=factorial
    def part(total,k):
        if k==1:yield (total,)
        else:
            for a in range(total+1):
                for b in part(total-a,k-1):yield (a,)+b
    order=(1,0)+tuple(range(q-1,1,-1))
    for a in part(n,q):
        mul=f(n)
        for v in a:mul//=1 # keep integer once after all
        den=1
        for v in a:den*=f(v)
        mul//=den
        if all(a[i]==r for i in order):tau=0
        else:
            j=next(k for k,i in enumerate(order) if a[i]!=r)
            if j>=1:tau=j+q-1 if a[order[j]]>0 else j+q-2
            elif a[1]>0:tau=q-1
            else:
                alive=[s for s in range(2,q) if a[s]>0]
                tau=q-min(alive) if alive else 0
        d[tau]+=mul
    return tuple(d[i] for i in range(2*q-1))

checks=0
for q in range(3,8):
 for r in range(1,5):
  for n in range(1,18):
   x=coeff_exponential(q,r,n)
   y=occupancy_counts(q,r,n)
   assert x==y,(q,r,n,x,y)
   assert sum(x)==q**n,(q,r,n)
   if n>0:
    bound=min(2*q-2,q-1+(n-1)//r)-(n==q*r)
    assert max(k for k,v in enumerate(x) if v)==bound,(q,r,n,bound,x)
   checks+=1
print('CENSUS_OK',checks,'parameter_triples')
