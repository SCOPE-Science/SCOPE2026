"""Numerical cross-checks for the high-redundancy exponential-window frame law.

Requires mpmath; execute: python check_gabor.py.
Finite precision checks corroborate, but do not establish, the asymptotic theorem.
"""
from mpmath import mp

mp.dps = 70
checks = 0

def verify(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1

def a_value(n, h):
    t=h/n
    return mp.tanh(h/2)*(t/mp.sinh(t)-h/mp.sinh(h))

def b_value(n, h):
    t=h/n
    return mp.coth(h/2)*(t*mp.coth(t)+h/mp.sinh(h))

def k_value(n, h):
    return b_value(n,h)/a_value(n,h)

def f_leading(n,h,kind):
    if kind=='A':
        return 1-h*h/(6*n*n)-2*(1+h)*mp.exp(-h)
    if kind=='B':
        return 1+h*h/(3*n*n)+2*(1+h)*mp.exp(-h)
    return 1+h*h/(2*n*n)+4*(1+h)*mp.exp(-h)

for n_int in [40, 100, 500, 3000, 10000]:
    n=mp.mpf(n_int)
    L=mp.log(n)
    for kind,c,fun in [('A',6,a_value),('B',3,b_value),('K',4,k_value)]:
        h0=2*L+mp.log(c)
        root=mp.findroot(lambda h:mp.diff(lambda u:fun(n,u),h),(h0-mp.mpf('0.3'),h0+mp.mpf('0.3')))
        verify(abs(root-h0)<mp.mpf('5')*L*L/n**2, f'{kind} root correction {n_int}')
        hminus=h0-mp.mpf('0.2')
        hplus=h0+mp.mpf('0.2')
        dminus=mp.diff(lambda u:fun(n,u),hminus)
        dplus=mp.diff(lambda u:fun(n,u),hplus)
        verify(dminus>0 if kind=='A' else dminus<0, f'{kind} left derivative {n_int}')
        verify(dplus<0 if kind=='A' else dplus>0, f'{kind} right derivative {n_int}')
        verify(abs(fun(n,h0)-f_leading(n,h0,kind)) < 200*L**4/n**4, f'{kind} expansion {n_int}')

# Independently reconstruct the Gabor frame Zak multipliers by two-dimensional
# Poisson summation, at the extremizing phase-space points.
for n_int, eta_str in [(2,'3.4'),(3,'4.1'),(5,'5.1'),(10,'6.1')]:
    n=mp.mpf(n_int); eta=mp.mpf(eta_str); a=eta/n
    for time_fraction,phase,expected in [(mp.mpf('0.5'),1,a_value(n,eta)),(mp.mpf('0'),0,b_value(n,eta))]:
        t=a*time_fraction
        # The full multiplier is eta * sum_{k,l} g(t-ka)g(t-ka-l*eta)e^{2*pi*i*l*omega}.
        # For omega = 0 or 1/2, the phase is real and equals (-1)^(l*phase).
        approx=mp.mpf('0')
        for k in range(-110,111):
            x=t-k*a
            for ell in range(-18,19):
                approx += mp.exp(-abs(x)-abs(x-ell*eta))*((-1)**(ell*phase))
        approx *= eta/n
        verify(abs(approx-expected) < mp.mpf('4e-14'),f'Zak multiplier n={n_int} t={time_fraction} phase={phase}')

# The sharp limiting regret coefficients are positive.
regret_lower=mp.mpf(1)/3+mp.mpf(2)/3*mp.log(mp.mpf(2)/3)
regret_upper=mp.mpf(4)/3*mp.log(mp.mpf(4)/3)-mp.mpf(1)/3
verify(regret_lower>0,'lower regret positivity')
verify(regret_upper>0,'upper regret positivity')
for n_int in [100,1000,10000]:
    n=mp.mpf(n_int); L=mp.log(n)
    hA=mp.findroot(lambda h: mp.diff(lambda u: a_value(n,u),h),2*L+mp.log(6))
    hB=mp.findroot(lambda h: mp.diff(lambda u: b_value(n,u),h),2*L+mp.log(3))
    hK=mp.findroot(lambda h: mp.diff(lambda u: k_value(n,u),h),2*L+mp.log(4))
    lower=(a_value(n,hA)-a_value(n,hK))*n*n/L
    upper=(b_value(n,hK)-b_value(n,hB))*n*n/L
    verify(abs(lower-regret_lower)<mp.mpf('2')/L, f'lower regret n={n_int}')
    verify(abs(upper-regret_upper)<mp.mpf('2')/L, f'upper regret n={n_int}')
print(f'GABOR_HIGH_DENSITY_CHECKS_PASS {checks}')
