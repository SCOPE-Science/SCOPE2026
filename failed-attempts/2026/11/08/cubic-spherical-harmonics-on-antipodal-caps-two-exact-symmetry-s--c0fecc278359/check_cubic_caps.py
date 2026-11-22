"""Reproduce the cubic spherical-harmonic double-cap spectral identities.

Dependencies: Python >=3.10, sympy, numpy, scipy.
Run: python check_cubic_caps.py
"""
from math import comb, sqrt, pi
import numpy as np
import sympy as sp
from scipy.special import roots_legendre, sph_harm_y, beta
from scipy.integrate import quad

D,t=sp.symbols('d t', positive=True)
a=1/(D+2)
P=[t*(t-3*a)**2, (1-t)*(t-a)**2, t*(1-t)**2, (1-t)**3]
N=[6*(D-1)/(D*(D+2)**2*(D+4)),
 2*(D-1)*(D+1)/(D*(D+2)**2*(D+4)),
 (D-1)*(D+1)/(D*(D+2)*(D+4)),
 (D-1)*(D+1)*(D+3)/(D*(D+2)*(D+4))]
checks=0

def check(c, message):
 global checks
 assert bool(c), message
 checks+=1

# Exact beta moments: E[t^j] = (1/2)_j/(d/2)_j.
def moment(k):
 return sp.prod((sp.Rational(1,2)+j)/(D/sp.Integer(2)+j) for j in range(k))
for k in range(4):
 expr=sp.Poly(sp.expand(P[k]),t)
 integrated=sum(coef*moment(power[0]) for power,coef in expr.terms())
 check(sp.factor(integrated-N[k])==0,f'normalizer {k}')

# The fundamental derivative identity for the beta-weighted tail.
S={
 (0,1):-D*(D+4)*((D+2)*t-3)*((D+2)*t-1)/(3*(D-1)*(D+1)),
 (0,2):-D*(D+4)*t*((D+2)*t-1)/(3*(D+1)),
 (1,2): D*(D+4)*(t-1)*((D+2)*t-1)/((D-1)*(D+1)),
 (1,3): D*(D+4)*(t-1)*((D+2)*t+1)/((D-1)*(D+3)),
 (2,3):-2*D*(D+2)*(D+4)*(t-1)**2/((D-1)*(D+1)*(D+3)),
}
for (i,j),s in S.items():
 derivative=(1-D*t)*s/2+t*(1-t)*sp.diff(s,t)
 check(sp.factor(derivative-(P[i]/N[i]-P[j]/N[j]))==0,f'difference {i},{j}')

# Harmonic decomposition dimensions (m=0,1,2,3).
for d in range(3,20):
 mul=[1,d-1,comb(d,2)-1,comb(d+1,3)-(d-1)]
 check(sum(mul)==comb(d+2,3)-d,f'dimensions {d}')
 check(all(m>0 for m in mul),f'positive dimensions {d}')

# Compare independent sph_harm_y quadrature on S^2 with beta-integral formula.
def lam(d,k,u):
 norm=[float(x.subs(D,d)) for x in N][k]
 p=sp.lambdify(t,P[k].subs(D,d),'numpy')
 exponent=(d-3)/2
 ans=quad(lambda x:x**(-.5)*(1-x)**exponent*p(x),u,1,
          epsabs=1e-12,epsrel=1e-12)[0]
 return ans/(norm*beta(.5,(d-1)/2))

for d in [3,4,5,8,13]:
 for u in [0.04, 1/(d+2), (1/(d+2)+3/(d+2))/2,
           3/(d+2), .95]:
  if not (0<u<1):continue
  vals=[lam(d,k,u) for k in range(4)]
  check(all(0<v<1 for v in vals),f'positive concentration d={d} u={u}')
  check(vals[3]<min(vals[:3]),f'low sector d={d} u={u}')
  if abs(u-1/(d+2))<1e-12:
   check(max(vals[:3])-min(vals[:3])<5e-11,'triple crossing')
  elif u<1/(d+2):
   check(vals[2]>vals[0]>vals[1]>vals[3],'first ordering')
  elif u<3/(d+2):
   check(vals[1]>vals[0]>vals[2]>vals[3],'second ordering')
  elif abs(u-3/(d+2))<1e-12:
   check(abs(vals[0]-vals[1])<5e-11,'second crossing')
  else:
   check(vals[0]>vals[1]>vals[2]>vals[3],'third ordering')

# Spherical harmonic integration is independent of beta-moment derivations.
for c in [0.2,1/sqrt(5),sqrt(3/5),0.88]:
 x,w=roots_legendre(25)
 z=(1-c)*x/2+(1+c)/2
 quadrature=(1-c)/2*w
 for m in range(4):
  theta=np.arccos(z)
  y=sph_harm_y(3,m,theta,np.full_like(theta,0.37))
  sphere_norm=4*pi*np.sum(quadrature*np.abs(y)**2)
  expected=lam(3,m,c*c)
  check(abs(sphere_norm-expected)<3e-11,f'3D direct mode m={m}, c={c}')
  # The opposite cap contributes equally because squared odd-degree harmonics are even.
  # Full spherical harmonic normalization is exactly 1 under these conventions.
  if c==0.2:
   fullz,fullw=roots_legendre(25)
   fulltheta=np.arccos(fullz)
   yy=sph_harm_y(3,m,fulltheta,np.full_like(fulltheta,0.37))
   check(abs(2*pi*np.dot(fullw,np.abs(yy)**2)-1)<3e-12,'full norm')

# The exact thin-cap spectral conditioning coefficient.
for d in [3,5,10]:
 const=(d-1)*(d+1)*(d+3)*(d+5)/(6*(d+2))
 for u in [.99,.999,.9999]:
  approx=(lam(d,0,u)/lam(d,3,u))*(1-u)**3
  check(abs(approx/const-1)<5.0*(1-u),f'thin cap d={d}, u={u}')

print(f'CUBIC_DOUBLE_CAP_CHECKS_PASS {checks}')
