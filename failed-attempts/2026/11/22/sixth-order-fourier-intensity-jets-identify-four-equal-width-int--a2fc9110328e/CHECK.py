"""Reproduce exact algebra for equal-width four-interval Fourier intensity recovery.

Usage: python CHECK.py (requires SymPy). All infinite-domain claims are established
in the accompanying analytic proof, not by sampling.
"""
from itertools import combinations
from random import Random
import sympy as s

S,T,m,a=s.symbols('S T m a',real=True)
P,Q,W,E,F,G=s.symbols('P Q W E F G',real=True)
xs=(-S,m-T,m+T,S)
ds=tuple(xs[j]-xs[i] for i,j in combinations(range(4),2))

def assert_zero(expr):
    assert s.expand(expr)==0,s.factor(expr)

polys={
 1:2*P+W,
 2:5*P**2-4*Q+W**2+6*P*W,
 3:17*P**3-36*P*Q+W**3+15*W*P**2+15*W**2*P+60*W*Q,
}
for k in range(1,4):
    val=sum(d**(2*k) for d in ds)/4
    assert_zero(val-polys[k].subs({P:S**2+T**2,Q:S**2*T**2,W:m**2}))

Eexpr=polys[1]
Fexpr=polys[2]
assert_zero(4*Eexpr**2-3*Fexpr-((P-W)**2+12*Q))
D=F-8*E*P+12*P**2
H=s.expand(polys[3].subs({W:E-2*P,Q:(E**2+2*E*P-3*P**2-F)/4}))
assert_zero(H-(16*E**3-15*E*F+39*F*P-156*E*P**2+156*P**3))
assert_zero(s.diff(H,P)-39*D)
assert_zero(D.subs(P,E/3)-(F-4*E**2/3))
assert_zero(D.subs({E:2*P+W,F:polys[2]})-((P-W)**2-4*Q))

# Direct Taylor intensity from the four intervals agrees with recovered distance moments.
t=s.symbols('t',real=True)
Xs=(-5,0,2,5)
AA=s.Rational(1,4)
J=4+2*sum(s.cos(t*(Xs[j]-Xs[i])) for i,j in combinations(range(4),2))
I=AA**2*(s.sin(AA*t/2)/(AA*t/2))**2*J
# Use factorial coefficient identities to avoid symbolic differentiation of quotients.
for k in range(4):
    coeff=s.expand(s.series(I,t,0,8).removeO()).coeff(t,2*k)
    direct=s.expand(s.series((sum(s.exp(-s.I*t*x) for x in Xs)*sum(s.exp(s.I*t*x) for x in Xs))*AA**2*(s.sin(AA*t/2)/(AA*t/2))**2,t,0,8).removeO()).coeff(t,2*k)
    assert_zero(coeff-direct)

# Exact explicit pair of distinct geometries with matching jets through order four.
p_alt=s.Rational(2599,100)
E0=s.Integer(53); F0=s.Integer(3437)
w_alt=E0-2*p_alt
q_alt=(E0**2+2*E0*p_alt-3*p_alt**2-F0)/4
u_alt=(p_alt+s.sqrt(p_alt**2-4*q_alt))/2
v_alt=(p_alt-s.sqrt(p_alt**2-4*q_alt))/2
assert q_alt>0 and w_alt>0
assert p_alt**2-4*q_alt>0
assert u_alt>v_alt>0
assert u_alt>s.Rational(2401,100)
assert s.Rational(1,4)<v_alt<s.Rational(121,100)
assert 0<w_alt<s.Rational(121,100)
assert s.sqrt(u_alt)-s.sqrt(v_alt)-s.sqrt(w_alt)>s.Rational(27,10)
assert 2*s.sqrt(v_alt)>1
assert_zero(polys[1].subs({P:p_alt,Q:q_alt,W:w_alt})-E0)
assert_zero(polys[2].subs({P:p_alt,Q:q_alt,W:w_alt})-F0)
assert p_alt!=26

rng=Random(830671)
for _ in range(500):
    # Completely rational four-interval examples, including asymmetric interiors.
    aa=s.Rational(rng.randint(1,10),10)
    tt=aa+s.Rational(rng.randint(1,30),10)
    mm=s.Rational(rng.randint(-20,20),10)
    ss=tt+abs(mm)+aa+s.Rational(rng.randint(1,40),10)
    p=ss**2+tt**2
    q=ss**2*tt**2
    w=mm**2
    e=polys[1].subs({P:p,Q:q,W:w})
    f=polys[2].subs({P:p,Q:q,W:w})
    g=polys[3].subs({P:p,Q:q,W:w})
    assert_zero((H-g).subs({E:e,F:f,P:p}))
    assert (p-w)**2>4*q
    assert (f-8*e*p+12*p*p)>0
print('FOUR_INTERVAL_SIXTH_JET_CHECKS_PASSED')
