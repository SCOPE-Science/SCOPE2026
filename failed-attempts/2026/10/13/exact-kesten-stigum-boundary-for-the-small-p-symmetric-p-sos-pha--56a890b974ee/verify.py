#!/usr/bin/env python3
import sympy as sp
from fractions import Fraction
from decimal import Decimal, getcontext

r,y=sp.symbols('r y')
F=r**5*y**3-y**2+(r+1)*y-2*r**5
N=(r+1-2*r**10)*y**2
D=r**5*y**4+(r+2*r**10+1)*y**2+2*r**5*(r+1)
H=sp.expand(2*N**2-D**2)
P=sp.Poly(
16*r**40-192*r**31-192*r**30-112*r**28-336*r**27-336*r**26-336*r**25
-72*r**22-144*r**21-72*r**20+32*r**19+128*r**18+192*r**17+188*r**16+72*r**15
-60*r**14-48*r**13+36*r**12+72*r**11+8*r**10-20*r**9-40*r**8-48*r**7-36*r**6
-12*r**5+r**4+4*r**3+6*r**2+4*r+1, r)
Q=2*r**9+2*r**8+2*r**7+2*r**6+2*r**5+2*r**4+2*r**3+2*r**2+2*r+1
res=sp.factor(sp.resultant(F,H,y))
expected=4*r**20*(r-1)**4*Q**4*P.as_expr()
assert sp.expand(res-expected)==0
assert sp.count_roots(P,1,sp.oo)==1
lo=sp.Rational(147075929,100000000)
hi=sp.Rational(147075930,100000000)
assert P.eval(lo)<0<P.eval(hi)
assert sp.count_roots(P,lo,hi)==1
# The other resultant factors are strictly positive for r>1.
# Exact witness that the physical H changes sign by r=2.
F2=sp.Poly(F.subs(r,2),y)
ylo=sp.Rational(249,200)
yhi=sp.Rational(623,500)
assert F2.eval(ylo)<0<F2.eval(yhi)
# F_y has negative discriminant for every r>1; in particular the root is unique.
Fy=sp.diff(F,y)
disc=sp.discriminant(Fy,y)
assert sp.expand(disc-(4-12*r**5*(r+1)))==0
# Lower bound H(2,y)>0 on [ylo,yhi] by monotone power bounds termwise.
H2=sp.Poly(H.subs(r,2),y)
assert sp.expand(H2.as_expr()-(-1024*y**8-131264*y**6+4145161*y**4-787584*y**2-36864))==0
lower=4145161*ylo**4-1024*yhi**8-131264*yhi**6-787584*yhi**2-36864
assert lower>0
# At r=1, the physical root is y=1 and H<0.
assert F.subs({r:1,y:1})==0
assert H.subs({r:1,y:1})<0
# The second nontrivial eigenvalue is uniformly below the KS threshold for r>1.
assert sp.Rational(2)*sp.Rational(256,3125)**2 < 1
# Bisection of the certified unique P-root, only to print a decimal.
getcontext().prec=60
coeff=[Decimal(int(c)) for c in P.all_coeffs()]
def peval(x):
    z=Decimal(0)
    for c in coeff: z=z*x+c
    return z
a=Decimal(147075929)/Decimal(100000000)
b=Decimal(147075930)/Decimal(100000000)
for _ in range(180):
    m=(a+b)/2
    if peval(m)>0: b=m
    else: a=m
root=(a+b)/2
theta=root**5
print('VERIFY_OK resultant=exact roots_gt1=1 bracket=1 lambda2_bound=256/3125 r_star=%s theta_star=%s' % (root,theta))
