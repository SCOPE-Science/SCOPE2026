#!/usr/bin/env python3
"""Numerical checks for a normalized two-source delayed wash-off model.

The theorem and asymptotics are analytic; these computations independently test
its formulas over representative parameter sets and do not replace the proof.
"""
import math

checks = 0

def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def limits(a, d):
    q = math.exp(-a)
    f0 = a / (-math.expm1(-a))
    f1 = a / math.expm1(a)
    fd = a / math.expm1(a*(1-d))
    Fd = -math.expm1(-a*d)/(-math.expm1(-a))
    L = 1-d/Fd
    U0 = 1-1/f0
    U1 = (1-f1)/(fd-f1)
    return L,U0,U1

def H(a,d,w,v):
    F1 = -math.expm1(-a*v)/(-math.expm1(-a))
    F2 = 0 if v <= d else -math.expm1(-a*(v-d))/(-math.expm1(-a*(1-d)))
    return (1-w)*F1+w*F2-v

def bisection(f,l,r,positive_left=True):
    fl=f(l); fr=f(r)
    verify(fl*fr < 0, 'bisection signs')
    for _ in range(78):
        m=(l+r)*.5
        fm=f(m)
        if (fl>0)==(fm>0):
            l=m;fl=fm
        else:
            r=m;fr=fm
    return (l+r)*.5

for a in [0.05,0.3,0.9,1.0,1.3862943611198906,2,5,9]:
    c=a/math.expm1(a)
    U0=limits(a,.5)[1]
    K=c+(1-c)/U0
    dstar=1-math.log1p(a/K)/a
    verify(0<dstar<1,'crossover between 0 and 1')
    for d in [.03,.1,.25,.4,.5,.75,.9,.97]:
        L,_,U1=limits(a,d)
        U=min(U0,U1,1)
        verify(0<L<U<1,'nonempty open two-crossing interval')
        verify((d<dstar)==(U0<U1), 'unique crossover formula')
        w=(L+U)/2
        h=lambda v:H(a,d,w,v)
        eps=min(1.e-6,d/100,(1-d)/100)
        verify(h(eps)>0,'positive near origin')
        verify(h(d)<0,'negative at delay')
        verify(h(1-eps)>0,'positive before end')
        r1=bisection(h,eps,d)
        r2=bisection(h,d,1-eps)
        verify(0<r1<d<r2<1, 'two interior intersections')
        verify(abs(h(r1))<2.e-13 and abs(h(r2))<2.e-13, 'roots')
        for v in [r1*.5,(r1+d)*.5,(d+r2)*.5,(r2+1)*.5]:
            sign=(v<r1) or (v>r2)
            verify((h(v)>0)==sign,'expected sign pattern')
    for d in [1e-4,2e-4,5e-4]:
        L,U0,U1=limits(a,d)
        width=min(U0,U1)-L
        ratio=width / ((-math.expm1(-a))/2*d)
        verify(abs(ratio-1)<.02,'short delay asymptotic')
    for eps in [1e-3,2e-3,5e-3]:
        L,U0,U1=limits(a,1-eps)
        width=min(U0,U1)-L
        ratio=width / (a*eps*eps/2)
        verify(abs(ratio-1)<.05,'terminal delay asymptotic')

a=2*math.log(2);d=.5;w=1/3
L,U0,U1=limits(a,d)
verify(abs(L-.25)<1e-14, 'illustrative exact threshold 1/4')
verify(abs(H(a,d,w,d)+1/18)<1e-14,'illustrative exact mid-event deficit')
r1=bisection(lambda v:H(a,d,w,v),.001,d)
r2=bisection(lambda v:H(a,d,w,v),d,.999)
verify(abs(r1-.3125783675428164)<1e-10,'first root')
verify(abs(r2-.6383174432943601)<1e-10,'second root')
print('PASS',checks,'assertions')
print('illustration: L=',L,'U0=',U0,'U1=',U1,'roots=',r1,r2)
