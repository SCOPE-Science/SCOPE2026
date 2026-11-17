#!/usr/bin/env python3
"""Numerical and exact finite checks of rectangular-L parallel-volume identities.
This corroborates, but does not replace, the analytic proof in RESULT.md.
"""
import math
from fractions import Fraction
def integral(f, a, b, tol=2e-12):
    if b <= a:
        return 0.
    def simp(x0, x1, f0, fm, f1):
        return (x1-x0)*(f0+4*fm+f1)/6.
    def rec(x0,x1,f0,fm,f1,whole,eps,depth):
        mid=(x0+x1)/2
        lm=(x0+mid)/2
        rm=(mid+x1)/2
        fl=f(lm); fr=f(rm)
        left=simp(x0,mid,f0,fl,fm)
        right=simp(mid,x1,fm,fr,f1)
        err=left+right-whole
        if depth<=0 or abs(err)<=15*eps:
            return left+right+err/15.
        return (rec(x0,mid,f0,fl,fm,left,eps/2,depth-1)
                +rec(mid,x1,fm,fr,f1,right,eps/2,depth-1))
    mid=(a+b)/2
    f0=f(a);fm=f(mid);f1=f(b)
    return rec(a,b,f0,fm,f1,simp(a,b,f0,fm,f1),tol,28)


N = 0

def check(condition, detail):
    global N
    N += 1
    if not condition:
        raise AssertionError(detail)

def T_direct(t, u, v):
    # Untranslated intersection of the two rectangle offsets in the positive quadrant.
    # x<=t, y<=sqrt(t^2-(max(0,x-u))^2),
    # and, if y>v, y<=v+sqrt(t^2-x^2).
    def height(x):
        y1 = math.sqrt(max(0., t*t - max(x-u, 0.)**2))
        y2 = v + math.sqrt(max(0., t*t - x*x))
        return min(y1, y2)
    special=[]
    if v<t<=u:
        special.append(math.sqrt(t*t-(t-v)**2))
    if u==v and t>u and t<1.2*u:
        special.append((u+math.sqrt(2*t*t-u*u))/2)
    split = sorted(set([0.,min(t,u),min(t,v),t]+special))
    return sum(integral(height,a,b) for a,b in zip(split,split[1:]) if b>a)

def T_unequal_branch(t, u, v):
    A = min(u,v)
    B = max(u,v)
    assert A<t<B
    s = t-A
    return A*t + (s*math.sqrt(t*t-s*s)+t*t*math.asin(s/t))/2

def T_equal_branch(t, a):
    assert a<t<a*1.2
    eta = (math.sqrt(2*t*t-a*a)-a)/2
    # this formula is valid near the first contact for equal arms
    I1 = (eta*math.sqrt(t*t-eta*eta)+t*t*math.asin(eta/t))/2
    def F(x):
        return (x*math.sqrt(max(0.,t*t-x*x))+t*t*math.asin(min(1.,x/t)))/2
    I2 = F(t)-F(a+eta)
    return a*(2*t-a-eta)+I1+I2

for u,v in [(1.,1.),(0.5,1.5),(1.,2.),(0.75,1.25),(2.,0.5), (0.3,0.7)]:
    R=min(u,v)
    for t in [R*.2,R*.5,R*.8,R, R*1.01]:
        Td=T_direct(t,u,v)
        if t <= R:
            check(abs(Td-t*t)<1e-9,(u,v,t,Td,t*t))
        else:
            check(Td<t*t,(u,v,t,Td,t*t))
            if u!=v and t<max(u,v):
                Ta=T_unequal_branch(t,u,v)
            elif u==v:
                Ta=T_equal_branch(t,u)
            else:
                continue
            check(abs(Td-Ta)<2e-9,(u,v,t,Td,Ta))

for r in [.2,.5,1.,2.]:
    for u,v in [(r,2*r),(2*r,r),(r,r)]:
        coeff = (1/3 if u==v else 1/6)/r
        for relative in [0.02,0.01,0.005]:
            t=r*(1+relative)
            T= T_equal_branch(t,r) if u==v else T_unequal_branch(t,u,v)
            measured=(t*t-T)/(t-r)**3
            check(abs(measured-coeff)/coeff < .045,(r,u,v,t,measured,coeff))

# Exact rational scale and pairwise arm limits.
for a in [Fraction(1,17),Fraction(1,7),Fraction(1),Fraction(5,2)]:
    for b in [Fraction(1,13),Fraction(2,3),Fraction(3)]:
        for u,v in [(Fraction(1),Fraction(1)),(Fraction(2),Fraction(1)),
                    (Fraction(1),Fraction(3))]:
            m=min(a,b,u,v)
            C=m/3
            R=min(u,v)
            check(3*C==m,(a,b,u,v))
            check(R>=3*C,(a,b,u,v))

for epsilon in [Fraction(1,2),Fraction(1,10),Fraction(1,100),Fraction(1,10000)]:
    c=epsilon/3
    p=Fraction(1)
    check(p/c == 3/epsilon,epsilon)

print(f'PASS: {N} independent numerical/rational assertions')
