#!/usr/bin/env python3
"""Numerical/symbolic-arithmetic checks for an SSEP spectral dissipation law.
Standard library only. The checks support, but do not replace, the proof.
"""
import math
import cmath

pi=math.pi
zstar=1.26459650688644

def J(s):
    if not (s>0):raise ValueError('s must be positive')
    if s<0.18:
        # cancellation-free small-s expansion (not used for proof)
        return s**4/180  # only used for stable limit test to leading order
    return s*(math.sinh(s)+math.sin(s))/(2*(math.cosh(s)-math.cos(s)))-1

def q_closed(n,s):
    lam=(n*pi)**2
    x=s**4/(lam*lam)
    return (lam*lam/405)*(s**4/(lam*lam))*(x+9)/((x+1)*(x+4)*J(s))

def q_from_complex_response(n,s):
    lam=(n*pi)**2;omega=2*s*s
    g=0.0317;eps=0.00043;chi=0.187
    resp=16*g*eps*lam/((2*lam+1j*omega)*(4*lam+1j*omega))
    adiabatic=2*g*eps/lam
    sigma=eps*eps*J(s)/(2*chi)
    return lam**4*abs(resp-adiabatic)**2/(3240*g*g*chi*sigma)

def integral_J(s,N=4000):
    k=cmath.sqrt(2j*s*s)
    def val(x):return abs(k*cmath.cosh(k*(x-.5))/(2*cmath.sinh(k/2))-1)**2
    return (val(0)+val(1)+4*sum(val(j/N) for j in range(1,N,2))+2*sum(val(j/N) for j in range(2,N,2)))/(3*N)

def h(z):return z**1.5*(z*z+9)/((z*z+1)*(z*z+4))
def polynomial(z):return z**6+30*z**4+17*z*z-108
C3=2*pi**3*h(zstar)/405
C2=4*pi*pi*h(zstar)/(405*math.sqrt(zstar))

def max_golden(f,lo,hi):
    r=(math.sqrt(5)-1)/2
    a=hi-r*(hi-lo); b=lo+r*(hi-lo);fa=f(a);fb=f(b)
    for _ in range(120):
        if fa<fb:lo=a;a=b;fa=fb;b=lo+r*(hi-lo);fb=f(b)
        else:hi=b;b=a;fb=fa;a=hi-r*(hi-lo);fa=f(a)
    x=(lo+hi)/2;return x,f(x)

checks=0
assert abs(polynomial(zstar))<3e-12;checks+=1
for x in [0.01,.5,1.,1.26]:
    assert polynomial(x)<0;checks+=1
for x in [1.27,2.,10.]:
    assert polynomial(x)>0;checks+=1
for s in [.25,.4,.6,1.,1.7,2.5,3.2,5.,8.,12.,20.]:
    target=J(s);actual=integral_J(s)
    assert abs(target-actual)<2e-8*(1+target),(s,target,actual)
    checks+=1
for n in [1,2,3,4,8,10,20,40,60]:
    for s in [.25,.5,1.,2.,3.5,5.5,8.2,12.,20.,30.,50.]:
        q1=q_closed(n,s);q2=q_from_complex_response(n,s)
        assert math.isclose(q1,q2,rel_tol=6e-13,abs_tol=3e-11),(n,s,q1,q2)
        checks+=1
for n in [2,3,4,5,10,20,30,50,100]:
    s,v=max_golden(lambda x:q_closed(n,x),max(.25,.5*n),4.4*n)
    z=s*s/(n*pi)**2
    if n>=10:
        assert abs(z-zstar)<.1
        # two-term asymptotic has an O(n) remainder
        assert abs(v-C3*n**3-C2*n*n)<.08*n
    checks+=1
print('PASS',checks,'independent arithmetic checks')
print('root',format(zstar,'.15g'),'C3',format(C3,'.15g'),'C2',format(C2,'.15g'))
for n in [2,3,4,10,20,50,100]:
    s,v=max_golden(lambda x:q_closed(n,x),max(.25,.5*n),4.4*n)
    print('n',n,'peak',round(v,9),'omega/lambda',round(2*s*s/(n*pi)**2,9),'error_over_n',round((v-C3*n**3-C2*n*n)/n,9))
