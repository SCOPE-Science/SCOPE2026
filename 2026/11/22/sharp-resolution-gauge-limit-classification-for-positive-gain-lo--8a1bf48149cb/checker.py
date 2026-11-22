"""Reproduce the uniform gauge shadow-flow bounds for scalar and diagonal NSFD steps."""
from fractions import Fraction
from math import exp, log

def update_ratio(h, phi, kappa, alpha):
    assert h>0 and phi>0 and kappa>0 and alpha>=0
    return (1+phi*alpha)/(1+phi*(kappa+alpha))

# Exact rational equality for each finite index, including large positive gauges.
checks=0
for N in (4,10,50,200):
    h=Fraction(1,N)
    for k in (Fraction(1,2),Fraction(1),Fraction(3)):
      for alpha in (Fraction(0),Fraction(1),Fraction(N),Fraction(N*N)):
        phi=h+h*h/Fraction(3)
        r=update_ratio(h,phi,k,alpha)
        z=phi/h
        v=z/(1+phi*alpha)
        q=1/(1+h*alpha)
        assert r == 1/(1+k*h*v)
        assert v-q == (z-1)/((1+z*h*alpha)*(1+h*alpha))
        assert 0<r<1 and abs(float(v-q))<=float(z-1)
        assert 0 <= float(k*h*v-log(1+float(k*h*v))) <= float((k*h*v)**2/2)+1e-13
        checks += 1

# For phi=h, the entire scalar decay phase diagram has the predicted rates.
for theta in (0,0.2,0.5,0.9,1):
  for N in (100,1000,10000):
    h=1/N
    alpha = (1-theta)/(theta*h) if theta>0 else 1/h**2
    r=update_ratio(h,h,1,alpha)
    value=r**N
    target=exp(-theta)
    tolerance=0.015 if N==100 else 0.002
    assert abs(value-target)<tolerance, (theta,N,value,target)
    checks+=1

# The phase is coordinatewise independent in diagonal dimensions.
for lambdas,thetas in [((1,2,3),(0,0.5,1)), ((3,4,5),(0.25,0.75,1))]:
  N=10000;h=1/N
  for k,theta in zip(lambdas,thetas):
    alpha=(1-theta)/(theta*h) if theta>0 else 1/h**2
    assert abs(update_ratio(h,h,k,alpha)**N-exp(-k*theta))<0.003
    checks+=1
print('PASS',checks,'exact rational algebra / finite phase checks')
