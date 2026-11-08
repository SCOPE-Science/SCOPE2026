"""Deterministic independent numerical checks of analytical covariance formulae.
The analytic statements are proved independently in RESULT.md; finite tests are not proofs.
"""
import math

def params(s,b):
    if abs(s+b-1)<1e-12:
        return 0.0,s,None
    q=s*b/(s+b-1)
    L=math.log((1-s)*(1-b)/(s*b))
    r=math.log((1-s)/b)/L
    return L,r,q

def forward(s,b,x):
    return s+(1-s)*x/b if x < b else s*(x-b)/(1-b)

def invert_phase(s,b,u):
    L,r,q=params(s,b)
    return u if q is None else q*(1-math.exp(L*u))

def phase(s,b,x):
    L,r,q=params(s,b)
    return x if q is None else math.log(abs((x-q)/q))/L

def cov_closed(L,t):
    t=t%1
    if abs(L)<1e-10:
        return (t*t-t+1/6)/2
    ell=abs(L)
    return math.cosh(ell*(.5-min(t,1-t)))/(2*ell*math.sinh(ell/2))-1/(ell*ell)

def bitcov(r,t):
    t=t%1
    return max(0,r-t)+max(0,r+t-1)-r*r

for s,b in [(0.2,0.5),(0.33,0.21),(0.8,0.63),(0.7,0.3),(0.2,0.8),(0.95,0.11)]:
    L,r,q=params(s,b)
    assert 0<r<1
    for u in [0.011,0.13,0.47,0.73,0.997]:
        x=invert_phase(s,b,u)
        xx=forward(s,b,x)
        u2=(u+r)%1
        if xx>1-1e-11: xx=0
        assert abs(xx-invert_phase(s,b,u2))<1e-10,(s,b,u,xx,invert_phase(s,b,u2))
        assert abs(phase(s,b,x)-u)<1e-11
    N=20000
    uu=[(k+.5)/N for k in range(N)]
    xs=[invert_phase(s,b,u) for u in uu]
    mean=sum(xs)/N
    for lag in [0,1,2,3,11]:
        shift=(lag*r)%1
        ys=[invert_phase(s,b,(u+shift)%1) for u in uu]
        empirical=sum((x-mean)*(y-mean) for x,y in zip(xs,ys))/N
        theoretical=cov_closed(L,shift)
        assert abs(empirical-theoretical)<1.2e-5,(s,b,lag,empirical,theoretical)
        b1=[int(x>b) for x in xs]
        b2=[int(y>b) for y in ys]
        empirical_bit=sum((x-r)*(y-r) for x,y in zip(b1,b2))/N
        theoretical_bit=bitcov(r,shift)
        assert abs(empirical_bit-theoretical_bit)<2e-4,(s,b,lag,empirical_bit,theoretical_bit)
    print('PASS',s,b,'rotation',round(r,9),'mean',round(mean,9),'cov0',round(cov_closed(L,0),9))
print('CIRCLE_COVARIANCE_AND_STURMIAN_CHECK_OK')
