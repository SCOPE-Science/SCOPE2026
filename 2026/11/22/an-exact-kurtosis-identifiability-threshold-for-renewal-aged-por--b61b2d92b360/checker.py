"""Reproduce stationary moment ratios and interval-certified sign brackets.

Requires mpmath >= 1.3. Run: python checker.py
"""
from mpmath import mp, iv

mp.dps = 65
iv.dps = 55


def kurtosis(sigma, lib=mp):
    x = lib.mpf(sigma)
    w = 2/(x+2)
    return 3*(3*x+2)/(5*x+2)*lib.gamma(1+2*w)/lib.gamma(1+w)**2


def sixth_ratio(sigma, lib=mp):
    x = lib.mpf(sigma)
    w = 2/(x+2)
    return 15*(3*x+2)**2/((5*x+2)*(7*x+2))*lib.gamma(1+3*w)/lib.gamma(1+w)**3


def iv_eval(f, num, den):
    x = iv.mpf(num)/den
    return f(x, iv)


def bounds(z):
    return float(z.a), float(z.b)

assert bounds(iv_eval(kurtosis, 114, 100))[0] > 3
assert bounds(iv_eval(kurtosis, 115, 100))[1] < 3
assert bounds(iv_eval(sixth_ratio, 114, 100))[1] < 15

root = mp.findroot(lambda x: kurtosis(x)-3,(mp.mpf('1.1'), mp.mpf('1.2')))
assert mp.mpf('1.14') < root < mp.mpf('1.15')
assert abs(kurtosis(root)-3)<mp.mpf('1e-55')
assert sixth_ratio(root)<15

for sigma in ('0.25','0.5','1','1.5','2','3','5','10'):
    s=mp.mpf(sigma)
    a=1/s
    c=1/mp.beta(mp.mpf('0.5'), 1+a)
    # Independently integrate normalized compact seed and age moment.
    raw=[]
    for j in (1,2,3):
        seed=2*c*mp.quad(lambda y: y**(2*j)*(1-y*y)**a,[0,mp.mpf('0.5'),1])
        age=mp.quad(lambda t: t**(2*j/(s+2))*mp.exp(-t),[0,1,mp.inf])
        raw.append(seed*age)
    K=raw[1]/raw[0]**2
    S=raw[2]/raw[0]**3
    assert abs(K-kurtosis(s)) < mp.mpf('1e-36')
    assert abs(S-sixth_ratio(s)) < mp.mpf('1e-36')

print('CERTIFIED K(1.14)-3:',bounds(iv_eval(kurtosis,114,100)-3))
print('CERTIFIED K(1.15)-3:',bounds(iv_eval(kurtosis,115,100)-3))
print('CERTIFIED S(1.14)-15:',bounds(iv_eval(sixth_ratio,114,100)-15))
print('critical sigma', mp.nstr(root,40))
print('critical sixth ratio',mp.nstr(sixth_ratio(root),40))
print('normalized critical sixth cumulant',mp.nstr(sixth_ratio(root)-15,40))
print('PASS: 3 interval inequalities; 3 root tests; 16 independently integrated moments')
