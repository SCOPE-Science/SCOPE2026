#!/usr/bin/env python3
"""Finite-precision diagnostic checks of the Gaussian soft-wall spectral formula.
This checker is not a substitute for the analytic Sturm–Liouville proof.
Requirements: Python 3.9+, mpmath.
"""
import mpmath as mp
mp.mp.dps = 75

def edge_ratio(nu):
    return nu / mp.sqrt(2) * mp.gamma((1-nu)/2) / mp.gamma(1-nu/2)

def coefficients(kappa_left, kappa_right):
    C = mp.sqrt(mp.pi/2) * (kappa_left**(-mp.mpf('.5')) + kappa_right**(-mp.mpf('.5')))
    B = mp.sqrt(mp.pi/2) * (mp.log(2)-mp.pi/6)*(kappa_left**(-mp.mpf('1.5')) + kappa_right**(-mp.mpf('1.5')))
    return C,B

def root(L,T,kleft,kright):
    C,B=coefficients(kleft,kright)
    guess = mp.pi/(L+C*mp.sqrt(T))
    def fun(k):
        lam=T*k*k
        alpha_l=mp.sqrt(kleft/T)*edge_ratio(lam/kleft)
        alpha_r=mp.sqrt(kright/T)*edge_ratio(lam/kright)
        return k*L+mp.atan(alpha_l/k)+mp.atan(alpha_r/k)-mp.pi
    k=mp.findroot(fun,(guess*mp.mpf('.999'),guess*mp.mpf('1.001')))
    lam=T*k*k
    return lam,k,fun(k)

count=0
for Ls,cls,crs in [('1','1','1'),('1','.5','3'),('2.5','1.5','.75'),('.8','4','2'),('5','2','9')]:
    L,kl,kr=map(mp.mpf,(Ls,cls,crs))
    C,B=coefficients(kl,kr)
    print('parameters',Ls,cls,crs)
    for tstr in ['.04','.01','.0025','.0004','.0001','.000025']:
        T=mp.mpf(tstr)
        lam,k,defect=root(L,T,kl,kr)
        eff=mp.pi**2*T/(L+C*mp.sqrt(T))**2
        refined=eff-2*mp.pi**4*B*T**mp.mpf('2.5')/L**5
        assert lam>0 and lam<mp.pi**2*T/L**2;count+=1
        assert abs(defect)<mp.mpf('1e-55');count+=1
        assert abs(lam-eff)<10000*T**mp.mpf('2.5')/L**5;count+=1
        if T<=mp.mpf('.0004'):
            assert abs(lam-refined)<10000*T**3/L**6;count+=1
        if T<=mp.mpf('.0001'):
            z=(eff-lam)/T**mp.mpf('2.5')
            pred=2*mp.pi**4*B/L**5
            print(' T',tstr,'ratio observed/predicted',mp.nstr(z/pred,11))
            assert abs(z/pred-1)<mp.mpf('.35');count+=1
for vstr in ['.00001','.002','.01','.05','.1','.2','.4']:
    nu=mp.mpf(vstr)
    d0=mp.pcfd(nu,0)
    deriv=mp.diff(lambda y:mp.exp(y*y/4)*mp.pcfd(nu,y),mp.mpf('0'))
    assert abs(deriv/d0-edge_ratio(nu))<mp.mpf('1e-55');count+=1
for vstr in ['.00001','.0001','.001']:
    nu=mp.mpf(vstr)
    approx=mp.sqrt(mp.pi/2)*nu*(1+nu*mp.log(2))
    assert abs(edge_ratio(nu)-approx)<4*nu**3;count+=1
print('PASSED',count,'numeric assertions')
