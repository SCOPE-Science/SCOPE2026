"""Standalone arithmetic diagnostics for the quadratic Bergman sign-multiplier theorem.

This executable checks formulas on finite test cases. It is not a proof
of strict convexity, global optimality, or continuous-parameter monotonicity.
Requires Python 3.9+ standard library only.
"""
from math import sqrt, exp, cosh, sinh, log, isclose
from itertools import product
from fractions import Fraction

COUNT=0

def check(condition, note):
    global COUNT
    COUNT+=1
    if not condition:
        raise AssertionError(note)

def moments(beta):
    a=[1.0]
    for k in range(1,5):
        a.append(a[-1]*k/(beta+k-1))
    return a

def d(beta,s):
    C=sqrt(3*(beta+1)/(2*(beta+2)))
    A=3*beta/(beta+2)
    B=2*(beta+1)/(beta+3)
    return 2*C*cosh(s)+0.5*sqrt(4+A*exp(2*s)+B*exp(-2*s))

def dd(beta,s):
    C=sqrt(3*(beta+1)/(2*(beta+2)))
    A=3*beta/(beta+2)
    B=2*(beta+1)/(beta+3)
    return 2*C*sinh(s)+(A*exp(2*s)-B*exp(-2*s))/(2*sqrt(4+A*exp(2*s)+B*exp(-2*s)))

def optimum(beta):
    lo,hi=-20.,20.
    for _ in range(110):
        mid=(lo+hi)/2
        if dd(beta,mid)<0:lo=mid
        else:hi=mid
    s=(lo+hi)/2
    return s,1/d(beta,s)

def fourth(beta, aa,bb,cc):
    m=moments(beta)
    coeff=[aa*aa, 2*aa*bb, bb*bb+2*aa*cc, 2*bb*cc,cc*cc]
    return sum(m[k]*abs(coeff[k])**2 for k in range(5))

def baseline(beta,aa,bb,cc):
    m=moments(beta)
    a,b,c=abs(aa),abs(bb),abs(cc)
    return a**4+4*m[1]*a*a*b*b+m[2]*b**4 +4*m[2]*a*a*c*c+4*m[3]*b*b*c*c+m[4]*c**4

# Exact-rational independent convolution and moment comparison for beta=2.
for p,q,r in product(range(-3,4),repeat=3):
    if p==q==r==0: continue
    b=Fraction(q,3);a=Fraction(p,4);c=Fraction(r,5)
    m=[Fraction(1)]
    for k in range(1,5):m.append(m[-1]*k/(2+k-1))
    cf=[a*a,2*a*b,b*b+2*a*c,2*b*c,c*c]
    F=sum(m[k]*cf[k]*cf[k] for k in range(5))
    B=a**4+4*m[1]*a*a*b*b+m[2]*b**4+4*m[2]*a*a*c*c+4*m[3]*b*b*c*c+m[4]*c**4
    check(F==B+4*m[2]*a*c*b*b,'exact quartic Fourier identity')
    ave=sum(sum(m[k]*u[k]*u[k] for k in range(5)) for u in
            ([aa*aa,2*aa*bb,bb*bb+2*aa*cc,2*bb*cc,cc*cc]
             for aa,bb,cc in ((sx*a,sy*b,sz*c) for sx,sy,sz in product([-1,1],repeat=3))))/8
    check(ave==B,'exact sign average')

for beta in [1.001,1.01,1.1,1.3,1.8,2.,3.,5.,10.,30.,100.,1000.]:
    s,delta=optimum(beta)
    check(abs(dd(beta,s))<1e-12,'stationarity')
    check(0<delta<0.5,'delta range')
    check(s<0,'negative balancing displacement')
    for offset in [-2.,-1.,-.5,-.2,-.05,0,.05,.2,.5,1.,2.]:
        check(d(beta,s+offset)+1e-12>=d(beta,s),'unique local best by grid')
    m=moments(beta)
    t=sqrt(6/((beta+1)*(beta+2)))*exp(s)
    x=sqrt(m[2]/(t*t+4*m[2]+m[4]/(t*t)))
    a=sqrt(x*t);b=1.;c=sqrt(x/t)
    Fp=fourth(beta,a,b,c);Fn=fourth(beta,a,b,-c);B=baseline(beta,a,b,c)
    check(abs((Fp-Fn)/(Fp+Fn)-delta)<3e-13,'extremal contrast')
    check(abs(Fp/B-(1+delta))<3e-13,'upper sharp expectation')
    check(abs(Fn/B-(1-delta))<3e-13,'lower sharp expectation')
    for xs in [0.3,0.7,1.,2.,5.]:
        for ys in [0.4,1.3,3.]:
            a1=xs*sqrt(x*t);c1=ys*sqrt(x/t)
            contrast=4*m[2]*a1*c1/baseline(beta,a1,1.,c1)
            check(contrast<=delta+2e-12,'global test grid')

betas=[1.000001,1.01,1.1,1.4,2.,3.,5.,8.,20.,100.,10000.]
values=[optimum(x)[1] for x in betas]
for j in range(len(values)-1):check(values[j]>values[j+1],'strict tested monotonicity')
check(abs(values[0]-2/(4+sqrt(6)))<1e-6,'Hardy endpoint')
check(abs(values[-1]-.253414805434882467)<.00003,'Gaussian endpoint')
print('PASS:',COUNT,'finite checks')
print('beta=2:',optimum(2.),'K=',((1+optimum(2.)[1])/(1-optimum(2.)[1]))**.25)
