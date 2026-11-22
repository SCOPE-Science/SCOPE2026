#!/usr/bin/env python3
"""Reproducibility checks for a two-condition water/sediment exchange model.

Only numerical checks: analytic identifiability and minimality are proved in RESULT.md.
Requires Python standard library and mpmath (arbitrary precision).
"""
import random
import mpmath as mp
mp.mp.dps = 70

def response(A,D,B,t):
    v=mp.sqrt((A-D)**2+4*B)
    l=(A+D-v)/2
    u=(A+D+v)/2
    return (D-l)/v*mp.exp(-l*t)+(u-D)/v*mp.exp(-u*t)

def characterize(y1,y2,y3,h):
    V=y2-y1*y1
    assert V>0
    S=(y3-y1*y2)/V
    P=S*y1-y2
    discr=S*S-4*P
    assert discr>0
    slow=(S+mp.sqrt(discr))/2
    fast=(S-mp.sqrt(discr))/2
    assert 0<fast<slow<1
    w=(y1-fast)/(slow-fast)
    assert 0<w<1
    l=-mp.log(slow)/h;u=-mp.log(fast)/h
    A=w*l+(1-w)*u
    D=l+u-A
    B=A*D-l*u
    return A,D,B

def recover(vals,h,theta1,theta2):
    A,D,B=characterize(*vals[:3],h)
    target=vals[3]
    lower=B/D
    upper=max(A*2,D*2,mp.mpf(1))
    assert response(lower,D,B,h)>target
    while response(upper,D,B,h)>target:
        upper*=2
    for _ in range(250):
        middle=(lower+upper)/2
        if response(middle,D,B,h)>target:lower=middle
        else:upper=middle
    A2=(lower+upper)/2
    d=(A2-A)/(theta2-theta1)
    a=A-theta1*d
    b=B/a
    e=D-b
    return a,b,d,e

def run():
    rng=random.Random(440023)
    checks=0
    theta1=mp.mpf('1');theta2=mp.mpf('2.5')
    for j in range(150):
        aa,bb,dd,ee=[mp.mpf(str(rng.uniform(.15,2.5))) for _ in range(4)]
        h=mp.mpf(str(rng.uniform(.2,1.3)))
        A1=aa+theta1*dd;A2=aa+theta2*dd;D=bb+ee;B=aa*bb
        obs=[response(A1,D,B,h*k) for k in (1,2,3)]+[response(A2,D,B,h)]
        got=recover(obs,h,theta1,theta2)
        for val,actual in zip(got,(aa,bb,dd,ee)):
            assert abs(val-actual)<mp.mpf('1e-47')
            checks+=1
        A,D2,B2=characterize(*obs[:3],h)
        for u,v in ((A,A1),(D2,D),(B2,B)):
            assert abs(u-v)<mp.mpf('1e-48')
            checks+=1
        c=aa*mp.mpf('.8')+mp.mpf('.2')*A1
        # c strictly within (B/D,A1) is required for alternate physical rates.
        c=(B/D+A1)/2
        b2=B/c;d2=(A1-c)/theta1;e2=D-b2
        assert min(c,b2,d2,e2)>0
        for t in (mp.mpf('0'),h/3,h,4*h):
            assert abs(response(A1,D,B,t)-response(c+theta1*d2,b2+e2,c*b2,t))<mp.mpf('1e-55')
            checks+=1
        assert abs(response(A2,D,B,h)-response(c+theta2*d2,b2+e2,c*b2,h))>mp.mpf('1e-22')
        checks+=1
        # A-derivative is negative on the admissible interval.
        for scale in (mp.mpf('1.01'),mp.mpf('1.2'),mp.mpf('2')):
            assert response(A2*scale,D,B,h)<response(A2,D,B,h)
            checks+=1
    aa=mp.mpf('1.2');bb=mp.mpf('.8');dd=mp.mpf('.7');ee=mp.mpf('.5');h=mp.mpf('.7')
    v=[response(aa+theta1*dd,bb+ee,aa*bb,k*h) for k in (1,2,3)]+[response(aa+theta2*dd,bb+ee,aa*bb,h)]
    got=recover(v,h,theta1,theta2)
    print('EXAMPLE',*[mp.nstr(g,18) for g in got])
    print('BASELINE_DATA',*[mp.nstr(g,19) for g in v[:3]])
    print('PERTURBED_DATA',mp.nstr(v[-1],19))
    print('NUMERICAL_ASSERTIONS_PASSED',checks)

if __name__=='__main__':run()
