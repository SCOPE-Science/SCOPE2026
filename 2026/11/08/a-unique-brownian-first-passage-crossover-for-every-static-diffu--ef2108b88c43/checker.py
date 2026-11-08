#!/usr/bin/env python3
"""Independent exact-differentiation and high-precision examples for the static-diffusivity FPT crossover."""
from math import isclose
import mpmath as mp
import sympy as sp
mp.mp.dps = 65
D,t,a = sp.symbols('D t a', positive=True)
F = sp.erfc(a / (2*sp.sqrt(D*t)))
D2 = sp.simplify(sp.diff(F,D,2))
T1 = sp.simplify(sp.diff(F,t))
wanted_D2= a*sp.exp(-a*a/(4*D*t))/(2*sp.sqrt(sp.pi*t)*D**sp.Rational(5,2))*(a*a/(4*D*t)-sp.Rational(3,2))
wanted_T1 = a*sp.exp(-a*a/(4*D*t))/(2*sp.sqrt(sp.pi*D)*t**sp.Rational(3,2))
assert sp.simplify(D2-wanted_D2)==0
assert sp.simplify(T1-wanted_T1)==0

def bisect_sign(f,l,r,n=320):
    fl=f(l);fr=f(r)
    assert fl*fr<0, (l,r,fl,fr)
    for _ in range(n):
        m=(l+r)/2; fm=f(m)
        if fl*fm>0:l=m;fl=fm
        else:r=m;fr=fm
    return (l+r)/2

def check(weights, ds, label,expected=None):
    ws=list(map(mp.mpf,weights));ds=list(map(mp.mpf,ds))
    assert len(ws)==len(ds)>=2 and all(w>0 for w in ws) and all(d>0 for d in ds) and mp.almosteq(sum(ws),1)
    mean=sum(w*d for w,d in zip(ws,ds)); dmin=min(ds);dmax=max(ds)
    c=mp.sqrt(1/mean)
    def cdf(d,x):return mp.erfc(1/(2*mp.sqrt(d*x)))
    def gap(x):return sum(w*cdf(d,x) for w,d in zip(ws,ds))-cdf(mean,x)
    def K(y):return sum(w/mp.sqrt(d)*mp.exp(-y*(1/d-1/mean)) for w,d in zip(ws,ds))
    def K2(y):return sum(w/mp.sqrt(d)*(1/d-1/mean)**2*mp.exp(-y*(1/d-1/mean)) for w,d in zip(ws,ds))
    lo=mp.mpf(1)/(6*dmax);hi=mp.mpf(1)/(6*dmin)
    assert gap(lo)>0 and gap(hi)<0
    root=bisect_sign(gap,lo,hi)
    if expected is not None: assert abs(root-mp.mpf(expected))<mp.mpf('1e-30'), (root,expected)
    assert gap(root) == 0 or abs(gap(root))<mp.mpf('1e-60')
    assert K(0)>c and all(K2(mp.power(10,k))>0 for k in range(-9,10))
    # Locate the two crossings of the differentiated CDF gap, with y = 1/(4*t).
    f=lambda tt:K(1/(4*tt))-c
    ts=[mp.power(10,mp.mpf(k)/20) for k in range(-90,91)]
    brackets=[(p,q) for p,q in zip(ts,ts[1:]) if f(p)*f(q)<0]
    assert len(brackets)==2,brackets
    extrema=[bisect_sign(f,p,q) for p,q in brackets]
    assert extrema[0]<root<extrema[1]
    assert gap(extrema[0])>0 and gap(extrema[1])<0
    for factor in [mp.mpf('0.001'),mp.mpf('0.01'),mp.mpf('0.1'),mp.mpf('0.5')]:
        assert gap(root*factor)>0
    for factor in [mp.mpf('1.1'),mp.mpf('2'),mp.mpf('10'),mp.mpf('100'),mp.mpf('1000')]:
        assert gap(root*factor)<0
    print(label, 't_star=',mp.nstr(root,40),'CDF=',mp.nstr(cdf(mean,root),25),'peak_t=',mp.nstr(extrema[0],22),'trough_t=',mp.nstr(extrema[1],22))
    return root
r=check(['0.5','0.5'],[1,4],'binary', '0.076433482509034972001084981222609529')
assert mp.mpf(1)/24<r<mp.mpf(1)/6
check(['0.2','0.3','0.5'],['0.1',1,5],'3atom')
check(['0.05','0.15','0.55','0.25'],['0.01','0.7',2,12],'4atom')
print('PASS: 2 symbolic identities, two derivative extrema and unique crossover on three nondegenerate mixtures, high-precision bounds and signs')
# A positive finite-mean law whose inverse square-root moment diverges:
# D=U^2 with U uniform on (0,1), E[D]=1/3, E[D^(-1/2)]=infinity.
def heavy_gap(tt):
    b=mp.mpf(1)/(2*mp.sqrt(tt))
    return mp.erfc(b)-b/mp.sqrt(mp.pi)*mp.e1(b*b)-mp.erfc(mp.sqrt(3)*b)
def heavy_K(y):
    return mp.exp(3*y)*mp.e1(y)/2
z=bisect_sign(heavy_gap,mp.mpf('.3'),mp.mpf('1'))
assert mp.almosteq(z,mp.mpf('0.61606293116130586060783880064700849025288930235186'),rel_eps=mp.mpf('1e-45'))
ycrit=mp.mpf(3)**mp.mpf('.5')
assert heavy_K(mp.mpf('1e-20'))>ycrit and heavy_K(mp.mpf('50'))>ycrit
assert heavy_K(mp.mpf('.5'))<ycrit
assert heavy_gap(mp.mpf('.1'))>0 and heavy_gap(mp.mpf('10'))<0
assert mp.sqrt(mp.mpf('1e10'))*heavy_gap(mp.mpf('1e10'))< -6
print('heavy inverse-moment example t_star=',mp.nstr(z,43))
print('PASS: additional explicit U^2-law example with divergent negative half moment')
