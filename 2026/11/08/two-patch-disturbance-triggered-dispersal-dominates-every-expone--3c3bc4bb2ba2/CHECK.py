"""Reproduce the two-patch pulse/continuous persistence theorem.

Requires Python 3.10+ and SymPy. All decisive algebra and the finite-time
counterexample use exact rational arithmetic; floating-point output is only
illustrative.
"""
from fractions import Fraction
from math import factorial
import sympy as S

checks = 0

def verify(statement):
    global checks
    assert statement
    checks += 1

z, ell, e, b, q = S.symbols('z ell e b q', positive=True)
c = b*q
Qp2 = S.Matrix([[-(e+b+ell), ell], [b*(1+q), -(e+2*b)]])
Qc3 = S.Matrix([[-(e+b+ell), ell, 0],
                [b, -(e+2*b+c), c],
                [2*b, 2*e, -2*(e+b)]])
Dp = S.factor((z*S.eye(2)-Qp2).det())
Dc = S.factor((z*S.eye(3)-Qc3).det())
P = (z**2 + (ell+b*q+3*b+2*e)*z
     + ell*b*q+ell*b+ell*e+2*b**2*q+2*b**2+3*b*e+e**2)
Up = S.cancel(((z*S.eye(2)-Qp2).inv()*S.ones(2,1))[1])
Uc = S.cancel(((z*S.eye(3)-Qc3).inv()*S.ones(3,1))[1])
verify(S.cancel((Up-Uc) - b*q*(z+e+b+ell)*P/(Dp*Dc)) == 0)
verify(S.factor(Dp - ((z+e+b+ell)*(z+e+2*b)-ell*b*(1+q)))==0)
verify(S.factor(Dc - ( (z+e+b+ell)*((z+e+2*b+b*q)*(z+2*(e+b))-2*e*b*q) - ell*b*(z+2*(e+b)+2*b*q) ))==0)
# All coefficients of Dp, Dc, P in z are nonnegative sums of
# monomials with nonnegative coefficients in ell,e,b,q.
r=S.symbols('r', nonnegative=True)
for poly in (Dp,Dc,P):
    # Dp positivity additionally uses the physical bound q<=1.
    pp=S.expand(poly.subs(q,1-r)) if poly==Dp else S.expand(poly)
    symbols=(ell,e,b,r) if poly==Dp else (ell,e,b,q)
    for coeff in S.Poly(pp,z).all_coeffs():
        cp=S.Poly(S.expand(coeff),*symbols)
        verify(all(a>=0 for a in cp.coeffs()))

v={ell:S.Rational(1,10),e:S.Integer(3),b:S.Integer(1),q:S.Integer(1)}
for zz in [0,S.Rational(1,7),1,3]:
    verify(S.cancel(Up.subs(v).subs(z,zz)-Uc.subs(v).subs(z,zz))>0)
verify(Up.subs(v).subs(z,0)==S.Rational(61,203))
verify(Uc.subs(v).subs(z,0)==S.Rational(469,1712))

# Direct full five-state model, with patches individually labelled.
# 0 unsuitable; 1 empty-suitable; 2 occupied-suitable.
states=[(2,0),(2,1),(0,2),(1,2),(2,2)]
def full_generator(ell_, e_, b_, q_, pulse):
    mat=S.zeros(5)
    for i,st in enumerate(states):
        for k in range(2):
            other=1-k
            def jump(dest, rate):
                if rate==0: return
                mat[i,i]-=rate
                if 2 in dest: mat[i,states.index(tuple(dest))]+=rate
            if st[k]==0:
                dest=list(st);dest[k]=1;jump(dest,ell_)
            elif st[k]==1:
                dest=list(st);dest[k]=0;jump(dest,b_)
            elif st[k]==2:
                dest=list(st);dest[k]=1;jump(dest,e_)
                dest=list(st);dest[k]=0
                if pulse and st[other]==1:
                    d2=dest.copy();d2[other]=2
                    jump(d2,b_*q_)
                    jump(dest,b_*(1-q_))
                else: jump(dest,b_)
                if not pulse and st[other]==1:
                    dest=list(st);dest[other]=2;jump(dest,b_*q_)
    return mat

for ell_,e_,b_,q_ in [(S.Rational(1,10),3,1,1),(1,2,3,S.Rational(1,2)),(2,1,1,1)]:
    for zz in [0,S.Rational(1,7),1]:
        for pulsed,Q in [(True,Qp2),(False,Qc3)]:
            full=full_generator(ell_,e_,b_,q_,pulsed)
            exact=((zz*S.eye(5)-full).inv()*S.ones(5,1))[1]
            reduced=((zz*S.eye(Q.rows)-Q.subs({ell:ell_,e:e_,b:b_,q:q_})).inv()*S.ones(Q.rows,1))[1]
            verify(S.factor(exact-reduced)==0)

# Rational uniformization certificate for t=2, e=3, b=1,
# ell=1/10, q=1. An exit-rate envelope of 8 works for both models.
F=Fraction
P_p=[[F(39,80),F(1,80),F(0)],
     [F(1,4),F(3,8),F(0)],
     [F(1,4),F(3,4),F(0)]]
P_c=[[F(39,80),F(1,80),F(0)],
     [F(1,8),F(1,4),F(1,8)],
     [F(1,4),F(3,4),F(0)]]
for M in (P_p,P_c):
    for row in M:
        verify(all(x>=0 for x in row) and sum(row)<=1)
v_p=[F(0),F(1),F(0)]
v_c=v_p[:]
W=F(0)
for n in range(81):
    h_p=sum(v_p)
    h_c=sum(v_c)
    verify(0<=h_p<=1 and 0<=h_c<=1)
    W += F(16**n,factorial(n))*(h_p-h_c)
    v_p=[sum(v_p[i]*P_p[i][j] for i in range(3)) for j in range(3)]
    v_c=[sum(v_c[i]*P_c[i][j] for i in range(3)) for j in range(3)]
# The omitted absolute tail is at most T: successive term ratios <=16/82.
T=F(16**81,factorial(81))/(1-F(16,82))
verify(W < -90)
verify(T < F(1,1000))
verify(W+T < 0)
print('PASS: exact symbolic identity, full-state resolvents, and uniformization sign')
print('Verified assertions:',checks)
print('Partial scaled survival difference W80 is between -98 and -97:',-98<W<-97)
print('Remainder bound < 1/1000:',T<F(1,1000))
print('Counterexample: survival_pulse(2) < survival_continuous(2)')
