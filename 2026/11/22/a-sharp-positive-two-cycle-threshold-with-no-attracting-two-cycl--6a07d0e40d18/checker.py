"""Exact algebraic checks for the unit-step modified reduced Lorenz map.

Usage: python checker.py.  Requires sympy.  This complements the written proof;
numerical samples below are diagnostics, not the infinite-case argument.
"""
import sympy as s

a,u,v,t,p,q=s.symbols('a u v t p q', real=True)
B=a*a-a-3
P=v*v-B*v+(a+2)
Delta=s.factor(s.discriminant(P,v))
assert s.factor(Delta-(a*a-3*a-1)*(a*a+a-1))==0
V=a*(u-1)-2
E=s.expand(a*(u-u*u+2*V)-u*V)
assert s.factor(s.resultant(P,v-V,v))==s.factor(P.subs(v,V))
assert s.factor(a*E+2*P.subs(v,V))==0
# Reduced two-cycle equations (q and p are successive first coordinates).
Eq1=q-p*(1+a-a*p-q*q)
Eq2=p-q*(1+a-a*q-p*p)
assert s.factor(Eq1+Eq2)==s.factor(-a*(p+q-(p*p+q*q))+p*q*(p+q))
assert s.factor(Eq1-Eq2)==s.factor(-(p-q)*(2+a*(1-p-q)+p*q))
# q-p identities after using the two symmetric relations.
U=1+(v+2)/a
D=s.factor(U*U-4*v)
fu=s.factor(-a*u*u+(a*a+a+1)*u-a*a-2*a)
assert s.factor(s.resultant(fu,u*u-4*(a*(u-1)-2),u)+(a+2)*(3*a**3-10*a*a-8*a-4))==0
# Floquet: J at (p,q^2), then J at (q,p^2).
Jp=s.Matrix([[1+a-2*a*p-q*q,-p],[2*p,0]])
Jq=s.Matrix([[1+a-2*a*q-p*p,-q],[2*q,0]])
K=Jq*Jp
T=s.expand(s.trace(K))
DET=s.factor(K.det())
assert s.factor(DET-4*(p*q)**2)==0
# On an actual orbit, q/p = 1+a-a*p-q^2 and vice versa.
TrOrbit=1-a*((p**3+q**3)/(p*q))+a*a*p*q-2*(p*p+q*q)
assert s.simplify(Jp[0,0]-(q/p-a*p)+Eq1/p)==0
assert s.simplify(Jq[0,0]-(p/q-a*q)+Eq2/q)==0
# The trace formula derived by substituting the two orbit equations.
TrUV=1-a*(U**3-3*U*v)/v+a*a*v-2*(U*U-2*v)
H=s.factor((1+TrUV+4*v*v)*v*a*a)
assert s.denom(H)==1
Q=5*a**8-14*a**7-55*a**6+60*a**5+93*a**4-86*a**3-72*a*a+22*a+10
assert s.factor(s.resultant(P,H,v)+a*a*(a+2)*Q)==0
shift=s.Poly(s.expand(Q.subs(a,t+s.Rational(9,2))),t)
assert all(c>0 for c in shift.all_coeffs())
assert s.simplify(P.subs(v,s.Rational(1,2))-(-2*a*a+6*a+15)/4)==0
assert 3*4**3-10*4**2-8*4-4<0<3*5**3-10*5**2-8*5-4
V5=(17-s.sqrt(261))/2
H5=s.simplify((1+TrUV+4*v*v).subs({a:5,v:V5}))
assert s.simplify(H5-(39269-7347*s.sqrt(29))/50)==0
assert s.sign(H5)==-1
D5=s.simplify(D.subs({a:5,v:V5}))
assert s.simplify(D5-(-1089+207*s.sqrt(29))/50)==0
assert s.sign(D5)==1
V5large=(17+s.sqrt(261))/2
assert s.sign(s.simplify(D.subs({a:5,v:V5large})))==-1
# Reconstruct representative exact positive two-cycles; numeric diagnostics.
for aa in [s.Rational(41,10),s.Rational(5),s.Rational(10)]:
 BB=B.subs(a,aa)
 vv=(BB-s.sqrt(Delta.subs(a,aa)))/2
 uu=U.subs({a:aa,v:vv})
 dd=D.subs({a:aa,v:vv})
 pp=(uu+s.sqrt(dd))/2;qq=(uu-s.sqrt(dd))/2
 assert float(pp)>float(qq)>0
 assert abs(float(Eq1.subs({a:aa,p:pp,q:qq})))<1e-9
 assert abs(float(Eq2.subs({a:aa,p:pp,q:qq})))<1e-9
 assert abs(float((K.det()-4*p*p*q*q).subs({a:aa,p:pp,q:qq})))<1e-8
print('PASS: exact discriminant, cycle elimination, Floquet determinant, resultant, positive-shift certificate, sign and sample identities')
