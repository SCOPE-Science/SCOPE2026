"""Independent algebraic and numerical checks for two OU trajectory sensors.

Requirements: Python 3, sympy, mpmath. The analytic proof is in RESULT.md.
"""
import math
import sympy as sp
import mpmath as mp

count = 0
b, r, T, t, a = sp.symbols('b r T t a', positive=True)
P = b*(1-T*(r+1/r)/2)-r**2*(1+t)+T*r
Pt = -b*T*(1/r-r)/2+r**2*(1+2*t)-T*r
D = b**2-r**2
H = sp.expand(Pt*D-2*r**2*P)

def assert_zero(expr):
    global count
    assert sp.simplify(expr) == 0, repr(expr)
    count += 1

assert_zero(H.subs({r:1,t:0})-(1-T)*(b-1)**2)
assert_zero(H.subs({r:T,t:a})-b*(-(1-T**2)*(b**2+T**2)+4*a*T**2*b)/2)
assert_zero(sp.diff((1-T*sp.cosh(t))*2/a,t).subs(t,0))
assert_zero(sp.diff((1-T*sp.cosh(t))*2/a,t,2).subs(t,0)+2*T/a)

mp.mp.dps=70

def info(a, eta, c, d):
    b=1+eta; T=mp.exp(-a); r=mp.exp(-2*a*d)
    C=mp.cosh(2*a*(c-mp.mpf('0.5')))
    msum=2/a*(1-T*mp.cosh(2*a*d)*C)
    m12=r*(2*d+1/a)-T*C/a
    return (b*msum-2*r*m12)/(b*b-r*r)

def direct_info(a, eta, x, y):
    b=1+eta
    k=lambda s,z: mp.exp(-a*abs(s-z))
    m11=mp.quad(lambda s:k(s,x)**2,[0,x,1])
    m22=mp.quad(lambda s:k(s,y)**2,[0,y,1])
    m12=mp.quad(lambda s:k(s,x)*k(s,y),[0,x,y,1]) if x<y else m11
    r=mp.exp(-a*(y-x))
    return (b*(m11+m22)-2*r*m12)/(b*b-r*r)

for av,etav,c,d in [('.5','.4','.5','.1'),('1','2','.4','.08'),('2','.2','.5','.15'),('1','10','.5','0')]:
    av,etav,c,d=map(mp.mpf,(av,etav,c,d))
    xx,yy=c-d,c+d
    assert abs(info(av,etav,c,d)-direct_info(av,etav,xx,yy))<mp.mpf('1e-54')
    count+=1
    if c != mp.mpf('.5'):
        assert info(av,etav,mp.mpf('.5'),d)>info(av,etav,c,d)
        count+=1

# Boundary directional derivatives: strict improvement from collision and from endpoints.
for av in [mp.mpf('.2'),mp.mpf('1'),mp.mpf('3')]:
    for etav in [mp.mpf('.01'),mp.mpf('1'),mp.mpf('10')]:
        derivative0=mp.diff(lambda d:info(av,etav,mp.mpf('.5'),d),0)
        theoretical=4*(1-mp.exp(-av))/(etav+2)**2
        assert abs(derivative0-theoretical)<mp.mpf('1e-50')
        assert derivative0>0
        assert mp.diff(lambda d:info(av,etav,mp.mpf('.5'),d),mp.mpf('.5'))<0
        count+=3

# High-noise asymptotic placement and regret; numerical only, NOT an infinite proof.
for av in [mp.mpf('.5'),mp.mpf('1'),mp.mpf('2')]:
    eta=mp.mpf(10)**6
    C=(mp.exp(av)-1)/(2*av)
    d=mp.findroot(lambda z:mp.diff(lambda w:info(av,eta,mp.mpf('.5'),w),z),
                  (C/(eta+1)*mp.mpf('.9'),C/(eta+1)*mp.mpf('1.1')))
    coefficient=(1-mp.exp(-av))**2/(av*mp.exp(-av))
    gain=info(av,eta,mp.mpf('.5'),d)-info(av,eta,mp.mpf('.5'),0)
    assert abs(d*(eta+1)/C-1)<mp.mpf('0.0001')
    assert abs(gain*(eta+1)**3/coefficient-1)<mp.mpf('0.0001')
    count+=2

print('PASS:',count,'symbolic identities / independent quadrature / boundary / asymptotic checks')
