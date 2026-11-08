"""Reproduce the five-site cyclic-logistic Neimark--Sacker coefficient.
Requires Python 3 and SymPy; no network access or external data.
"""
import math
import sympy as S
u=S.symbols('u',positive=True,real=True)
k=(S.sqrt(5)-1)/2
P=(10-9*k)*u**3+(18-30*k)*u**2+(11*k-18)*u+6
Q=5*(1-k)*u**2+(3*k-2)*u+1
assert S.simplify((3*k-2)**2-20*(1-k))==-(13+S.sqrt(5))/2
assert S.simplify(k*k+k-1)==0
for a,sign in [(S.Rational(1,2),1),(S.Rational(3,4),-1),(S.Rational(5,4),-1),(S.Rational(3,2),1)]:
 assert sign*float(P.subs(u,a).evalf(50))>0
ucrit=(5+S.sqrt(5))/8
assert float(P.subs(u,ucrit).evalf(50))<0
assert float(Q.subs(u,ucrit).evalf(50))>0
# Evaluate Fourier Lyapunov formula and its independent rational-polynomial reduction.
b=S.symbols('b',positive=True,real=True)
t=2/(1+b*b)
r=1+t
lam=1-t+S.I*t*b
lam2=1-t+S.I*t*k*b
h11=-2*r/t
h20=2*r*(-1+S.I*b)/(lam*lam-lam2)
g=2*r*h11*(-2+S.I*b)+r*(-2+S.I*(k-1)*b)*h20
# Rational polynomial expression in b, k with k^2+k=1.
P_b=P.subs(u,b*b)
Q_b=Q.subs(u,b*b)
expected=-(b*b+3)**2*P_b/(2*(b*b+1)**2*Q_b)
assert S.simplify(S.re(S.conjugate(lam)*g)/2-expected)==0
# Independent complex Fourier tensor sum, with both convolution pathways.
for alpha in [S.Rational(1,4),S.Rational(1,2),S.Rational(3,4)]:
 beta=2*alpha*S.sin(2*S.pi/5)
 uval=S.simplify(beta*beta)
 tc=2/(1+uval);rc=1+tc
 L=1-tc+S.I*tc*beta
 L2=1-tc+S.I*tc*2*alpha*S.sin(4*S.pi/5)
 H11=-2*rc/tc
 H20=2*rc*(-1+S.I*beta)/(L**2-L2)
 B1=rc*(-2+S.I*(2*alpha*S.sin(4*S.pi/5)-beta))*H20
 B2=2*rc*(-2+S.I*beta)*H11
 val=S.re(S.conjugate(L)*(B1+B2))/2
 direct=S.N(val,35)
 reduced=S.N(expected.subs(b,beta),35)
 assert abs(complex(direct)-complex(reduced))<1e-25
# Global criticality sign and nonresonant example.
roots=S.nroots(P,maxsteps=100)
positive=sorted([float(S.re(z)) for z in roots if abs(float(S.im(z)))<1e-14 and float(S.re(z))>0])
assert len(positive)==2 and .5<positive[0]<.75 and 1.25<positive[1]<1.5
print('VERIFY_OK five_site_quadratic_normal_form=1 golden_cyclotomic_identity=1 exact_sign_brackets=4 explicit_subcritical_parameter=1 arbitrary_alpha_fourier_checks=3 roots=', positive)
