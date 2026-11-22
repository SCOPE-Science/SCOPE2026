#!/usr/bin/env python3
"""Independent high-precision finite checks of analytic kernel-cubature identities.

Requires mpmath (tested with 1.3+). These finite tests are not an infinite proof.
"""
import mpmath as mp
mp.mp.dps = 70
pi = mp.pi
k0 = 1 + pi**4/45
a = 2*pi**4/3
b0 = pi**2/12 + pi**4/720
b2 = 4*pi**2 - pi**4/3
A = b0/(8*k0) + b2/(16*a)
checks = 0

def test(cond, desc):
    global checks
    if not cond:
        raise AssertionError(desc)
    checks += 1

def kernel(t):
    t = abs(mp.mpf(t))
    return k0-a*(t*t-2*t**3+t**4)

def mean(t, terms=4500):
    t=mp.mpf(t)
    return 1-mp.fsum(mp.cos(4*pi*j*t)/(8*j**4*(4*j*j-1)) for j in range(1,terms+1))

def solve(nodes):
    q=mp.matrix([[kernel(x-y) for y in nodes] for x in nodes])
    v=mp.matrix([mean(x) for x in nodes])
    w=mp.lu_solve(q,v)
    for i in range(len(nodes)):
        test(abs(sum(q[i,j]*w[j] for j in range(len(nodes)))-v[i])<mp.mpf('1e-48'), 'Gram residual')
    return w

# Independent Fourier/series checks, including one exact Bernoulli polynomial identity.
for t in [mp.mpf(0),mp.mpf(1)/7,mp.mpf(1)/5,mp.mpf(1)/3]:
    freqs=mp.fsum(2*mp.cos(2*pi*j*t)/j**4 for j in range(1,5000))+1
    test(abs(kernel(t)-freqs)<mp.mpf('2e-11'), 'Bernoulli v. Fourier kernel')
test(abs(mean(0)-b0)<mp.mpf('1e-18'), 'kernel mean at zero')
test(b2>0 and A>0, 'strict positivity of asymptotic constant')

for N in [8,12,16,32,64,128,256]:
    h=mp.mpf(1)/N
    w2=solve([0,h]); w3=solve([0,h,2*h])
    exact2_0=b0/(2*k0)-b2/(4*a)
    exact2_1=b0/(2*k0)+b2/(4*a)
    test(abs(w2[0]-exact2_0)<mp.mpf('0.04'), 'bounded two-node left weight')
    test(abs(w2[1]-exact2_1)<mp.mpf('0.04'), 'bounded two-node right weight')
    test(w3[0]>0 and w3[1]<0 and w3[2]>0, 'three-node signs')
    test(abs(h*w3[0]-A)<mp.mpf('0.12'), 'left leading coefficient')
    test(abs(h*w3[1]+2*A)<mp.mpf('0.12'), 'middle leading coefficient')
    test(abs(h*w3[2]-A)<mp.mpf('0.12'), 'right leading coefficient')
    test(abs(h*sum(abs(w3[i]) for i in range(3))-4*A)<mp.mpf('0.12'), 'total variation coefficient')
    test(abs(h*h*sum(w3[i]*w3[i] for i in range(3))-6*A*A)<mp.mpf('0.12'), 'noise variance coefficient')

# The tolerance tightens at larger N; excludes inference of asymptotics from tests.
for N,tol in [(32,'0.003'),(64,'0.002'),(128,'0.001'),(256,'0.0006')]:
    h=mp.mpf(1)/N
    w=solve([0,h,2*h])
    test(abs(h*w[1]+2*A)<mp.mpf(tol), f'scaled middle weight N={N}')
print('VERIFY_OK',checks,'checks','A=',mp.nstr(A,19))
