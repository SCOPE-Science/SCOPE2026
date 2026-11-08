"""Independent finite-dimensional arithmetic checks for an annular Zernike concentration theorem.
Run: python verify.py. Uses mpmath and Python standard library; analytic proof is in RESULT.md.
"""
from math import comb
import mpmath as mp
mp.mp.dps=90
checks=0

def check(test, message):
    global checks
    assert bool(test), message
    checks+=1

def gram(m,n,eps):
    z=n+1
    g=mp.matrix([[mp.beta(m+1,i+j+1) for j in range(z)] for i in range(z)])
    b=mp.matrix([[mp.betainc(i+j+1,m+1,0,eps,regularized=False) for j in range(z)] for i in range(z)])
    return g,b

def evals(g,b):
    l=mp.cholesky(g)
    q=l**-1*b*(l.T**-1)
    return list(mp.eigsy(q,eigvals_only=True))

for m in (0,1,3,8):
 for n in (1,2,3,4):
    hilbert=mp.matrix([[mp.mpf(1)/(i+j+1) for j in range(n+1)] for i in range(n+1)])
    dinv=(hilbert**-1)[n,n]
    check(mp.almosteq(dinv,(2*n+1)*comb(2*n,n)**2,rel_eps=mp.mpf('1e-65')),('Hilbert inverse',m,n))
    small=(mp.mpf(2*n+1)*comb(2*n,n)**2*mp.beta(m+1,2*n+1))**-1
    large=(n+1)*(n+m+1)
    for eps in (mp.mpf('.0005'),mp.mpf('.0001')):
       g,b=gram(m,n,eps)
       ev=evals(g,b)
       check(0<ev[0]<ev[-1]<1,('spectrum',m,n,eps))
       check(abs(ev[0]/(small*eps**(2*n+1))-1)<mp.mpf('.02'),('min',m,n,eps))
       check(abs(ev[-1]/(large*eps)-1)<mp.mpf('.06'),('max',m,n,eps))
       kcoef=large/small
       check(abs((ev[-1]/ev[0])*eps**(2*n)/kcoef-1)<mp.mpf('.08'),('condition',m,n,eps))

for tau in (mp.mpf('0.25'),mp.mpf('0.8'),mp.mpf('2'),mp.mpf('4')):
   expv=mp.exp(-tau);rad=mp.sqrt(1+tau*tau/4)
   lower=1-expv*(1+tau*tau/2)-tau*expv*rad
   upper=1-expv*(1+tau*tau/2)+tau*expv*rad
   check(0<lower<upper<1,('limit signs',tau))
   for m in (200,1000,4000):
      eps=tau/(m+1)
      g,b=gram(m,1,eps)
      ev=evals(g,b)
      check(abs(ev[0]-lower)<mp.mpf('.013'),('cross lower',tau,m))
      check(abs(ev[1]-upper)<mp.mpf('.013'),('cross upper',tau,m))

# First two Taylor coefficients of the limiting special-function branches.
for tau in (mp.mpf('.004'),mp.mpf('.001')):
  e=mp.exp(-tau);r=mp.sqrt(1+tau*tau/4)
  lo=1-e*(1+tau*tau/2)-tau*e*r
  hi=1-e*(1+tau*tau/2)+tau*e*r
  check(abs(lo/(tau**3/24)-1)<mp.mpf('.0002'),('small crossover lower',tau))
  check(abs(hi/(2*tau)-1)<mp.mpf('.01'),('small crossover upper',tau))
print('ANNULAR_ZERNIKE_CHECKS_PASS',checks)
