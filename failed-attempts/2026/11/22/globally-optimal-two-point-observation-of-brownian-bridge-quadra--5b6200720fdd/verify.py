"""Reproduce symbolic and finite numerical checks for two-observation bridge-energy design."""
from fractions import Fraction
import math
import sympy as sp

x, y, r, t, u = sp.symbols('x y r t u', real=True)
S = sp.Matrix([[x*(1-x), x*(1-y)], [x*(1-y), y*(1-y)]])
H = sp.Matrix([[y, (y-x)/2], [(y-x)/2, 1-x]]) / 3
F = sp.factor(sp.trace((H*S)**2))
G = sp.factor(F.subs({x: sp.Rational(1,2)+t-r, y: sp.Rational(1,2)+t+r}))
G_ref = (5*r**4/sp.Integer(9) - r**3/3 - r**2/18 + r/36 + sp.Rational(1,144)
         +t**2*(4*r**3/9+2*r**2/3-sp.Rational(1,18))
         +t**4*(1-4*r)/9)
assert sp.simplify(G-G_ref)==0
G0=(2*r-1)**2*(20*r*r+8*r+1)/144
assert sp.simplify(G.subs(t,0)-G0)==0
assert sp.simplify(sp.diff(G0,r)-(2*r-1)*(40*r*r+2*r-1)/36)==0
assert sp.simplify(G.subs(r,sp.Rational(1,4))-(sp.Rational(17,2304)-t*t/144))==0
P=sp.factor(36*sp.diff(G,r))
assert sp.simplify(P-(80*r**3-36*r**2-4*r+1+(48*r**2+48*r)*t**2-16*t**4))==0
assert sp.factor(P.subs(t**2,(sp.Rational(1,2)-r)**2)-16*r*(2*r-1)*(r*r+4*r-1))==0
rstar=(sp.sqrt(41)-1)/40
fstar=sp.simplify(G0.subs(r,rstar))
assert sp.simplify(fstar-(3373+287*sp.sqrt(41))/576000)==0
riskstar=sp.simplify(sp.Rational(1,45)-2*fstar)
assert sp.simplify(riskstar-(sp.Rational(1009,96000)-287*sp.sqrt(41)/288000))==0
assert sp.simplify(sp.diff(G0,r).subs(r,rstar))==0
assert sp.simplify(sp.Rational(1,45)-2*sp.Rational(1,144)-sp.Rational(1,120))==0

# Independent bridge conditional-mean covariance: quadrature of three local segments.
a,b,c=sp.symbols('a b c',positive=True)
U,V=sp.symbols('U V',real=True)
z=sp.symbols('z',real=True)
mleft=(z/a)*U
mmid=(1-z/b)*U+z*V/b
mright=(1-z/c)*V
quad=sp.integrate(mleft**2,(z,0,a))+sp.integrate(mmid**2,(z,0,b))+sp.integrate(mright**2,(z,0,c))
assert sp.simplify(quad-((a+b)*U*U+b*U*V+(b+c)*V*V)/3)==0
condmean=sp.expand(quad+(a*a+b*b+c*c)/6)
condmean_xy=condmean.subs({a:x,b:y-x,c:1-y})
assert sp.simplify(sp.expand(condmean_xy-(sp.Matrix([U,V]).T*H*sp.Matrix([U,V]))[0]-(x*x+(y-x)**2+(1-y)**2)/6))==0
assert sp.simplify(sp.trace(H*S)+(x*x+(y-x)**2+(1-y)**2)/6-sp.Rational(1,6))==0
s,v=sp.symbols('s v',real=True)
trace_k2=2*sp.integrate(sp.integrate((s*(1-v))**2,(s,0,v)),(v,0,1))
assert trace_k2==sp.Rational(1,90)

# Independent exact rational comparison of matrix formula and expanded polynomial.
N=0
for i in range(1,26):
 for j in range(i+1,27):
  xx,yy=sp.Rational(i,27),sp.Rational(j,27)
  SS=sp.Matrix([[xx*(1-xx),xx*(1-yy)],[xx*(1-yy),yy*(1-yy)]])
  HH=sp.Matrix([[yy,(yy-xx)/2],[(yy-xx)/2,1-xx]])/3
  direct=sp.trace((HH*SS)**2)
  shifted=G.subs({r:(yy-xx)/2,t:(xx+yy-1)/2})
  assert direct==shifted
  N+=1

# Boundary and global finite-grid assertions only as supplementary diagnostics.
Fnum=sp.lambdify((x,y),F,'math')
for i in range(101):
 for j in range(i,101):
  a1,b1=i/100,j/100
  assert Fnum(a1,b1)<=float(fstar)+1.e-11
assert float(riskstar)>0
print('PASS: 12 symbolic identities and conditional-mean/moment checks')
print(f'PASS: {N} independent exact rational covariance-matrix comparisons')
print('PASS: 5151 finite-grid inequality checks (not a continuum proof)')
print('Optimal sites:',sp.simplify(sp.Rational(1,2)-rstar),sp.simplify(sp.Rational(1,2)+rstar))
print('Optimal mean-square risk:',riskstar,'=',float(riskstar))
print('One-site midpoint risk:',sp.Rational(1,120))
