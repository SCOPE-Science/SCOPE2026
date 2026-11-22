#!/usr/bin/env python3
"""Numerical diagnostics for singular spectral-density purity under uniform-history quantum resetting.
Finite checks only; the theorem's large-time assertions are analytical."""
import mpmath as mp
mp.mp.dps = 38

def f_exact(r,delta,t):
    a=1j*delta/(r+1j*delta)
    return mp.hyp1f1(a,1,-(r+1j*delta)*t)

def q_formula(alpha,delta):
    a=mp.mpf(str(alpha)); d=mp.mpf(str(delta))
    if d<=0 or d>=1: raise ValueError('0<delta<1')
    return (1-a)**2*d**(1-2*a)*mp.betainc(1-a,2*a-1,0,1-d)

def q_numeric(alpha,delta):
    a=mp.mpf(str(alpha));d=mp.mpf(str(delta))
    return (1-a)**2*mp.quad(lambda u:20*(1-d)**(1-a)*u**(20*(1-a)-1)*((1-d)*u**20+d)**(-a),[0,mp.mpf(".2"),mp.mpf(".7"),1])

n=0
for a in ['0','0.25','0.5','0.75','0.9']:
  for d in ['0.005','0.07','0.3']:
    x=q_formula(a,d);y=q_numeric(a,d)
    assert mp.almosteq(x,y,rel_eps=mp.mpf('1e-17')), (a,d,x,y)
    n+=1

for d in ['0.01','0.1','0.4']:
    x=q_formula('0.5',d)
    y=mp.asinh(mp.sqrt((1-mp.mpf(d))/mp.mpf(d)))/2
    assert mp.almosteq(x,y,rel_eps=mp.mpf('1e-28'))
    n+=1

for d in [mp.mpf('0.02'),mp.mpf('0.2'),mp.mpf('0.7')]:
    for t in [mp.mpf('0.04'),mp.mpf('0.2')]:
        F=f_exact(1,d,t)
        a=1j*d/(1+1j*d);z=-(1+1j*d)*t
        approx=sum(mp.rf(a,k)*z**k/mp.factorial(k)**2 for k in range(70))
        assert abs(F-approx)<mp.mpf('2e-28')
        assert abs(F)<=1+mp.mpf('1e-20')
        n+=1

for L in [mp.mpf('10'),mp.mpf('20')]:
    t=mp.exp(L)
    for u in [mp.mpf('0'),mp.mpf('0.5'),mp.mpf('1')]:
        d=u/mp.sqrt(2*L)
        F=f_exact(1,d,t)
        a=1j*d/(1+1j*d)
        leading=((1+1j*d)*t)**(-a)/mp.gamma(1-a)
        assert abs(F-leading)<mp.mpf('0.0005'),(L,u,F,leading)
        n+=1

for a in ['0.5','0.75']:
    for d in ['1e-7','1e-9']:
        x=q_formula(a,d)
        aa=mp.mpf(a);dd=mp.mpf(d)
        target=(mp.log(1/dd)/4 if a=='0.5' else (1-aa)**2*mp.beta(1-aa,2*aa-1)*dd**(1-2*aa))
        assert abs(x/target-1)<(mp.mpf('0.20') if a=='0.5' else mp.mpf('0.02')), (a,d,x,target)
        n+=1
print(f'PASS {n} analytic and finite kernel identities')
for alpha in [mp.mpf('0'),mp.mpf('.5'),mp.mpf('.75')]:
    print('alpha',alpha)
    for L in [mp.mpf('10'),mp.mpf('30'),mp.mpf('1000')]:
        scale=1/mp.sqrt(2*L)
        def q(d):
            if alpha==0: return 1-d
            if alpha==mp.mpf('.5'): return mp.asinh(mp.sqrt((1-d)/d))/2
            return q_formula(str(alpha),str(d))
        # normalized Gaussian limiting-kernel proxy, independent from exact special function;
        # do not interpret the proxy as a finite-time test.
        z=2*mp.quad(lambda y: scale*q(scale*y)*mp.exp(-y*y),[mp.mpf('1e-12'),1,3,min(10,mp.mpf(".999")/scale)])
        if alpha==0: ref=mp.sqrt(mp.pi/2)/mp.sqrt(L)
        elif alpha==mp.mpf('.5'): ref=mp.sqrt(mp.pi)/(8*mp.sqrt(2*L))*mp.log(L)
        else: ref=(1-alpha)**2*mp.beta(1-alpha,2*alpha-1)*mp.gamma(1-alpha)*(1/(2*L))**(1-alpha)
        print(' L',int(L),'Gaussian proxy ratio',float(z/ref))
