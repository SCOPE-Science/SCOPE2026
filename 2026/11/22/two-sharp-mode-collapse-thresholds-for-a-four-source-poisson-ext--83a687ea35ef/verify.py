#!/usr/bin/env python3
"""Exact polynomial/Sturm verification for the four-Poisson-source mode law.
Requires sympy. Run: python3 verify.py
"""
import sympy as s
u,q=s.symbols('u q')

def d(a):return u**2+2*(q-a)*u+(q+a)**2
def n(a):return (q+a)*(3*a-q)-2*(q+a)*u-u**2
P=s.Poly(s.expand(n(1)*d(9)**2+n(9)*d(1)**2),u)
H=123245*q**5-361571*q**4+965120*q**3+1003680*q**2-3075840*q-2633472
Q=q**4+42*q**2-40*q-1107
C=664082786653543858176
checks=0
def check(x,msg):
 global checks
 assert x,msg
 checks+=1
check(s.simplify(s.discriminant(P.as_expr(),u)-C*(q+1)**5*(q+4)**4*(q+9)*H)==0,'discriminant')
check(s.expand(P.eval(0)+2*(q+1)*(q+9)*Q)==0,'center coefficient')
check(s.discriminant(616225*q**2-1084713*q+1447680,q)<0,'strictly positive quadratic')
check(s.expand(s.diff(H,q,2)-4*(q*(616225*q**2-1084713*q+1447680)+501840))==0,'H convexity')
check(H.subs(q,1)<0<H.subs(q,2),'first threshold bracket')
check(Q.subs(q,4)<0<Q.subs(q,5),'second threshold bracket')
check(s.expand(s.diff(Q,q,2)-(12*q**2+84))==0,'second threshold convexity')

def variations(signs):
 signs=[z for z in signs if z]
 return sum(1 if a*b<0 else 0 for a,b in zip(signs,signs[1:]))

for t,expected in [(1,3),(2,1),(5,0)]:
 poly=s.Poly(P.as_expr().subs(q,t),u)
 st=s.sturm(poly.as_expr(),u)
 s0=[s.sign(z.subs(u,0)) for z in st]
 sinfty=[s.sign(s.LC(s.Poly(z,u))) for z in st]
 count=variations(s0)-variations(sinfty)
 check(count==expected, f'Sturm count at q={t}: {count}')
 check(poly.count_roots(0,s.oo)==expected, 'independent root count')

x=s.symbols('x',real=True)
Fx=s.diff(sum(1/((x-a)**2+q) for a in [-3,-1,1,3]),x)
assert s.factor(Fx-4*x*P.as_expr().subs(u,x*x)/(d(1).subs(u,x*x)**2*d(9).subs(u,x*x)**2))==0
checks+=1
# Isolated positive real algebraic thresholds (approximation is presentation only).
rootsH=[complex(v) for v in s.nroots(H)]
rootsQ=[complex(v) for v in s.nroots(Q)]
positive=lambda arr:[z.real for z in arr if abs(z.imag)<1e-11 and z.real>0]
check(len(positive(rootsH))==1,'first positive threshold numerical supplementary check')
check(len(positive(rootsQ))==1,'second positive threshold numerical supplementary check')
print('CHECKS_PASSED',checks)
print('critical_q_fold',format(positive(rootsH)[0],'.15f'))
print('critical_q_center',format(positive(rootsQ)[0],'.15f'))
print('sturm_positive_root_counts',{t:s.Poly(P.as_expr().subs(q,t),u).count_roots(0,s.oo) for t in [1,2,5]})
