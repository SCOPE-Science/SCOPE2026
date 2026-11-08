"""Finite high-precision consistency checks for the EOS three-cycle crossover.

Run with: python check_eos_crossover.py
Requires mpmath. Finite tests corroborate, and do not replace, the proof.
"""
from mpmath import mp

mp.dps = 95

def sigma(z):
    return 1/(1+mp.exp(-z))


def trial(a_int, t_int):
    a = mp.mpf(a_int)
    t = mp.mpf(t_int)
    eps = mp.exp(-a/6)
    b = mp.mpf(1)/3 + mp.mpf(2)/3*eps*t
    F = lambda x: x+b-sigma(a*x)
    h = lambda u: (F(F(F(-mp.mpf(1)/2+u/a)))-(-mp.mpf(1)/2+u/a))/eps
    u = mp.findroot(h, (mp.asinh(t)-mp.mpf('0.04'), mp.asinh(t)+mp.mpf('0.04')))
    x0 = -mp.mpf(1)/2+u/a
    x1 = F(x0)
    x2 = F(x1)
    assert abs(F(x2)-x0) < mp.mpf('1e-75')
    assert x0 < x1 < x2 and abs(x0+mp.mpf('1')/2)<mp.mpf('0.1')
    d = [1-a*sigma(a*x)*(1-sigma(a*x)) for x in (x0,x1,x2)]
    L = mp.fprod(d)
    assert all(mp.mpf(0)<v<mp.mpf(1) for v in d)
    assert mp.mpf(0)<L<mp.mpf(1)
    scaled_mu = (1-L)/(2*a*eps)
    scaled_sensitivity = a*eps*(1+d[2]+d[2]*d[1])/(1-L)
    if a_int >= 120:
        bound = mp.mpf('0.001') if a_int==120 else mp.mpf('0.00003')
        assert abs(u-mp.asinh(t)) < bound
        assert abs(scaled_mu-mp.sqrt(1+t*t)) < bound
        assert abs(scaled_sensitivity-mp.mpf(3)/(2*mp.sqrt(1+t*t))) < bound
    return u, L

n = 0
for a in [45,60,90,120,180]:
    for t in [-3,-1,0,1,3]:
        trial(a,t)
        n += 1
print(f'VERIFY_OK high_precision_period_three_and_response_cases={n} precision_digits={mp.dps}')
