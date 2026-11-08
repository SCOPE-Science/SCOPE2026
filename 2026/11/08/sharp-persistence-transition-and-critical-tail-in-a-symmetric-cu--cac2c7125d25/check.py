"""Independent arithmetic checks for the cubic neuronal Lorenz slice.

Run: python check.py
Uses the Python standard library only. Analytic results are proved separately.
"""
import math

def c_of(mu): return math.sqrt(0.25-1/mu)
def branch(mu,u):
    c=c_of(mu)
    return (1+mu/4)*u-mu*u**3-(c if u>=0 else -c)
def right_fixed(mu):
    c=c_of(mu)
    return (-c+math.sqrt(c*c+4/mu))/2

for mu in (4.1,4.5,5,5.7,6,6.1,7,7.9):
    c=c_of(mu)
    assert abs(branch(mu,c)-c)<1e-12
    assert abs(branch(mu,-c)+c)<1e-12
    assert abs((1+mu/4)-mu*c*c-2)<1e-12
    assert abs((1+mu/4)-3*mu*c*c-(4-mu/2))<1e-12
    ustar=right_fixed(mu)
    assert abs(branch(mu,ustar)-ustar)<1e-12
    if mu<6: assert ustar>c and (4-mu/2)>1
    if mu>6: assert 0<ustar<c and 0<(4-mu/2)<1
    if mu==6: assert abs(ustar-c)<1e-14
    for j in range(501):
        u=c*j/500
        assert -c-1e-12 <= branch(mu,u) <= c+1e-12
        assert (1+mu/4)-3*mu*u*u>0

# Critical inverse branch recurrence for the exact first-switch tail.
mu=6.0
c=c_of(mu)
a=3*math.sqrt(3)
v=c
for n in range(1,10001):
    target=v
    x=target
    for _ in range(10):
        fun=x+a*x*x-6*x**3-target
        der=1+2*a*x-18*x*x
        x-=fun/der
    assert 0<x<target
    v=x
    if n in (10,100,1000,10000):
        tail=v/c
        print('n',n,'P(tau>n)',format(tail,'.12g'),'nP',format(n*tail,'.10g'))
        if n==10000:assert abs(n*tail-2/3)<0.002
print('CUBIC_NEURON_SYMMETRIC_PARABOLIC_CHECK_OK')
