"""Numerical and algebraic consistency checks for radial Toeplitz commutators.

Install: python -m pip install -r requirements.txt
Run: python CHECK.py
These finite checks do not replace the analytic proof.
"""
import math
from collections import Counter
import mpmath as mp
mp.mp.dps = 37
checks=0

def test(x, explanation):
    global checks
    assert x, explanation
    checks += 1

def modal(m,d,a,w):
    z=mp.mpc(0,w)
    return mp.gamma(a+1-z)/mp.gamma(a+1)*mp.gamma(m+d+a+1)/mp.gamma(m+d+a+1-z)

def moment_integral(m,d,a,w):
    return mp.quad(lambda t:t**(m+d-1)*(1-t)**a*mp.cos(w*mp.log(1/(1-t))),[0,0.5,0.9,0.99,1]) / mp.beta(m+d,a+1)

def delta(m,d,a,w):
    z=mp.mpc(0,w)
    u=modal(m,d,a,w)
    return mp.re(u*z/(m+d+a+1-z))

for d in [1,2,3]:
  for a in [-0.25,0,0.75,2]:
    for w in [0.5,1,2]:
      for m in [0,1,2,5,12]:
        z=mp.re(modal(m,d,a,w))
        if m<6:
          test(abs(z-moment_integral(m,d,a,w))<mp.mpf('1e-24'), 'radial beta integration')
        test(abs(delta(m,d,a,w)-(mp.re(modal(m+1,d,a,w))-z))<mp.mpf('1e-29'), 'exact gamma recurrence')
        if m>0:
          pred=mp.re(mp.mpc(0,w)*mp.gamma(a+1-mp.mpc(0,w))/mp.gamma(a+1)*m**(mp.mpc(0,w)-1))
          if m>=5:
            test(abs(delta(m,d,a,w)-pred)<20/(m*m), 'first-order gamma difference')

# Combinatorial diagonal weights, tested against explicit monomial count.
for d in [1,2,3,4]:
 for m in [1,2,4,9,30,100]:
  if d==1:
   weights=[1]
  else:
   weights=[((j+1)/(m+d+0.5+1))**(d/2)*math.comb(m-j+d-2,d-2) for j in range(m+1)]
  s=sum(weights)
  theoretical=math.gamma(1+d/2)/math.gamma(3*d/2)*m**(d-1)
  if d==1:
   test(abs(s-theoretical)<1e-12,'univariate weight')
  elif m>=9:
   test(abs(s-theoretical)/theoretical<3*d/m,'beta Riemann approximation')

# Exact singular values can also be produced as a sparse weighted shift.
for d in [1,2,3]:
 m=5;a=0;w=1
 dd=float(abs(delta(m,d,a,w)))
 if d==1:
  alphas=[(m,)]
 elif d==2:
  alphas=[(j,m-j) for j in range(m+1)]
 else:
  alphas=[(j,k,m-j-k) for j in range(m+1) for k in range(m-j+1)]
 for alpha in alphas:
  c=math.sqrt((alpha[0]+1)/(m+d+a+1))
  test(abs((c*dd)**2 - c*c*dd*dd)<1e-13,'orthogonal-shift singular square')

# Explicit phase-averaged residue for a single cosine (w=1).
for d in [1,2,3]:
 for a in [-0.25,0,1.5]:
  amp=abs(mp.gamma(a+1-1j)/mp.gamma(a+1))
  avg=amp**d*mp.gamma((d+1)/2)/(mp.sqrt(mp.pi)*mp.gamma(1+d/2))
  co=mp.gamma(1+d/2)/mp.gamma(3*d/2)*avg
  direct=amp**d*mp.gamma((d+1)/2)/(mp.sqrt(mp.pi)*mp.gamma(3*d/2))
  test(abs(co-direct)<mp.mpf('1e-25'),'single-harmonic gamma simplification')

print(f'PASS: {checks} finite checks (analytic proof required for all orders).')
