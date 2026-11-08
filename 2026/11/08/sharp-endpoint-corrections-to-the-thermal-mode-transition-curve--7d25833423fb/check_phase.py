"""Standalone numerical diagnostics for a Gaussian-convolved symmetric beta law.

Install mpmath if needed: python -m pip install mpmath
Run: python check_phase.py
Finite numerical checks are not the proof of the analytic statements.
"""
import mpmath as mp
mp.mp.dps = 55
checks = 0

def check(condition, label):
    global checks
    assert condition, label
    checks += 1

def mm(a, lam, order=1):
    aa = mp.mpf(a)
    beta_ratio = mp.rf(mp.mpf('0.5'), order) / mp.rf(aa+mp.mpf('0.5'), order)
    return beta_ratio * mp.hyp1f1(mp.mpf('0.5')+order, aa+mp.mpf('0.5')+order, -lam) / mp.hyp1f1(mp.mpf('0.5'), aa+mp.mpf('0.5'), -lam)

def g(a, lam):
    return 2*lam*mm(a, lam)-1

def root(a):
    lo = mp.mpf('1.e-8'); hi = mp.mpf('2')
    while g(a, hi) < 0:
        hi *= 2
    for _ in range(145):
        mid=(lo+hi)/2
        if g(a,mid) > 0: hi=mid
        else: lo=mid
    return (lo+hi)/2

cases=['0.005','0.03','0.15','0.4','0.72','0.93','0.999','0.99999']
prev_s=mp.inf
for astr in cases:
    a=mp.mpf(astr); lam=root(a); s=1/(2*lam)
    check(abs(g(a,lam)) < mp.mpf('1e-35'), f'critical root {astr}')
    check(g(a,lam*mp.mpf('0.97'))<0, f'lower parameter sign {astr}')
    check(g(a,lam*mp.mpf('1.03'))>0, f'upper parameter sign {astr}')
    check(s<prev_s, f'monotone threshold {astr}')
    prev_s=s
    variance=mm(a,lam,2)-mm(a,lam,1)**2
    check(abs(variance/(2*a*s*s)-1)<mp.mpf('1e-30'),f'variance identity {astr}')
    fourth=mm(a,lam,2)/s**4-6*mm(a,lam,1)/s**3+3/s**2
    check(abs(fourth+2*(1-a)/s**2)<mp.mpf('1e-25')*max(1,abs(fourth)),f'negative quartic {astr}')
    gp=mp.diff(lambda t:g(a,t),lam)
    check(abs(gp-(1-a)/lam)<mp.mpf('1e-25'),f'root transversality {astr}')
    print('a=',astr,'s_c=',mp.nstr(s,21),'lambda=',mp.nstr(lam,21))

A=mp.exp(mp.mpf('0.5')) * mp.sqrt(2*mp.pi) * mp.erf(1/mp.sqrt(2))
for astr in ['.01','.001','.0001']:
    a=mp.mpf(astr); sc=1/(2*root(a)); delta=abs(sc-(1-A*a))
    check(delta < 8*a*a, f'small-a second order residual {astr}')
    print('small a=',astr,'residual=',mp.nstr(delta,12))

prev_abs=mp.inf
for e_str in ['1e-5','1e-8','1e-12','1e-18']:
    eps=mp.mpf(e_str); lam=root(1-eps); L=mp.log(1/eps)
    lam_pred=L+mp.mpf('1.5')*mp.log(L)+mp.log(2/mp.sqrt(mp.pi))
    delta=abs(lam-lam_pred)
    check(delta<prev_abs, f'loglog approximation improves {e_str}')
    prev_abs=delta
    check(delta < 3*mp.log(L)/L, f'predicted remainder scale {e_str}')
    print('eps=',e_str,'lambda=',mp.nstr(lam,20),'remainder=',mp.nstr(delta,14))
print('A=',mp.nstr(A,23))
print('PASS',checks,'independent numerical identities/diagnostics')
