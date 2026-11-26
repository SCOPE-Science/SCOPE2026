#!/usr/bin/env python3
"""Independent numerical checks for a rank-two Müntz projection theorem.

Only standard-library modules are required. Finite checks do not certify
universal statements; see the accompanying mathematical proof.
"""
import math

def moment(alpha): return 1.0 / (alpha + 1.0)
def variance(alpha):
    return alpha * alpha / ((2.0 * alpha + 1.0) * (alpha + 1.0)**2)
def kernel(alpha, x, y):
    m = moment(alpha)
    return 1.0 + (x**alpha - m)*(y**alpha - m)/variance(alpha)
def l0(alpha):
    return 2.0*(alpha+1)/alpha * ((alpha+1)/(2*alpha+1))**(1/alpha) - 1.0
def l1(alpha):
    return 1.0 + 2.0 * (2.0*alpha+1.0)**(-1.0/alpha)
def peak(alpha):
    return max((1+1/alpha)**2, 2*(alpha+1))
def adaptive_simpson(fun, a, b, tol=2e-10, levels=16):
    def sim(a,b,fa,fm,fb): return (b-a)*(fa+4*fm+fb)/6
    fa, fb = fun(a), fun(b)
    m=(a+b)/2; fm=fun(m)
    whole=sim(a,b,fa,fm,fb)
    def split(a,b,fa,fm,fb,whole,tol,depth):
        m=(a+b)/2; l=(a+m)/2; r=(m+b)/2
        fl,fr=fun(l),fun(r)
        s1=sim(a,m,fa,fl,fm);s2=sim(m,b,fm,fr,fb)
        if depth==0 or abs(s1+s2-whole)<15*tol:
            return s1+s2+(s1+s2-whole)/15
        return split(a,m,fa,fl,fm,s1,tol/2,depth-1)+split(m,b,fm,fr,fb,s2,tol/2,depth-1)
    return split(a,b,fa,fm,fb,whole,tol,levels)
def integrate01(fun):
    q=32
    return adaptive_simpson(lambda z:q*z**(q-1)*fun(z**q),0,1,tol=1e-10,levels=22)
def close(a,b,err=3e-7):
    assert abs(a-b)<err*(1+abs(a)+abs(b)), (a,b)

checks=0
exponents=(0.08,0.11,0.2,0.25,0.5,0.75,0.95,1.0,1.1,1.3,1.7,2.0,2.6,3.5,5.0,7.0,12.0,25.0,50.0)
for a in exponents:
    m=moment(a); v=variance(a)
    close(integrate01(lambda x:x**a),m);checks+=1
    close(integrate01(lambda x:(x**a-m)**2),v);checks+=1
    for x in (0.0,0.15,0.45,0.83,1.0):
        close(integrate01(lambda y:kernel(a,x,y)),1.0);checks+=1
    v0=integrate01(lambda y:abs(kernel(a,0,y)))
    v1=integrate01(lambda y:abs(kernel(a,1,y)))
    close(v0,l0(a));checks+=1
    close(v1,l1(a));checks+=1
    for x in (.03,.2,.4,.6,.8,.96):
        z=integrate01(lambda y:abs(kernel(a,x,y)))
        assert z<=max(v0,v1)+2e-7,(a,x,z,v0,v1)
        checks+=1
    assert abs(max(kernel(a,0,0),kernel(a,1,1))-peak(a))<2e-9;checks+=1
    if a<1:
        assert l0(a)>l1(a) and l0(a)>5/3;checks+=1
    elif a>1:
        assert l1(a)>l0(a) and l1(a)>5/3;checks+=1
    else:
        close(l0(a),5/3);close(l1(a),5/3);checks+=1
for a,b in zip(exponents,exponents[1:]):
    assert l0(a)>l0(b) and l1(a)<l1(b)
    checks+=1
for z in (0.001,0.015,0.05,0.1,0.2,0.35,0.49):
    assert 2*z + math.log1p(-z)>0 and (1-2*z)/(1-z)>0
    checks+=1
for a in (.01,.005,.002):
    ratio=l0(a)*a*math.e/2
    assert abs(ratio-1)<5*a
    checks+=1
for a in (100.,1000.,10000.):
    assert abs(l1(a)-3)<3*math.log1p(2*a)/a
    checks+=1
print(f'PASS: {checks} deterministic integration, kernel and asymptotic sanity checks')
