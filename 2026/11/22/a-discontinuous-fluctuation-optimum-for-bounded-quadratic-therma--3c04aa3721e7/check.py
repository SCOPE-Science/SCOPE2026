"""Numerical consistency checks for the clipped-parabola sinusoidal mean-response theorem.

Only the analytic proof, not these finite tests, establishes the global classifications.
Run: python check.py
"""
from mpmath import mp

mp.dps=65
pi=mp.pi

def alpha(t): return pi-mp.acos(t)
def s(t): return mp.sqrt(1-t*t)
def K(t): return t*s(t)/alpha(t)
def P(t): return (1-2*t*t)*alpha(t)-t*s(t)
def R(t): return (alpha(t)+s(t)/(2*t)-s(t)*s(t)/(2*alpha(t)))/pi

def t_bisect(fn,lo,hi,steps=260):
    a,b=mp.mpf(lo),mp.mpf(hi)
    fa=fn(a)
    assert fa*fn(b)<0
    for j in range(steps):
        c=(a+b)/2
        if fn(c)*fa>0:a,fa=c,fn(c)
        else:b=c
    return (a+b)/2

tstar=t_bisect(P,mp.mpf('0.5'),mp.mpf('0.8'))
t0=t_bisect(lambda t:R(t)-1,mp.mpf('0.2'),mp.mpf('0.5'))
mu_spin=K(tstar)/(1+K(tstar))
mu_switch=K(t0)/(1+K(t0))
a_switch=mu_switch/t0

def F_phase(mu,A):
    return mp.quad(lambda theta: max(mp.mpf('0'),(mu+A*mp.cos(theta))*(1-mu-A*mp.cos(theta))) if 0<=mu+A*mp.cos(theta)<=1 else mp.mpf('0'), [0,pi])/pi

def F_formula_lower(mu,A):
    t=mu/A
    return (alpha(t)*(mu*(1-mu)-A*A/2)+A*(1-mp.mpf('1.5')*mu)*s(t))/pi

def dF_lower(mu,A):
    t=mu/A
    return ((1-mu)*s(t)-A*alpha(t))/pi

def locate_extrema(mu):
    target=mu/(1-mu)
    tlo=t_bisect(lambda t:K(t)-target,mp.mpf('1e-15'),tstar)
    thi=t_bisect(lambda t:K(t)-target,tstar,mp.mpf(1)-mp.mpf('1e-15'))
    return mu/thi,mu/tlo

count=0
assert mp.mpf('0.13') < mu_switch < mp.mpf('0.14');count+=1
assert mp.mpf('0.17') < mu_spin < mp.mpf('0.19');count+=1
assert 0<t0<tstar<1;count+=1
assert mp.fabs(R(t0)-1)<mp.mpf('1e-60');count+=1
assert mp.fabs(P(tstar))<mp.mpf('1e-60');count+=1
for mu_str in ['0.01','0.05','0.10','0.13','0.14','0.16','0.175','0.19','0.30','0.50']:
    m=mp.mpf(mu_str)
    for a_fac in ['0.20','0.70','1.20','2.00','3.00','5.00']:
        a=m*mp.mpf(a_fac)
        if m<a<1-m:
            v=F_formula_lower(m,a)
            # Split at zero to ensure quadrature at the kink is stable.
            cutoff=alpha(m/a)
            integral=mp.quad(lambda z:(m+a*mp.cos(z))*(1-m-a*mp.cos(z)),[0,cutoff])/pi
            assert abs(v-integral)<mp.mpf('1e-55')
            count+=1
            h=mp.mpf('1e-13')
            diff=(F_formula_lower(m,a+h)-F_formula_lower(m,a-h))/(2*h)
            assert abs(diff-dF_lower(m,a))<mp.mpf('1e-14')
            count+=1
for m in [mp.mpf('0.05'),mp.mpf('0.10'),mp.mpf('0.13'),mp.mpf('0.15'),mp.mpf('0.17')]:
    a_min,a_max=locate_extrema(m)
    assert m<a_min<a_max<1-m
    assert dF_lower(m,(m+a_min)/2)<0
    assert dF_lower(m,(a_min+a_max)/2)>0
    assert dF_lower(m,(a_max+1-m)/2)<0
    comparison=F_formula_lower(m,a_max)-m*(1-m)
    assert (comparison>0)==(m<mu_switch)
    count+=5
for t in [mp.mpf('0.05'),mp.mpf('0.2'),mp.mpf('0.35'),mp.mpf('0.5'),mp.mpf('0.7'),mp.mpf('0.85')]:
    h=mp.mpf('1e-13')
    Rp=(R(t+h)-R(t-h))/(2*h)
    identity=-P(t)*(alpha(t)+t*s(t))/(2*pi*s(t)*t*t*alpha(t)*alpha(t))
    assert abs(Rp-identity)<mp.mpf('1e-14')
    count+=1
# At the exact first-order switch the nonzero stationary response and constant response coincide.
assert abs(F_formula_lower(mu_switch,a_switch)-mu_switch*(1-mu_switch))<mp.mpf('1e-55');count+=1
print('checks_passed',count)
for label,val in [('t_local_fold',tstar),('mean_local_fold',mu_spin),('t_global_switch',t0),('mean_global_switch',mu_switch),('amplitude_jump',a_switch)]:
    print(label,mp.nstr(val,36))
for label,m in [('beneficial',mp.mpf('0.10')),('metastable',mp.mpf('0.15')),('monotone',mp.mpf('0.20'))]:
    if m<mu_spin:
        a_min,a_max=locate_extrema(m)
        print(label,'local_min',mp.nstr(a_min,25),'local_max',mp.nstr(a_max,25),'baseline',mp.nstr(m*(1-m),25),'local_max_response',mp.nstr(F_formula_lower(m,a_max),25))
    else: print(label,'no_positive_local_max')
