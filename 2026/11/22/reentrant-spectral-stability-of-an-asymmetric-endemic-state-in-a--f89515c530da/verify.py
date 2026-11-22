"""Exact symbolic checks for endemic spectral reentrance in a q-voter SIS model.
Run: python verify.py (requires SymPy)."""
import sympy as sp

z,u=sp.symbols('z u', positive=True)
R=1+z+u
p=R**2*u/(z*(1+z))
x=z/R; y=1/R; v=u/(R*(1+z))
# Time is measured in units of the recovery period. Here alpha=0, delta=1.
F=sp.Matrix([
 -R*x*v+p*x*y*(x-y)+v,
 -R*y*v+p*x*y*(y-x)+z*v,
 R*y*v-v
])
assert all(sp.cancel(a)==0 for a in F)
assert sp.cancel(x+y+v+z*v-1)==0

X,Y,V=sp.symbols('X Y V')
full=sp.Matrix([
 -R*X*V+p*X*Y*(X-Y)+V,
 -R*Y*V+p*X*Y*(Y-X)+1-X-Y-V,
 R*Y*V-V
])
# In the y equation, I_B=1-x-y-v is used; J is the true simplex Jacobian.
J=sp.simplify(full.jacobian((X,Y,V)).subs({X:x,Y:y,V:v}))
Jtarget=sp.Matrix([
 [u*(z-1)/(z*(z+1)), u*(z-2)/(z+1), 1-z],
 [(u*(1-2*z)-z*(z+1))/(z*(z+1)),(u*(1-z)-z-1)/(z+1),-2],
 [0,u/(z+1),0]
])
assert all(sp.factor(e)==0 for e in J-Jtarget)
tr=sp.factor(sp.trace(J));det=sp.factor(J.det());S2=sp.factor((tr**2-sp.trace(J*J))/2)
A=(1-z)**2*(z*z-3*z+1)
B=(z+1)*(z**4-3*z+1)
C=z*(z+1)**2*(2*z*z-2*z+1)
P=sp.expand(A*u*u+B*u+C)
assert sp.factor(tr+(u*(1-z)**2+z*(z+1))/(z*(z+1)))==0
assert sp.factor(det-u*(z-1)*(u*(2*z+1)+z*(z+1))/(z*(z+1)**2))==0
assert sp.factor(tr*S2-det+u*P/(z*z*(z+1)**3))==0

zz=sp.Rational(3,8)
Q=200*u*u-4741*u+12342
assert sp.factor(P.subs(z,zz)-Q/32768)==0
assert sp.factor(tr.subs(z,zz)+(25*u+33)/33)==0
assert sp.factor(det.subs(z,zz)+5*u*(112*u+33)/363)==0
assert sp.factor(S2.subs(z,zz)-u*(8*u+539)/363)==0
assert sp.factor(((-tr*S2+det).subs(z,zz))-u*Q/11979)==0
umin=(sp.Integer(4741)-11*sp.sqrt(104161))/400
umax=(sp.Integer(4741)+11*sp.sqrt(104161))/400
assert sp.simplify(Q.subs(u,umin))==0 and sp.simplify(Q.subs(u,umax))==0
assert umin>0 and umax>umin
assert Q.subs(u,1)>0 and Q.subs(u,10)<0 and Q.subs(u,30)>0
# A nonzero discriminant gives transverse spectral crossings.
assert sp.discriminant(Q,u)==11**2*104161
assert sp.gcd(Q,sp.diff(Q,u))==1
assert sp.factor(sp.diff(u*Q,u).subs(u,umin))!=0
assert sp.factor(sp.diff(u*Q,u).subs(u,umax))!=0
# Exact polynomial coefficient signs establish Routh-Hurwitz at the test points.
for uu,expected in [(1,1),(10,-1),(30,1)]:
 j=J.subs({z:zz,u:uu})
 h=sp.factor(-tr*S2+det).subs({z:zz,u:uu})
 assert sp.sign(h)==expected
 import numpy as np
 eig=np.linalg.eigvals(np.array(j,dtype=float))
 npos=sum(a.real>1e-12 for a in eig)
 assert npos==(0 if expected>0 else 2)
 assert sp.factor(x.subs({z:zz,u:uu})+y.subs({z:zz,u:uu}) + (1+zz)*v.subs({z:zz,u:uu})-1)==0
 print('u=',uu,'R=',sp.factor(R.subs({z:zz,u:uu})),
       'p=',sp.factor(p.subs({z:zz,u:uu})),
       'Hurwitz sign=',expected,'positive-real-part eigenvalues=',npos)
print('two exact thresholds:',umin,umax)
print('approximate thresholds:',sp.N(umin,12),sp.N(umax,12))
print('All symbolic identities and spectral tests passed.')
