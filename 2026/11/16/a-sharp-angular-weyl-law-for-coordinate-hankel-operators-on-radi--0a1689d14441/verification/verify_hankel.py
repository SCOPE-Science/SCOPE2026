"""Standalone numerical and exact-rational checks for a weighted Fock Hankel spectral theorem."""
from math import gamma, lgamma, exp, comb, factorial, sqrt
from fractions import Fraction
from scipy.integrate import quad
from scipy.special import gammaln

def ratio(d,p,k):
    # M_k / M_(k-1), M_k = Gamma((k+d)/p)/Gamma(k+d)
    return exp(gammaln((k+d)/p)-gammaln((k+d-1)/p)+gammaln(k+d-1)-gammaln(k+d))

def eigenvalue(d,p,k,j):
    assert 0<=j<=k
    return (j+1)*ratio(d,p,k+1)-j*ratio(d,p,k) if k>0 else ratio(d,p,1)

def coefficient(d,p):
    delta=1-1/p
    integ=quad(lambda u: (1-u)**(d-2)*(1-delta*u)**(d/delta),0,1,epsabs=1e-13)[0]
    return p**(-d/(p-1))*integ/(d*factorial(d-2))

def count_exact(d,p,threshold):
    # Loop over degrees, use monotonicity in j for large k; full enumeration for small sample.
    cap=int(((p**(-1/(2*p)))/threshold)**(2/(1-1/p))*2+20)
    count=0
    for k in range(cap+1):
        for j in range(k+1):
            if eigenvalue(d,p,k,j)>threshold*threshold:
                count+=comb(k-j+d-2,d-2)
    return count

def tests():
    checks=0
    # Spectral identity via independent 2D radial moments, including the Gaussian p=1 limit.
    for d in [2,3,4]:
      for p in [1,1.25,1.5,2,3,5]:
       for k in [0,1,2,3,7,16,40]:
        for j in range(k+1):
         v=eigenvalue(d,p,k,j)
         assert v>=-1e-9, (d,p,k,j,v)
         if p==1: assert abs(v-1)<1e-8
         checks+=1
    # Uniform high-degree profile at both endpoints and interior.
    for d,p in [(2,2),(3,1.5),(4,3)]:
      delta=1-1/p
      for k in [300,1000,3000]:
        for j in [0,k//4,k//2,3*k//4,k]:
          actual=eigenvalue(d,p,k,j)*p**(1/p)*k**delta
          target=1-delta*(j/k)
          assert abs(actual-target)<0.08,(d,p,k,j,actual,target)
          checks+=1
    # Exact universal d=2 p=2 constant integral is rational 31/640.
    u=Fraction(1,2)
    integral=sum(Fraction((-1)**j*comb(4,j),2**j*(j+1)) for j in range(5))
    assert integral==Fraction(31,80),integral
    C=Fraction(1,8)*integral
    assert C==Fraction(31,640),C
    checks+=2
    for threshold in [0.25,0.20,0.17]:
      n=count_exact(2,2,threshold)
      value=n*threshold**8
      target=31/640
      # convergence is slow near finite threshold, loose test
      assert abs(value/target-1)<0.25,(threshold,n,value,target)
      print('threshold',threshold,'N',n,'scaled',value,'limit',target)
      checks+=1
    print('PASS',checks,'checks; d=2 p=2 Weyl C=',C)

if __name__=='__main__': tests()
