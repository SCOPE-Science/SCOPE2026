"""Reproduce symbolic and numerical checks for the May--Leonard period theorem."""
from fractions import Fraction
import sympy as sp
import mpmath as mp

x, y, z, p, d = sp.symbols('x y z p d', real=True)
alpha, beta = 1-d, 1+d
F = [x*(1-x-alpha*y-beta*z),
     y*(1-beta*x-y-alpha*z),
     z*(1-alpha*x-beta*y-z)]
S=x+y+z
assert sp.expand(sum(F) - S*(1-S) - d*(x*y+y*z+z*x)*0) == 0
# Ratio xyz/S^3 is constant even off S=1.
H=x*y*z/S**3
assert sp.factor(sum(sp.diff(H,v)*f for v,f in zip((x,y,z),F))) == 0
assert sp.factor(F[0].subs(z,1-x-y) - d*x*(y-(1-x-y))) == 0
P = x*x*(1-x)**2-4*p*x
B=6*x**5-15*x**4+11*x**3-(6*p+2)*x*x
identity=12*p*(1-27*p)*x*x+2*(1-54*p)*x*P-6*P**2-(sp.diff(B,x)*P-sp.Rational(3,2)*B*sp.diff(P,x))
assert sp.simplify(identity) == 0

mp.mp.dps=65
D=mp.mpf('0.4')
for ps in ('0.0007','0.003','0.01','0.025'):
    t=mp.mpf(ps)
    roots=sorted([mp.re(r) for r in mp.polyroots([1,-2,1,-4*t],maxsteps=600)])
    r1,r2,r3=roots
    assert 0 < r1 < mp.mpf(1)/3 < r2 < 1 < r3
    def x_theta(theta): return r1+(r2-r1)*mp.sin(theta)**2
    by_quad=(4/D)*mp.quad(lambda theta: 1/mp.sqrt(x_theta(theta)*(r3-x_theta(theta))),[0,mp.pi/2])
    by_hyp=(2*mp.pi*mp.sqrt(3)/D)*mp.hyp2f1(mp.mpf(1)/3,mp.mpf(2)/3,1,1-27*t)
    assert abs(by_quad/by_hyp-1)<mp.mpf('1e-52'),(ps,by_quad,by_hyp)
    print('p',ps,'period',mp.nstr(by_quad,19),'rel_error',mp.nstr(abs(by_quad/by_hyp-1),4))

# Monotonicity in p follows rigorously from positive hypergeometric coefficients.
for n in range(1,15):
    coeff=sp.rf(sp.Rational(1,3),n)*sp.rf(sp.Rational(2,3),n)/sp.factorial(n)**2
    assert coeff>0

# Check leading and first logarithmic corner term at decreasing p.
for ps in ('1e-5','1e-6'):
    t=mp.mpf(ps)
    T=(2*mp.pi*mp.sqrt(3))*mp.hyp2f1(mp.mpf(1)/3,mp.mpf(2)/3,1,1-27*t)
    asymp=3*(mp.log(1/t)+6*t*(mp.log(1/t)-mp.mpf('2.5')))
    assert abs(T-asymp)<1000*t*t*mp.log(1/t)
    print('asymptotic p',ps,'error',mp.nstr(T-asymp,12))
print('CHECKS_PASS')
