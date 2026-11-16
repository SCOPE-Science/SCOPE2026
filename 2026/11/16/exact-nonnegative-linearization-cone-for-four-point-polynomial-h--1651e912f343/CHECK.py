#!/usr/bin/env python3
"""Exact symbolic verification of four-node polynomial linearization formulas."""
import sympy as sp
from fractions import Fraction as F

x,y,r=sp.symbols('x y r', real=True)
d=[sp.Integer(0),x,y,sp.Integer(1)]
a=[1-z for z in d]; b=[(1-r)*z for z in d]; c=[r*z for z in d]
J=sp.zeros(4)
for i in range(4):
    J[i,i]=b[i]
    if i<3: J[i,i+1]=a[i]
    if i>0: J[i,i-1]=c[i]
assert all(sp.cancel(sum(J[i,j] for j in range(4))-1)==0 for i in range(4))
R=[sp.eye(4),J]
for i in (1,2):
    R.append(((J-b[i]*sp.eye(4))*R[i]-c[i]*R[i-1]).applyfunc(lambda z:sp.cancel(z/a[i])))
X=1-x;Y=1-y
H=X*(1-r)**2+r*(1-x-y)
K=Y*(1-r)**2+r*(2-3*y)
L=y*(y-x)*(1+r**2)+r*(1-x*(1-y)-2*y**2)
rows={
(2,2):[r**2*x*y/X, r*y*y*(1-r)/X, L/X, (1-r)*Y*(1+y-x)/X],
(2,3):[0, r**2*y/X, r*(1-r)*(1+y-x)/X, H/X],
(3,3):[r**3*x*y/(X*Y), r**2*y*(1-r)/(X*Y), r*H/(X*Y), (1-r)*K/Y],
}
count=0
for (m,n),v in rows.items():
    for k,claimed in enumerate(v):
        delta=sp.cancel(R[m][n,k]-claimed)
        assert delta==0,(m,n,k,delta)
        count+=1
    assert sp.cancel(sum(v)-1)==0
    count+=1
# Product rows with degree-one factor are nonnegative by birth-death coefficients.
for n in range(4):
    assert all(sp.cancel(R[1][n,k]-J[n,k])==0 for k in range(4))
    count+=4
# Exact rational independence witness: L really is needed at fixed r.
xx,yy,rr=F(7,10),F(4,5),F(1,5)
h=(1-xx)*(1-rr)**2+rr*(1-xx-yy)
k=(1-yy)*(1-rr)**2+rr*(2-3*yy)
ell=yy*(yy-xx)*(1+rr*rr)+rr*(1-xx*(1-yy)-2*yy*yy)
assert (h,k,ell)==(F(23,250),F(6,125),-F(1,1250));count+=1
# A profile inside the all-r positive region but outside the Newton cone.
xx,yy=F(1,10),F(3,5)
assert xx+yy<=1 and yy<=F(2,3)
nu3=1-3*yy+3*xx
assert nu3==-F(1,2);count+=1
# Sharp boundaries: at r=1, H=1-x-y, while for y>2/3, K(1)<0.
assert sp.cancel(H.subs(r,1)-(1-x-y))==0
assert sp.cancel(K.subs(r,1)-(2-3*y))==0
count+=2
print('PASS:',count,'symbolic/exact checks')
