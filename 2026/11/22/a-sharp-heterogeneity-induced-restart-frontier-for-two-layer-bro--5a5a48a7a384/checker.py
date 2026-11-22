#!/usr/bin/env python3
"""Exact and numerical checks for two-layer Fickian diffusion exit/restart.
Requires sympy and mpmath. This script is supplementary verification, not an
alternative to the analytical proof in RESULT.md.
"""
import sympy as S
import mpmath as M

x = S.symbols('x', real=True)
a,b,P,Q = S.symbols('a b P Q', positive=True)

def solve_moment(left,right,n, lengths=(a,b)):
    la, rb = lengths
    A,B,C,E = S.symbols('A B C E')
    f = S.integrate(S.integrate(-n*P*left,x),x)+A*x+B
    g = S.integrate(S.integrate(-n*Q*right,x),x)+C*x+E
    z = S.solve((f.subs(x,-la),g.subs(x,rb),B-E,A/P-C/Q),(A,B,C,E), simplify=False)
    return S.factor(f.subs(z)),S.factor(g.subs(z)),S.factor(z[B])

u0,v0=S.Integer(1),S.Integer(1)
u1,v1,m1=solve_moment(u0,v0,1)
u2,v2,m2=solve_moment(u1,v1,2)
H=a*P+b*Q
expected_m1=a*b*P*Q*(a+b)/(2*H)
expected_m2=a*b*P*Q*(a**4*P**2+5*a**3*b*P*Q+8*a**2*b**2*P*Q+5*a*b**3*P*Q+b**4*Q**2)/(12*H**2)
assert S.simplify(m1-expected_m1)==0
assert S.simplify(m2-expected_m2)==0
slope=S.factor(m1**2-m2/2)
expected_slope=-a*b*P*Q*(a**4*P**2-a*b*(a**2+4*a*b+b**2)*P*Q+b**4*Q**2)/(24*H**2)
assert S.simplify(slope-expected_slope)==0
print('PASS: general geometric and material parameter moment identities (3)')

# For the equal-length case compute an independent third moment by the same
# differential interface transmission equations.
u1s=S.factor(u1.subs({a:1,b:1}));v1s=S.factor(v1.subs({a:1,b:1}))
u2s=S.factor(u2.subs({a:1,b:1}));v2s=S.factor(v2.subs({a:1,b:1}))
u3s,v3s,m3s=solve_moment(u2s,v2s,3,lengths=(1,1))
exp_m3=P*Q*(3*P**4+42*P**3*Q+398*P**2*Q**2+42*P*Q**3+3*Q**4)/(120*(P+Q)**3)
assert S.simplify(m3s-exp_m3)==0
m1s=S.factor(m1.subs({a:1,b:1}));m2s=S.factor(m2.subs({a:1,b:1}))
c2=S.factor(m1s**3-m1s*m2s+m3s/6)
z=S.symbols('z')
poly=3*z**4-18*z**3+38*z**2-18*z+3
assert S.factor(c2-P*Q*(3*P**4-18*P**3*Q+38*P**2*Q**2-18*P*Q**3+3*Q**4)/(720*(P+Q)**3))==0
assert S.rem(poly-32*z**2,z*z-6*z+1,z)==0
assert S.simplify((S.Rational(2,45))-(S.Rational(94,15)/6-1))==0
print('PASS: symmetric third moment, critical normalized curvature and exact polynomial reduction (4)')

M.mp.dps=55

def LT(r,aa,bb,dl,dr):
    if r==0: return M.mpf(1)
    t1=M.sqrt(r/dl)*aa;t2=M.sqrt(r/dr)*bb
    return (M.sqrt(dl)/M.sinh(t1)+M.sqrt(dr)/M.sinh(t2))/(M.sqrt(dl)/M.tanh(t1)+M.sqrt(dr)/M.tanh(t2))

def reset_mean(r,aa,bb,dl,dr):
    if r==0:return aa*bb*(aa+bb)/(2*(aa*dr+bb*dl))
    f=LT(r,aa,bb,dl,dr)
    return (1-f)/(r*f)

cases=[(M.mpf(i)/7,M.mpf(j)/6,M.mpf(k)/5,M.mpf(h)/4)
        for i,j,k,h in [(2,3,4,5),(5,2,7,3),(8,13,2,19),(21,5,8,2),(4,9,17,7),(11,15,1,2),(17,1,19,11),(2,25,7,13),(3,4,12,4),(15,8,5,13)]]
for aa,bb,dl,dr in cases:
    vals={a:S.Rational(str(aa)),b:S.Rational(str(bb)),P:1/S.Rational(str(dl)),Q:1/S.Rational(str(dr))}
    target=[M.mpf(str(S.N(sym.subs(vals),45))) for sym in (m1,m2)]
    def fun(r):return LT(r,aa,bb,dl,dr)
    # Cauchy coefficient extraction with high-precision derivatives near zero.
    d1=M.diff(fun,0,1,method='step');d2=M.diff(fun,0,2,method='step')
    assert M.almosteq(-d1,target[0],rel_eps=M.mpf('1e-25'),abs_eps=M.mpf('1e-25'))
    assert M.almosteq(d2,target[1],rel_eps=M.mpf('1e-25'),abs_eps=M.mpf('1e-25'))
print('PASS: ten independent Laplace-transform moment comparisons (20)')

for ratio in [M.mpf('1'),M.mpf('2'),M.mpf('5'),M.mpf('6'),M.mpf('10'),M.mpf('25')]:
    aa=bb=dl=M.mpf(1);dr=ratio
    t0=reset_mean(0,aa,bb,dl,dr)
    w=ratio+1/ratio-6
    for r in [M.mpf('0.00001'),M.mpf('0.00002'),M.mpf('0.00004')]:
        actual=reset_mean(r,aa,bb,dl,dr)
        approx=t0-(w/24)*t0**2*r
        assert abs(actual-approx)<M.mpf('0.01')*r**2
print('PASS: six contrast ratios and three positive rates for small-rate expansion (18)')

for ratio in [3+2*M.sqrt(2),3-2*M.sqrt(2)]:
    t0=reset_mean(0,1,1,1,ratio)
    for rr in [M.mpf('0.00002'),M.mpf('0.00005'),M.mpf('0.0001')]:
        actual=reset_mean(rr,1,1,1,ratio)
        predicted=t0+M.mpf(2)/45*t0**3*rr**2
        assert abs(actual-predicted)<rr**3*2*t0**4
print('PASS: two critical ratios and three rates for positive quadratic curvature (6)')
print('All 51 independent assertions/parameter cases passed.')
