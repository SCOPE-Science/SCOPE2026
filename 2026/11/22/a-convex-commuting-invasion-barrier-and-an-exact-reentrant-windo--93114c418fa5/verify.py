"""Independent algebraic and matrix checks for a two-city epidemic-invasion theorem."""
import sympy as sp
import numpy as np
from itertools import combinations
s,a,d,b=sp.symbols('s a d b',real=True,positive=True)
f=sp.sqrt((a*(1-s)-d)**2+4*b*s**2)
rho=(a*(1-s)+d+f)/2
r2=sp.simplify(sp.diff(rho,s,2))
assert sp.factor(r2*f**3-2*b*(a-d)**2)==0
print('SECOND DERIV VERIFIED')
st=2*a*(a-d)/(a*a+4*b)
rmin=a*(a*d+4*b)/(a*a+4*b)
P=lambda z,t:(z-a*(1-t))*(z-d)-b*t**2
assert sp.factor(P(rmin,st))==0
assert sp.factor(a*(rmin-d)-2*b*st)==0
print('OPTIMAL STATIONARY POLYNOMIAL IDENTITIES VERIFIED')
# 10-node explicit graph, City 1 K4 and City 2 3-edge matching.
pairs=list(combinations(range(4),2))
C=np.ones((4,4))-np.eye(4)
D=np.zeros((6,6))
for i,j in [(0,1),(2,3),(4,5)]:D[i,j]=D[j,i]=1
F=np.zeros((4,6))
for j,(i,k) in enumerate(pairs):F[i,j]=F[k,j]=1
assert np.all(F.sum(axis=1)==3) and np.all(F.sum(axis=0)==2)
for q in [0, (7-np.sqrt(7))/48,1/7,(7+np.sqrt(7))/48,1]:
 M=np.block([[(1-q)*(2/3)*C,q*F],[q*F.T,D]])
 full=np.linalg.eigvalsh(M)[-1]
 calc=(2*(1-q)+1+np.sqrt((2*(1-q)-1)**2+24*q*q))/2
 print('sigma',q,'full',full,'quotient',calc,'growth',0.8+(8/75)*full,'resid',abs(full-calc))
 assert abs(full-calc)<1e-12
r=sp.Rational(15,8)
poly=sp.expand((r-2+2*s)*(r-1)-6*s*s)
print('THRESHOLD FACTOR',sp.factor(poly))
assert sp.solve(poly,s)==[(7-sp.sqrt(7))/48,(7+sp.sqrt(7))/48]
print('ROOTS VERIFIED',sp.solve(poly,s))
print('MINIMUM',sp.simplify(rmin.subs({a:2,d:1,b:6})))
assert sp.simplify(rmin.subs({a:2,d:1,b:6})-sp.Rational(13,7))==0
print('OK')
