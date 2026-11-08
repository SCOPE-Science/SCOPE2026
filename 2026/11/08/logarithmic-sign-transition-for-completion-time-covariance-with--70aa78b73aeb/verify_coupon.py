from fractions import Fraction
from functools import lru_cache
from math import factorial

def mu(n,r):
 # Coefficients of the exact exponential-moment generating function.
 a=[Fraction(1)]+[Fraction(0)]*r
 for k in range(2,n+1):
  old=a[:]
  for j in range(1,r+1):
   a[j]=sum(old[j-h]*Fraction(1,k**h) for h in range(j+1))
 return a[r]*factorial(r)

def dp(n,r):
 @lru_cache(None)
 def fg(st):
  if st[0]==0: return Fraction(st[r]),Fraction(0)
  s=Fraction(0); u=Fraction(0)
  for j in range(r+1):
   if st[j]:
    ls=list(st);ls[j]-=1;ls[j+1]+=1
    f,g=fg(tuple(ls)); s+=st[j]*f; u+=st[j]*g
  denominator=n-st[r+1]
  f=s/denominator
  g=(n*f+u)/denominator
  return f,g
 start=(n,)+(0,)*(r+1)
 return fg(start)


def main():
    comparisons=0
    for n in range(2,9):
        for r in range(1,7):
            f,g=dp(n,r)
            H=sum((Fraction(1,k) for k in range(1,n+1)),Fraction())
            m0=mu(n,r);m1=mu(n,r+1)
            assert f==Fraction(1 if r==1 else 0)+m0/factorial(r)
            assert g-n*H*f==n*(m1-H*m0)/factorial(r)
            comparisons+=2
    for n in range(2,33):
        H=sum((Fraction(1,k) for k in range(1,n+1)),Fraction())
        ratios=[mu(n,r+1)/mu(n,r) for r in range(1,13)]
        assert ratios[0]<H
        assert all(a<b for a,b in zip(ratios,ratios[1:]))
        comparisons+=12
    # The r=2 zero boundary is real, not a numerical tolerance.
    assert Fraction(mu(2,3),mu(2,2))==Fraction(3,2)
    comparisons+=1
    print(f"PASS: {comparisons} exact assertions; independent truncated-count state recursion versus Poissonized moments")

if __name__=='__main__': main()
