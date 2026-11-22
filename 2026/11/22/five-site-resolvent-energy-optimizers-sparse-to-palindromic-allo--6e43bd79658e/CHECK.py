"""Finite exact checks and numerical stress tests for five-site nilpotent resolvent design.
Pure Python; checks support the independently stated analytic proof, not its replacement.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random

def qfun(x):
    a,b,c,d=x
    return a*b+b*c+c*d+a*b*c+b*c*d+a*b*c*d

def qsym(E):
    s=E/2
    lo,hi=0.,s
    for _ in range(100):
        u=(lo+hi)/2;v=s-u
        derivative=(u+1)*v*v-u*(u+2)*v-u
        if derivative>0:lo=u
        else:hi=u
    u=(lo+hi)/2;v=s-u
    return s*s-u*u+u*(u+2)*v*v, (u,v,v,u)

def qboundary(E):
    y=(E-4+sqrt(E*E+4*E+16))/6
    return y*(y+2)*(E-2*y), (y,E-2*y,y,0)

def exact_symmetric_identity(x):
    a,b,c,d=x
    A=a+d; B=b+c; p=a-d; q=b-c
    Q0=(A*A*B*B+4*A*B*B+8*A*B+4*B*B)/16
    dd=(-B*B*p*p-(A+2)**2*q*q+p*p*q*q+8*p*q)/16
    return qfun(x)==Q0+dd

rnd=Random(16042)
checks=0
for _ in range(6000):
    x=[F(rnd.randrange(0,51),rnd.randrange(1,30)) for _ in range(4)]
    assert exact_symmetric_identity(x)
    checks+=1
for _ in range(600):
    E=10**rnd.uniform(-2,3)
    P,px=qsym(E);B,bx=qboundary(E)
    top=max(P,B)
    assert all(v>=-1e-10 for v in px+bx)
    assert abs(sum(px)-E)<1e-8*max(1,E)
    assert abs(sum(bx)-E)<1e-8*max(1,E)
    assert abs(qfun(px)-P)<1e-8*max(1,P)
    assert abs(qfun(bx)-B)<1e-8*max(1,B)
    for __ in range(100):
        z=[rnd.expovariate(1) for i in range(4)]
        x=[E*t/sum(z) for t in z]
        assert qfun(x)<top+2e-8*max(1,top), (E,x,qfun(x),top)
        checks+=1
    checks+=4
for E in (F(1,20),F(1,8),F(1,4),F(1,3)):
    if E<F(3,8):
        # Explicit small-budget strict comparison: boundary trial > palindromic upper.
        assert E*E/4+E**3/32>E*E/4+E**4/12
        checks+=1
for E in (F(10),F(11),F(20),F(100)):
    assert -F(1,16)-F(5,864)*E+E*E/256>0
    checks+=1
print('PASS',checks,'exact-rational identities or numerical stress assertions')
for E in (0.25,1.0,2.0,2.25,3.,10.):
    B,bx=qboundary(E);P,px=qsym(E)
    print('E=',E,'boundary=',round(B,12),'palindrome=',round(P,12),'winner=',('boundary' if B>P else 'palindrome'))
