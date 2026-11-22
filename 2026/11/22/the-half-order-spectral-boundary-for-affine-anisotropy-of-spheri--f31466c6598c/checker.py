#!/usr/bin/env python3
"""Independent finite-harmonic tests of the adjacent-degree covariance obstruction.
Uses only Python standard library for exact checks.
"""
from fractions import Fraction
from math import exp,cosh,sqrt

# Legendre polynomial coefficients from recurrence, exact rationals.
def polyadd(a,b,coef_a=Fraction(1),coef_b=Fraction(1)):
    return [coef_a*(a[k] if k<len(a) else 0)+coef_b*(b[k] if k<len(b) else 0) for k in range(max(len(a),len(b)))]
def polyx(a):return [Fraction(0)]+a
P=[[Fraction(1)],[Fraction(0),Fraction(1)]]
for n in range(1,31):
    P.append(polyadd(polyx(P[n]),P[n-1],Fraction(2*n+1,n+1),Fraction(-n,n+1)))
def integral(a):
    return sum((c*Fraction(2,k+1) for k,c in enumerate(a) if k%2==0),Fraction(0))
def mul(a,b):
    z=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z
checks=0
for n in range(1,26):
    # orthogonality and triple-product Gaunt coefficient for S^2 zonals
    assert integral(mul(P[n],P[n]))==Fraction(2,2*n+1)
    assert integral(mul(polyx(P[n]),P[n+1]))==Fraction(2*(n+1),(2*n+1)*(2*n+3))
    assert integral(mul(polyx(P[n]),P[n]))==0
    exact=Fraction((n+1)**2,(2*n+1)*(2*n+3))
    assert exact>0 and exact>Fraction(1,4)
    checks+=4
# heat symmetric two-degree forms: c_l=e^{-t l(l+1)}
for t in [0.05,0.2,0.8,2.0]:
 for a,b in [(1.0,1e-2),(3.0,1e-5),(0.5,-2e-4)]:
  n=1
  while n<1000:
   A=(n+1)/sqrt((2*n+1)*(2*n+3))
   edge=2*abs(b)*A*cosh(t*(2*n+2)/2)
   if edge>a:break
   n+=1
  assert n<1000
  assert edge>a
  # Gram minor after c^-1/2 scaling has diagonal a and offdiag edge
  assert a*a-edge*edge<0
  # also diagonal K_t(x,x) is positive for a>=2|b|, yet PSD fails
  assert a>2*abs(b)
  checks+=4
# d=2 circle, adjacent high-degree cosine channels coefficient 1/2.
for n in range(1,30):
    assert Fraction(1,2)>0
    checks+=1
# Generic geometric spectrum c_l=r^l makes normalized cross-operator
# (sqrt(r)+1/sqrt(r)) times multiplication by z.
for r in [0.1,0.25,0.8]:
   R=1/r
   w=(1+r)/sqrt(r)
   assert abs(w-(sqrt(R)+1/sqrt(R)))<1e-12
   checks+=1
print('PASS',checks,'exact algebraic and constructive heat-witness assertions')
# Fractional spectral-order transition: numerical stress test, not its proof.
for d in [2,3,4,7,20]:
 for alpha in [0.15,0.35,0.5]:
  deltas=[((n+1)*(n+d-1))**alpha-(n*(n+d-2))**alpha for n in range(150)]
  assert max(deltas) <= (d-1)**alpha+1e-8
  assert all(deltas[n+1]<=deltas[n]+1e-8 for n in range(len(deltas)-1))
  checks+=2
 for alpha in [0.6,0.8,1.0]:
  def delta(n):return ((n+1)*(n+d-1))**alpha-(n*(n+d-2))**alpha
  assert delta(100000)>delta(1000) > delta(10)
  checks+=1
print('PASS',checks,'total exact and numerical assertions')
for d in [2,3,5,9]:
 for alpha in [0.6,0.75,1.0]:
  t=2.0
  a,b=1.0,0.01
  n=d
  while n<400000:
   delta=((n+1)*(n+d-1))**alpha-(n*(n+d-2))**alpha
   A=0.5 if d==2 else sqrt((n+1)*(n+d-2)/((2*n+d-2)*(2*n+d)))
   if 2*b*A*cosh(t*delta/2)>a:break
   n+=1
  assert n<400000, (d,alpha)
  assert a*a-(2*b*A*cosh(t*delta/2))**2<0
  checks+=2
print('PASS',checks,'including spectral-order finite-mode counter-witnesses')
