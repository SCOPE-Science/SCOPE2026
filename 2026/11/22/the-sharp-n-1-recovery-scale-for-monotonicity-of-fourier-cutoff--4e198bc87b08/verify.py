"""Numerical diagnostics for the spectral-cutoff monotonicity theorem.

Run: python3 verify.py
Requires mpmath. These finite checks are not a proof of the asymptotic theorem.
"""
import mpmath as mp

mp.mp.dps = 90
checks = 0


def close(a, b, rel=mp.mpf('1e-48')):
    global checks
    assert abs(a-b) <= rel * (1 + abs(a) + abs(b)), (a, b)
    checks += 1


def theta(t, x, n=200):
    return 1 + 2*mp.fsum(mp.exp(-t*k*k)*mp.cos(k*x) for k in range(1,n+1))


def image_theta(t, x):
    return mp.sqrt(mp.pi/t) * mp.fsum(mp.exp(-(x-2*mp.pi*j)**2/(4*t)) for j in range(-8,9))


def f_full(t, x):
    return mp.fsum(k*mp.exp(-t*k*k)*mp.sin(k*x) for k in range(1,300))


def f_finite(N, t, x):
    return mp.fsum(k*mp.exp(-t*k*k)*mp.sin(k*x) for k in range(1,N+1))


def f_image(t, x):
    return mp.sqrt(mp.pi/t)/(4*t)*mp.fsum(
        (x-2*mp.pi*j)*mp.exp(-(x-2*mp.pi*j)**2/(4*t))
        for j in range(-8,9))


for t in [mp.mpf('.1'),mp.mpf('.3'),mp.mpf('.7')]:
    for x in [mp.mpf('.2'),mp.mpf('1.4'),mp.mpf('2.5')]:
        close(theta(t,x),image_theta(t,x),mp.mpf('1e-45'))
        close(f_full(t,x),f_image(t,x),mp.mpf('1e-45'))
        q=mp.exp(-t)
        # Partial product identity to verify the normalization and sign.
        product=mp.fprod((1-q**(2*j))*(1+2*q**(2*j-1)*mp.cos(x)+q**(4*j-2)) for j in range(1,800))
        close(theta(t,x), product,mp.mpf('1e-40'))
        bound = image_theta(t,x)*mp.sin(x)*q/(1+q)**2
        assert f_full(t,x) > bound
        checks += 1

for n in [20,21,30,31,40,41,60,61]:
    a=mp.pi/2 if n%2==0 else 3*mp.pi/2
    x=mp.pi-a/n
    t=mp.mpf('1.3')/n
    F=f_finite(n,t,x)
    assert F<0, ('negative predicted', n, F)
    checks += 1
    tail=f_full(t,x)-F
    assert tail>0
    checks+=1
    # Normalization converges to 1/(1+e^{2c}) in both parities.
    normalized=tail/(n*mp.exp(-mp.mpf('1.3')*n))
    assert abs(normalized-1/(1+mp.exp(mp.mpf('2.6'))))<mp.mpf('.02')
    checks+=1

for n in [10,11,20,21,30,31,40,41]:
    t=mp.mpf('1.7')/n
    for j in range(1,61):
        x=mp.pi*mp.mpf(j)/61
        assert f_finite(n,t,x)>0, ('positivity predicted',n,j)
        checks+=1

# Check the finite-spectral derivative identity on a spread of scales.
for n in [3,5,12,24,48]:
    for t in [mp.mpf('0.07'),mp.mpf('0.15'),mp.mpf('0.5')]:
        for x in [mp.mpf('.23'),mp.mpf('1.1'),mp.mpf('2.7')]:
            deriv=-2*mp.fsum(k*mp.exp(-t*k*k)*mp.sin(k*x) for k in range(1,n+1))
            close(deriv,-2*f_finite(n,t,x))

print('PASS:',checks,'finite high-precision diagnostics; no infinite proof asserted')
