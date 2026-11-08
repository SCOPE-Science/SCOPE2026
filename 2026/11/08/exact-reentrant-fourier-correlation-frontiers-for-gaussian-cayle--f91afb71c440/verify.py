"""Reproduce exact algebraic identities and numerical checks for Gaussian Cayley rotation.

Requires Python 3 and mpmath.  Finite checks supplement the stated analytic proof.
"""
import mpmath as mp

mp.mp.dps = 65
TOL = mp.mpf('1e-47')
checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def J(r):
    return mp.sqrt(mp.pi / (2*r)) * mp.exp(1/(2*r)) * mp.erfc(1/mp.sqrt(2*r))

def lambda_formula(m, h):
    r = mp.mpf(h)/4
    if m == 1:
        return 2*J(r) - 1
    if m == 2:
        return 1 + 4/r - 4*(1+1/r)*J(r)
    raise ValueError('Closed form is only used for modes 1 and 2')

def lambda_quadrature(m, h):
    b = mp.sqrt(h)/2
    density = lambda z: mp.exp(-z*z/2) / mp.sqrt(2*mp.pi)
    f = lambda z: mp.cos(2*m*mp.atan(b*z))*density(z)
    return 2 * mp.quad(f, [0, 1, 3, 9, mp.inf])

def chebyshev(x,m):
    a,b = mp.mpf(1), x
    if m==0: return a
    if m==1: return b
    for _ in range(2,m+1): a,b = b, 2*x*b-a
    return b

for m in range(1,9):
    for h in [mp.mpf('0.08'),mp.mpf('0.7'),mp.mpf('4'),mp.mpf('16')]:
        b = mp.sqrt(h)/2
        for z in [mp.mpf('0'),mp.mpf('0.7'),mp.mpf('1'),mp.mpf('2')]:
            x = (1-b*b*z*z)/(1+b*b*z*z)
            check(abs(mp.cos(2*m*mp.atan(b*z))-chebyshev(x,m))<TOL,
                  f'Chebyshev angle identity m={m} h={h} z={z}')

for m in [1,2]:
    for h in [mp.mpf('0.15'),mp.mpf('0.75'),mp.mpf('1'),mp.mpf('4'),mp.mpf('8'),mp.mpf('20'),mp.mpf('40'),mp.mpf('100')]:
        v=lambda_formula(m,h)
        q=lambda_quadrature(m,h)
        check(abs(v-q)<mp.mpf('1e-42'),f'Integral formula m={m},h={h}: {v-q}')

root1 = mp.findroot(lambda h:lambda_formula(1,h), (mp.mpf('8'),mp.mpf('15')))
root2a = mp.findroot(lambda h:lambda_formula(2,h),(mp.mpf('1'),mp.mpf('2')))
root2b = mp.findroot(lambda h:lambda_formula(2,h),(mp.mpf('30'),mp.mpf('42')))
check(root2a < 4 < root2b, 'Second mode negative interval surrounds h=4')
check(lambda_formula(2,4) < -mp.mpf(1)/75,'Exact certified negative test contradicts numerics')
check(lambda_formula(1,4) > 0, 'First Fourier mode at h=4')
check(root2a < root1 < root2b, 'Ordering of three mode thresholds')
for m,r in [(1,root1),(2,root2a),(2,root2b)]:
    check(abs(lambda_formula(m,r))<TOL, 'Root residual')

print('Checks passed:',checks)
print('lambda_2(h=4):',mp.nstr(lambda_formula(2,4),35))
print('First-mode unique zero h:',mp.nstr(root1,35))
print('Second-mode first zero h:',mp.nstr(root2a,35))
print('Second-mode second zero h:',mp.nstr(root2b,35))
for h in [mp.mpf('.01'),mp.mpf('2'),mp.mpf('4'),mp.mpf('12'),mp.mpf('38'),mp.mpf('150')]:
    print('h',mp.nstr(h,8),'lambda1',mp.nstr(lambda_formula(1,h),16),'lambda2',mp.nstr(lambda_formula(2,h),16))
print('Numerical quadrature and algebraic identities agree at tested points.')
print('Global uniqueness and zero-count conclusions rely on the analytic exponential-Chebyshev proof.')
