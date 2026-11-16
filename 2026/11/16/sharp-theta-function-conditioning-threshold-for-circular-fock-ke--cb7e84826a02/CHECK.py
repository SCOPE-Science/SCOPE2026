"""Finite checks for circular Fock Gram spectra and the theta crossover."""
import numpy as np
from scipy.stats import poisson
from scipy.optimize import brentq

def spectrum(n,t):
    # Directly stable residue probabilities on Poisson support.
    hi = int(np.ceil(t+12*np.sqrt(t+1)+100))
    v=np.arange(hi+1)
    probs=poisson.pmf(v,t)
    p=np.bincount(v % n, weights=probs, minlength=n)
    assert abs(p.sum()-1)<2e-10
    return n*p

def theta_ratio(a):
    k=np.arange(1,200)
    qterms=np.exp(-2*np.pi**2*a*k*k)
    return (1+2*qterms.sum())/(1+2*np.sum(qterms*(-1.)**k))

checks=0
for n in (2,3,4,5,7,11):
 for t in (.1,.35,1.1,3.5,9.5):
  z=np.sqrt(t)*np.exp(2j*np.pi*np.arange(n)/n)
  G=np.exp(np.outer(z,np.conj(z))-t)
  eig=np.linalg.eigvalsh(G)
  p=np.sort(spectrum(n,t))
  assert np.allclose(eig,p,atol=2e-9,rtol=2e-9), (n,t,eig,p)
  checks+=1
for n in (4,8,16,32,64):
 for a in (.08,.16,.3):
  vals=spectrum(n,a*n*n)
  err=abs(vals.max()/vals.min()-theta_ratio(a))
  if n==64:
   assert err<.1,(n,a,err)
  checks+=1
for n in (3,7,16):
 v=[spectrum(n,t).max()/spectrum(n,t).min() for t in (.5,1.0,3.0,6.,10.)]
 assert all(x>y for x,y in zip(v,v[1:])),(n,v)
 checks+=1
alpha2=brentq(lambda a:theta_ratio(a)-2,.015,.6)
assert abs(theta_ratio(alpha2)-2)<4e-11
print('PASS',checks,'finite checks; alpha_2=',f'{alpha2:.12f}')
