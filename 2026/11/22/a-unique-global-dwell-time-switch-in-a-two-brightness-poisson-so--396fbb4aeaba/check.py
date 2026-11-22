"""Reproducible rational interval checks for two-rate Poisson detection-yield theorem.

Only computational endpoint inequalities and diagnostic root isolation are checked.
The all-parameter zero-count arguments are mathematical proofs in RESULT.md.
"""
from fractions import Fraction as F
from math import factorial, ceil

COUNT=0

def verify(condition, desc):
    global COUNT
    assert condition, desc
    COUNT += 1


def eminus(x):
    """Rigorous rational enclosure for exp(-x), x >= 0.

For y=x/m in [0,1], alternating-series even/odd sums enclose exp(-y).
Raising positive bounds to m preserves their order.
    """
    x=F(x)
    verify(x >= 0, 'nonnegative exponential input')
    if x == 0:
        return F(1),F(1)
    m=ceil(x)
    y=x/m
    n=22
    lo=sum(((-y)**k)/factorial(k) for k in range(2*n+2))
    hi=sum(((-y)**k)/factorial(k) for k in range(2*n+1))
    verify(0<lo<=hi<1, 'alternating bounds')
    return lo**m,hi**m


def q2(x):
    e_lo,e_hi=eminus(x)
    k=1+F(x)
    return 1-k*e_hi,1-k*e_lo


def single_D(rate,t):
    # D=(1+t)*f'-f for f(t)=Q2(rate*t)
    rate,t=F(rate),F(t)
    e_lo,e_hi=eminus(rate*t)
    k=1+rate*t+rate*rate*t*(1+t)
    return k*e_lo-1,k*e_hi-1


def mixture_D(p,t):
    p=F(p)
    dlo,dhi=single_D(100,t)
    elo,ehi=single_D(1,t)
    return p*dlo+(1-p)*elo,p*dhi+(1-p)*ehi


def J_interval(p,t):
    p,t=F(p),F(t)
    xlo,xhi=q2(100*t)
    ylo,yhi=q2(t)
    return (p*xlo+(1-p)*ylo)/(1+t),(p*xhi+(1-p)*yhi)/(1+t)

# Uniform derivative-sign certificates: D is affine in the mixture fraction.
for p in [F(11,50),F(7,25)]:
    for t,sgn in [(F(1,20),1),(F(1,10),-1),(F(1),1),(F(3),-1)]:
        lo,hi=mixture_D(p,t)
        verify(lo>0 if sgn>0 else hi<0,f'D sign p={p},t={t}')
        print('D sign',p,t,'positive' if sgn>0 else 'negative')

# Endpoint p=11/50: ANY short stationary point lies in (1/20,1/10).
# Upper-bound its value using Q2(100t)<=1 and Q2(t)<=Q2(1/10).
low_p=F(11,50)
_,qhi=q2(F(1,10))
short_upper=(low_p+(1-low_p)*qhi)/(1+F(1,20))
long_lower,_=J_interval(low_p,F(2))
verify(short_upper<long_lower,'lower bright fraction favors long dwell')
verify(short_upper<F(213,1000),'strict short-upper decimal comparison')
verify(long_lower>F(22777,100000),'strict long-lower decimal comparison')
print('p=11/50 short bound < J(2):',float(short_upper),float(long_lower))

# Endpoint p=7/25: any long stationary point at t>1 has J<1/4.
# Analytical inequality: for 1<=t<=3, exp(t)*(3-t)/(1+t) is decreasing
# and at t=1 equals e<72/25. For t>=3, 1/(1+t)<=1/4.
# Here verify e<72/25 by a rational geometric tail bound.
# e < 1+1+1/2 + sum_{k=3}infty (1/6)*(1/4)^(k-3)=49/18
verify(F(49,18)<F(72,25),'rational e upper')
high_p=F(7,25)
short_lower,_=J_interval(high_p,F(7,100))
verify(short_lower>F(1,4),'higher bright fraction favors short dwell')
verify(short_lower>F(26134,100000),'strict short-lower decimal comparison')
print('p=7/25 J(7/100) > 1/4:',float(short_lower))

# Strong envelope derivative separation for all p in [11/50,7/25]:
# if short t in (1/20,1/10), (Q2(100t)-Q2(t))/(1+t)
# >= (Q2(5)-Q2(1/10))/(11/10) > 1/2; for long t>1,
# (Q2(100t)-Q2(t))/(1+t) <=1/2.
q5_lo,_=q2(F(5))
_,q01_hi=q2(F(1,10))
verify((q5_lo-q01_hi)/F(11,10)>F(1,2), 'strict envelope separation')
print('short envelope slope lower:', float((q5_lo-q01_hi)/F(11,10)))

# Optional numerical reconstruction is diagnostic, not relied on for the proof.
try:
    import scipy.optimize as opt
    import math
    def q(x):return -math.expm1(-x)-x*math.exp(-x)
    def d(p,t):return (1+t)*t*(p*10000*math.exp(-100*t)+(1-p)*math.exp(-t))-(p*q(100*t)+(1-p)*q(t))
    def j(p,t):return (p*q(100*t)+(1-p)*q(t))/(1+t)
    def branches(p):
        s=opt.brentq(lambda t:d(p,t),.05,.1,xtol=1e-14)
        l=opt.brentq(lambda t:d(p,t),1,3,xtol=1e-14)
        return s,l,j(p,s)-j(p,l)
    pc=opt.brentq(lambda p:branches(p)[2],.22,.28,xtol=1e-14)
    print('DIAGNOSTIC ONLY: p_star~',pc,'short~',branches(pc)[0],'long~',branches(pc)[1])
except ImportError:
    print('scipy unavailable: exact-rational checks remain complete')

print('RIGOROUS RATIONAL CHECKS PASSED:',COUNT)
