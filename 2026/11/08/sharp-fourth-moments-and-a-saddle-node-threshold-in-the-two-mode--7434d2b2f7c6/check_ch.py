#!/usr/bin/env python3
"""Exact rational/symbolic checks for two-mode Poisson–Charlier fourth-moment geometry.
Requires SymPy (tested with 1.14.0); no network or private inputs.
"""
import sympy as sp
x, lam, t, u = sp.symbols('x lam t u')
C1=x-lam
C2=x*(x-1)-2*lam*x+lam**2
X=sp.Poly((C1+t*C2)**4,x)
M=lambda n: sum(sp.functions.combinatorial.numbers.stirling(n,k,kind=2)*lam**k for k in range(n+1))
F=sp.factor(sum(co*M(deg[0]) for deg,co in X.terms()))
N=lam+2*lam**2*t**2
F_expected=lam*(1+3*lam+24*lam*t+(48*lam+60*lam**2)*t**2+(32*lam+192*lam**2)*t**3+(8*lam+144*lam**2+60*lam**3)*t**4)
assert sp.expand(F-F_expected)==0
assert sp.expand(sum(co*M(deg[0]) for deg,co in sp.Poly((C1+t*C2)**2,x).terms())-N)==0
Q=(48*lam**2+8*lam)*t**4-(48*lam+4)*t**3-(54*lam+12)*t**2-(12*lam+11)*t-3
assert sp.expand(sp.diff(F,t)*N-2*F*sp.diff(N,t)+8*lam**3*Q)==0
print('EXACT_POISSON_MOMENTS_AND_CRITICAL_QUARTIC_OK')
p=(5038848*lam**8-11967264*lam**7+4047408*lam**6+4710798*lam**5+251748*lam**4+10260*lam**3+7587*lam**2+180*lam-1)
assert sp.expand(sp.discriminant(Q,t)+256*p)==0
assert sp.gcd(p,sp.diff(p,lam))==1
st=sp.sturm(p,lam)
def signs(point):
 return [int(sp.sign(sp.Poly(z,lam).LC() if point==sp.oo else z.subs(lam,point))) for z in st]
def variation(a):
 ss=[z for z in a if z]
 return sum(ss[i]!=ss[i+1] for i in range(len(ss)-1))
assert [variation(signs(q)) for q in [0,sp.Rational(1,250),sp.Rational(1,200),sp.oo]] == [3,3,2,2]
assert sp.sign(p.subs(lam,sp.Rational(1,250)))==-1 and sp.sign(p.subs(lam,sp.Rational(1,200)))==1
print('EXACT_UNIQUE_POSITIVE_DISCRIMINANT_ROOT_STURM_OK')
a=-sp.Rational(1,2)
D=sp.factor((F*N.subs(t,a)**2-F.subs(t,a)*N**2)/lam**4)
P=sp.Poly(sp.expand(D.subs(t,-1-u)),u)
co=[sp.factor(P.nth(i)) for i in range(5)]
assert all(sp.expand(a-b)==0 for a,b in zip(co,[(192*lam**3+284*lam**2+53*lam+2)/4,2*lam*(120*lam**2+185*lam+58),2*(216*lam**3+360*lam**2+163*lam-2),8*lam*(42*lam**2+79*lam+46),4*(24*lam**3+52*lam**2+37*lam+2)]))
R=104-2812*lam-12850*lam**2-22109*lam**3-17340*lam**4-5256*lam**5
assert sp.expand(4*co[0]*co[4]-co[2]**2-32*lam*R)==0
assert R.subs(lam,sp.Rational(1,200))>0
assert sp.factor(Q.subs(t,-1))==2*lam*(24*lam+7)
assert sp.factor(Q.subs(t,-sp.Rational(1,2)))==lam*(3*lam-1)
assert sp.factor(Q.subs(t,0))==-3
assert sp.expand(Q.subs(lam,0)+ (t+1)*(2*t+1)*(2*t+3))==0
print('EXACT_GLOBAL_MIN_BRANCH_COMPARISON_OK')
for L,want in [(sp.Rational(1,1000),4),(sp.Rational(1,100),2),(sp.Integer(1),2)]:
 assert sp.Poly(Q.subs(lam,L),t).count_roots(-sp.oo,sp.oo)==want
print('EXACT_SAMPLE_ROOT_COUNTS_OK')
print('ALL_POISSON_CHARLIER_CHECKS_PASSED')
