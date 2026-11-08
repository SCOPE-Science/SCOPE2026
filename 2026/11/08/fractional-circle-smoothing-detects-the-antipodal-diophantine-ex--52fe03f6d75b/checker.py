"""Numerical consistency checks for fractional circle-smoothing/rotation multipliers.

All infinite/asymptotic assertions in the accompanying theorem are analytic;
these finite checks are illustrative consistency tests only.
"""
import math
import cmath
import numpy as np

checks=0

def ok(test,msg):
    global checks
    if not test: raise AssertionError(msg)
    checks+=1

def sharp(alpha,sigma,t,N):
    n=np.arange(1,N+1,dtype=float)
    vals=2*np.exp(-t*n**sigma)*np.abs(np.sin(np.pi*n*alpha))
    j=int(np.argmax(vals))
    return float(vals[j]),j+1

def delta(alpha,sigma,t,N):
    a,k=sharp(alpha,sigma,t,N)
    return 2-a,k

# Independent construction on finite Fourier spaces: smoothing followed by rotation.
rng=np.random.default_rng(331)
for sigma in (0.5,1.0,1.6,2.0):
 for alpha in (math.sqrt(2)-1,(math.sqrt(5)-1)/2,1/5,1/6):
  for t in (.1,.025,.008):
   N=180
   n=np.arange(-N,N+1)
   x=rng.normal(size=2*N+1)+1j*rng.normal(size=2*N+1)
   x[N]=0
   mult=np.exp(-t*np.abs(n)**sigma)*(1-np.exp(2j*np.pi*n*alpha))
   operator_norm=np.linalg.norm(mult*x)/np.linalg.norm(x)
   spectral_norm,k=sharp(alpha,sigma,t,N)
   ok(operator_norm <= spectral_norm+2e-12,(sigma,alpha,t,'Parseval'))
   ok(abs(abs(mult[N+k])-spectral_norm)<1e-12,(sigma,alpha,t,'extremizing basis'))

# Rational even denominator: for sufficiently small t the exact winning mode is q/2.
for q in (2,4,6,8,10,12):
 for p in range(1,q):
  if math.gcd(p,q)>1:continue
  for sigma in (.5,1,2):
   t=1.e-5
   m,k=sharp(p/q,sigma,t,300)
   ok(k==q//2,(p,q,sigma,'even denominator winner'))
   ok(abs(m-2*math.exp(-t*(q/2)**sigma))<1e-10,(p,q,sigma,'even denominator norm'))
# Rational odd denominator: angular maximum cos(pi/2q).
for q in (3,5,7,9,11):
 for p in range(1,q):
  if math.gcd(p,q)>1:continue
  for sigma in (1.,2.):
   m,k=sharp(p/q,sigma,1e-7,300)
   residues=[n for n in range(1,q+1) if abs(abs(math.sin(math.pi*n*p/q))-math.cos(math.pi/(2*q)))<1e-12]
   best=min(residues)
   ok(k==best,(p,q,sigma,'odd denominator winner'))
   ok(abs(m-2*math.exp(-1e-7*best**sigma)*math.cos(math.pi/(2*q)))<1e-10,(p,q,sigma,'odd denominator norm'))
# Bounded type: empirical power-normalized deficits remain bounded on a sample of t.
phi=(math.sqrt(5)-1)/2
for sigma in (.5,1,1.5,2):
 vals=[]
 for t in (0.07,0.04,.025,.015,.008,.005,.002,.001,.0005):
  d,k=delta(phi,sigma,t,30000)
  ratio=d/t**(2/(sigma+2))
  ok(0.01<ratio<100,(sigma,t,'bounded-type scaling'))
  vals.append(ratio)
 ok(max(vals)/min(vals)<100,(sigma,'scaling oscillations'))
# Distance-to-antipode equals half angular multiplier defect asymptotically.
for alpha in (phi,math.sqrt(2)-1,1/7):
 for n in range(1,201):
  d=abs(((n*alpha-.5+.5)%1)-.5)
  y=2*abs(math.sin(math.pi*n*alpha))
  ok(abs(y-2*math.cos(math.pi*d))<2e-12,(alpha,n,'distance identity'))
print('FRACTIONAL_ROTATION_CHECKS_PASS',checks)
