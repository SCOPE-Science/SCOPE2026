"""Reproduce the rational algebra, root isolation and eigenvalue crossing certificates.
Requires Python 3 and SymPy (tested with SymPy 1.13)."""
import sympy as sp
u=sp.symbols('u',positive=True)
a,b,c,d,e,f=map(sp.Rational,['3/2','99/100','3/2','5','1/4','4'])
R=sp.Matrix([[1,a,c],[b,1,d],[e,f,0]])
assert R.det()==-sp.Rational(314,25)
x,y,z=[sp.factor(q) for q in R.inv()*sp.Matrix([1,1,1/u])]
assert sp.simplify(x-25*(7*u-3)/(157*u))==0
assert sp.simplify(y-(703-175*u)/(2512*u))==0
assert sp.simplify(z-(97-17*u)/(2512*u))==0
J=sp.Matrix([[-x,-a*x,-c*x],[-b*y,-y,-d*y],[u*e*z,u*f*z,0]])
lam=sp.symbols('lam'); chi=sp.Poly(J.charpoly(lam).as_expr(),lam)
A=7*(375*u-71)/(2512*u)
B=(20825*u**3-115685*u**2+131823*u+204573)/(3155072*u**2)
C=(7*u-3)*(17*u-97)*(175*u-703)/(3155072*u**2)
for coeff,want in zip(chi.all_coeffs(),[1,A,B,C]):assert sp.factor(coeff-want)==0
Q=2353225*u**4+217031234*u**3-1013526060*u**2+985375470*u-101672781
H=sp.factor(A*B-C)
assert sp.factor(H-Q/(7925540864*u**3))==0
P=sp.together(B).as_numer_denom()[0]
assert sp.expand(P)==20825*u**3-115685*u**2+131823*u+204573
assert sp.discriminant(P,u)==-350833582372132531200
assert [sp.sign(Q.subs(u,r)) for r in [0,sp.Rational(1,5),sp.Rational(6,5),sp.Rational(5,4),3,sp.Rational(13,4)]]==[-1,1,1,-1,-1,1]
# Descartes: three positive roots; transformed Q(-u) has one sign change.
assert [sp.sign(c) for c in sp.Poly(Q,u).all_coeffs()]==[1,1,-1,1,-1]
assert [sp.sign(c) for c in sp.Poly(Q.subs(u,-u),u).all_coeffs()]==[1,-1,-1,-1,-1]
rr=sorted(float(sp.re(root)) for root in sp.nroots(Q,maxsteps=300))
assert rr[0]<0 and 0<rr[1]<.2 and 1.2<rr[2]<1.25 and 3<rr[3]<3.25
for q in [sp.Rational(1,1),sp.Rational(2,1),sp.Rational(7,2)]:
 assert sp.sign(H.subs(u,q))== (1 if q!=2 else -1)
print('PASS: symbolic equilibrium, characteristic coefficients, exact discriminant, four isolated roots and stability signs')
print('interior crossover parameters:',*[f'{r:.14f}' for r in rr[2:]])
