"""Independent finite Fourier checks accompanying a six-cycle cubic-moment bound.

Run: python checker.py (requires SymPy; uses only deterministic local arithmetic).
The exact algebraic identities and polynomial root counts supplement, but do not
replace, the handwritten Fourier and Rayleigh-quotient proofs.
"""
import cmath
import math
import random
import sympy as sp

z=sp.symbols('z', real=True)
R=81*z**2+168*z+16
P2=3*z**2+18*z+20
C0=-81*z**3-174*z**2+108*z+272
Q=243*z**4-225*z**3-1800*z**2-912*z+704
assert sp.expand(C0**2-P2**2*R-24*(z+2)**2*Q)==0
assert Q.subs(z,0)>0 and Q.subs(z,1)<0
assert Q.subs(z,3)<0 and Q.subs(z,4)>0
# These two disjoint positive brackets exhaust the positive roots by Descartes.
assert list(sp.Poly(Q,z).all_coeffs())==[243,-225,-1800,-912,704]
roots=sp.nroots(Q,maxsteps=300)
zstar=float(next(sp.re(root) for root in roots if abs(float(sp.im(root)))<1e-12 and 0<float(sp.re(root))<1))
def kval(t):
 return (3*t+8+math.sqrt(81*t*t+168*t+16))/(2*(t+2)*math.sqrt(2*(t+1)))
K=kval(zstar)
r=math.sqrt(zstar)
lmb=(3*zstar+8+math.sqrt(81*zstar*zstar+168*zstar+16))/(2*(zstar+2))
t=3*r/(lmb-3)
assert 0.4177<zstar<0.4178 and 2.36649<K<2.36650
assert K>3/math.sqrt(2)
assert abs((6*t*t+2+12*t*r)/((2*t*t+2+r*r)*math.sqrt(2+2*r*r))-K)<3e-14
assert abs(C0.subs(z,zstar)-float(P2.subs(z,zstar))*math.sqrt(float(R.subs(z,zstar))))<3e-10
checks=8

def measures(a,b,c):
 # a,b complex Fourier coefficients, c is the real Nyquist coefficient.
 u=[(a*cmath.exp(2j*math.pi*x/6)+a.conjugate()*cmath.exp(-2j*math.pi*x/6)+
     b*cmath.exp(4j*math.pi*x/6)+b.conjugate()*cmath.exp(-4j*math.pi*x/6)+
     c*((-1)**x)).real for x in range(6)]
 s=sum(v*v for v in u)/6
 m3=sum(v**3 for v in u)/6
 T=2*abs(b)**2+2*c*c
 return s,T,m3

rng=random.Random(20261116)
for _ in range(4000):
 A=rng.uniform(0,4); B=rng.uniform(0.05,3); c=rng.uniform(-3,3)
 a=A*cmath.exp(1j*rng.uniform(-math.pi,math.pi))
 b=B*cmath.exp(1j*rng.uniform(-math.pi,math.pi))
 s,T,m3=measures(a,b,c)
 cubic=6*(a*a*b.conjugate()).real+2*(b**3).real+12*c*(a*b).real
 assert abs(s-(2*A*A+2*B*B+c*c))<3e-12
 assert abs(T-(2*B*B+2*c*c))<1e-14
 assert abs(m3-cubic)<4e-10
 assert abs(m3)<=K*s*math.sqrt(T)+5e-10
 checks+=4

# Equality and its six translations, both signs.
for shift in range(6):
 alpha=math.pi*shift/3
 a=t*cmath.exp(1j*alpha)
 b=cmath.exp(2j*alpha)
 c=((-1)**shift)*r
 for sign in (-1,1):
  s,T,m3=measures(sign*a,sign*b,sign*c)
  assert abs(abs(m3)/(s*math.sqrt(T))-K)<1e-12
  checks+=1

print('PASS',checks,'assertions; z*',format(zstar,'.15f'),
      'K6',format(K,'.15f'),'K6^2',format(K*K,'.15f'),
      'a/b',format(t,'.15f'),'c/b',format(r,'.15f'))
