"""Exact finite certificates for the two-frequency circle-Poisson theorem.
Requires sympy (see requirements.txt). All displayed moment identities use exact rationals.
"""
from fractions import Fraction as F
from itertools import product
import sympy as S

u,z = S.symbols('u z', real=True)
N = S.Rational(3,2)*(1+u**4*z**4)+6*u**2*z**2+2*u*z
D = (1+z**2)**2
P = S.factor((S.diff(N,z)*(1+z*z)-4*z*N)/2)
assert S.expand(P - (3*u**4-6*u**2)*z**3-(-3*u*z**2+ (6*u**2-3)*z+u)) == 0
A = 9*u**8-72*u**6+162*u**4-56*u**2+9
B = 1323*u**14-567*u**12-2160*u**10+1125*u**8+1080*u**6-972*u**4+278*u**2-36
Q = S.expand(2*(u*u*N-D))
assert S.expand(S.resultant(2*P,Q,z)-32*A*B)==0
assert S.Poly(B,u).count_roots(S.Rational(719,1000),S.Rational(720,1000))==1
qlo = S.Poly(S.expand(D-u*u*N).subs(u,S.Rational(719,1000)),z)
assert qlo.count_roots(0,S.oo)==0 and qlo.eval(0)>0
assert S.expand(D-u*u*N).subs({u:S.Rational(720,1000),z:S.Rational(12,25)})<0
# Count zero-sum fourth-order Fourier terms exactly, using 4-term sparse spectra.
def four_moment(m,n,a,b):
  # f=sqrt(2)*(a*cos(m*x)+b*cos(n*x))
  # fourth moment: each cos amplitude has Fourier coeff amplitude/sqrt(2)
  from collections import defaultdict
  c=defaultdict(lambda:F(0))
  for k,v in [(m,a),(n,b)]:
    c[k]+=v; c[-k]+=v
  # use f without sqrt(2) then multiply final by four
  out=F(0)
  for p,v in c.items():
    for q,w in c.items():
      for k,x in c.items():
        for l,y in c.items():
          if p+q+k+l==0:out+=v*w*x*y
  return out/F(4)

count=0
for m in range(1,13):
 for n in range(m+1,19):
  for a,b in product([F(1),F(2,3),F(3,5)],[F(1),F(1,3)]):
   observed=four_moment(m,n,a,b)
   expected=F(3,2)*(a**4+b**4)+6*a*a*b*b+(2*a**3*b if n==3*m else 0)
   assert observed==expected,(m,n,a,b,observed,expected)
   count+=1
# Check exact stationarity cubic has one positive root using Descartes signs.
for j in range(1,100):
 t=S.Rational(j,100)
 C=S.Poly(-(P.subs(u,t)),z)
 # leading coefficient positive, constant negative, with exactly one sign change
 signs=[S.sign(v) for v in C.all_coeffs() if v!=0]
 assert sum(signs[k]!=signs[k+1] for k in range(len(signs)-1))==1
print('FOURIER_FOURTH_MOMENT_IDENTITIES_PASSED',count)
print('RESULTANT_STURM_THRESHOLD_CERTIFICATE_PASSED')
print('RESONANT_CUBIC_DESCARTES_CHECKS_PASSED',99)
print('ALL_TWO_FREQUENCY_POISSON_CHECKS_PASSED')
