"""Standalone arithmetic and numerical diagnostics for the three-dimensional sine map.
Run python3 checker.py; finite diagnostics do not establish infinite convergence.
"""
from fractions import Fraction as Q
from math import sin,cos,sqrt,pi

def check(r,s):
    b=1-r+s;D=2+r+s
    assert 0<s<r<1 and b+r-s==1
    # (L-1)(L^2+(1+s)L+r)=L^3+s L^2-b L-r
    assert r-(1+s)==-b
    assert (r+(1+s)+1)==D
    assert r+b==1+s # W(F)-W=sin(z)-z, exactly
    assert 1-r>0 and r-s>0 and 2+r+s>0
    cubic=-Q(1,6)/D
    assert cubic<0
    x=y=z=.1;n=250000
    for _ in range(n):
        x,y,z=y,sin(z),float(r)*x+float(b)*y-float(s)*sin(z)
    got=n*z*z;expected=3*float(D)
    assert abs(got/expected-1)<.02
    print('parameters',r,s,'b*',b,'cubic',cubic,'n*z_n^2',got,'expected',expected)

def detuning():
    r=.5;s=.25;eps=1e-5;h=1+eps;b=.75+eps;D=2+r+s
    lo=0.;hi=min(h,pi)
    for _ in range(90):
        m=(lo+hi)/2
        if h*sin(m)>m:lo=m
        else:hi=m
    z=(lo+hi)/2
    assert abs(z-h*sin(z))<1e-13
    c=cos(z)
    def P(l):return l**3+s*c*l*l-b*c*l-r*c
    lo=.8;hi=1.2
    for _ in range(80):
        m=(lo+hi)/2
        if P(m)>0:hi=m
        else:lo=m
    lam=(lo+hi)/2
    assert abs(z/sqrt(6*eps)-1)<.0001
    assert abs((lam-1)/eps+2/D)<.0001
    print('branch',z,'multiplier',lam,'expected slope',-2/D)

if __name__=='__main__':
    for r,s in ((Q(1,2),Q(1,4)),(Q(3,5),Q(3,10)),(Q(4,5),Q(1,10))):check(r,s)
    detuning()
    print('PASS: arithmetic and finite diagnostics')
