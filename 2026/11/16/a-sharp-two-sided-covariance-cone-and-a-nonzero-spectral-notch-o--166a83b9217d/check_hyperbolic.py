#!/usr/bin/env python3
"""Exact symbolic and numerical checks for a signed hyperbolic radial kernel.

Requirements: Python 3, sympy, mpmath.  Tests are supplementary to proof.
"""
import sympy as s
import mpmath as mp

x, B, a = s.symbols('x B a', positive=True)
y = x+B
D0 = (y+1)**2 - 4*B
N = (y+2)**2 - 8*(B+1)
D1 = (y*y+8*B+4)**2 - 16*B*(y+2)**2
R = s.factor(D0*N/D1)
Q = s.cancel(s.diff(R,x)*D1**2/2)
expected = (
 -3*x**6-3*(2*B-1)*x**5
 +3*(5*B**2-11*B+10)*x**4
 +2*(30*B**3-49*B**2-140*B+20)*x**3
 +(75*B**4-66*B**3-60*B**2+88*B+160)*x**2
 +(42*B**5+15*B**4+72*B**3+120*B**2+64*B+112)*x
 +(9*B**6+19*B**5-178*B**4+72*B**3+32*B**2-272*B-32)
)
assert s.expand(Q-expected)==0
assert s.factor(R.subs(x,0)-(B-1)**2*(B**2-4*B-4)/(B**2+4)**2)==0
assert s.factor(D1-D0*N).subs(x,0)==s.expand(6*B**3+3*B**2-4*B+20)
# Verify positivity of each Descartes coefficient by a strictly nonnegative
# coefficient expansion in u=B-4.
u=s.symbols('u',nonnegative=True)
qpoly=s.Poly(expected,x)
for k in range(5):
 coeff=s.expand(qpoly.coeff_monomial(x**k).subs(B,4+u))
 cs=s.Poly(coeff,u).all_coeffs()
 assert all(v>0 for v in cs),(k,cs)
for k in (5,6):
 coeff=s.expand(qpoly.coeff_monomial(x**k).subs(B,4+u))
 assert all(v<0 for v in s.Poly(coeff,u).all_coeffs())

# Independent complex-shift spherical transform (not using rational R formula)
f=lambda z,X: 4*z/((X+(z-1)**2)*(X+(z+1)**2))
re=s.re(s.expand_complex(f(a-s.I,x)))
assert s.simplify(s.factor(re/f(a,x)).subs(a,s.sqrt(B))-R)==0

mp.mp.dps=45
count=0
for aa in (mp.mpf('2.01'),mp.mpf('2.15'),mp.mpf('2.5'),mp.mpf('3'),mp.mpf('6')):
 bb=aa**2
 def rq(X):
  Y=X+bb
  return ((Y+1)**2-4*bb)*((Y+2)**2-8*(bb+1))/(((Y*Y+8*bb+4)**2)-16*bb*(Y+2)**2)
 def fhat(z,X):
  return 8*mp.pi*z/((X+(z-1)**2)*(X+(z+1)**2))
 for X in (0,mp.mpf('0.125'),mp.mpf('2'),mp.mpf('10'),mp.mpf('100'),mp.mpf('500')):
  direct=mp.re(fhat(aa-1j,X))/fhat(aa,X)
  assert abs(direct-rq(X))<mp.mpf('1e-33'),(aa,X)
  count+=1
 # Solve exact Q polynomial numerically at fixed a and bracket max.
 qf=s.lambdify((B,x),expected,'mpmath')
 lo=mp.mpf('0'); hi=10*(bb+2)**2
 assert qf(bb,lo)>0 and qf(bb,hi)<0
 for _ in range(170):
  mid=(lo+hi)/2
  if qf(bb,mid)>0:lo=mid
  else:hi=mid
 xx=(lo+hi)/2
 rr=rq(xx)
 assert rr>1 and rq(0)<rr and rq(xx-1e-5)<rr and rq(xx+1e-5)<rr
 # Both sharp endpoints were checked through exact spectral formula
 lower=-1/rr
 upper=(-1/rq(0)) if rq(0)<0 else None
 for X in [0,xx/2,xx,xx*2,10*xx,100*xx]:
  assert 1+lower*rq(X)>-mp.mpf('1e-30')
  if upper is not None: assert 1+upper*rq(X)>-mp.mpf('1e-30')
 count+=6
print('PASS: exact derivative, coefficient positivity, transform identity; numerical cross checks:',count)
