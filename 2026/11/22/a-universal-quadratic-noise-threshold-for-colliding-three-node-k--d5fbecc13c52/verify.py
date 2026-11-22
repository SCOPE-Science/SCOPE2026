"""Reproduce finite algebraic and numerical checks for the three-node regularization law.
The infinite-domain assertions use the analytical proof, not these finite checks.
"""
from __future__ import annotations
import mpmath as mp
import sympy as sp

mp.mp.dps = 110

# Independent symbolic Cramer's-rule check for the symmetric three-node system.
a, k, e, m, n = sp.symbols('a k e m n', real=True)
D = a*(a+e)-2*k*k
u = (a*n-k*m)/D
v = ((a+e)*m-2*k*n)/D
M = sp.Matrix([[a,k,e],[k,a,k],[e,k,a]])
assert all(sp.simplify(z) == 0 for z in M*sp.Matrix([u,v,u])-sp.Matrix([n,m,n]))

# Taylor certificates for a general Gaussian scale mixture.
d, q1, q2, m0, mp2 = sp.symbols('d q1 q2 m0 mp2', positive=True)
k_small = 1-q1*d*d+q2*d**4/2
k_double = 1-4*q1*d*d+8*q2*d**4
m_small = m0+mp2*d*d/2
D0 = sp.expand(1+k_double-2*k_small**2)
A = 2*q1+mp2/m0
assert sp.simplify(D0.coeff(d,4)-2*(3*q2-q1*q1))==0
eta_critical = 2*k_small*m_small/m0-1-k_double
assert sp.simplify(sp.expand(eta_critical).coeff(d,2)-A)==0

# A general finite Gaussian mixture with a non-point symmetric integration measure.
Q = [(mp.mpf('0.4'),mp.mpf('0.3')),(mp.mpf('1.7'),mp.mpf('0.7'))]
measure = [(mp.mpf('-0.4'),mp.mpf('0.2')),(mp.mpf('0'),mp.mpf('0.6')),(mp.mpf('0.4'),mp.mpf('0.2'))]
Kmix = lambda x: sum(w*mp.exp(-q*x*x) for q,w in Q)
mmix = lambda y: sum(w*Kmix(x-y) for x,w in measure)

def check(K,mean,spacing,eta):
    c=K(spacing); e=K(2*spacing); m0=mean(0); m1=mean(spacing)
    de=(1+eta)*(1+eta+e)-2*c*c
    left=((1+eta)*m1-c*m0)/de
    middle=((1+eta+e)*m0-2*c*m1)/de
    direct=mp.lu_solve(mp.matrix([[1+eta,c,e],[c,1+eta,c],[e,c,1+eta]]),mp.matrix([m1,m0,m1]))
    assert max(abs(direct[0]-left),abs(direct[1]-middle),abs(direct[2]-left)) < mp.mpf('1e-48')
    assert de > 0 and left > 0
    ec=2*c*m1/m0-1-e
    if eta > ec+mp.mpf('1e-35'):assert middle > 0
    if eta < ec-mp.mpf('1e-35'):assert middle < 0
    return left,middle,ec

number=0
for spacing in ['0.005','0.02','0.1','0.3','0.8']:
    dd=mp.mpf(spacing)
    for eta in ['0','0.00001','0.001','0.04','1']:
        check(Kmix,mmix,dd,mp.mpf(eta));number+=1
q1m=sum(q*w for q,w in Q)
q2m=sum(q*q*w for q,w in Q)
m00=mmix(0)
mp2m=sum(weight*sum(qweight*mp.exp(-q*(x*x))*(4*q*q*x*x-2*q) for q,qweight in Q) for x,weight in measure)
Am=2*q1m+mp2m/m00
assert Am > 0
for spacing in ['0.03','0.01','0.003']:
    dd=mp.mpf(spacing)
    left,mid,critical=check(Kmix,mmix,dd,0)
    assert abs(critical/(dd*dd)/Am-1)<mp.mpf('0.03')
    scale=2*(3*q2m-q1m*q1m)
    assert abs(mid*dd*dd/(-m00*Am/scale)-1)<mp.mpf('0.08')
    number+=1

# Matérn 5/2 explicit primitive and critical noise, no numerical integration needed.
kernel=lambda r:(1+r+r*r/3)*mp.exp(-r)
J=lambda r:mp.mpf(8)/3-(r*r+5*r+8)*mp.exp(-r)/3
for lam_s in ['0.5','1','3','10']:
    lam=mp.mpf(lam_s);L=lam/2
    KK=lambda x:kernel(lam*abs(x))
    MEAN=lambda x:(J(lam*(mp.mpf('.5')+x))+J(lam*(mp.mpf('.5')-x)))/lam
    m_cent=2*J(L)/lam
    coeff=(1-(L+L*L)*mp.exp(-L)/J(L))/3
    assert coeff > 0
    for dd_s in ['0.02','0.05','0.1','0.25','0.45']:
        dd=mp.mpf(dd_s)
        _,_,crit=check(KK,MEAN,dd,mp.mpf('0'))
        _,_,_=check(KK,MEAN,dd,mp.mpf('0.01'))
        if crit>0:
            _,z,_=check(KK,MEAN,dd,crit)
            assert abs(z)<mp.mpf('1e-48')
            _,_,_=check(KK,MEAN,dd,2*crit)
        number+=3
    for dd_s in ['0.001','0.0004','0.0001']:
        dd=mp.mpf(dd_s)
        _,v0,crit=check(KK,MEAN,dd,mp.mpf('0'))
        assert abs(crit/((lam*dd)**2)/coeff-1)<mp.mpf('.03')
        assert abs(v0*(lam*dd)**2/(-mp.mpf(9)/4*m_cent*coeff)-1)<mp.mpf('.08')
        # c*(lambda*d)^2 regularization has the predicted finite limiting weights.
        strength=2*coeff
        out,mid,_=check(KK,MEAN,dd,strength*(lam*dd)**2)
        assert abs(mid-m_cent*(strength-coeff)/(3*strength))<mp.mpf('.03')
        number+=2

print('PASS: symbolic Gramian identities and Taylor coefficients')
print('PASS: mixture covariance and Matérn 5/2 direct-solve, sign, and asymptotic comparisons')
print('finite parameter groups:',number)
lam=mp.mpf('1');d=mp.mpf('.1');L=lam/2
k1=kernel(lam*d);k2=kernel(2*lam*d)
mo=2*J(L)/lam;me=(J(L-lam*d)+J(L+lam*d))/lam
threshold=2*k1*me/mo-1-k2
cen=((1+k2)*mo-2*k1*me)/(1+k2-2*k1*k1)
print('Matérn example: lambda=1, d=0.1')
print('critical noise variance =',mp.nstr(threshold,30))
print('noiseless central weight =',mp.nstr(cen,30))
