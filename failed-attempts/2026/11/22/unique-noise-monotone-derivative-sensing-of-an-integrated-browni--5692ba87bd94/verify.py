"""Independent computational checks of an integrated Brownian-bridge sensor design.

Python >=3.10, SymPy >=1.11. This checker supports the analytic proof;
finite numerical tests are not a substitute for the global sign arguments.
"""
import math
import sympy as sp

s, t, e = sp.symbols('s t e', real=True)
checks = 0

def check(statement, why):
    global checks
    assert statement, why
    checks += 1

p_left = sp.Rational(1, 2)*(1-t)*s**2
p_right = t*(s-s**2/2)-t**2/2
f = 4*t**3+9*t**2-24*t+8
A = 2*(4-3*t)*(t**2+4*t-2)
B = t*(t-1)*f
F = t**2*(1-t)**2*(8-4*t-t**2)/60
v = t*(1-t)
G = F/(e+v)
alpha = sp.sqrt(6)-2

check(sp.simplify(sp.integrate(p_left**2,(s,0,t))+sp.integrate(p_right**2,(s,t,1))-F)==0,'integrated squared covariance')
check(sp.simplify(sp.integrate(s**3/3-s**4/4,(s,0,1))-sp.Rational(1,30))==0,'prior trajectory risk')
check(sp.simplify(p_right.subs(s,1)-v/2)==0,'endpoint cross covariance')
check(sp.simplify(sp.diff(G,t)-t*(t-1)*(e*A+B)/(60*(e+v)**2))==0,'gain derivative factorization')
check(sp.simplify(A.subs(t,alpha))==0,'infinite-noise root')
check(sp.simplify(sp.diff(A,t).subs(t,alpha)-(-72+40*sp.sqrt(6)))==0,'asymptotic coefficient derivative')
check(sp.simplify(B.subs(t,alpha)-(-720+294*sp.sqrt(6)))==0,'asymptotic coefficient numerator')
check(sp.simplify(F.subs(t,sp.Rational(1,2))-sp.Rational(23,3840))==0,'midpoint gain numerator')
check(sp.simplify(F.subs(t,alpha)/F.subs(t,sp.Rational(1,2))-(112896-46080*sp.sqrt(6))/23)==0,'high-noise gain ratio')
check(f.subs(t,sp.Rational(2,5))==sp.Rational(12,125),'lower beta bracket')
check(f.subs(t,sp.Rational(5,12))==sp.Rational(-4,27),'upper beta bracket')
check(sp.simplify(sp.diff(f,t).subs(t,alpha))<0,'negative derivative at alpha')
check(f.subs(t,1)==-3,'f at right endpoint')

# Numeric quadrature independently integrates the piecewise covariance, without using F.
def simpson(func, low, high, n=3000):
    h=(high-low)/n
    return h/3*(func(low)+func(high)+4*sum(func(low+(2*k-1)*h) for k in range(1,n//2+1))+2*sum(func(low+2*k*h) for k in range(1,n//2)))

def C(x,z):
    return 0.5*(1-z)*x*x if x<=z else z*(x-x*x/2)-z*z/2

def polyF(z):
    return z*z*(1-z)**2*(8-4*z-z*z)/60

for z in [0.02,0.125,0.27,0.4,0.42,0.45,0.5,0.67,0.9,0.98]:
    integral=simpson(lambda u:C(u,z)**2,0,z)+simpson(lambda u:C(u,z)**2,z,1)
    check(abs(integral-polyF(z))<5e-12,'numeric quadrature for t='+str(z))

bb=float(sp.nroots(f)[1]) # the only root inside (0,1)
aa=float(alpha)
for noise in [1e-5,1e-3,.01,.1,1,10,100,1e5]:
    def h(z):
        return noise*float(A.subs(t,z))+float(B.subs(t,z))
    left,right=bb,aa
    check(h(left)<0 and h(right)>0,'unique-root endpoint signs')
    for i in range(90):
        mid=(left+right)/2
        if h(mid)<0:left=mid
        else:right=mid
    optimum=(left+right)/2
    check(bb<optimum<aa,'root in interval')
    def gain(z):return polyF(z)/(noise+z*(1-z))
    check(gain(optimum)>gain(.5)+1e-10/(1+noise),'beats endpoint-design time')
    for offset in [-.15,-.03,.005,.02,.15]:
        z=optimum+offset
        if 0<z<1:
            check(gain(optimum)>gain(z),'global comparative grid')

print('PASS:',checks,'exact symbolic and independent numeric checks.')
