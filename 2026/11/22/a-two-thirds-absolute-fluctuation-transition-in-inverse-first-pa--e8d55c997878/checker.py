#!/usr/bin/env python3
"""Reproduce exact and numerical checks for power-law first-passage variance.

Requires mpmath and sympy. This is a supplementary checker, not a replacement
for the analytic proof or a simulation of an infinite-distance limit.
"""
import math
import mpmath as mp
import sympy as sp

mp.mp.dps = 60
count = 0


def assert_close(u, v, tol=mp.mpf('1e-22')):
    global count
    if abs(u-v) > tol*max(1, abs(u), abs(v)):
        raise AssertionError(f"mismatch: {u} vs {v}")
    count += 1


def params(alpha, A):
    a = A*alpha
    b = 2-alpha
    c = 1/(a*b)
    return a, b, c


def q(alpha, A, x):
    a, _, _ = params(alpha, A)
    return a*x**(alpha-1)


def H(alpha, A, x):
    _, b, c = params(alpha, A)
    return c*x**b


def J(alpha, A, x):
    a, b, c = params(alpha, A)
    p = alpha/b
    h = c*x**b
    return a/b*c**(-p)*mp.exp(h)*mp.gammainc(p, h, mp.inf)


def Vprime(alpha, A, x):
    return 2*q(alpha,A,x)*J(alpha,A,x)


def V(alpha,A,x):
    # The singular endpoint x=0 is integrable for every positive alpha.
    return mp.quad(lambda t:Vprime(alpha,A,t), [0,x/4,x])


def plateau(alpha,A):
    a,b,c=params(alpha,A)
    p=alpha/b
    assert alpha < mp.mpf(2)/3
    return 2*a*a/b**2 *c**(-2*p)*mp.gamma(2*p)*mp.beta(p,1-2*p)


# Independent exact solution of backward second-moment ODE for alpha=3/2.
x, A = sp.symbols('x A', positive=True)
alpha = sp.Rational(3, 2)
a = A*alpha
Uprime = (alpha-1)/x + x**(1-alpha)/a
mean = A*x**alpha
# This elementary special case is evaluated only at A=1.
var1 = sp.Rational(27,10)*x**sp.Rational(5,2) + sp.Rational(81,16)*x**2 + sp.Rational(81,16)*x**sp.Rational(3,2)
U1 = Uprime.subs(A,1)
mean1=mean.subs(A,1)
raw2=mean1**2+var1
assert sp.simplify(sp.diff(mean1,x,2)-U1*sp.diff(mean1,x)+1)==0
count += 1
assert sp.simplify(sp.diff(raw2,x,2)-U1*sp.diff(raw2,x)+2*mean1)==0
count += 1
assert sp.limit(var1,x,0,dir='+')==0
count += 1

# Drift and potential identities from the prescribed mean for several parameters.
for alpha_s in ['0.25','0.5','0.666666666666666666667','1','1.5','1.8']:
    al=mp.mpf(alpha_s)
    for As in ['0.8','1','2.5']:
        aa=mp.mpf(As)
        for xx in ['0.3','1','3','10']:
            y=mp.mpf(xx)
            qq=q(al,aa,y)
            up=(al-1)/y+y**(1-al)/(aa*al)
            assert_close(up*qq-(al-1)*qq/y,1)
            # Derivative of q and the integrated-tail factor J give L V=-2q^2.
            # J'(x)=-q(x)+J(x)/q(x) by the change-of-variable identity.
            jj=J(al,aa,y)
            qprime=(al-1)*qq/y
            jprime=-qq+jj/qq
            vp=2*qq*jj
            vpp=2*(qprime*jj+qq*jprime)
            assert_close(vpp-up*vp,-2*qq**2)

# Closed-form inverse-Gaussian constant-force check (alpha=1).
for xx in ['0.1','1','5','30']:
    y=mp.mpf(xx)
    for As in ['0.6','1','3']:
        aa=mp.mpf(As)
        assert_close(Vprime(mp.mpf(1),aa,y), 2*aa**3)
        assert_close(V(mp.mpf(1),aa,y), 2*aa**3*y)

# The second exactly solvable power provides an independent differential check.
for xx in ['0.2','1','4','16']:
    y=mp.mpf(xx)
    expected=mp.mpf(27)/4*y**(mp.mpf(3)/2) + mp.mpf(81)/8*y + mp.mpf(243)/32*mp.sqrt(y)
    assert_close(Vprime(mp.mpf('1.5'),mp.mpf(1),y),expected)

# Subcritical exact Gamma-Beta plateau, including a nontrivial alpha=1/2 special value.
half=mp.mpf('0.5')
closed=(mp.mpf(2)/9)*(mp.mpf(3)/4)**(mp.mpf(2)/3)*mp.gamma(mp.mpf(1)/3)**2
assert_close(plateau(half,1),closed)
for al in [mp.mpf('0.45'),mp.mpf('0.5'),mp.mpf('0.6')]:
    exact=plateau(al,mp.mpf('1.25'))
    # Two independent integrals must account for the whole plateau.
    partial=mp.quad(lambda t:Vprime(al,mp.mpf('1.25'),t),[0,1,3])
    tail=mp.quad(lambda t:Vprime(al,mp.mpf('1.25'),t),[3,15,mp.inf])
    assert_close(partial+tail,exact,mp.mpf('2e-10'))

# Verify the leading derivative asymptotics without assuming any finite test
# proves the limiting assertion.
for al in [mp.mpf('0.5'), mp.mpf(2)/3, mp.mpf(1),mp.mpf('1.5')]:
    aa=mp.mpf('1.1')
    vals=[]
    for xx in [mp.mpf(10),mp.mpf(1000),mp.mpf(100000)]:
        leading=2*(aa*al)**3*xx**(3*al-3)
        ratio=Vprime(al,aa,xx)/leading
        assert ratio>0
        vals.append(abs(ratio-1))
        count+=1
    assert vals[-1] <= vals[0] + mp.mpf("1e-38")
    count+=1

# Alpha=1.5 exact variance at several points, not only its derivative.
for xx in [mp.mpf('0.3'),mp.mpf(1),mp.mpf(5)]:
    exact=(mp.mpf(27)/10)*xx**(mp.mpf(5)/2)+(mp.mpf(81)/16)*xx**2+(mp.mpf(81)/16)*xx**(mp.mpf(3)/2)
    assert_close(V(mp.mpf('1.5'),mp.mpf(1),xx), exact)

print(f'PASS: {count} independent symbolic/numerical assertions')
print(f'alpha=1/2, A=1 exact limiting variance = {mp.nstr(closed, 18)}')
print('Limit statements require the analytic argument; finite checks are illustrative.')
