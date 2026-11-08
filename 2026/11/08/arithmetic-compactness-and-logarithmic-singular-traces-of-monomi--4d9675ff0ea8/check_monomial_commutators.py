"""Standalone finite checks for monomial composition adjoint commutators on Bergman spaces.
All tests are finite corroboration; infinite assertions have analytic proofs elsewhere.
"""
import math
from fractions import Fraction
from math import gcd, lgamma, exp
checks=0

def checked(c):
 global checks
 assert c
 checks+=1

def h(k, alpha):
 return exp((lgamma(alpha+2)+lgamma(k+1)-lgamma(k+alpha+2))/2)

def w(r,k,alpha):
 return h(r*k,alpha)/h(k,alpha)

def coefficient(m,n,q,alpha):
 g=gcd(m,n);a=m//g;b=n//g
 # column e_{bq}, output e_{aq}
 other=w(m,b*q,alpha)*w(n,a*q,alpha)
 return (w(n,q//g,alpha)*w(m,q//g,alpha) if q%g==0 else 0)-other

for m in range(2,10):
 for n in range(2,10):
  g=gcd(m,n);a=m//g;b=n//g
  for q in range(1,21):
   # Exact index arithmetic for the two product branches
   k=b*q
   checked((k % n==0)==(q%g==0))
   checked((m*k % n==0))
   checked((m*k//n)==a*q)
   if g==1:
    # rational numerator for alpha =0
    numerator=(q+1)*(m*n*q+1)-(m*q+1)*(n*q+1)
    checked(numerator==q*(m-1)*(n-1))
    exact=(m-1)*(n-1)*q/((m*n*q+1)*math.sqrt((m*q+1)*(n*q+1)))
    checked(abs(coefficient(m,n,q,0)-exact)<2e-12)
   else:
    checked(q%g!=0 or abs(coefficient(m,n,q,0))<1)

for alpha in [0,1,2,-0.5,0.4]:
 delta=alpha+1
 for m,n in [(2,3),(3,4),(4,5),(7,11)]:
  C=(m*n)**(-delta/2)*delta*(delta+1)/2*(1-1/m)*(1-1/n)
  for q in [1000,10000,100000]:
   # moderately tolerant for floating loggamma cancellation
   got=coefficient(m,n,q,alpha)*q
   checked(abs(got-C)<0.03*C)
for alpha in [0,1,-0.5]:
 for m,n in [(2,2),(4,6),(6,10),(2,4)]:
  g=gcd(m,n);a=m//g;b=n//g
  C=(m*n)**(-(alpha+1)/2)
  for q in [1000,10000,50000]:
   if q%g==0:q+=1
   val=abs(coefficient(m,n,q,alpha))
   checked(abs(val-C)<.015*C)

# Exact rational identity for standard Bergman using independent products
for m,n in [(2,3),(3,5),(4,7),(5,8),(7,11)]:
 for q in range(1,100):
  A2=Fraction((q+1)**2,(m*q+1)*(n*q+1))
  B2=Fraction((m*q+1)*(n*q+1),(m*n*q+1)**2)
  checked(A2>B2)
  checked(Fraction((q+1)*(m*n*q+1)-(m*q+1)*(n*q+1))==Fraction(q*(m-1)*(n-1)))

print('MONOMIAL_BERGMAN_CHECK_OK',checks,'finite assertions')
